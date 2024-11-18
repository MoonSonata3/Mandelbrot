import numpy as np
import matplotlib.pyplot as plt

def pure_random_sampling(N, max_iter):
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
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    counter = 0

    for _ in range(N // 2):  
        x_sample = np.random.uniform(xmin, xmax)
        y_sample = np.random.uniform(ymin, ymax)
        c = x_sample + 1j * y_sample

        ax_sample = (xmin + xmax) - x_sample
        ay_sample = (ymin + ymax) - y_sample
        antithetic_c = ax_sample + 1j * ay_sample

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
sample_sizes = [100, 200, 500, 1000, 2000, 5000, 10000]
max_iter = 500
runs = 100

#Storing lists
pure_std_devs = []
antithetic_std_devs = []

for N in sample_sizes:
    pure_areas = [pure_random_sampling(N, max_iter) for _ in range(runs)]
    antithetic_areas = [antithetic_area(N, max_iter) for _ in range(runs)]
    
    pure_std_devs.append(np.std(pure_areas, ddof=1))
    antithetic_std_devs.append(np.std(antithetic_areas, ddof=1))

# Plotting results
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, pure_std_devs, label="Random standard deviation", marker="o", linestyle="-")
plt.plot(sample_sizes, antithetic_std_devs, label="Antithetic standard deviation", marker="s", linestyle="--")
plt.xlabel("Number of Samples")
plt.ylabel("Standard Deviation")
plt.title("Comparison of Standard Deviation: Pure random vs Antithetic Sampling")
plt.legend()
plt.grid()
plt.show()
