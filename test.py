from __future__ import division
import numpy as np
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from helpers.preprocessing import load_data
from helpers.util import fScore

processed = load_data()
unprocessed = np.loadtxt('final_weekly_data_500.txt')
unprocessed[unprocessed > 0] = 1

indices = np.nonzero(np.any(unprocessed != 0, axis=0))[0]

processed[processed >= .5] = 1
processed[processed < .5] = 0

X = processed[:-1]
Y = unprocessed[1:]

F = 0.0
for i in range(X.shape[0]):
    F += fScore(X[i, indices], Y[i, indices])

F /= X.shape[0]
print F
# np.savetxt('avg_crime.txt', b, delimiter=' ', fmt='%2.12f')

# max_data = np.amax(data, axis=0)
# min_data = np.amin(data, axis=0)

# with np.errstate(divide='ignore', invalid='ignore'):
#     a = np.true_divide(data-min_data, max_data-min_data)
#     a[a == np.inf] = 0
#     a = np.nan_to_num(a)

# avg = np.average(data, axis=0)
# indices = np.nonzero(np.any(data != 0, axis=0))[0]
# data[:, indices] = np.true_divide(data[:, indices], avg[indices])

# print data.shape
# SE = data[:, :, 107/2:, 0:72/2]

# SE = SE.reshape(157, 54*36)

# for i in range(data.shape[0]):
# print (max_data >= 1).sum()
# transform_data = np.ones((155, 3, 1, 54, 36))

# for i in range(transform_data.shape[0]):
#     transform_data[i, :, :, :, :] = SE[i:i+3]
# print transform_data
    # indices = np.nonzero(np.any(SE != 0, axis=0))[0]
# a = SE[:, indices]
# for i in range(a.shape[0]):
#     print ((a[i] >= 1).sum(), (SE[i] >= 1).sum())
