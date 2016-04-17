import numpy as np
from keras.models import model_from_json
from keras.utils import np_utils
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from helpers.util import fScore

test_input = np.loadtxt('../test_set/exp2/X.txt')
ground_truth = np.loadtxt('../test_set/exp2/Y.txt')

model = model_from_json(open('../models/exp2.json').read())
model.load_weights('../weights/exp2.hdf5')

test_input = test_input.reshape(test_input.shape[0], 1, 27, 18)
prediction = model.predict(test_input, batch_size=test_input.shape[0])

prediction[prediction >= .1] = 1
prediction[prediction < .1] = 0

F = acc = 0.0
for i in range(prediction.shape[0]):
    acc += np_utils.accuracy(prediction[i], ground_truth[i])
    F += fScore(prediction[i], ground_truth[i])

acc /= prediction.shape[0]
F /= prediction.shape[0]
print('Accuracy:', acc, ' F-score', F)
