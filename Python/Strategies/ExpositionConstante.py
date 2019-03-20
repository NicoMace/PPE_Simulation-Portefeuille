#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 08:27:45 2019

@author: mithurangajendran
"""
#P######################################## PATH
import os
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    #Mithuran
os.chdir('D:/Users/Pierre/Documents/8 - Scolarite/ECE/PPE/PPE_GIT/Python')    #Pierre
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    'Mithuran
#os.chdir('/Users/nmace/Documents/GitHub/PPE_GIT/Python')          #Nicolas


######################################### INISTIALISATION ######################@
from Classes import *


        
        
def strat_EC(treshold, portfolio, index, start, Nb_Obs, periode):
    m_PnL=[]
    value=[]
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
        p1.comp_ptf_PnL()
        value.append(portfolio.comp_ptf_value())
        
        m_PnL.append(p1.get_ptf_PnL())
        #print("Investment Quantity :"+ str(investment.get_investment_quantity())+" Price night :"+ str(investment.comp_investment_price(b1)))
        #print("PnL :"+ str(p1.get_ptf_PnL())+"\n")
        
    return m_PnL, value




        
def strat_EC_1(treshold, portfolio, index, start, Nb_Obs, periode):
    m_PnL=[0]
    value=[]
    investment= portfolio.get_ptf_list_investments()[index] 
    
    for jour in range(start, Nb_Obs+start, periode):
        #print(jour)
        investment.get_investment_asset().set_asset_price(data.iloc[jour][investment.get_investment_asset().get_asset_ISIN()])
        lower_qty= treshold// investment.get_investment_asset().get_asset_price()
        upper_qty=lower_qty+1
        #print(investment.get_investment_quantity())
        
        if investment.get_investment_asset().comp_asset_cost(abs(lower_qty-investment.get_investment_quantity()),portfolio.get_ptf_broker())>15:
        
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
        p1.comp_ptf_PnL()
        value.append(portfolio.comp_ptf_value())
        
        m_PnL.append(p1.get_ptf_PnL())
        #print("Investment Quantity :"+ str(investment.get_investment_quantity())+" Price night :"+ str(investment.comp_investment_price(b1)))
        #print("PnL :"+ str(p1.get_ptf_PnL())+"\n")
        
    return m_PnL, value







    

