import matplotlib.pyplot as plt
import numpy as np
from DFT import DFT

'''
    Nesse primeiro exemplo vamos considerar uma janela de 32 e amostragem com periodo igual a 2
    O sinal no tempo e: v(t) = cos(2*pi*t/16) + 0.75 cos(2*pi*t/8) 
'''




#Definindo o sinal amostrado com frequencia igual a 0.5 Hz limitado por uma janela de tamanho 32
T = 2
N = 8
n = np.array(range(N))
x = np.cos(2*np.pi/16*n*T) + 0.75*np.cos(2*np.pi/8*n*T)


y = DFT(x)
eixo = np.array(range(len(y)))
markerline, stemlines, baseline = plt.stem(eixo, y, '-.')
plt.setp(baseline, 'color', 'r', 'linewidth', 2)
plt.show()

