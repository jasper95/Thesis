import numpy as np
from scipy import stats

data = np.loadtxt('../final_weekly_data_500.txt')


def reject_outliers(data, m=6.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s < m]

a = data.T
data_min = data.min(0)
data_max = data.max(0)
# for i in range(a.shape[0]):
#     no_outliers = reject_outliers(a[i])
#     data_min[i] = no_outliers.min()
#     data_max[i] = no_outliers.max()

min_max_diff = data_max-data_min
nonzero_indices = np.nonzero(min_max_diff)
temp = np.subtract(data, data_min)
normalized_data = np.zeros(data.shape)
normalized_data[:, nonzero_indices] = np.true_divide(temp[:, nonzero_indices],
                                                     min_max_diff[nonzero_indices])
# for i in range(normalized_data.shape[0]):
#     print (normalized_data[i] > 0).sum(), (data[i] >= 1).sum()

# np.savetxt('../avg_crime.txt', b, delimiter=' ')
# np.savetxt('../proba_crime.txt', c, delimiter=' ')
np.savetxt('../normalized_data.txt', normalized_data, delimiter=' ')
