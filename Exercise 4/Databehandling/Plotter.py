import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Exercise 4/Data/Day 1/sol 3.txt", skiprows=1)
data2 = np.loadtxt("Exercise 4/Data/Day 1/H2.txt", skiprows=1)
back = np.loadtxt("Exercise 4/Data/Day 1/H2 background.txt", skiprows=1)

fig, ax = plt.subplots()
ax.plot(data2[::,0], data2[::,1]-back[::,1])
ax.plot(data[::,0], data[::,1])

plt.show()