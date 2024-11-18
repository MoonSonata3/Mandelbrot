import numpy as np
import matplotlib.pyplot as plt

def pure_random_sampling_fixed_samples(nb_samples, itermax):
    """
    Estimates the area of the Mandelbrot set for a fixed number of random samples and a given itermax.

    Parameters:
        nb_samples: Total number of points to sample.
        itermax: Maximum number of iterations to test for divergence.

    Returns:
        Estimated area of the Mandelbrot set.
    """
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

# My parameters
nb_samples = 100000  # Fixed number of random samples
itermax_values = range(10, 510, 10)
areas = []

# We compute area for each itermax
for itermax in itermax_values:
    area = pure_random_sampling_fixed_samples(nb_samples, itermax)
    areas.append(area)

# Stabilized mean area (ignore the first 10 values)
stable_start = 10  # Ignore the first 10 itermax values
mean_area = np.mean(areas[stable_start:])

# Plotting the results
plt.plot(itermax_values, areas, label="Estimated Area")
plt.axhline(y=mean_area, color="green", linestyle="--", label=f"Mean Area (from {stable_start} values): {mean_area:.3f}")
plt.xlabel("Maximum Iterations (itermax)")
plt.ylabel("Estimated Area")
plt.title("Convergence of Mandelbrot Set Area Estimation with Itermax")
plt.legend()
plt.grid()
plt.show()
