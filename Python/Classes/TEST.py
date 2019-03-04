#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:34:21 2019

@author: mithurangajendran
"""
#import os #os.getcwd()
import pandas as pd

# AUTOLOADER DES CLASSES
from User import User
from Portfolio import Portfolio
from Stock import Stock
from Broker import Broker
from Investment import Investment

# DATAS EXTERNES

d_broker= pd.read_csv("/Users/mithurangajendran/Documents/PPE_GIT/Python/Data/Courtiers.txt",header=0, delimiter=" ")
data= pd.read_csv("/Users/mithurangajendran/Documents/PPE_GIT/Python/Data/d_historique.txt", header=0, delimiter="\t")
# TEST IMBRIQUEMENTS ET METHODES DIFFERENTES CLASSES
u1=User("Macé", "Nicolas")

p1= Portfolio(b1, 0.30, 0.15)

b1= Broker("BoursoramaDecouverte",(0,500,1.99,0,501,10**10,0,0.006))
b2= Broker("BoursoramaClassic", (0,5000,5.5,0,5001,10**10,0,0.0048))

s1=Stock("NATIXIS",6,"$")
s2=Stock("ORANGE",39,"$")



#Investment( asset, qté, date, cout unitaire)
i1=Investment(s1,100,"7/02/2019",5.5)
i2=Investment(s2,100,"07/02/2019",39)

p1.add_ptf_investment(i1)
p1.add_ptf_investment(i2)

#p1.comp_ptf_line_cost(0)
#p1.comp_ptf_line_price(0)
#print(p1.comp_ptf_PnL())

#u1.set_user_list_portfolio([p1,p2])
#u1.add_user_list_portfolio(p3)


print(p1.comp_ptf_PnL())
