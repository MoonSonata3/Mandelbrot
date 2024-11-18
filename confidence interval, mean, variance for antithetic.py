import numpy as np
import math
from scipy.stats import norm

def antithetic_area(N, max_iter):
    """
    Estimates the area of the Mandelbrot set using antithetic variables.
    """
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    counter = 0

    for _ in range(N // 2):  #Only half since each pair is going to generate two points
        x_sample = np.random.uniform(xmin, xmax)
        y_sample = np.random.uniform(ymin, ymax)
        c = x_sample + 1j * y_sample

        # Generate the antithetic variable
        ax_sample = (xmin + xmax) - x_sample
        ay_sample = (ymin + ymax) - y_sample
        antithetic_c = ax_sample + 1j * ay_sample

        #To test if both points belong to the mandelbrodt set
        z, z_anti = 0 + 0j, 0 + 0j
        is_inside = [True, True]
        for n in range(max_iter):
            z = z**2 + c if abs(z) <= 2 else z
            z_anti = z_anti**2 + antithetic_c if abs(z_anti) <= 2 else z_anti

            if abs(z) > 2:
                is_inside[0] = False
            if abs(z_anti) > 2:
                is_inside[1] = False

            if not any(is_inside):
                break

        counter += sum(is_inside)

    proportion_of_points = counter / N
    area = 16 * proportion_of_points
    return area


# Function to compute mean and variance:
def compute_varandmean(method_func, N, max_iter, runs):
    areas = [method_func(N, max_iter) for _ in range(runs)]
    variance = np.var(areas, ddof=1)  # Sample variance
    mean = np.mean(areas)
    return mean, variance

# Function to compute confidence interval:
def conf_int(mean, var, runs, p=0.95):
    z_value = norm.ppf((p + 1) / 2)  
    std_dev = math.sqrt(var)         
    margin_of_error = z_value * std_dev / math.sqrt(runs)
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return lower_bound, upper_bound

#My Parameters
nb_samples = 100000  
itermax = 500        
runs = 30            

pr_mean, pr_var = compute_varandmean(antithetic_area, nb_samples, itermax, runs)

ci_lower, ci_upper = conf_int(pr_mean, pr_var, runs, p=0.95)

# Print results
print(f"Antithetic Sampling Mean Area: {pr_mean:.4f}")
print(f"Antithetic Sampling Variance: {pr_var:.4e}")
print(f"95% Confidence Interval: [{ci_lower:.4f}, {ci_upper:.4f}]")
