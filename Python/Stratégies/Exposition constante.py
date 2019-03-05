#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 08:27:45 2019

@author: mithurangajendran
"""
# INIT
import numpy as np
import matplotlib.pyplot as plt

### BROKER
b1= Broker("BoursoramaDecouverte",(0,500,1.99,0,501,10**10,0,0.006))
b2= Broker("BoursoramaClassic", (0,5000,5.5,0,5001,10**10,0,0.0048))


#### NICOLAS

u1=User("Macé", "Nicolas")
p1= Portfolio(b1, 0.30, 0.15,10000)

s1=Stock("NATIXIS_SPOT",6.95,"€")
s2=Stock("CAC_SPOT",5365.83,"P")

i1=Investment(s1,100,"7/02/2019",6.95)
i2=Investment(s2,10,"07/02/2019",5365.83)

p1.add_ptf_investment(i1)
#p1.add_ptf_investment(i2)

# FUNCTION INTERMEDIARE

def strat_EC(treshold, portfolio, index,start,Nb_Obs, periode):#index of an investment
    
    investment= portfolio.get_ptf_list_investments()[index]
        
    for jour in range(start, Nb_Obs+start, periode):
        
        print("Jour " +str(jour)+" Price morning: "+ str(investment.comp_investment_price(b1)))
        investment_qty= investment.get_investment_quantity()
        asset_price= data.iloc[jour][investment.get_investment_asset().get_asset_ISIN()]
        investment.get_investment_asset().set_asset_price(asset_price)
        lower_qty = (treshold-investment.get_investment_asset()//asset_price
        upper_qty= lower_bound +1.
        
        if lower_bound !=0:
            
            lower_bound_price=investment.get_investment_asset().comp_asset_cost(lower_bound, portfolio.get_ptf_broker())
            print(lower_bound_price)
            upper_bound_price=investment.get_investment_asset().comp_asset_cost(upper_bound, portfolio.get_ptf_broker())

            
            if (lower_bound <investment_qty and upper_bound<investment_qty):
                        
                if lower_bound_price<=upper_bound_price:
                    portfolio.sell_ptf(index, abs(lower_bound-investment_qty))
                else:
                    portfolio.sell_ptf(index, abs(upper_bound-investment_qty))
    
            
            elif (lower_bound >investment_qty and upper_bound>investment_qty):
                
                if lower_bound_price>=upper_bound_price:
                    portfolio.buy_ptf(index, abs(lower_bound-investment_qty))
                else:
                    print(upper_bound-investment_qty)
                    portfolio.buy_ptf(index, abs(upper_bound-investment_qty))
            p1.comp_ptf_PnL()
            
        print("Investment Quantity :"+ str(investment.get_investment_quantity())+" Price night :"+ str(investment.comp_investment_price(b1)))
        print("PnL :"+ str(p1.get_ptf_PnL())+"\n")
            

strat_EC(500, p1,0,0,1,1)
