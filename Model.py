import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D, ZeroPadding2D
from keras.layers.core import Dense, Flatten, Activation, Dropout
from keras.layers.advanced_activations import LeakyReLU
from keras.callbacks import EarlyStopping

all_data = np.loadtxt('all_data2.txt')
sample_size = all_data.shape[0]
boxes = all_data.shape[1]
all_data = all_data.reshape((sample_size, 1, 107, 72))

filter_size = 3
padding_size = 1

X_train = all_data[0:sample_size*.6]
Y_train = all_data[1:(sample_size*.6)+1]
X_test = all_data[sample_size*.6:-1]
Y_test = all_data[(sample_size*.6)+1:]

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

Y_train[Y_train > 0] = Y_test[Y_test > 0] = 1
Y_train = Y_train.reshape((X_train.shape[0], boxes))
Y_test = Y_test.reshape((Y_test.shape[0], boxes))


Y_train = Y_train.astype('int32')
Y_test = Y_test.astype('int32')

model = Sequential()
model.add(ZeroPadding2D((padding_size, padding_size),
                        input_shape=(1, 107, 72)))
model.add(Convolution2D(1, filter_size, filter_size))
model.add(LeakyReLU())
model.add(ZeroPadding2D((padding_size, padding_size)))
model.add(Convolution2D(1, filter_size, filter_size))
model.add(LeakyReLU())
model.add(ZeroPadding2D((padding_size, padding_size)))
model.add(Convolution2D(1, filter_size, filter_size))
model.add(LeakyReLU())
model.add(ZeroPadding2D((padding_size, padding_size)))
model.add(Convolution2D(1, filter_size, filter_size))
model.add(LeakyReLU())
model.add(ZeroPadding2D((padding_size, padding_size)))
model.add(Convolution2D(1, filter_size, filter_size))
model.add(LeakyReLU())
model.add(ZeroPadding2D((padding_size, padding_size)))
model.add(Convolution2D(1, filter_size, filter_size))
model.add(LeakyReLU())
model.add(ZeroPadding2D((padding_size, padding_size)))
model.add(Convolution2D(1, filter_size, filter_size))
model.add(LeakyReLU())
model.add(ZeroPadding2D((padding_size, padding_size)))
model.add(Convolution2D(1, filter_size, filter_size))
model.add(LeakyReLU())
model.add(Flatten())
model.add(Dense(boxes))
model.add(LeakyReLU())
model.add(Dense(boxes, activation='sigmoid'))
model.compile(loss='poisson', optimizer='adagrad')
model.fit(X_train, Y_train, batch_size=16, nb_epoch=1,
          validation_data=(X_test, Y_test), show_accuracy=True,
          callbacks=[EarlyStopping(patience=3)])

json_string = model.to_json()
open('crime_prediction_model.json', 'w').write(json_string)
model.save_weights('crime_prediction_model_weights.h5')
