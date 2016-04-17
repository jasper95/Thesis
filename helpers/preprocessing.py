import numpy as np


def load_data(cell_size=500):
    data = np.loadtxt('../final_weekly_data_'+str(cell_size)+'.txt').astype(
        'float32')
    avg = np.loadtxt('../avg_crime.txt').astype('float32')
    proba = np.loadtxt('../proba_crime.txt').astype('float32')
    nonzero_avg_indices = np.nonzero(avg)
    data[:, nonzero_avg_indices] = np.true_divide(data[:, nonzero_avg_indices],
                                                  avg[nonzero_avg_indices])
    data[data > 1] = 1
    data = data * .2
    return np.add(data, proba)
