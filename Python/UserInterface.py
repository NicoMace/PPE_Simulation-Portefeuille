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
Date = "7/02/2019"
# End date.

# Expected return.
Return = 0.30
# Expected risk.
Risk = 0.15


### Create assets basket.
# Total time.
T = 1
# Number of steps.
N = 12
# Time step size
dt = T/N
# Number of realizations to generate.
NumberOfRealizations = 100
# Annual yield.
AnnualYield=0.02
# Create an empty array to store the realizations.
x = np.empty((NumberOfRealizations,N+1))
# Initial values of x2.
x[:, 0] = 100
# Black Scholes compute.
blacksholes.comp_price_model_bs(x[:, 0], N,NumberOfRealizations,T,AnnualYield,out=x[:,1:])
# Names.
Name = ["Stock"+str(i+1) for i in range(NumberOfRealizations)]
# Create data frame.
Data = pd.DataFrame(np.array(x.transpose()), columns=Name)
# Initials Assets Prices.
Price = [i for i in x[:,0]]
# Assets currencys.
Currency = ["€" for i in range(NumberOfRealizations)]
# Create the stock.
Stock = Stock(Name, Price, Currency)


### Create a portfolio.
# Fees.
Fees = (0,500,1.99,0,501,10**10,0,0.006)
# Portfolio compute.
Portfolio = Portfolio(Broker(BrokerName,Fees), Return, Risk,Capital)


### Add the investment to the portfolio.
# Number.
Number = 10
# Price.
Price = 6.95
# Adding.
Portfolio.add_ptf_investment(Investment(Stock,Number,Date,Price))


### Buy and Hold plot.
PnL = strat_buy_and_hold(Portfolio,0,N,1,Data)

for k in range(NumberOfRealizations):
    plot([i for i in range(len(PnL))], PnL)
xlabel('t', fontsize=16)
ylabel('x', fontsize=16)
grid(True)
show()