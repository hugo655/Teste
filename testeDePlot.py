
import matplotlib.pyplot as plt
import numpy as np
from DFT import DFT



x = np.array(range(50))
x = np.cos(2*np.pi/21*x)

y = DFT(x)
eixo = np.array(range(len(y)))



markerline, stemlines, baseline = plt.stem(eixo, y, '-.')
plt.setp(baseline, 'color', 'r', 'linewidth', 2)
plt.show()
