# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:09:35 2019

@author: Pierre



"""
#P######################################## PATH
import os
os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    #Mithuran
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    'Mithuran
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    'Mithuran

#os.chdir('/Users/nmace/Documents/GitHub/PPE_GIT/Python')          #Nicolas


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
start=0
u1=User("Macé", "Nicolas")
p1= Portfolio(b1, 0.30, 0.15,10000)

s1=Stock("NATIXIS_SPOT","€",6.95)
s2=Stock("CAC_SPOT","P",5365.83)

i1=Investment(s1,100,"07/02/2019",6.95)
i2=Investment(s2,10,"07/02/2019",5365.83)

p1.add_ptf_investment(i1,data)
#p1.add_ptf_investment(i2)


def strat_buy_and_hold(portfolio,start,Nb_Obs, periode,data):

    value=[]
    capital=[]
    
    
    for jour in range(start,Nb_Obs+start,periode):
        #print("Jour " +str(jour))
        for investment in portfolio.get_ptf_list_investments():
            investment.set_investment_cost(data.iloc[start][investment.get_investment_asset().get_asset_ISIN()])

            
            prix_actif= data.iloc[jour][investment.get_investment_asset().get_asset_ISIN()]
            investment.get_investment_asset().set_asset_price(prix_actif)
        
            portfolio.comp_ptf_PnL()
            value.append(portfolio.comp_ptf_value())
            capital.append(portfolio.get_ptf_capital())
        
    return ([jour for jour in range(start,Nb_Obs+start,periode)],value, capital)

jours,value,capital= strat_buy_and_hold(p1,0,263,1,data)

#PNL POTENTIEL PRNBLEME DE FRAIS

def chart(jours,Y1, Y2):
    

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2, right=0.85)
    
    newax = fig.add_axes(ax.get_position())
    newax.patch.set_visible(False)
    
    newax.yaxis.set_label_position('right')
    newax.yaxis.set_ticks_position('right')
    
    newax.spines['bottom'].set_position(('outward', 35))
    
    ax.plot(Y2, 'r-')
    ax.set_xlabel('Red X Axis',color='red')
    ax.set_ylabel('Red Y-axis', color='red')
    
    
    newax.plot(Y1, 'g-')
    
    newax.set_xlabel('Green X-axis', color='green')
    newax.set_ylabel('Green Y-axis', color='green')
    
    
    plt.show()





chart(jours,capital,value)



