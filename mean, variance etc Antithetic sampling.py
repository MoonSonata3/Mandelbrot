import numpy as np
def antithetic_area(N, max_iter):
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    counter = 0
    for i in range(N):
        # Generate random sample within bounds
        x_sample = np.random.uniform(xmin, xmax)
        y_sample = np.random.uniform(ymin, ymax)
        c = x_sample + 1j * y_sample

        # Compute region-centered antithetic counterpart
        ax_sample = (xmin + xmax) - x_sample
        ay_sample = (ymin + ymax) - y_sample
        antithetic_c = ax_sample + 1j * ay_sample


        z = 0
        z_anti = 0

        # Mandelbrot membership test
        for n in range(max_iter):
            z = z**2 + c
            z_anti = z_anti**2 + antithetic_c
            if abs(z) > 2 or abs(z_anti) > 2:
                break
        else:
            # Both points are inside the Mandelbrot set
            counter += 2

    # Calculate area
    proportion_of_points = counter / N
    area = 16 * proportion_of_points  # Total area of the sampling region is 16
    return area
antithetic_area(100000,500)

# Calculate mean and variance for zzzz :
pr_mean, pr_var = compute_varandmean(antithetic_area, nb_samples, itermax, runs)

# Calculate confidence interval :
ci_lower, ci_upper = conf_int(pr_mean, pr_var, runs, p=0.95)

print(f"Pure Random Sampling Mean Area: {pr_mean:.4f}")
print(f"Pure Random Sampling Variance: {pr_var:.4e}")
print(f"95% Confidence Interval: [{ci_lower:.4f}, {ci_upper:.4f}]")
