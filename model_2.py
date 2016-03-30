import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Flatten, Activation, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.utils import np_utils
from collections import Counter
from keras.optimizers import SGD


output_data = np.loadtxt('final_weekly_data.txt')
trained_data = np.loadtxt('spatial_prediction_output.txt')
trained_data_samples = output_data.shape[1]
SE = output_data.reshape((output_data.shape[0], 1, 107, 72))
SE = SE[:, :, 107/2:, 0:72/2]
SE = SE[1:]
SE = SE.reshape((156, 1944))
indices = np.nonzero(np.any(SE != 0, axis=0))[0]
output_data = SE[:, indices]


Y_train = output_data[:output_data.shape[0]*.6]
X_train = trained_data[:trained_data.shape[0]*.6]
X_test = trained_data[(trained_data.shape[0]*.6):]
Y_test = output_data[output_data.shape[0]*.6:]

Y_train[Y_train > 0] = Y_test[Y_test > 0] = 1
# print X_train
# print Y_train
# print X_test
# print Y_test
# for i in range(Y_train.shape[0]):
#     print((X_train[i] >= 1).sum(), (Y_train[i] == 1).sum())
# print(X_test.shape, X_train.shape)
# print(Y_test.shape, Y_train.shape)

model = Sequential()
model.add(Dense(Y_train.shape[1], input_dim=X_train.shape[1],
                activation='tanh'))
# model.add(Dense(X_train.shape[1], activation='tanh'))
sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='mse', optimizer='adam')
checkpoint = ModelCheckpoint('crime_prediction_classification_weight_54x36_SE_final.hdf5',
                             verbose=1, save_best_only=True)
model.fit(X_train, Y_train, batch_size=32, nb_epoch=100,
          validation_data=(X_test, Y_test), show_accuracy=True,
          callbacks=[checkpoint])
json_string = model.to_json()
open('crime_prediction_model_classification_54x36_SE_final.json', 'w').write(json_string)
