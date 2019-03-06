#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:44:49 ù


@author: mithurangajendran
"""


#La class Asset est un abstract des classes sous jacentes.
# Elle est composé du prix et du code de l'asset.
class Asset:
    
    #__asset_price = None
    #__asset_ISIN = None
    
    def __init__(self,asset_ISIN,asset_price=None):
        self.__asset_ISIN = asset_ISIN 
        self.__asset_price = asset_price

         
    
    def __repr__(self):
        return '{asset_ISIN: '+self.__asset_ISIN +\
        ', asset_price: '+str(self.__asset_price)+'}'    

#ACCESSEURS


    
    def get_asset_price(self):
        return self.__asset_price
    
    def get_asset_ISIN(self):
        return self.__asset_ISIN
    

    
        
    def set_asset_price(self,asset_price):
        self.__asset_price = asset_price
    
    def set_asset_ISIN(self,asset_ISIN):
        self.__asset_ISIN = asset_ISIN
        
    def comp_asset_cost(self, asset_quantity, broker):
        return self.__asset_price*asset_quantity + broker.comp_broker_fees(asset_quantity,self.__asset_price)
    
    