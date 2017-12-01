import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from numpy import linalg as LA


MarteP = np.loadtxt("MarsOrbit.dat" , usecols=(1,2,3))*149597870700
MarteT = np.loadtxt("MarsOrbit.dat", usecols=(0))*365*24*60*60
TierraP = np.loadtxt("EarthOrbit.dat", usecols=(1,2,3))*149597870700
TierraT = np.loadtxt("EarthOrbit.dat", usecols=(0))*365*24*60*60
Negro = mpatches.Patch(color='k', label='Orbita Tierra')
Azul = mpatches.Patch(color='b', label='Orbita Marte')
G = 6.674*10**(-11)

	
fig = plt.figure()
ax = fig.gca(projection='3d')
xMarte = MarteP[:,0]
yMarte = MarteP[:,1]
zMarte = MarteP[:,2]
xTierra = TierraP[:,0]
yTierra = TierraP[:,1]
zTierra = TierraP[:,2]
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('z (m)')
ax.plot(xTierra, yTierra, zTierra, label='Orbita Tierra',color ='k')
ax.plot(xMarte, yMarte, zMarte, label='Orbita Marte',color ='b')
ax.legend(loc = 1)
fig.savefig("Orbitas.pdf")

MarteV1 = np.zeros((len(MarteP[:,0]),len(MarteP[0,:])))
TierraV1 = np.zeros((len(TierraP[:,0]),len(TierraP[0,:])))


for j in range(len(MarteP[0,:])):
	for i in range(1,len(MarteP[:,0])-1):
		MarteV1[i,j] = (MarteP[:,j][i+1] - MarteP[:,j][i-1])/((MarteT[i+1] - MarteT[i-1]))

MarteV = MarteV1[1:-1]


for j in range(len(TierraP[0,:])):
	for i in range(1,len(TierraP[:,0])-1):
		TierraV1[i,j] = (TierraP[:,j][i+1] - TierraP[:,j][i-1])/((TierraT[i+1] - TierraT[i-1]))

TierraV = TierraV1[1:-1]



MarteA1 = np.zeros((len(MarteV[:,0]),len(MarteV[0,:])))
TierraA1 = np.zeros((len(TierraV[:,0]),len(TierraV[0,:])))

for j in range(len(MarteV[0,:])):
	for i in range(1,len(MarteV[:,0])-1):
		MarteA1[i,j] = (MarteV[:,j][i+1] - MarteV[:,j][i-1])/((MarteT[i+1] - MarteT[i-1]))

MarteA = MarteA1[1:-1]

for j in range(len(TierraV[0,:])):
	for i in range(1,len(TierraV[:,0])-1):
		TierraA1[i,j] = (TierraV[:,j][i+1] - TierraV[:,j][i-1])/((TierraT[i+1] - TierraT[i-1]))

TierraA = TierraA1[1:-1]


MarteP1 = MarteP[2:-2]
TierraP1 = TierraP[2:-2]



aceleracionT = LA.norm(TierraA, axis=1)
posicionT = LA.norm(TierraP1, axis=1)
MasaSolT1 = np.zeros(len(aceleracionT))

aceleracionM = LA.norm(MarteA, axis=1)
posicionM = LA.norm(MarteP1, axis=1)
MasaSolM1 = np.zeros(len(aceleracionM))

for j in range(len(aceleracionT)):
	MasaSolT1[j] = (aceleracionT[j]*posicionT[j]**2)/G 

for j in range(len(aceleracionM)):
	MasaSolM1[j] = (aceleracionM[j]*posicionM[j]**2)/G 


#for j in range(len(TierraA[0,:])):
	#aceleracion[j] = np.sqrt(TierraA[j,0]**2 + TierraA[j,1]**2 + TierraA[j,2]**2)
#for j in range(len(TierraP1[0,:])):
	#posicion[j] = np.sqrt(TierraP1[j,0]**2 + TierraP1[j,1]**2 + TierraP1[j,2]**2)

#for i in range(len(posicion)):
	#MasaSolT1[i] = aceleracion[i]*posicion[i]**2  


MasaSolT = np.mean(MasaSolT1)

MasaSolM = np.mean(MasaSolM1)



print('La masa del Sol obtenida a partir de las posiciones de la Tierra es', MasaSolT,'kg y la obtenida a partir de las posiciones de Marte es', MasaSolM,'kg')





