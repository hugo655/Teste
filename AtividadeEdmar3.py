import matplotlib.pyplot as plt
import numpy as np
from DFT import DFT

'''
    Nesse primeiro exemplo vamos considerar uma janela de 32 e amostragem com periodo igual a 2
    O sinal no tempo e: x(t) = cos(2*pi*500*t) +  cos(2*pi*1500*t) 
'''




#Definindo o sinal amostrado com frequencia igual a 0.5 Hz limitado por uma janela de tamanho 27
T = 1.0/4500
N = 27
n = np.array(range(N))
x = np.cos(2*np.pi*500*T*n) + np.cos(2*np.pi*1500*T*n)


y = DFT(x)
eixo = np.array(range(len(y)))

markerline, stemlines, baseline = plt.stem(eixo, y, '-.')
plt.setp(baseline, 'color', 'r', 'linewidth', 2)
plt.show()

#Definindo o sinal amostrado com frequencia igual a 0.5 Hz limitado por uma janela de tamanho 90
T = 1.0/4500
N = 90
n = np.array(range(N))
x = np.cos(2*np.pi*500*T*n) + np.cos(2*np.pi*1500*T*n)


y = DFT(x)
eixo = np.array(range(len(y)))

markerline, stemlines, baseline = plt.stem(eixo, y, '-.')
plt.setp(baseline, 'color', 'r', 'linewidth', 2)
plt.show()