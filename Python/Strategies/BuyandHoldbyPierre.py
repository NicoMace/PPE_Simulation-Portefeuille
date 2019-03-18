# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:54:29 2019

@author: Pierre
"""

### Path.
import os
#BDD
#os.chdir('/Server/PPE_GIT/Python')
#Mithuran
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')
#Nicolas
#os.chdir('/Users/nmace/Documents/GitHub/PPE_GIT/Python')
#Pierre
os.chdir('D:/Users/Pierre/Documents/8 - Scolarite/ECE/PPE/PPE_GIT/Python')


### Importations.
from Classes import *


### Buy and Hold.

def strat_buy_and_hold_bis(Capital, Broker, Start, End, Return, Risk, Portfolio, DataAsset, DataBroker):
    
    '''help'''
    
    ### Initialisations.   
    # Compute initials investment cost.
    L_Investments = Portfolio.get_ptf_list_investments()
    InitialInvestmentCost = []
    for investment in L_Investments:
        investment.set_investment_cost(DataAsset.iloc[Start][investment.get_investment_asset().get_asset_ISIN()])
        InitialInvestmentCost += investment.get_investment_cost()
    
    
    ### Daily processing.
    PortfolioPnL = []
    Periode = End - Start #Revoir le calcul
    for day in range(Periode):
        
        # For each portfolio line.
        for investment in L_Investments:
            # Refresh asset price.
            AssetPrice = DataAsset.iloc[day][investment.get_investment_asset().get_asset_ISIN()]
            investment.get_investment_asset().set_asset_price(AssetPrice)
        
        # Compute portfolio PnL.
        Portfolio.comp_ptf_PnL()    # Revoir la methode & les arguments
        PnL = Portfolio.get_ptf_PnL
        PortfolioPnL += [PnL]








