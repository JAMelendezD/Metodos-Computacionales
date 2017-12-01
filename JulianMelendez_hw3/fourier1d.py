import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,fftfreq


datos = np.genfromtxt("funcion.dat")

t = datos[:,0]
f = datos[:,1]



def fourier(function):
	N = len(function)
	fourier = np.zeros(N)
	for i in range(N):
		coeficientes = 0.0
		for j in range(N):
			coeficientes += function[j]*np.exp((-2*np.pi*1j*i*j)/N)
		fourier[i] = abs(coeficientes)
	return fourier

n = len(f)
x = fourier(f)/n
dt = t[2]-t[1]
freq = fftfreq(n,dt)
fmax = np.argmax(x)
frecuencia = int(freq[fmax])

print('La frecuencia es:',frecuencia, 'Hz')





