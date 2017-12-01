import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt('datos.txt', delimiter = ',')

r = datos[:,0]
v = datos[:,1]

plt.scatter(r,v)
plt.show()
