# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:51:35 2019

@author: Pierre
"""

#P######################################## PATH
import os
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    #Mithuran
os.chdir('D:/Users/Pierre/Documents/8 - Scolarite/ECE/PPE/PPE_GIT/Python')    #Pierre
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    'Mithuran
#os.chdir('/Users/nmace/Documents/GitHub/PPE_GIT/Python')          #Nicolas


######################################### INISTIALISATION ######################@
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Classes import *


d_broker = pd.read_csv("Data/Courtiers.txt",header=0, delimiter=" ")
data = pd.read_csv("Data/d_historique.txt", header=0, delimiter="\t")

##################### BODY ########################
### BROKER
b1= Broker("BoursoramaDecouverte",(0,500,1.99,0,500,10**10,0,0.006))
b2= Broker("BoursoramaClassic", (0,5000,5.5,0,5000,10**10,0,0.0048))


#### NICOLAS

u1=User("Macé", "Nicolas")
p1= Portfolio(b1, 0.30, 0.15,10000)

s1=Stock("NATIXIS_SPOT","€")
s2=Stock("CAC_SPOT","P",5894)

i1=Investment(s1,100,"07/02/2019",6.95)
i2=Investment(s2,10,"07/02/2019",5365.83)

p1.add_ptf_investment(i1,data)
#p1.add_ptf_investment(i2)

# FUNCTION INTERMEDIARE

m_PnL, value = strat_EC_1(300, p1,0,0,263,1)


print(np.mean(m_PnL))
print(np.std(m_PnL))



def chart(Y1, Y2):
    

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2, right=0.85)
    
    newax = fig.add_axes(ax.get_position())
    newax.patch.set_visible(False)
    
    newax.yaxis.set_label_position('right')
    newax.yaxis.set_ticks_position('right')
    
    newax.spines['bottom'].set_position(('outward', 35))
    
    ax.plot(Y1, 'r-')
    ax.set_xlabel('Red X1-axis', color='red')
    ax.set_ylabel('Y1', color='red')
    
    
    newax.plot(Y2, 'g-')
    
    newax.set_xlabel('Green X1-axis', color='green')
    newax.set_ylabel('Y2', color='green')
    
    print(" Moyenne :"+str(np.mean(m_PnL))+" Std :"+str(np.std(m_PnL)))
    

    plt.show()
chart(m_PnL,value)
