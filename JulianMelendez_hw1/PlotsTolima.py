#Final
import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as mpatches

Marzo = np.loadtxt('DatosMarzo.txt')
GRF = np.loadtxt('GRF_vs_EQ.txt')
Negro = mpatches.Patch(color='k', label='Todos los Meses')
Verde = mpatches.Patch(color='g', label='Mes de Marzo')


fig = plt.figure()
plt.scatter(Marzo[:,1],Marzo[:,0],color = 'g',s=100,label = 'Mes de Marzo')
plt.scatter(GRF[:,1],GRF[:,0], color = 'k',s = 10, label = 'Todos los Meses')
plt.title('Terremotos Tolima')
plt.ylabel('Glacier&&RockFall')
plt.xlabel('Largest Earthquake')
plt.legend()
fig.savefig("PlotTolima.pdf")


