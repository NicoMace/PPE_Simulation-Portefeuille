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
# Global imports.
import numpy as np
import pandas as pd
from pylab import plot, show, grid, xlabel, ylabel
# Particulars imports.
from Modelisation import blacksholes
from Strategies.buyandhold import strat_buy_and_hold
from Strategies.ExpositionConstante import strat_EC_1
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
x[:, 0] = 100.00
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
Broker =Broker(BrokerName,(0,500,1.99,0,500,10**10,0,0.006))     #Revoir DataBroker
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
#Portfolio.set_ptf_list_investments(Investments)
for i in range(len(Investments)):
    Portfolio.add_ptf_investment(Investments[i], Data)


### Buy and Hold compute.
Jours, H_Value_BnH, H_Capital_BnH, H_PnL_BnH = strat_buy_and_hold(Portfolio,0,N,1,Data)


### Exposition constante compute.
H_Value_CE, H_PnL_CE = strat_EC_1(1000,Portfolio,0, 0,N,1, Data)


### Data shaping.
# Output Buy and Hold.
if os.path.isfile('Out_BnH.txt')==True:
    os.remove('Out_BnH.txt')
    
Out_BnH = open('Out_BnH.txt','w')

Out_BnH.write('Date, Value, Capital, PnL')
Out_BnH.write('\n')

for i in range(len(Jours)):
    Out_BnH.write(str(Jours[i])+ ', ')
    Out_BnH.write(str(H_Value_BnH[i])+ ', ')
    Out_BnH.write(str(H_Capital_BnH[i])+ ', ')
    Out_BnH.write(str(H_PnL_BnH[-1][i])+ ', ')
    Out_BnH.write('\n')

Out_BnH.close()
# Output Constant Exposition.
if os.path.isfile('Out_CE.txt')==True:
    os.remove('Out_CE.txt')
    
Out_CE = open('Out_CE.txt','w')

Out_CE.write('Value, PnL')
Out_CE.write('\n')

for i in range(len(Jours)):
    Out_CE.write(str(H_Value_CE[i])+ ', ')
    Out_CE.write(str(H_PnL_CE[-1][i]))
    Out_CE.write('\n')

Out_CE.close()


### Buy and Hold Display.
# Investments PnL.
for k in range(NumberOfRealizations-1):
    plot(H_PnL_BnH[k])
xlabel('t', fontsize=16)
ylabel('x', fontsize=16)
grid(True)
show()

# Portfolio PnL.
plot(H_PnL_BnH[-1])
xlabel('t', fontsize=16)
ylabel('x', fontsize=16)
grid(True)
show()


### Constant Exposition Display.
# Investments PnL.
for k in range(NumberOfRealizations-1):
    plot(H_PnL_CE[k])
xlabel('t', fontsize=16)
ylabel('x', fontsize=16)
grid(True)
show()

# Portfolio PnL.
plot(H_PnL_CE[-1])
xlabel('t', fontsize=16)
ylabel('x', fontsize=16)
grid(True)
show()