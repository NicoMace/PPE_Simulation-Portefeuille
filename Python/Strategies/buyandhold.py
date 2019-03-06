# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:09:35 2019

@author: Pierre



"""
#P######################################## PATH
import os
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    'Mithuran
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    'Mithuran
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    'Mithuran

######################################### INISTIALISATION ######################@
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Classes import *

d_broker= pd.read_csv("Data/Courtiers.txt",header=0, delimiter=" ")
data= pd.read_csv("Data/d_historique.txt", header=0, delimiter="\t")

##################### BODY ########################

### BROKER
b1= Broker("BoursoramaDecouverte",(0,500,1.99,0,501,10**10,0,0.006))
b2= Broker("BoursoramaClassic", (0,5000,5.5,0,5001,10**10,0,0.0048))


#### NICOLAS

u1=User("Macé", "Nicolas")
p1= Portfolio(b1, 0.30, 0.15,10000)

s1=Stock("NATIXIS_SPOT",6.95,"€")
s2=Stock("CAC_SPOT",5365.83,"P")

i1=Investment(s1,1,"7/02/2019",6.95)
i2=Investment(s2,10,"07/02/2019",5365.83)

p1.add_ptf_investment(i1)
#p1.add_ptf_investment(i2)


def strat_buy_and_hold(portfolio,start,Nb_Obs, periode,data):
    L_investments=portfolio.get_ptf_list_investments()
    m_PnL=[]
    for jour in range(start,Nb_Obs+start,periode):
        print("Jour " +str(jour))
        for investment in L_investments:
            investment.set_investment_cost(data.iloc[start][investment.get_investment_asset().get_asset_ISIN()])
            cout_investment = investment.get_investment_cost()
            
            prix_actif= data.iloc[jour][investment.get_investment_asset().get_asset_ISIN()]
            investment.get_investment_asset().set_asset_price(prix_actif)
            portfolio.comp_ptf_PnL()
            m_PnL.append(portfolio.get_ptf_PnL())
            
            print(investment.get_investment_asset().get_asset_ISIN()+": Spot t0 :"+ str(cout_investment) + " Spot :" + str(investment.get_investment_asset().get_asset_price()))
        print("PnL de :"+ str(portfolio.get_ptf_PnL())+"\n")
    return m_PnL
m_PnL= strat_buy_and_hold(p1,0,100,1,data)
            
plt.figure(1)
plt.plot([i for i in range(len(m_PnL))],m_PnL)
plt.figure(2)
plt.plot(data.NATIXIS_SPOT)
plt.show()

print(np.mean(data.NATIXIS_SPOT))
print(np.std(data.NATIXIS_SPOT))


print(np.mean(m_PnL))
print(np.std(m_PnL))


