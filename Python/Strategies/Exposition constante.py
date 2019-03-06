#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 08:27:45 2019

@author: mithurangajendran
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

def strat_EC1(treshold, portfolio, index,start,Nb_Obs, periode):#index of an investment
    
    investment= portfolio.get_ptf_list_investments()[index]  
    for jour in range(start, Nb_Obs+start, periode):
        
        print("Jour " +str(jour)+" Price morning: "+ str(investment.comp_investment_price(b1)))
        investment_qty= investment.get_investment_quantity()
        asset_price= data.iloc[jour][investment.get_investment_asset().get_asset_ISIN()]
        investment.get_investment_asset().set_asset_price(asset_price)
        lower_qty = abs(treshold-investment.comp_investment_price(b1))//asset_price
        upper_qty = lower_qty +1

        if lower_qty !=0:
            
            lower_bound_price=investment.get_investment_asset().comp_asset_cost(abs(lower_qty), portfolio.get_ptf_broker())
            upper_bound_price=investment.get_investment_asset().comp_asset_cost(abs(upper_qty), portfolio.get_ptf_broker())
            if (lower_qty <investment_qty and upper_qty<investment_qty):
                if lower_bound_price<=upper_bound_price:
                    portfolio.sell_ptf(index, abs(lower_qty))
                    investment_qty= investment.get_investment_quantity()
                    print(investment_qty)
                    print(investment.comp_investment_cost(b1))
                else:

                    portfolio.sell_ptf(index, abs(upper_qty))

            elif (lower_qty >investment_qty and upper_qty>investment_qty):
                print("lol")
                if lower_bound_price<=upper_bound_price:
                    portfolio.buy_ptf(index, abs(lower_qty))
                else:
                    print(upper_bound-investment_qty)
                    portfolio.buy_ptf(index, abs(upper_qty))
            p1.comp_ptf_PnL()
        else:
            print("Lower_qty=0")


        print("Investment Quantity :"+ str(investment.get_investment_quantity())+" Price night :"+ str(investment.comp_investment_price(b1)))
        print("PnL :"+ str(p1.get_ptf_PnL())+"\n")
        
        
def strat_EC(treshold, portfolio, index, start, Nb_Obs, periode):
    m_PnL=[]
    capital=[]
    investment= portfolio.get_ptf_list_investments()[index] 
    
    for jour in range(start, Nb_Obs+start, periode):
        investment.get_investment_asset().set_asset_price(data.iloc[jour][investment.get_investment_asset().get_asset_ISIN()])
        lower_qty= treshold// investment.get_investment_asset().get_asset_price()
        upper_qty=lower_qty+1
        #print(investment.get_investment_quantity())
        
        
        if investment.get_investment_asset().comp_asset_cost(lower_qty,b1)<investment.get_investment_asset().comp_asset_cost(upper_qty,b1):
            if lower_qty-investment.get_investment_quantity()<0:
            
                portfolio.sell_ptf(index,abs(lower_qty-investment.get_investment_quantity()))
                
            elif lower_qty-investment.get_investment_quantity()>0:
                portfolio.buy_ptf(index,abs(lower_qty-investment.get_investment_quantity()))
                
        
        elif investment.get_investment_asset().comp_asset_cost(lower_qty,b1)>investment.get_investment_asset().comp_asset_cost(upper_qty,b1):
            if upper_qty-investment.get_investment_quantity()<0:
                portfolio.sell_ptf(index,abs(upper_qty-investment.get_investment_quantity()))
            
            elif upper_qty-investment.get_investment_quantity()>0:
                portfolio.buy_ptf(index,abs(upper_qty-investment.get_investment_quantity()))
        capital.append(portfolio.get_ptf_capital())
        p1.comp_ptf_PnL()
        m_PnL.append(p1.get_ptf_PnL())
        #print("Investment Quantity :"+ str(investment.get_investment_quantity())+" Price night :"+ str(investment.comp_investment_price(b1)))
        #print("PnL :"+ str(p1.get_ptf_PnL())+"\n")
        
    return m_PnL, capital

    

m_PnL, capital=strat_EC(1000, p1,0,50,70,1)


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
    ax.set_xlabel('Red X-axis', color='red')
    ax.set_ylabel('Red Y-axis', color='red')
    
    
    newax.plot(Y2, 'g-')
    
    newax.set_xlabel('Green X-axis', color='green')
    newax.set_ylabel('Green Y-axis', color='green')
    
    print(" Moyenne :"+str(np.mean(m_PnL))+" Std :"+str(np.std(m_PnL)))
    print(" Moyenne :"+str(np.mean(capital))+" Std :"+str(np.std(capital)))
    

    plt.show()
chart(m_PnL,capital)