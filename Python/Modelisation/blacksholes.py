# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:20:46 2019

@author: Pierre
"""

from math import exp
import numpy as np
from Modelisation import brownian

def comp_price_model_bs(x0,
                        N=12,
                        NumberOfRealizations=100,
                        T=1,
                        AnnualYield=0.02,
                        out=None):
    """help"""
    
    # Initial parameters.
    Volatility=1/N
    Yield=AnnualYield/N
    x0 = np.asarray(x0)
    
    # Create an empty array to store the realizations.
    BrownianMotion = np.empty((NumberOfRealizations,N+1))
    # Initial values of BrownianMotion.
    BrownianMotion[:,0]=0
    # Compute the brownian motion.
    brownian.comp_brownian(BrownianMotion[:,0],N,T/N,out=BrownianMotion[:,1:])
    # If `out` was not given, create an output array.
    if out is None:
        out = np.empty(x0.shape)
    
    # Modelization.
    for i in range(NumberOfRealizations):
        for j in range(N):
            out[i][j]=x0[0]*exp((Yield-(Volatility**2)/2)*i/N+Volatility*BrownianMotion[i][j+1])
    
    return out