import numpy as np


def load_data(time_period, cell_size=500):
    data = np.loadtxt('../final_'+str(time_period)+'_data_'+str(cell_size)+'.txt')
    mean = np.mean(data.T, axis=1)
    std = np.std(data.T, axis=1)
    zero_centered = np.subtract(data, mean)
    nonzero_avg_indices = np.nonzero(std)
    zero_centered[:, nonzero_avg_indices] = np.true_divide(
        zero_centered[:, nonzero_avg_indices], std[nonzero_avg_indices])
    return zero_centered


def denormalize(a):
    data = np.loadtxt('../final_weekly_data_'+str(cell_size)+'.txt')
    mean = np.mean(data.T, axis=1)
    std = np.std(data.T, axis=1)
    a = np.multiply(a, std)
    return np.add(a, mean)
