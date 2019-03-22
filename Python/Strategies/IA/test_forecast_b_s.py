#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:50:25 2019

@author: mithurangajendran
"""
#P######################################## PATH
import os
os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    #Mithuran
#os.chdir('D:/Users/Pierre/Documents/8 - Scolarite/ECE/PPE/PPE_GIT/Python')    #Pierre
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    'Mithuran
#os.chdir('/Users/nmace/Documents/GitHub/PPE_GIT/Python')          #Nicolas


######################################### INISTIALISATION ######################@
import pandas as pd
from pylab import plot
from Classes import *
from Strategies.IA.forecast_b_s import *

d_broker= pd.read_csv("Data/Courtiers.txt",header=0, delimiter=" ")
data= pd.read_csv("Data/d_historique.txt", header=0, delimiter="\t")

##################### BODY ########################

### BROKER
b1= Broker("BoursoramaDecouverte",(0,500,1.99,0,501,10**10,0,0.006))
b2= Broker("BoursoramaClassic", (0,5000,5.5,0,5001,10**10,0,0.0048))

#### NICOLAS
start=0
u1=User("Macé", "Nicolas")
p1= Portfolio(b1, 0.30, 0.15,10000)

s1=Stock("NATIXIS_SPOT","€",6.95)
s2=Stock("EURUSD_SPOT","P",1.181)

i1=Investment(s1,100,"09/10/2017",6.95)
i2=Investment(s2,100,"09/10/2017",1.181)

p1.add_ptf_investment(i1,data)
p1.add_ptf_investment(i2,data)
#####

jours,value,capital,m_PnL, model=strat_forecast(p1,"09/10/2017","10/10/2018",1,data,model)

######


plot(value, "r")





