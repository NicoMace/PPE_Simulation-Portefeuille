# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:09:35 2019

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

d_broker= pd.read_csv("Data/Courtiers.txt",header=0, delimiter=" ")
data= pd.read_csv("Data/d_historique.txt", header=0, delimiter="\t")




def strat_buy_and_hold(portfolio,b_date,e_date, periode,data):

    value=[]
    capital=[]
    m_PnL=[]
    for i in range(len(portfolio.get_ptf_list_investments())):
        m_PnL.append([])
    m_PnL.append([])
    
    start= data.loc[data["Date"] == b_date].index[0]
    end= data.loc[data["Date"] == e_date].index[0]

    
    
    for jour in range(start,end+1,periode):

        for investment in portfolio.get_ptf_list_investments():
            #print(portfolio.get_ptf_list_investments().index(investment))
            investment.set_investment_cost(data.iloc[start][investment.get_investment_asset().get_asset_ISIN()])
            prix_actif= data.iloc[jour][investment.get_investment_asset().get_asset_ISIN()]
            investment.get_investment_asset().set_asset_price(prix_actif)
            portfolio.comp_ptf_PnL()
            m_PnL[portfolio.get_ptf_list_investments().index(investment)].append(investment.comp_investment_PnL(portfolio.get_ptf_broker()))
        portfolio.comp_ptf_PnL()
        capital.append(portfolio.get_ptf_capital())
        m_PnL[-1].append(portfolio.get_ptf_PnL())
        value.append(portfolio.comp_ptf_value())
    #portfolio.comp_max_drawdown(m_PnL[-1])
    portfolio.comp_max_drawdown(value)
        
    return (data.loc[start:end].Date.tolist(),value, capital, m_PnL)



m=data.loc[data["Date"] == "14/09/2018"]["NATIXIS_SPOT"].iloc[0]


