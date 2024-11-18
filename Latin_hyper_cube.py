# latin hyper cube
import numpy as np
def lhs_area(N, max_iter):
    #counter to count how many points remain in the Mandelbrot set
    counter = 0
    samples = N

    #defining the real and imaginary axes and dividing into strata
    realaxis = np.linspace(-2, 2, samples)
    imaginaryaxis = np.linspace(-2, 2, samples)

    storage_real = []
    storage_imaginary = []

    #getting random points within each stratum for both axes
    for i in range(samples-1):
        # Select a random point in the real-axis stratum
        start_real = realaxis[i]
        end_real = realaxis[i + 1]
        randompoint_real = np.random.uniform(start_real, end_real)

        # Select a random point in the imaginary-axis stratum
        start_imag = imaginaryaxis[i]
        end_imag = imaginaryaxis[i + 1]
        randompoint_imaginary = np.random.uniform(start_imag, end_imag)

        # Store for later
        storage_real.append(randompoint_real)
        storage_imaginary.append(randompoint_imaginary)

    #shuffle the points within each axis independently to create randomized strata combinations
    np.random.shuffle(storage_real)
    np.random.shuffle(storage_imaginary)

    #combine the shuffled real and imaginary parts into complex numbers
    lhs_samples = np.array(storage_real) + 1j * np.array(storage_imaginary)

    # Check whether each sampled point belongs to the Mandelbrot set
    for i in range(N-1):
        c = lhs_samples[i]
        z = 0

        #Mandelbrot iteration for the current point
        for n in range(max_iter):
            z = z**2 + c
            if abs(z) > 2:  # If the point escapes stop
                break
        else:  #if the point does not escape, it is in the set
            counter += 1

    #the area by scaling the proportion of points in the set
    proportion_of_points = counter / N
    area = 16 * proportion_of_points  # The total area of the region [-2, 2] x [-2, 2] is 16
    return area

# Parameters
import matplotlib.pyplot as plt

#true area of mandelbrot set
true_area = 1.514

#parameters for the number of iterations, samples, and runs
max_iter = 500
sample_sizes = [100, 500, 1000, 3000, 5000, 7000, 10000]
runs = 30

#storage for results
mean_areas = []
mse_errors = []

# Run simulations
for s in sample_sizes:
    areas = [lhs_area(s, max_iter) for i in range(runs)]
    mean_areas.append(np.mean(areas))
    mse = np.mean([(a - true_area)**2 for a in areas])
    mse_errors.append(np.sqrt(mse))  # Root Mean Squared Error for error bars

# Plotting
plt.figure(figsize=(10, 6))
plt.errorbar(sample_sizes, mean_areas, yerr=mse_errors, fmt='o-', capsize=5, label='LHS')
plt.axhline(y=true_area, color='r', linestyle='--', label='True Area (approx.)')
plt.xlabel('Number of Samples')
plt.ylabel('Estimated Area')
plt.title('Convergence of Estimated Mandelbrot Area (LHS)')
plt.legend()
plt.grid()
plt.show()

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

# number of samples, iterations and runs
N = 10000
max_iter = 500
runs = 30

#getting mean and variance
lhs_mean, lhs_var = compute_varandmean(lhs_area, N, max_iter, runs)

#getting the confidence interval
ci_lower, ci_upper = conf_int(lhs_mean, lhs_var, runs, p=0.95)

#displaying the results
print(f"LHS Mean Area: {lhs_mean:.4f}")
print(f"LHS Variance: {lhs_var:.4e}")
print(f"95% Confidence Interval: [{ci_lower:.4f}, {ci_upper:.4f}]")
