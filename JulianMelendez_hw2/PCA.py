import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

Datos = np.loadtxt('siliconwaferthickness.csv', skiprows=1,delimiter=',')



def normalizar(A):
	B = np.zeros(np.shape(A))
	for i in range(len(A[0,:])):
		B[:,i]  = (A[:,i] - np.mean(A[:,i]))/np.std(A[:,i])
	return B


DatosN = normalizar(Datos)


colores = ['k','b','r','c','g','y','violet','coral','m']
fig1 = plt.figure()
for i in range(len(DatosN[0,:])):
	plt.plot(DatosN[:,i],c = colores[i],label = '$G_%d$'%(i+1))
plt.legend()
plt.ylabel('Grosor')
plt.title('Visualizacion Datos')
fig1.savefig('ExploracionDatos.pdf')




def co(array):
	matriz = np.zeros((len(array[0]),len(array[0])))
	for i in range(len(array[0])):
		for j in range(len(array[0])):
			x_i = array[:,i] 
			x_j = array[:,j]
			promedio_i = sum(x_i)/len(x_i)
			promedio_j = sum(x_j)/len(x_j)
			valor = (x_i - promedio_i)*(x_j - promedio_j)
			matriz[i,j] = sum(valor)/(len(valor)-1)
	return matriz

cov_matrix = co(DatosN)





values1, vectors1 = np.linalg.eig(cov_matrix)

vectors = np.zeros(np.shape(vectors1))	
vectors[:,0] = vectors1[:,0]
vectors[:,1] = vectors1[:,1]
vectors[:,2] = vectors1[:,2]
vectors[:,3] = vectors1[:,3]
vectors[:,4] = vectors1[:,8]
vectors[:,5] = vectors1[:,7]
vectors[:,6] = vectors1[:,6]
vectors[:,7] = vectors1[:,5]
vectors[:,8] = vectors1[:,4]

values2 = np.sort(values1)
values = values2[::-1]

print ('Los autovalores son',values,'los autovectores son',vectors, 'los componentes principales serian los primeros cuatro')



P = np.dot(vectors.T,DatosN.T)


fig2 = plt.figure()
plt.scatter(P[0,:],P[1,:])
plt.xlabel('PC $G_1$')
plt.ylabel('PC $G_2$')
plt.title('$G_1$ vs $G_2$')
fig2.savefig('PCAdatos.pdf')



fig3 = plt.figure()
for i in range(len(DatosN[0,:])):
	plt.scatter(vectors[i,0],vectors[i,1],c = colores[i],label = '$G_%d$'%(i+1))
plt.legend(loc=2)
plt.xlabel('PC $G_1$')
plt.ylabel('PC $G_2$')
plt.title('Agrupaciones Variables')
fig3.savefig('PCAvariables.pdf')

print ('Teniendo en cuenta la ultima grafica se ve que los grupos agrupados serian los correspondientes a la variables $G_1$, $G_2$, $G_3$, $G_4$, $G_5$ las demas no se ve ningun tipo de agrupacion por lo cual se podrian tomar medidas de una unica variable interna en especial la del medio y agruparla con grosor interno y luego medir los otros cuatro puntos asi se reduciria el sistema a una variable interna y cuatro externas, se pasaria de 9 variables a 5 variables')




