from __future__ import absolute_import
from __future__ import division
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

all_data = np.loadtxt('final_weekly_data.txt')
sample_size = all_data.shape[0]
boxes = all_data.shape[1]
all_data = all_data.reshape((sample_size, 1, 107, 72))

filter_size = 3
padding_size = 1

SE = all_data[:, :, 107/2:, 0:72/2]
SE = SE.reshape((sample_size, 54*36))
indices = np.nonzero(np.any(SE != 0, axis=0))[0]
mask = np.ones(SE.shape, dtype=bool)
mask[:, indices] = False
SE[mask] = -1

SE = SE.reshape((sample_size, 1, 54, 36))

# get SE division only
X_train = SE[0:sample_size*.6]
Y_train = SE[1:(sample_size*.6)+1]
X_test = SE[sample_size*.6:-1]
Y_test = SE[(sample_size*.6)+1:]


# change label shape
Y_train = Y_train.reshape((X_train.shape[0], 54*36))
Y_test = Y_test.reshape((Y_test.shape[0], 54*36))

# change input to -1 or 1
# X_train[X_train < 1] = X_test[X_test < 1] = -1
# X_train[X_train >= 1] = X_test[X_test >= 1] = 1

# change output to 0 or 1
# Y_train[Y_train < 1] = Y_test[Y_test < 1] = 0
# Y_train[Y_train >= 1] = Y_test[Y_test >= 1] = 1


# build model
model = Sequential()
model.add(Convolution2D(1, filter_size, filter_size, border_mode='same',
                        input_shape=(1, 54, 36)))
model.add(LeakyReLU())
model.add(Convolution2D(1, filter_size, filter_size, border_mode='same'))
model.add(LeakyReLU())
model.add(Convolution2D(1, filter_size, filter_size, border_mode='same'))
model.add(LeakyReLU())
model.add(Convolution2D(1, filter_size, filter_size, border_mode='same'))
model.add(LeakyReLU())
model.add(Flatten())
model.compile(loss='mse', optimizer='rmsprop')
checkpoint = ModelCheckpoint('weights/exp1_1.hdf5',
                             verbose=1, save_best_only=True)
model.fit(X_train, Y_train, batch_size=32, nb_epoch=2000,
          validation_data=(X_test, Y_test), show_accuracy=True,
          callbacks=[checkpoint])

# save model to json
json_string = model.to_json()
open('models/exp1_1.json', 'w').write(json_string)
# model.save_weights('weights/exp1_1.hdf5',
#                    overwrite=True)
