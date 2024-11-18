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

# Function to estimate area using orthogonal sampling
def estimate_area(N, max_iter):
    samples = orthogonal_sampling(a=-2, b=2, c=-2, d=2, no_of_subspaces=N)
    samples = np.array(samples)

    inside = []
    for x, y in samples:
        c = complex(x, y)
        n_iter = is_in_set(c, max_iter=max_iter)
        if n_iter == max_iter:
            inside.append((x, y))

    # Area calculation
    sample_area = (2 - (-2)) * (2 - (-2))
    orthogonal_area = (len(inside) / len(samples)) * sample_area
    return orthogonal_area

# Number of samples, iterations and runs
N = 1000
max_iter = 500
runs = 30

# Getting mean and variance
os_mean, os_var = compute_varandmean(estimate_area, N, max_iter, runs)

# Getting the confidence interval
ci_lower, ci_upper = conf_int(os_mean, os_var, runs, p=0.95)

# Displaying the results
print(f"OS Mean Area: {os_mean:.4f}")
print(f"OS Variance: {os_var:.4e}")
print(f"95% Confidence Interval: [{ci_lower:.4f}, {ci_upper:.4f}]")
