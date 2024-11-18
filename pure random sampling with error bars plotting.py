import numpy as np
import matplotlib.pyplot as plt

def pure_random_sampling_run(nb_samples, itermax, step):
    """
    Run a single simulation of pure random sampling and record convergence at intervals.
    """
    counter = 0
    convergence = []

    for i in range(1, nb_samples + 1):
        c = complex(np.random.uniform(-2, 2), np.random.uniform(-2, 2))
        z = 0
        for _ in range(itermax):
            z = z**2 + c
            if abs(z) > 2:
                break
        else:
            counter += 1

        if i % step == 0:
            proportion = counter / i
            estimated_area = 16 * proportion
            convergence.append(estimated_area)

    return convergence

def pure_random_sampling_with_error(nb_samples, itermax, step, runs):
    """
    Perform multiple runs of pure random sampling to calculate mean and RMSE."""

    all_convergences = []

    #Many runs
    for _ in range(runs):
        convergence = pure_random_sampling_run(nb_samples, itermax, step)
        all_convergences.append(convergence)

    #For easy computations
    all_convergences = np.array(all_convergences)

    mean_areas = np.mean(all_convergences, axis=0)
    rmse_errors = np.sqrt(np.mean((all_convergences - mean_areas)**2, axis=0))

    x_values = np.arange(step, nb_samples + 1, step)
    return x_values, mean_areas, rmse_errors

#My parameters
nb_samples = 100000
itermax = 500
step = 10000
runs = 10

# Compute results
x_values, mean_areas, rmse_errors = pure_random_sampling_with_error(nb_samples, itermax, step, runs)

# Plotting with error bars
plt.figure(figsize=(10, 6))
plt.errorbar(x_values, mean_areas, yerr=rmse_errors, fmt='o-', capsize=5, label="Pure Random Sampling")
plt.axhline(y=np.mean(mean_areas), color="green", linestyle="--", label="Mean Area")
plt.xlabel("Number of Samples")
plt.ylabel("Estimated Area")
plt.title("Convergence of Mandelbrot Set Area Estimation with Error Bars")
plt.legend()
plt.grid()
plt.show()
