import numpy as np
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D, Convolution3D
from keras.layers.recurrent_convolutional import LSTMConv2D
from keras.layers.core import TimeDistributedDense
from keras.callbacks import ModelCheckpoint
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from helpers.preprocessing import load_data
from helpers.util import shuffle_in_unison_inplace

# loading processed data
all_data = np.loadtxt('../final_weekly_data_750.txt')

# loading preprocessed with avg and proba data
input_data = load_data('weekly', 750)

height = 36
width = 24
input_length = 3

height_red = height/2
width_red = width/2

# height_red = height_red + 1 if (height_red % 2) == 1 else height_red
# reshaping to samples x height x width x channel
all_data = all_data.reshape((all_data.shape[0], height, width, 1))
input_data = input_data.reshape(all_data.shape)

# get SE part only
SE_input = input_data[:, height_red:, 0:width_red, :]
SE_output = all_data[:, height_red:, 0:width_red, :]

examples = all_data.shape[0]-input_length

# convert samples x sequences height x width x channel
ts_input_data = np.ones((examples, input_length+1, height_red, width_red, 1))
ts_output_data = np.ones((examples, input_length+1, height_red, width_red, 1))

print ts_input_data.shape, SE_input.shape
for i in range(ts_input_data.shape[0]):
    ts_input_data[i, :, :, :, :] = SE_input[i:i+input_length+1]
    ts_output_data[i, :, :, :, :] = SE_output[i:i+input_length+1]


X = ts_input_data[:, :-1, :, :, :]
Y = ts_output_data[:, 1:, :, :, :]

Y[Y > 0] = 1

# shuffling the data
X, Y = shuffle_in_unison_inplace(X, Y)

# 60% training, 20% validation, 20% test
X_train = X[: X.shape[0]*.6]
Y_train = Y[: Y.shape[0]*.6]
X_val = X[X.shape[0]*.6: X.shape[0]*.8]
Y_val = Y[Y.shape[0]*.6: Y.shape[0]*.8]
X_test = X[X.shape[0]*.8:]
Y_test = Y[Y.shape[0]*.8:]


# saving test set to files for prediction
np.savetxt('../train_set/weekly_750_X.txt',
           X_train.reshape(X_train.shape[0], input_length*height_red*width_red))
np.savetxt('../train_set/weekly_750_Y.txt',
           Y_train.reshape(Y_train.shape[0], input_length*height_red*width_red))
np.savetxt('../val_set/weekly_750_X.txt',
           X_val.reshape(X_val.shape[0], input_length*height_red*width_red))
np.savetxt('../val_set/weekly_750_Y.txt',
           Y_val.reshape(Y_val.shape[0], input_length*height_red*width_red))
np.savetxt('../test_set/weekly_750_X.txt',
           X_test.reshape(X_test.shape[0], input_length*height_red*width_red))
np.savetxt('../test_set/weekly_750_Y.txt',
           Y_test.reshape(Y_test.shape[0], input_length*height_red*width_red))


print 'Building Model'

model = Sequential()
model.add(LSTMConv2D(input_length, 3, 3,
          input_shape=(input_length, height_red, width_red, 1),
          border_mode='same', return_sequences=True))
model.add(LSTMConv2D(input_length, 3, 3, border_mode='same',
                     return_sequences=True))
model.add(LSTMConv2D(input_length, 3, 3, border_mode='same',
                     return_sequences=True))
model.add(Convolution3D(nb_filter=1, kernel_dim1=1, kernel_dim2=3,
                        kernel_dim3=3, activation='tanh',
                        border_mode="same", dim_ordering='tf'))
model.compile(loss='binary_crossentropy', optimizer='adadelta')
checkpoint = ModelCheckpoint('../weights/weekly_750.hdf5',
                             verbose=1, save_best_only=True)
model.fit(X_train, Y_train, batch_size=16, nb_epoch=1000,
          validation_data=(X_val, Y_val), show_accuracy=True,
          callbacks=[checkpoint])
