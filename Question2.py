import numpy as np
import matplotlib.pyplot as plt

def Mandel_area(N,max_iter):
    counter = 0

    for i in range(N):
        c = complex(np.random.uniform(-2, 2), np.random.uniform(-2, 2))
        z = 0

        for n in range(max_iter):
            z = z**2 + c
            if abs(z) > 2:
                break

        else :
            counter += 1
    proportion_of_points= counter/N
    area=16*proportion_of_points
    return area
  N = 100000  # samples
i = 500  # iteration count
A_is = 1.514
areas = []
differences = []

# A_js for j < i
for j in range(10, i, 10):
    area_j = Mandel_area(N, j)
    areas.append(area_j)
    differences.append(area_j - A_is)

#plot
j_values = range(10, i, 10)
plt.figure(figsize=(10, 6))
plt.plot(j_values, differences, marker='o', linestyle='-')
plt.xlabel("Iteration Count (j)")
plt.ylabel("Difference (A_js - A_is)")
plt.title("Convergence of Difference at 10000 samples")
plt.grid()
plt.show()
