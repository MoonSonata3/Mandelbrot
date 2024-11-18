#FUNCTIONS FOR VARIANCE MEAN AND CONFIDENCE INTERVALS
import numpy as np
import math
from scipy.stats import norm

#function to get mean and variance
def compute_varandmean(method_func, N, max_iter, runs):
    areas = [method_func(N, max_iter) for _ in range(runs)]
    variance = np.var(areas)
    mean = np.mean(areas)
    return mean, variance

#function to get confidence interval
def conf_int(mean, var, runs, p=0.95):
    z_value = norm.ppf((p + 1) / 2)  # Critical z-value
    std_dev = math.sqrt(var)         # Standard deviation
    margin_of_error = z_value * std_dev / math.sqrt(runs)  # Margin of error
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return lower_bound, upper_bound
