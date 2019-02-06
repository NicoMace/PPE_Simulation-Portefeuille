#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:34:21 2019

@author: mithurangajendran
"""
from User import User
from Portfolio import Portfolio
from Stock import Stock
from Broker import Broker



u1=User("Macé", "Nicolas")
u1


p1= Portfolio("BoursoramaClassic", 0.30, 0.15)
p1

s1= Stock("A",100,110,"ABC1562","$")
s1

b1= Broker("BoursoramaClassic",0.6)
b1