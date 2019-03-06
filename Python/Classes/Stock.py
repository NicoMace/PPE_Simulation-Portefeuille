#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:54:22 2019

@author: mithurangajendran
"""
from Classes.Asset import Asset


class Stock(Asset):
    
    #__stock_currency = None
   
    
    def __init__(self,asset_ISIN,stock_currency,asset_price=None):
        Asset.__init__(self,asset_ISIN,asset_price)
        self.__stock_currency = stock_currency

    def __repr__(self):
        return '{asset_ISIN: '+self.get_asset_ISIN()+\
        ', asset_price: '+str(self.get_asset_price())+\
        ', stock_currency:'+str(self.__stock_currency)+'}'

        
       
#ACCESSEURS
        

    
    def get_stock_currency(self) :
      return self.__stock_currency
    
        
    def set_stock_currency(self,stock_currency) :
      self.__stock_currency = stock_currency
    

    

