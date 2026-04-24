import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt("Exercise 4/Data/Day 1/sol 3.txt", skiprows=1)
data2 = np.loadtxt("Exercise 4/Data/Day 1/H2.txt", skiprows=1)
back = np.loadtxt("Exercise 4/Data/Day 1/H2 background.txt", skiprows=1)

fig, ax = plt.subplots()
ax.plot(data2[::,0], data2[::,1]-back[::,1])
#ax.plot(data[::,0], data[::,1])
rydberg_constant = 1.097e7 * 1e-9 # nm^-1
Balmer = [(rydberg_constant * (1/4 - 1/(i)**2))**(-1) for i in range(3,10)]
for lamb in Balmer:
    ax.axvline(lamb, color = "red", linestyle = "--", alpha = 0.5)

ax.set_ylim(min(data2[::,1]-back[::,1]), max(data2[::,1]-back[::,1]))
plt.show()