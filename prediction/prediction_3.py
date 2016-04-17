import h5py
import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D, Convolution3D
from keras.layers.recurrent_convolutional import LSTMConv2D
from keras.layers.core import TimeDistributedDense
from keras.callbacks import ModelCheckpoint
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from helpers.util import fScore
from helpers.preprocessing import load_data
import matplotlib.pyplot as plt


#load model
model = Sequential()
model.add(LSTMConv2D(3, 3, 3, input_shape=(3, 27, 18, 1),
          border_mode='same', return_sequences=True))
model.add(LSTMConv2D(3, 3, 3, border_mode='same', return_sequences=True))
model.add(LSTMConv2D(3, 3, 3, border_mode='same', return_sequences=True))
model.add(Convolution3D(nb_filter=1, kernel_dim1=1, kernel_dim2=3,
                        kernel_dim3=3, activation='tanh',
                        border_mode="same", dim_ordering='tf'))
model.compile(loss='binary_crossentropy', optimizer='adadelta')


f = h5py.File('../weights/exp3_7.hdf5')
for k in range(f.attrs['nb_layers']):
    if k >= len(model.layers):
        break
    g = f['layer_{}'.format(k)]
    weights = [g['param_{}'.format(p)] for p in range(g.attrs['nb_params'])]
    model.layers[k].set_weights(weights)
f.close()
print('Model loaded.')

#load file
all_data = np.loadtxt('../final_weekly_data_500.txt')

all_data = all_data.reshape((all_data.shape[0], 54, 36, 1))

SE_output = all_data[:, 27:, 0:18, :]

tempSE = SE_output.reshape((SE_output.shape[0], 27*18))
indices = np.nonzero(np.any(tempSE != 0, axis=0))[0]

X = np.loadtxt('../test_set/exp3/X2.txt')
Y = np.loadtxt('../test_set/exp3/Y2.txt')

X = X.reshape(X.shape[0], 3, 27, 18, 1)
Y = Y.reshape(Y.shape[0], 3, 27, 18, 1)

Y[Y > 0] = 1
prediction = model.predict(X)
actual = Y[:, -1, :, :, :]
actual = actual.reshape((actual.shape[0], 27*18))

spec_y_val = []
fscore_y_val = []
recall_y_val = []
x_val = np.arange(.1, .6, .001)

for threshold in x_val:
    thresholded_prediction = np.copy(prediction)
    thresholded_prediction[thresholded_prediction >= threshold] = 1
    thresholded_prediction[thresholded_prediction < threshold] = 0

    F = acc = f = recall = specificity = 0.0
    for i in range(prediction.shape[0]):
        result = thresholded_prediction[i, -1, :, :, :]
        result = result.reshape((27*18))
        acc += np_utils.accuracy(result[indices], actual[i, indices])
        f, r, s = fScore(result[indices], actual[i, indices])
        F += f
        recall += r
        specificity += s

    print 'Accuracy:', acc/prediction.shape[0]
    spec_y_val.append(specificity/prediction.shape[0])
    fscore_y_val.append(F/prediction.shape[0])
    recall_y_val.append(recall/prediction.shape[0])

plt.plot(x_val, recall_y_val, label='Sensitivity')
plt.plot(x_val, spec_y_val, label='Specificity')
plt.xlabel('Threshold')
plt.ylabel('Score')
plt.legend()
plt.show()
