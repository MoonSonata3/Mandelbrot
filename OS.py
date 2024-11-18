import numpy as np
import matplotlib.pyplot as plt

def orthogonal_sampling(a,b,c,d, no_of_subspaces): #effectively it will be no_of_subspaces^2
  #we will divide the rectangle (a,b) for Re-axis and (c,d) for the Im-axis in n subspaces and then take a sample in every subspace
  step_x = (b-a)/no_of_subspaces
  step_y = (d-c)/no_of_subspaces
  orthogonal_samples = []

  #sample a random coordinate in all subspaces:
  for i in range(no_of_subspaces):
    for j in range(no_of_subspaces):
      x_coord = a + (i + np.random.uniform()) * step_x
      y_coord = c + (j + np.random.uniform()) * step_y
      orthogonal_samples.append((x_coord, y_coord))

  return orthogonal_samples

#now do the sampling: (no of subspaces is essentially the same as "s" in last question)
orthogonal_samples = orthogonal_sampling(a=-2, b=2, c=-2, d=2, no_of_subspaces=100)
orthogonal_samples = np.array(orthogonal_samples)

#function to check if point is inside the set:
def is_in_set(c, max_iter):
    z = 0
    for n in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return n #stop iterating after it has escaped convergence radius and return number of iterations
    return max_iter #otherwise return the maximum number of iterations


area_per_no_of_subspaces = []
for subspaces in range(1,250):
    samples = orthogonal_sampling(a=-2, b=2, c=-2, d=2, no_of_subspaces=subspaces)
    samples = np.array(samples)

    inside = []
    for x, y in samples:
        c = complex(x, y)
        n_iter = is_in_set(c, max_iter=500)
        if n_iter == 500:
            inside.append((x, y))

    #area:
    sample_area = (2 - (-2)) * (2 - (-2))
    orthogonal_area = (len(inside) / len(samples)) * sample_area
    area_per_no_of_subspaces.append(orthogonal_area)

area_per_no_of_subspaces = np.array(area_per_no_of_subspaces)
mean_area2 = np.mean(area_per_no_of_subspaces[50:])

sem_list = []
true_area = 1.514
for j in range(1, len(area_per_no_of_subspaces) + 1):
    mse_j = np.mean((area_per_no_of_subspaces[:j] - true_area) ** 2)
    sem_j = np.sqrt(mse_j)
    sem_list.append(sem_j)


plt.plot(area_per_no_of_subspaces, label="area")
plt.errorbar(np.arange(1,250)[::5], area_per_no_of_subspaces[::5], yerr=np.array(sem_list)[::5], fmt='o', color='blue', ecolor='blue', capsize=4, alpha=0.7, label='Error (SEM)')
yticks = plt.yticks()[0] 
yticks = yticks[yticks != 1.50]
plt.yticks(yticks)
plt.axhline(mean_area2, label="mean area", color='red', linestyle='--')
plt.text(x=-15, y=mean_area2, s=f'{mean_area2:.3f}', color='red', va='center', ha='right', fontsize=10)
plt.xlabel("Number of Subspaces (n)")
plt.ylabel("Estimated Area")
# plt.suptitle("Convergence of Area (Orthogonal sampling)")
# plt.title("First run")
plt.grid()
plt.legend()
plt.show()
