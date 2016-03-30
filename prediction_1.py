import numpy as np
import os
import h5py
from keras.models import model_from_json
from keras.utils import np_utils
from collections import Counter
from keras.models import Sequential
from keras.layers.convolutional import (
    Convolution2D, ZeroPadding2D, MaxPooling2D)
from keras.layers.core import Dense, Flatten, Activation, Dropout
from keras.layers.advanced_activations import LeakyReLU
from keras.callbacks import EarlyStopping, ModelCheckpoint


data = np.loadtxt('final_weekly_data.txt')
nb_examples = data.shape[0]
data = data.reshape((nb_examples, 1, 107, 72))
model = model_from_json(open('models/exp1_1.json').read())
model.load_weights('weights/exp1_1.hdf5')

SE = data[:, :, 107/2:, 0:72/2]

test_input = SE[:-1]
ground_truth = SE[1:]
all_data = SE[:]

ground_truth = ground_truth.reshape((nb_examples-1, 54*36))
all_data = all_data.reshape(nb_examples, 54*36)

prediction = model.predict(test_input, batch_size=nb_examples)
indices = np.nonzero(np.any(all_data != 0, axis=0))[0]

print (prediction.shape, ground_truth.shape)
output_for_training = prediction[:, indices]
np.savetxt('outputs/exp1_1_output.txt', output_for_training, delimiter=' ')
