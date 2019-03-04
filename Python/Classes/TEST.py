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

d_broker=data = pd.read_csv("Users/nmace/Documents/GitHub/PPE_GIT/Python/DataCourtiers.txt",header=0, delimiter=" ")

# TEST IMBRIQUEMENTS ET METHODES DIFFERENTES CLASSES
u1=User("Macé", "Nicolas")
u1


p1= Portfolio("BoursoramaClassic", 0.30, 0.15)
p1

s1= Stock("A",110,"ABC1562","$")
s1

b1= Broker("BoursoramaClassic",0.6)
b1

i1=Investment(s1,10,"7/02/2019",100)
i1

p1.add_ptf_investment(i1)
p1.comp_ptf_line_cost(0)
p1.comp_ptf_line_price(0)

u1.set_user_list_portfolio(p1)



