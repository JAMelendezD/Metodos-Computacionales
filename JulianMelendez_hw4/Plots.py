import matplotlib.pyplot as plt
import numpy as np
import scipy
import os
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import scipy.io.wavfile


t = [0,9170,9290,9600]
T = ['t=0','t=T/8','t=T/4','t=T/2']
colores = ['k','b','r','c']
fig1 = plt.figure()

for i in range(4):
	x = np.zeros((129,4))
	up1 = np.zeros((129,4))
	os.system('echo %d|./Ondas.x' %t[i])
	datos = np.genfromtxt('datos.txt' , delimiter = ',')
	x[:,i] = datos[:,0]
	up1[:,i] = datos[:,1]
	plt.plot(x[:,i],up1[:,i],c = colores[i],label = '$%s$'%T[i])
plt.legend()
plt.title('Cuerda')
fig1.savefig('Cuerda.pdf')


to = [0,110,160,250]
fig2 = plt.figure()
for i in range(4):
	x = np.zeros((129,4))
	up2 = np.zeros((129,4))
	os.system('echo %d|./Ondas.x' %to[i])
	datos = np.genfromtxt('datos.txt' , delimiter = ',')
	x[:,i] = datos[:,0]
	up2[:,i] = datos[:,2]
	plt.plot(x[:,i],up2[:,i],c = colores[i],label = '$%s$'%T[i])
plt.legend()
plt.title('Onda')
fig2.savefig('Onda.pdf')


os.system('echo %d|./Ondas.x' %100000)
A = np.genfromtxt('datosA.txt')*1000
scipy.io.wavfile.write('sonido.wav',1000,A)


fig = plt.figure()
ax = plt.axes(xlim=(0, 0.7), ylim=(-2.0, 2.0))
line, = ax.plot([], [])

def init():
    line.set_data([], [])
    return line,

def animate(j):
	os.system('echo %d|./Ondas.x' %j)
	datos = np.genfromtxt('datos.txt' , delimiter = ',')
	x = datos[:,0]
	up2 = datos[:,2]
	line.set_data(x, up2)
	return line,



anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)

anim.save('cuerda.mp4', fps=60, extra_args=['-vcodec', 'libx264'])


x = np.linspace(0,0.5,101)
y = np.linspace(0,0.5,101)
X,Y = np.meshgrid(x,y)


fig5 = plt.figure()
os.system('echo %d|./Ondas.x' %0)
z = np.genfromtxt('datos2.txt')
z1 = np.array(z[:])
z2 = z1.reshape((101,101))
ax = fig5.gca(projection='3d')
ax.plot_surface(X, Y, z2,cmap=cm.autumn)
fig5.savefig("Tambor1.pdf")

fig6 = plt.figure()
os.system('echo %d|./Ondas.x' %35)
z = np.genfromtxt('datos2.txt')
z1 = np.array(z[:])
z2 = z1.reshape((101,101))
ax = fig6.gca(projection='3d')
ax.plot_surface(X, Y, z2,cmap=cm.autumn)
fig6.savefig("Tambor2.pdf")

fig7 = plt.figure()
os.system('echo %d|./Ondas.x' %50)
z = np.genfromtxt('datos2.txt')
z1 = np.array(z[:])
z2 = z1.reshape((101,101))
ax = fig7.gca(projection='3d')
ax.plot_surface(X, Y, z2,cmap=cm.autumn)
fig7.savefig("Tambor3.pdf")

fig8 = plt.figure()
os.system('echo %d|./Ondas.x' %100)
z = np.genfromtxt('datos2.txt')
z1 = np.array(z[:])
z2 = z1.reshape((101,101))
ax = fig8.gca(projection='3d')
ax.plot_surface(X, Y, z2,cmap=cm.autumn)
fig8.savefig("Tambor4.pdf")


figT = plt.figure()
ax = figT.gca(projection='3d')
ax.set_xlim(0.0,0.5)
ax.set_ylim(0.0,0.5)
ax.set_zlim(-0.01,0.01)


def animateT(j):
	ax.clear()
	ax.set_xlim(0.0,0.5)
	ax.set_ylim(0.0,0.5)
	ax.set_zlim(-0.01,0.01)
	os.system('echo %d|./Ondas.x' %j)
	z = np.genfromtxt('datos2.txt')
	z1 = np.array(z[:])
	z2 = z1.reshape((101,101))
	line = ax.plot_surface(X,Y,z2,cmap=cm.autumn)
	return line,

anim = animation.FuncAnimation(figT, animateT,frames=100, interval=20, blit=True)
anim.save('Tambor.mp4', fps=60, extra_args=['-vcodec', 'libx264'])






os.system('rm datos.txt')
os.system('rm datos2.txt')
os.system('rm datosA.txt')

