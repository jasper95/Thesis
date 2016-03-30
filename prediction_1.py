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
model = model_from_json(open('models/crime_prediction_model_classification' +
                             '_54x36_SE.json').read())
model.load_weights('weights/crime_prediction_classification_weight' +
                   '_54x36_SE.hdf5')

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
np.savetxt('spatial_prediction_output.txt', output_for_training, delimiter=' ')

# def fScore(pred, truth):
#     counts = Counter(zip(pred, truth))
#     true_pos = float(counts[1.0, 1.0])
#     false_pos = float(counts[0.0, 1.0])
#     true_neg = float(counts[1.0, 0.0])
#     false_neg = float(counts[0.0, 0.0])
#     print('true_pos', true_pos, 'false_pos', false_pos, 'true_neg', true_neg,
#           'false_neg', false_neg)
#     recall = float(true_pos)/float(true_pos+true_neg)
#     precision = true_pos/float(true_pos+false_pos)
#     print ('precision: ', precision, 'recall:', recall)
#     return 2.0/((1.0/recall) + (1.0/precision))


# ground_truth[ground_truth >= 1] = 1
# ground_truth[ground_truth < 1] = 0
# prediction[prediction >= 1] = 1
# prediction[prediction < 1] = 0

# for i in range(test_input.shape[0]):
#     print ((prediction[i] >= 1).sum(), (test[i] >= 1).sum())
# F = acc = 0.0

# for i in range(test_input.shape[0]):
#     acc += np_utils.accuracy(prediction[i], ground_truth[i])
#     F += fScore(prediction[i], ground_truth[i])

# acc /= test_input.shape[0]
# F /= test_input.shape[0]
# print('Accuracy:', acc, ' F-score', F)
