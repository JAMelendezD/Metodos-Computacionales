import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt('RadialVelocities.dat')
masas = np.genfromtxt('datos.txt', delimiter =',')

r = datos[:,0]
v = datos[:,1]

mb = masas[0]
md = masas[1]
mh = masas[2]

bb = 0.2497
bd = 5.16
ad = 0.3105
ah = 64.3
c = bd+ad

V = (np.sqrt(mb)*r)/((r**2+bb**2)**0.75) + (np.sqrt(md)*r)/((r**2+c**2)**0.75) + np.sqrt(mh)/((r**2+ah**2)**0.25) 
fig = plt.figure()
plt.scatter(r,v)
plt.plot(r,V,c='r')
fig.savefig('Velocidad.pdf')

