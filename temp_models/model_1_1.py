import numpy as np
from keras.models import Sequential
from keras.layers.convolutional import (
    Convolution2D, ZeroPadding2D, MaxPooling2D)
from keras.layers.core import Dense, Flatten, Activation, Dropout
from keras.layers.advanced_activations import LeakyReLU
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.utils import np_utils
from collections import Counter
from keras.optimizers import SGD
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from helpers.preprocessing import load_data
from helpers.util import shuffle_in_unison_inplace

all_data = np.loadtxt('../final_weekly_data_500.txt')
input_data = load_data('weekly', 500)

height = 54
width = 36

height_red = height/2
width_red = width/2
all_data = all_data.reshape((all_data.shape[0], 1, height, width))
input_data = input_data.reshape((input_data.shape[0], 1, height, width))
filter_size = 3
padding_size = 1

SE_input = input_data[:-1, :, height_red:, 0:width_red]
SE_output = all_data[1:, :, height_red:, 0:width_red]

X = SE_input.reshape((SE_input.shape[0], 1, height_red, width_red))
Y = SE_output.reshape((SE_output.shape[0], height_red*width_red))

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
np.savetxt('../train_set/exp1/1_X.txt',
           X_train.reshape(X_train.shape[0], height_red*width_red))
np.savetxt('../train_set/exp1/1_Y.txt',
           Y_train.reshape(Y_train.shape[0], height_red*width_red))
np.savetxt('../val_set/exp1/1_X.txt',
           X_val.reshape(X_val.shape[0], height_red*width_red))
np.savetxt('../val_set/exp1/1_Y.txt',
           Y_val.reshape(Y_val.shape[0], height_red*width_red))
np.savetxt('../test_set/exp1/1_X.txt',
           X_test.reshape(X_test.shape[0], height_red*width_red))
np.savetxt('../test_set/exp1/1_Y.txt',
           Y_test.reshape(Y_test.shape[0], height_red*width_red))

# build model
model = Sequential()
model.add(Convolution2D(1, filter_size, filter_size, border_mode='same',
                        input_shape=(1, height_red, width_red)))
model.add(LeakyReLU())
model.add(Flatten())
model.add(Dense(Y_train.shape[1], activation='tanh'))
model.compile(loss='binary_crossentropy', optimizer='rmsprop')
checkpoint = ModelCheckpoint('../weights/exp1_1.hdf5',
                             verbose=1, save_best_only=True)
model.fit(X_train, Y_train, batch_size=128, nb_epoch=1000,
          validation_data=(X_val, Y_val), show_accuracy=True,
          callbacks=[checkpoint])

# save model to json
json_string = model.to_json()
open('../models/exp1_1.json', 'w').write(json_string)
# model.save_weights('weights/exp1_1.hdf5',
#                    overwrite=True)
