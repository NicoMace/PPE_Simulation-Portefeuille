# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:45:01 2019

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
import numpy as np
import pandas as pd
from pylab import plot, show, grid, xlabel, ylabel
from Modelisation import blacksholes
from Strategies.buyandhold import strat_buy_and_hold
from Strategies.buyandhold import chart
from Classes.Portfolio import Portfolio
from Classes.Stock import Stock
from Classes.Broker import Broker
from Classes.Investment import Investment


### Universal datas.
# Funds.
Capital = 10000
# Broker.
BrokerName = "BoursoramaDecouverte"
# Start date.
Start = "7/02/2019"
# End date.
End = "27/02/2019"
# Expected return.
Return = 0.30
# Expected risk.
Risk = 0.15
# Historical prices from stocks.
HistoricalData = pd.read_csv("Data/d_historique.txt", header=0, delimiter="\t")
# Computed prices from Black-Sholes.
DataAsset = pd.read_csv("Data/d_historique.txt", header=0, delimiter="\t")
# Broker fees.
DataBroker = pd.read_csv("Data/Courtiers.txt",header=0, delimiter=" ")


### Date management.



### Create assets basket.
# Total time.
T = 1
# Number of steps.
N = 12
# Time step size
dt = T/N
# Number of realizations to generate.
NumberOfRealizations = 10
# Annual yield.
AnnualYield=0.02
# Create an empty array to store the realizations.
x = np.empty((NumberOfRealizations,N+1))
# Initial values of x2.
x[:, 0] = 100
# Black Scholes compute.
blacksholes.comp_price_model_bs(x[:, 0], N,NumberOfRealizations,T,AnnualYield,out=x[:,1:])
# Names.
Names = ["Stock"+str(i+1) for i in range(NumberOfRealizations)]
# Create data frame.
Data = pd.DataFrame(np.array(x.transpose()), columns=Names)
# Initials Assets Prices.
Price = [i for i in x[:,0]]
# Assets currencys.
Currencies = ["€" for i in range(NumberOfRealizations)]


### Create portfolio.
# Create Broker.
Broker = Broker(BrokerName, DataBroker)     #Revoir DataBroker
# Create Portfolio.
Portfolio = Portfolio(Broker, Return, Risk, Capital)
# Create Assets.
Assets = []
for i in range(len(Names)):
    AssetName = Names[i]
    Currency = Currencies[i]
    Assets += [Stock(AssetName, Currency,Price[i])]
# Create Investments.
Investments = []
for i in range(len(Assets)):   
    # Asset quantity.
    AssetQuantity = 10
    # Investments.
    Investments += [Investment(Assets[i], AssetQuantity, Start, Price[i])]    #Revoir DataAsset
# Add investments in portfolio.
Portfolio.set_ptf_list_investments(Investments)
    

### Buy and Hold compute.
Jours, H_Value, H_Capital, H_PnL = strat_buy_and_hold(Portfolio,0,N-1,1,Data)

### Data shaping.
if os.path.isfile('data.txt')==True:
    os.remove('data.txt')
    
fichier = open('data.txt','w')

fichier.write('Date, Value, Capital')
fichier.write('\n')

for i in range(len(Jours)):
    fichier.write(str(Jours[i])+ ', ')
    fichier.write(str(H_Value[i])+ ', ')
    fichier.write(str(H_Capital[i])+ ', ')
    fichier.write('\n')

fichier.close()


### Display.
chart(Jours, H_Value, H_Capital)