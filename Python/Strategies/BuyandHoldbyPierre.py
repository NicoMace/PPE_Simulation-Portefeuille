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
#os.chdir('D:/Users/Pierre/Documents/8 - Scolarite/ECE/PPE/PPE_GIT/Python')


### Importations.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Classes import *

d_broker= pd.read_csv("Data/Courtiers.txt",header=0, delimiter=" ")
data= pd.read_csv("Data/d_historique.txt", header=0, delimiter="\t")


### Buy and Hold.

def strat_buy_and_hold(Capital, BrokerName, Start, End, Return, Risk, AssetBasket, DataAsset, DataBroker):
    
    '''help'''
    
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
    InitialInvestmentCost = []
    for investment in L_Investments:
        investment.set_investment_cost(data.iloc[Start][investment.get_investment_asset().get_asset_ISIN()])
        InitialInvestmentCost += investment.get_investment_cost()
    
    
    ### Daily processing.
    Periode = End - Start #Revoir le calcul
    for day in range(Periode):
        
        # For each portfolio line.
        for index, investment in enumerate(L_Investments):
            
    
    
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
