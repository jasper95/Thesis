import numpy as np

data = np.loadtxt('all_data2.txt')
data = data.reshape((data.shape[0], 1, 107, 72))
SE = data[:, :, 107/2:, 0:72/2]
SE = SE.reshape(157, 54*36)

indices = np.nonzero(np.any(SE != 0, axis=0))[0]
a = SE[:, indices]
for i in range(a.shape[0]):
    print ((a[i] >= 1).sum(), (SE[i] >= 1).sum())
