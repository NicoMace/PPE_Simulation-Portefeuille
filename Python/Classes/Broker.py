#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:50:25 2019

@author: mithurangajendran
"""

class Broker:
    __broker_name=None
    __broker_fees = None
    
    def __init__(self,broker_name, broker_fees=None):
        self.__broker_name=broker_name
        self.__broker_fees = broker_fees
        
#ACCESSEURS
        
        def get_broker_name(self):
            return self.__broker_name
        
        def get_broker_fees(self):
            return self.__broker_fees
        
        
        def set_broker_name(broker_name):
            self.__broker_name = broker_name
            
        def set_broker_fees(broker_fees):
            self.__broker_fees= broker_fees
            
# METHODES
            
        def update_broker_fees(self,d_broker):
            for i in range(0,len(d_broker)):
                if self.__broker_name == d_broker[i][1]:
                    self.__broker_fees == list(d_broker[i][2:len(d_broker)])
                
        
        def comp_broker_fees(self,d_broker, asset_quantity, asset_price):
            #update_broker_fees(d_broker)
            
            for j in range (0,len(self.__broker_fees),4):
                if (asset_quantity * asset_price > self.__broker_fees[j] and
                    asset_quantity*asset_price <= self.__broker_fees[j+1]):
                    
                    fixed_fees = self.__broker_fees[j+2]
                    variable_fees= self.__broker_fees[j+3]
                    broker_fees = fixed_fees + variable_fees
            return broker_fees
    


