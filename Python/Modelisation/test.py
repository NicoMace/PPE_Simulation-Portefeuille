# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:22:43 2019

@author: Pierre
"""

import numpy as np
from pylab import plot, show, grid, xlabel, ylabel
import brownian
import blacksholes

# Total time.
T = 1
# Number of steps.
N = 12
# Time step size
dt = T/N
# Number of realizations to generate.
NumberOfRealizations = 100
# Create an empty array to store the realizations.
x1 = np.empty((NumberOfRealizations,N+1))
# Initial values of x1.
x1[:, 0] = 0
# Annual yield.
AnnualYield=0.02
# Create an empty array to store the realizations.
x2 = np.empty((NumberOfRealizations,N+1))
# Initial values of x2.
x2[:, 0] = 100


# Create an empty array to store the realizations.
x3 = np.empty((NumberOfRealizations,N+1))
# Initial values of x.
x3[:, 0] = 0

# Brownian motion plot.
brownian.comp_brownian(x1[:,0], N, dt, out=x1[:,1:])

t = np.linspace(0.0, N*dt, N+1)
for k in range(NumberOfRealizations):
    plot(t, x1[k])
xlabel('t', fontsize=16)
ylabel('x', fontsize=16)
grid(True)
show()

# Black Scholes plot.
blacksholes.comp_price_model_bs(x2[:, 0], N,NumberOfRealizations,T,AnnualYield,out=x2[:,1:])

t = np.linspace(0.0, N*dt, N+1)
for k in range(NumberOfRealizations):
    plot(t, x2[k])
xlabel('t', fontsize=16)
ylabel('x', fontsize=16)
grid(True)
show()