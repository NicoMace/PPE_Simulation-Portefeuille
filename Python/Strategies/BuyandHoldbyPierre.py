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

def strat_buy_and_hold_bis(Capital, BrokerName, Start, End, Return, Risk, AssetBasket, DataAsset, DataBroker):
    
    '''help'''
    
    # IMPLEMENTER LE RISK puis le ratio.
    
    ### Initialisations.
    
    # Create Broker.
    Broker = Broker(BrokerName, DataBroker)     #Revoir DataBroker
    
    # Create Portfolio.
    Portfolio = Portfolio(Broker, Return, Risk, Capital)
    
    # Create Assets.
    Assets = []
    for i in range(AssetBasket):
        AssetName = AssetBasket[i]
        Assets += [Stock(AssetName, "€")]
    
    # Create Investments.
    Investments = []
    for i in Assets:
        
        # Asset quantity.
        AssetQuantity = 0
        
        # Investments.
        Investments += [Investment(i, AssetQuantity, Start, DataAsset)]    #Revoir DataAsset
    
    # Add investments in portfolio.
    for i in range(Investments):
        Portfolio.add_ptf_investment(Investments[i])
    
    # Compute initials investment cost.
    L_Investments = portfolio.get_ptf_list_investments()
    for investment in L_Investments:
        investment.set_investment_cost(DataAsset.iloc[Start][investment.get_investment_asset().get_asset_ISIN()])
        
    
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








