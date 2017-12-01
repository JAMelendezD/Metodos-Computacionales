import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

#importar imagenes
Barca = plt.imread("Barcelona.jpg")
Paris = plt.imread("Paris.jpg")
frac = plt.imread("frac.jpeg")
tri = plt.imread("triangulos.png")

#metodo para usar solo intensidades
def gris(imagen):
	r = imagen[:,:,0]
	g = imagen[:,:,1] 
	b = imagen[:,:,2] 
	gris =  0.299*r +  0.587*g +  0.114*b
	return gris

#convertir imagenes a intensidades
BarcaG = gris(Barca)
ParisG = gris(Paris)
fracG = gris(frac)
triG = gris(tri)


#plot imagenes
fig1 = plt.figure()
plt.subplot(221)
plt.imshow(BarcaG,cmap='gray' )
plt.title('Barca')
plt.ylabel('Pixel')
plt.subplot(223)
plt.imshow(ParisG,cmap='gray')
plt.title('Paris')
plt.xlabel('Pixel')
plt.ylabel('Pixel')
plt.subplot(222)
plt.imshow(fracG,cmap='gray')
plt.title('Fractal A')
plt.subplot(224)
plt.imshow(triG,cmap='gray')
plt.title('Fractal S')
plt.xlabel('Pixel')
fig1.savefig("imagenes.pdf")

#definir tamano de las imagenes 
HB,WB = np.shape(BarcaG)
HP,WP = np.shape(ParisG)
HF,WF = np.shape(fracG)
HT,WT = np.shape(triG)
#definir mitad de las imagenes 
hWB = int(0.5*WB)
hHB = int(0.5*HB)
hWP = int(0.5*WP)
hHP = int(0.5*HP)
hWF = int(0.5*WF)
hHF = int(0.5*HF)
hWT = int(0.5*WT)
hHT = int(0.5*HT)

#transformada de Fourier
TBarca = np.fft.fft2(BarcaG)/(HB*WB)
TParis = np.fft.fft2(ParisG)/(HP*WP)
Tfrac = np.fft.fft2(fracG)/(HF*WF)
Ttri = np.fft.fft2(triG)/(HT*WT)

#obtener frecuencias correctas
f_Barca = np.fft.fftshift(TBarca)
f_Paris = np.fft.fftshift(TParis)
f_frac = np.fft.fftshift(Tfrac)
f_tri = np.fft.fftshift(Ttri)

#descartar parte imaginaria
magB = np.abs(f_Barca)
magP = np.abs(f_Paris)
magf = np.abs(f_frac)
magt = np.abs(f_tri)

#plot de transformadas
fig2 = plt.figure()
plt.subplot(221)
plt.imshow(np.log(magB))
plt.title('Barca')
plt.ylabel('Pixel')
plt.subplot(223)
plt.imshow(np.log(magP))
plt.title('Paris')
plt.xlabel('Pixel')
plt.ylabel('Pixel')
plt.subplot(222)
plt.imshow(np.log(magf))
plt.title('Fractal A')
plt.subplot(224)
plt.imshow(np.log(magt))
plt.title('Fractal S')
plt.xlabel('Pixel')
fig2.savefig("transformadas.pdf")

#arrays con corte horizontal en la mitad
A = np.log(magB[hHB,:])
B = np.log(magP[hHP,:])
C = np.log(magf[hHF,:])
D = np.log(magt[hHT,:])

#plot de cortes horizontales
fig3 = plt.figure()
plt.subplot(221)
plt.plot(A)
plt.title('Barca')
plt.ylabel('Intensidad')
plt.subplot(223)
plt.plot(B)
plt.title('Paris')
plt.xlabel('Pixel')
plt.ylabel('Intensidad')
plt.subplot(222)
plt.plot(C)
plt.title('Fractal A')
plt.subplot(224)
plt.plot(D)
plt.title('Fractal S')
plt.xlabel('Pixel')
fig3.savefig("cortes_transversales.pdf")

#filtro que elimina lineas verticales cerca del centro
for i in range(-20,20):
	f_Barca[:,hWB+i] = np.zeros(HB)

#transformada inversa y recuperar frecuencias 
f_BarcaS = np.fft.ifftshift(f_Barca)
TBarcaS = np.fft.ifft2(f_BarcaS)
magBS = np.abs(TBarcaS)

#plot de Barca luego del filtro
fig4 = plt.figure()
plt.imshow(magBS,cmap='gray')
plt.title('Barca')
plt.ylabel('Pixel')
plt.xlabel('Pixel')
fig4.savefig("sin_horizontales.pdf")





