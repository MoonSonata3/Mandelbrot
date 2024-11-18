import numpy as np
import matplotlib.pyplot as plt
width = 300
height = 300
max_iter=300

# arrays of evenly spaced real and imaginary values
real = np.linspace(-2, 1, width)
im = np.linspace(-1.5, 1.5, height)

# meshgrid from the real and imaginary arrays
real_grid, imag_grid = np.meshgrid(real, im)

# Combine into a complex array
array = real_grid + 1j * imag_grid
result=np.zeros((height,width),int)
for i in range(height):
    for j in range(width):
        c=array[i,j]
        z=0
        count=0
        for k in range(max_iter):
            z=z**2+c
            count+=1
            if np.abs(z)>2:
                break
            result[i,j]=count

# Plot the result array with a colormap
plt.figure(figsize=(10, 10))
plt.imshow(result, cmap='RdGy', extent=(-2, 1, -1.5, 1.5), origin='lower')
plt.colorbar(label="Escape Iterations")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.title("Mandelbrot Set Visualization")
plt.show()
