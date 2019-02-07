#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 21:17:14 2019

@author: mithurangajendran
"""

class Investment:
    #__investment_asset = NA,
    #__investment_quantity = NA,
    #__investment_date = NA,
    #__investment_cost = NA,
    #__investment_price = NA
    
    def __init__(self,investment_asset, investment_quantity, investment_date,\
                 investment_cost):
        self.__investment_asset = investment_asset
        self.__investment_quantity = investment_quantity
        self.__investment_date = investment_date
        self.__investment_cost = investment_cost

        
    def __repr__(self):
        return '{investment_asset: '+str(self.__investment_asset)+\
        ', investment_quantity: '+str(self.__investment_quantity)+\
        ', investment_date: '+str(self.__investment_date)+\
        ', investment_cost: '+str(self.__investment_cost)+'}'
        
    
# ACCESSEURS
        
    def get_investment_asset(self):
        return self.__investment_asset
    
    def get_investment_quantity(self):
        return self.__investment_quantity
    
    def get_investment_date(self):
        return self.__investment_date
    
    def get_investment_cost(self):
        return self.__investment_cost
    

    def set_investment_asset(self,investment_asset):
        self.__investment_asset  = investment_asset
    
    def set_investment__quantity(self,investment_quantity):
        self.__investment_quantity=investment_quantity
    
    def set_investment_date(self,investment_date):
        self.__investment_date=investment_date
    
    def set_investment_cost(self,investment_cost):
        self.__investment_cost=investment_cost

# METHODES
        
    def comp_investment_price(self):
        return(self.__investment_quantity*self.__investment_asset.get_asset_price())
    

    
        
    
        