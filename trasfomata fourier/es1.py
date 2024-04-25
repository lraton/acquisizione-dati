import numpy as np
import matplotlib.pyplot as plt 
from scipy import signal

t = np.linspace(0, 1, 1000)

def x(t1):  # N is the number of harmonics
    som = 0
    f0=50
    for k in range(1, 100):
        if k % 2 != 0:
            som=som+(1/k*pow(-1,(k-1)/2)*np.cos(2*np.pi*k*f0*t1))
    return 1/2+2/np.pi*som

xt = [x(i) for i in t]

plt.plot(t,xt)
plt.show()