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
all_data = np.loadtxt('../final_weekly_data_500.txt')

# loading preprocessed with avg and proba data
input_data = load_data()

# reshaping to samples x height x width x channel
all_data = all_data.reshape((all_data.shape[0], 54, 36, 1))
input_data = input_data.reshape(all_data.shape)

# get SE part only
SE_input = input_data[:, 27:, 0:18, :]
SE_output = all_data[:, 27:, 0:18, :]

# convert samples x sequences height x width x channel
ts_input_data = np.ones((154, 4, 27, 18, 1))
ts_output_data = np.ones((154, 4, 27, 18, 1))


for i in range(ts_input_data.shape[0]):
    ts_input_data[i, :, :, :, :] = SE_input[i:i+4]
    ts_output_data[i, :, :, :, :] = SE_output[i:i+4]

# input [x1,x2,x3]
X = ts_output_data[:, :-1, :, :, :]
# output [x2,x3,x4]
Y = ts_output_data[:, 1:, :, :, :]

# Y[Y > 0] = 1
# X[X > 0] = 1
# X[X == 0] = -1

# shuffling the data
X, Y = shuffle_in_unison_inplace(X, Y)

# 60% training, 20% validation, 20% test
X_train = X[:X.shape[0]*.8]
Y_train = Y[:Y.shape[0]*.8]
X_test = X[X.shape[0]*.8:]
Y_test = Y[Y.shape[0]*.8:]

# saving test set to files for prediction
np.savetxt('../test_set/exp3/unchanged_X.txt', X_test.reshape(X_test.shape[0], 3*27*18))
np.savetxt('../test_set/exp3/unchanged_Y.txt', Y_test.reshape(Y_test.shape[0], 3*27*18))


print 'Building Model'

model = Sequential()
model.add(LSTMConv2D(3, 3, 3, input_shape=(3, 27, 18, 1),
          border_mode='same', return_sequences=True))
model.add(LSTMConv2D(3, 3, 3, border_mode='same', return_sequences=True))
model.add(LSTMConv2D(3, 3, 3, border_mode='same', return_sequences=True))
model.add(Convolution3D(nb_filter=1, kernel_dim1=1, kernel_dim2=3,
                        kernel_dim3=3, activation='tanh',
                        border_mode="same", dim_ordering='tf'))
model.compile(loss='binary_crossentropy', optimizer='adadelta')
checkpoint = ModelCheckpoint('../weights/exp3_1.hdf5',
                             verbose=1, save_best_only=True)
model.fit(X_train, Y_train, batch_size=16, nb_epoch=1000,
          validation_split=0.25, show_accuracy=True,
          callbacks=[checkpoint])
