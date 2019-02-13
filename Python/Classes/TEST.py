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

d_broker=data = pd.read_csv("/Users/mithurangajendran/Documents/PPE_GIT/Python/Data/Courtiers.txt",header=0, delimiter=" ")

# TEST IMBRIQUEMENTS ET METHODES DIFFERENTES CLASSES
u1=User("Macé", "Nicolas")



p1= Portfolio("BoursoramaClassic", 0.30, 0.15)


s1= Stock("A",110,"ABC1562","$")


s2=Stock("B",10,"BACD19393","$")


b1= Broker("BoursoramaClassic",0.6)


i1=Investment(s1,10,"7/02/2019",100)
i2=Investment(s2,10000,"07/02/2019",9)

p1.add_ptf_investment(i1)
p1.add_ptf_investment(i2)
p2=p1
p3=p1
#p1.comp_ptf_line_cost(0)
#p1.comp_ptf_line_price(0)
print(p1.comp_ptf_PnL())

#u1.set_user_list_portfolio([p1,p2])
u1.add_user_list_portfolio(p3)



