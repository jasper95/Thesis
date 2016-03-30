import numpy as np
from keras.models import model_from_json
from keras.utils import np_utils
from collections import Counter

input_data = np.loadtxt('spatial_prediction_output.txt')
output_data = np.loadtxt('all_data2.txt')

SE = output_data.reshape((output_data.shape[0], 1, 107, 72))
SE = SE[:, :, 107/2:, 0:72/2]
SE = SE.reshape((157, 1944))
indices = np.nonzero(np.any(SE != 0, axis=0))[0]
SE = SE[94:]
output_data = SE[:, indices]
input_data = input_data[93:]

model = model_from_json(open('crime_prediction_model_classification_54x36_SE_final.json').read())
model.load_weights('crime_prediction_classification_weight_54x36_SE_final.hdf5')

output_data[output_data > 0] = 1
prediction = model.predict(input_data, batch_size=input_data.shape[0])


def fScore(pred, truth):
    counts = Counter(zip(pred, truth))
    true_pos = float(counts[1.0, 1.0])
    false_pos = float(counts[0.0, 1.0])
    true_neg = float(counts[1.0, 0.0])
    false_neg = float(counts[0.0, 0.0])
    print('true_pos', true_pos, 'false_pos', false_pos, 'true_neg', true_neg,
          'false_neg', false_neg)
    recall = float(true_pos)/float(true_pos+true_neg)
    precision = true_pos/float(true_pos+false_pos)
    print ('precision: ', precision, 'recall:', recall)
    return 2.0/((1.0/recall) + (1.0/precision))

prediction[prediction >= .5] = 1
prediction[prediction < .5] = 0

F = acc = 0.0
for i in range(input_data.shape[0]):
    acc += np_utils.accuracy(prediction[i], output_data[i])
    F += fScore(prediction[i], output_data[i])

acc /= input_data.shape[0]
F /= output_data.shape[0]
print('Accuracy:', acc, ' F-score', F)