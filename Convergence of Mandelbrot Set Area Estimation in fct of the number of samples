import numpy as np
import matplotlib.pyplot as plt

def pure_random_sampling_convergence(nb_samples, itermax, step=10000):
    """
    Estimates the area of the Mandelbrot set with pure random sampling and tracks convergence.

    Parameters:
        nb_samples: Total number of points to sample.
        itermax: Maximum number of iterations to test for divergence.
        step: Interval to record intermediate results for convergence tracking.

    Returns:
        area: Estimated area.
        convergence: List of estimated areas at every step.
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

        #Record data
        if i % step == 0:
            proportion = counter / i
            estimated_area = 16 * proportion
            convergence.append(estimated_area)

    #Estimated area
    proportion = counter / nb_samples
    area = 16 * proportion

    return area, convergence

#My parameters
nb_samples = 1000000
itermax = 500
step = 10000
stable_start = 10 #We decided to skip over the 10 first, so we avoid the fluctuations.

#
estimated_area, convergence = pure_random_sampling_convergence(nb_samples, itermax, step)

#Calculate the mean average, so we can have a reference
mean_area = np.mean(convergence[stable_start:])

#Plotting convergence
x = np.arange(step, nb_samples + step, step)
plt.plot(x, convergence, label="Estimated Area")
plt.axhline(y=mean_area, color="green", linestyle="--", label=f"Mean Area (from {stable_start} steps): {mean_area:.3f}")
plt.xlabel("Number of Samples")
plt.ylabel("Estimated Area")
plt.title("Convergence of Mandelbrot Set Area Estimation in fct of the number of samples")
plt.legend()
plt.grid()
plt.show()

