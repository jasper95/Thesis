import numpy as np
from keras.models import Sequential
from keras.layers.convolutional import (
    Convolution2D, ZeroPadding2D, MaxPooling2D)
from keras.layers.core import Dense, Flatten, Activation, Dropout
from keras.layers.advanced_activations import LeakyReLU
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.optimizers import SGD
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from helpers.preprocessing import load_data
from helpers.util import shuffle_in_unison_inplace

all_data = np.loadtxt('../final_weekly_data_500.txt')
input_data = load_data()

sample_size = all_data.shape[0]
all_data = all_data.reshape((sample_size, 1, 54, 36))
input_data = input_data.reshape(all_data.shape)

filter_size = 3

SE_input = input_data[:, :, 27:, 0:18]
SE_output = all_data[:, :, 27:, 0:18]
SE_output = SE_output.reshape((sample_size, 27*18))
indices = np.nonzero(np.any(SE_output != 0, axis=0))[0]

X = SE_input[:-1]
Y = SE_output[1:]

# Y = Y[:, indices]
X, Y = shuffle_in_unison_inplace(X, Y)

Y[Y > 0] = 1

X_train = X[:X.shape[0]*.8]
Y_train = Y[:Y.shape[0]*.8]
X_test = X[X.shape[0]*.8:]
Y_test = Y[Y.shape[0]*.8:]


np.savetxt('../test_set/exp2/X.txt', X_test.reshape(X_test.shape[0], 27*18))
np.savetxt('../test_set/exp2/Y.txt', Y_test)

# build model
model = Sequential()
model.add(Convolution2D(1, filter_size, filter_size, border_mode='same',
                        input_shape=(1, 27, 18)))
model.add(Activation('relu'))
model.add(Flatten())
model.add(Dense(Y_train.shape[1], activation='tanh'))
model.compile(loss='mse', optimizer='adadelta')
checkpoint = ModelCheckpoint('../weights/exp2.hdf5',
                             verbose=1, save_best_only=True)
model.fit(X_train, Y_train, batch_size=16, nb_epoch=1000,
          validation_split=.25, show_accuracy=True,
          callbacks=[checkpoint])

# save model to json
json_string = model.to_json()
open('../models/exp2.json', 'w').write(json_string)
# model.save_weights('weights/exp2.hdf5',
#                    overwrite=True)
