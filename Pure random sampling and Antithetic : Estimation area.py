import numpy as np
import matplotlib.pyplot as plt

def pure_random_sampling(N, max_iter):
    """
    Estimates the area of the Mandelbrot set using pure random sampling.
    """
    counter = 0
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2

    for _ in range(N):
        x_sample = np.random.uniform(xmin, xmax)
        y_sample = np.random.uniform(ymin, ymax)
        c = x_sample + 1j * y_sample

        z = 0
        for n in range(max_iter):
            z = z**2 + c
            if abs(z) > 2:
                break
        else:
            counter += 1

    proportion_of_points = counter / N
    area = 16 * proportion_of_points
    return area

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

#My Parameters
sample_sizes = range(100, 10100, 100)
max_iter = 500

# Compute areas for pure and antithetic sampling
pure_areas = [pure_random_sampling(N, max_iter) for N in sample_sizes]
antithetic_areas = [antithetic_area(N, max_iter) for N in sample_sizes]

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, pure_areas, label="Random", linestyle="-", alpha=0.8)
plt.plot(sample_sizes, antithetic_areas, label="Random(Antithetic)", linestyle="--", alpha=0.8)
plt.xlabel("Number of Samples")
plt.ylabel("Area")
plt.title("Comparison of Pure and Antithetic Sampling")
plt.legend()
plt.grid()
plt.show()
