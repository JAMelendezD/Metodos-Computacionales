import numpy as np
import matplotlib.pyplot as plt


a = 0.0
b = np.pi
c = 0.0
d = 1.0
n = 100000
m = 100000
q = 1000
p = 1000
def function(x,y):
    	return (x+np.cos(y)*x)**3

def montecarlo(f, a, b,c,d,n,m):    
	x = np.random.random(n)*(b - a) + a
	y = np.random.random(m)*(d - c) + c
	fevaluacion = f(x,y)
	resultado = fevaluacion.mean()*(b - a)*(d - c)
	return resultado

def trapezoid(f, a, b,c,d, q,p):
	x = np.linspace(a, b, q-1)
	y = np.linspace(c, d, p-1)
	h = (b-a)/q
	k = (d-c)/p
	resultado = 0
	resultado = f(a,c) + f(a,d) + f(b,c) + f(b,d) 
	for i in range(q-1):
		resultado += 2*(f(x[i],c)) + 2*(f(x[i],d)) + 2*(f(a,y[i])) + 2*(f(b,y[i])) 
		for j in range(p-1):
			resultado +=  4*(f(x[i],y[j]))
	resultado *= h*k/4
	return resultado
        

valorM = montecarlo(function, a, b,c,d,n,m)
valorT = trapezoid(function, a, b,c,d, q,p)
print('El valor de la integral con el metodo Montecarlo es', valorM, 'y con el metodo de trapezoides es', valorT)
