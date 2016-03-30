import numpy as np
from keras.models import model_from_json
from keras.utils import np_utils
import util

input_data = np.loadtxt('outputs/exp1_1_output.txt')
output_data = np.loadtxt('final_weekly_data.txt')

SE = output_data.reshape((output_data.shape[0], 1, 107, 72))
SE = SE[:, :, 107/2:, 0:72/2]
SE = SE.reshape((157, 1944))
indices = np.nonzero(np.any(SE != 0, axis=0))[0]
SE = SE[94:]
output_data = SE[:, indices]
input_data = input_data[93:]

model = model_from_json(open('models/exp1_2.json').read())
model.load_weights('weights/exp1_2.hdf5')

output_data[output_data > 0] = 1
prediction = model.predict(input_data, batch_size=input_data.shape[0])

prediction[prediction >= .3] = 1
prediction[prediction < .3] = 0

F = acc = 0.0
for i in range(input_data.shape[0]):
    acc += np_utils.accuracy(prediction[i], output_data[i])
    F += util.fScore(prediction[i], output_data[i])

acc /= input_data.shape[0]
F /= output_data.shape[0]
print('Accuracy:', acc, ' F-score', F)
