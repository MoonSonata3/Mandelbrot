import numpy as np
import math
from scipy.stats import norm

# Function for pure random sampling
def pure_random_sampling(nb_samples, itermax):
    """
    This function estimates the area of Mandelbrot with pure random sampling.

    Parameters:
        nb_samples: Total number of points that we will sample.
        itermax: The maximum number of iterations that we can use to test the divergence.

    Returns:
        Estimated area of the Mandelbrot set.
    """
    # Counter for points in the Mandelbrot set
    counter = 0

    for _ in range(nb_samples):
        c = complex(np.random.uniform(-2, 2), np.random.uniform(-2, 2))
        z = 0
        for _ in range(itermax):
            z = z**2 + c
            if abs(z) > 2:
                break
        else:
            counter += 1

    # Compute the estimated area
    proportion = counter / nb_samples
    area = 16 * proportion

    return area

# Function to compute mean and variance
def compute_varandmean(method_func, N, max_iter, runs):
    """
    Compute mean and variance for a given method function.

    Parameters:
        method_func: The function to estimate the area (e.g., pure_random_sampling).
        N: Number of samples.
        max_iter: Maximum number of iterations.
        runs: Number of runs to perform.

    Returns:
        Tuple containing the mean and variance.
    """
    areas = [method_func(N, max_iter) for _ in range(runs)]
    variance = np.var(areas, ddof=1)  # Sample variance
    mean = np.mean(areas)
    return mean, variance

# Function to compute confidence interval
def conf_int(mean, var, runs, p=0.95):
    """
    Compute the confidence interval for the given mean and variance.

    Parameters:
        mean: Mean of the sample.
        var: Variance of the sample.
        runs: Number of runs.
        p: Confidence level (default: 0.95).

    Returns:
        Confidence interval ( tuple).
    """
    z_value = norm.ppf((p + 1) / 2)  # Critical z-value
    std_dev = math.sqrt(var)         # Standard deviation
    margin_of_error = z_value * std_dev / math.sqrt(runs)  # Margin of error
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return lower_bound, upper_bound

#My Parameters
nb_samples = 10000
itermax = 500
runs = 30

# Calculate mean and variance for pure random sampling :
pr_mean, pr_var = compute_varandmean(pure_random_sampling, nb_samples, itermax, runs)

# Calculate confidence interval :
ci_lower, ci_upper = conf_int(pr_mean, pr_var, runs, p=0.95)

print(f"Pure Random Sampling Mean Area: {pr_mean:.4f}")
print(f"Pure Random Sampling Variance: {pr_var:.4e}")
print(f"95% Confidence Interval: [{ci_lower:.4f}, {ci_upper:.4f}]")
