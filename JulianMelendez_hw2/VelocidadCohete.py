import numpy as np
import matplotlib.pyplot as plt


b = np.array((45.948,119.985,231.497))
t = np.array((2.0,5.0,9.0))
A = np.zeros((len(b),len(b)))

def func(x):
	v = np.array((x**2,x,1.0))
	return v

def array(A,v):
	for i in range(len(A)):
		A[i,:] = func(t[i])
	return A

A = array(A,t)

def gauss(A,b): 
	for j in range(len(A)):
		a = A[j,j]
		A[j,:] = A[j,:]/a
		b[j] = b[j]/a
		for i in range(len(A)):
			if(i != j): 
				c = A[i,j]
				A[i,:] = A[i,:] - A[j,:]*c
				b[i] = b[i] - b[j]*c
	return(A,b)

coef = gauss(A,b)[1] 
def function(x):
	f = coef[0]*x**2 + coef[1]*x + coef[2]
	return f

x = np.linspace(0,12)
b = np.array((45.948,119.985,231.497))
plt.scatter(t,b,label='Datos',color = 'r')
plt.plot(x,function(x),label='Velocidad', color = 'k')
plt.xlim(0,12)
plt.ylim(0,350)
plt.xlabel('Tiempo ($s$)')
plt.ylabel('Velocidad ($m/s$)')
plt.title('Velocidad Cohete')
plt.legend(loc=2)
plt.savefig('VelocidadCohete.pdf')

print('a1 =', coef[0],'a2 =', coef[1],'a3 =', coef[2],'la velocidad en 7 segundos es:',function(7))
