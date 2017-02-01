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
from helpers.util import fScore, get_breakdown
from helpers.preprocessing import denormalize
import matplotlib.pyplot as plt
from operator import add
from sklearn.metrics import auc, roc_curve, roc_auc_score

height = 107
width = 72
input_length = 3

height_red = height/2
width_red = width/2

height_red = height_red + 1 if (height_red % 2) == 1 else height_red
#load model
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


f = h5py.File('../weights/weekly_250.hdf5')
for k in range(f.attrs['nb_layers']):
    if k >= len(model.layers):
        break
    g = f['layer_{}'.format(k)]
    weights = [g['param_{}'.format(p)] for p in range(g.attrs['nb_params'])]
    model.layers[k].set_weights(weights)
f.close()
print('Model loaded.')

#load file
all_data = np.loadtxt('../final_weekly_data_250.txt')

all_data = all_data.reshape((all_data.shape[0], height, width, 1))

SE_output = all_data[:, height_red:, 0:width_red, :]

tempSE = SE_output.reshape((SE_output.shape[0], height_red*width_red))
indices = np.nonzero(np.any(tempSE != 0, axis=0))[0]

X = np.loadtxt('../test_set/weekly_250.txt')
Y = np.loadtxt('../test_set/weekly_250.txt')

X = X.reshape(X.shape[0], input_length, height_red, width_red, 1)
Y = Y.reshape(Y.shape[0], input_length, height_red, width_red, 1)

Y[Y > 0] = 1
prediction = model.predict(X)
actual = Y[:, -1, :, :, :]
actual = actual.reshape((actual.shape[0], height_red*width_red))

"""
Uncomment this part to assess specificity, sensitivity, F-score, MCC for a
particular threshold
"""

threshold = 0.130834
prediction[prediction >= threshold] = 1
prediction[prediction < threshold] = 0

table = [0, 0, 0, 0]
a = 0
for i in range(prediction.shape[0]):
    b = prediction[i, -1, :, :, :]
    b = b.reshape(height_red*width_red)
    a += roc_auc_score(actual[i, indices], b[indices])
    temp_pred = prediction[i, -1, :, :, :]
    temp_pred = temp_pred.reshape(height_red*width_red)
    table = map(add, table, fScore(temp_pred[indices], actual[i, indices]))

print a/prediction.shape[0]
table = [x/prediction.shape[0] for x in table]
print table
"""
Uncomment this part to get a sample actual/prediction from test set
"""
# min_threshold = 0.130834
# max_threshold = 0.190109
# levels = 3
# interval = (max_threshold - min_threshold)/levels
# temp_min = min_threshold

# for i in range(levels):
#     temp_max = temp_min + interval
#     prediction[(prediction >= temp_min) & (prediction < temp_max)] = i+1
#     temp_min = temp_max

# prediction[(prediction >= temp_max) & (prediction < 1)] = levels+1
# prediction[prediction < min_threshold] = 0
# temp_sample_prediction = prediction[0, -1, :, :, :]
# temp_sample_prediction = temp_sample_prediction.reshape(height_red*width_red)
# no_crime_pred = indices[temp_sample_prediction[indices] == 0]
# temp_sample_prediction[no_crime_pred] = -1
# temp_sample_result = Y[0, -1, :, :, :]
# temp_sample_result = temp_sample_result.reshape(height_red*width_red)
# no_crime_act = indices[temp_sample_result[indices] == 0]
# temp_sample_result[no_crime_act] = -1
# pred = np.copy(temp_sample_prediction)
# act = np.copy(temp_sample_result)
# pred[pred >= 1] = 1
# pred[pred == -1] = 0
# act[act == -1] = 0
# print fScore(pred[indices], act[indices])
# temp_sample_prediction = temp_sample_prediction.reshape(1, height_red, width_red, 1)
# temp_sample_result = temp_sample_result.reshape(1, height_red, width_red, 1)
# sample_prediction = np.zeros((1, height, width, 1))
# sample_result = np.zeros((1, height, width, 1))
# sample_prediction[0, height_red:, 0:width_red, :] = temp_sample_prediction[0]
# sample_result[0, height_red:, 0:width_red, :] = temp_sample_result[0]
# sample_prediction = sample_prediction.reshape(height, width)
# sample_result = sample_result.reshape(height, width)
# np.savetxt('../outputs/3/1_actual.txt', sample_result, fmt='%.1i')
# np.savetxt('../outputs/3/1_pred.txt', sample_prediction, fmt='%.1i')


"""
Uncomment this part to see the graph of specificity, sensitivity, F-score
over threshold
"""
# spec_y_val = []
# fscore_y_val = []
# recall_y_val = []
# mcc_y_val = []
# x_val = np.arange(0.0, 0.23, 0.01)

# for threshold in x_val:
#     thresholded_prediction = np.copy(prediction)
#     thresholded_prediction[thresholded_prediction >= threshold] = 1
#     thresholded_prediction[thresholded_prediction < threshold] = 0

#     F = acc = f = recall = specificity = mcc = 0.0
#     for i in range(prediction.shape[0]):
#         result = thresholded_prediction[i, -1, :, :, :]
#         result = result.reshape((height_red*width_red))
#         acc += np_utils.accuracy(result[indices], actual[i, indices])
#         f, r, s, m = fScore(result[indices], actual[i, indices])
#         F += f
#         recall += r
#         specificity += s
#         mcc += m

#     print 'Accuracy:', acc/prediction.shape[0]
#     spec_y_val.append(specificity/prediction.shape[0])
#     fscore_y_val.append(F/prediction.shape[0])
#     recall_y_val.append(recall/prediction.shape[0])
#     mcc_y_val.append(mcc/prediction.shape[0])

# plt.plot(x_val, recall_y_val, label='Sensitivity')
# plt.plot(x_val, spec_y_val, label='Specificity')
# plt.plot(x_val, fscore_y_val, label='F-score')
# plt.plot(x_val, mcc_y_val, label='MCC')
# plt.xlabel('Threshold')
# plt.ylabel('Score')
# plt.legend()
# plt.show()
"""
Uncomment this part for creating table for confusion matrix result breakdown
for each prediction (added with classes)
"""
# min_threshold = 0.16
# max_threshold = 0.19
# levels = 3
# interval = (max_threshold - min_threshold)/levels
# temp_min = min_threshold
# class_breakdown = []

# for i in range(levels):
#     temp_max = temp_min + interval
#     prediction[(prediction >= temp_min) & (prediction < temp_max)] = i+1
#     temp_min = temp_max

# prediction[(prediction >= temp_max) & (prediction < 1)] = levels+1
# prediction[prediction < min_threshold] = 0

# for i in range(levels+1):
#     temp_pred = np.copy(prediction)
#     temp_pred[temp_pred != (i+1)] = 0
#     temp_pred[temp_pred == (i+1)] = 1
#     temp_table = [0, 0, 0, 0]
#     for j in range(temp_pred.shape[0]):
#         res = temp_pred[j, -1, :, :, :]
#         res = res.reshape(height_red*width_red)
#         print (res == 1).sum()
#         temp_table = map(add, temp_table, get_breakdown(res[indices], actual[j, indices]))
#     class_breakdown.append(temp_table)

# print class_breakdown
"""
Uncomment this part for to create roc curve for 1 random sample
"""
# scores = prediction[0, -1, :, :, :]
# scores = scores.reshape(height_red*width_red)
# target = actual[0]
# print target.shape, scores.shape
# fpr, tpr, _ = roc_curve(target[indices], scores[indices])
# area = auc(fpr, tpr)
# plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % area)
# plt.plot([0, 1], [0, 1], 'k--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.legend(loc="lower right")
# plt.show()
