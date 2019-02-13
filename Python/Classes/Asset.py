#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:44:49 2019

@author: mithurangajendran
"""


#La class Asset est un abstract des classes sous jacentes.
# Elle est composé du prix et du code de l'asset.
class Asset:
    
    #__asset_price = None
    #__asset_code = None
    
    def __init__(self,asset_code,asset_price):
        self.__asset_code = asset_code 
        self.__asset_price = asset_price
         
    
    def __repr__(self):
        return '{asset_code: '+self.__asset_code +\
        ', asset_price: '+str(self.__asset_price)+'}'    

#ACCESSEURS
    
    def get_asset_price(self):
        return self.__asset_price
    
    def get_asset_code(self):
        return self.__asset_code
    
        
    def set_asset_price(self,asset_price):
        self.__asset_price = asset_price
    
    def set_asset_code(self,asset_code):
        self.__asset_code = asset_code
    
    