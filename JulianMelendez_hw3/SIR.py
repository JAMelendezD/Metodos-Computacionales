import numpy as np
import matplotlib.pyplot as plt

#Inicializacion
tmin = 0.0
tmax = 30.0
h = 0.01
puntos = int((tmax-tmin)/h)
beta1 = 0.0022
gamma1 = 0.45
beta2 = 0.001
gamma2 = 0.2

t1 = np.zeros(puntos)
I1 = np.zeros(puntos)
R1 = np.zeros(puntos)
S1 = np.zeros(puntos)

t2 = np.zeros(puntos)
I2 = np.zeros(puntos)
R2 = np.zeros(puntos)
S2 = np.zeros(puntos)


#Frontera
t1[0] , t2[0] =  tmin,tmin
R1[0] , R2[0] =  0.0,0.0
I1[0] , I2[0] =  1.0,1.0
S1[0] , S2[0] =  770.0,770.0

def f1(gamma,t,I,R):
    return gamma*I

def f2(gamma,beta,t,I,S):
    return beta*I*S-gamma*I

def f3(beta,t,I,S):
    return -beta*I*S

def Runge(gamma,beta,t_a,I_a,S_a,R_a,f1,f2,f3):
	orden = 4
	kS = np.zeros(orden)
	kI = np.zeros(orden)
	kR = np.zeros(orden)
	ti = np.zeros(orden)
	Ii = np.zeros(orden)
	Si = np.zeros(orden)
	Ri = np.zeros(orden)
	for i in range(orden):
		if(i==0):
			w = 0.0
			ti[i] = t_a + w
			Ri[i] = R_a + w*kR[i]
			Ii[i] = I_a + w*kI[i]
			Si[i] = S_a + w*kS[i]
			kR[i] = f1(gamma,ti[i],Ii[i],Ri[i])
			kI[i] = f2(gamma,beta,ti[i],Ii[i],Si[i])
			kS[i] = f3(beta,ti[i],Ii[i],Si[i])    
		elif(i<=2):
			w = (h/2.0)
			ti[i] = t_a + w
			Ri[i] = R_a + w*kR[i-1]
			Ii[i] = I_a + w*kI[i-1]
			Si[i] = S_a + w*kS[i-1]
			kR[i] = f1(gamma,ti[i],Ii[i],Ri[i])
			kI[i] = f2(gamma,beta,ti[i],Ii[i],Si[i])
			kS[i] = f3(beta,ti[i],Ii[i],Si[i])   
		else:
			w = h
			ti[i] = t_a + w
			Ri[i] = R_a + w*kR[i-1]
			Ii[i] = I_a + w*kI[i-1]
			Si[i] = S_a + w*kS[i-1]
			kR[i] = f1(gamma,ti[i],Ii[i],Ri[i])
			kI[i] = f2(gamma,beta,ti[i],Ii[i],Si[i])
			kS[i] = f3(beta,ti[i],Ii[i],Si[i])  

	    
	    
	KR = (kR[0] + 2.0*kR[1] + 2.0*kR[2] + kR[3])/(6.0)
	KI = (kI[0] + 2.0*kI[1] + 2.0*kI[2] + kI[3])/(6.0)
	KS = (kS[0] + 2.0*kS[1] + 2.0*kS[2] + kS[3])/(6.0)
	    
	tn = t_a + h
	In = I_a + h*KI
	Rn= R_a + h*KR
	Sn = S_a + h*KS
	return tn,In,Sn,Rn



#Llenar Array con la solucion 
for i in range(1,puntos):
	t1[i],I1[i],S1[i],R1[i] = Runge(gamma1,beta1,t1[i-1],I1[i-1],S1[i-1],R1[i-1],f1,f2,f3)
#Llenar Array con la solucion 
for i in range(1,puntos):
	t2[i],I2[i],S2[i],R2[i] = Runge(gamma2,beta2,t2[i-1],I2[i-1],S2[i-1],R2[i-1],f1,f2,f3)

#Plot
fig1, axarr = plt.subplots(2, sharex=True, sharey=True)
axarr[0].plot(t1,R1, label = 'Recuperados')
axarr[0].plot(t1,I1, label = 'Infectados')
axarr[0].plot(t1,S1, label = 'Suceptibles')
axarr[0].set_title('Caso 1')
axarr[0].set_ylabel('Numero de individuos')
axarr[0].legend()
axarr[1].plot(t2,R2, label = 'Recuperados')
axarr[1].plot(t2,I2, label = 'Infectados')
axarr[1].plot(t2,S2, label = 'Suceptibles')
axarr[1].set_title('Caso 2')
axarr[1].set_xlabel('t(dias)')
axarr[1].set_ylabel('Numero de individuos')
axarr[1].legend()
fig1.savefig('SIR.pdf')

I1max = np.argmax(I1)
I2max = np.argmax(I2)

print('caso 1, tiempo I_max(dias):', t1[I1max])
print('caso 2, tiempo I_max(dias):', t2[I2max])


