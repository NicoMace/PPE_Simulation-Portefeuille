#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:54:22 2019

@author: mithurangajendran
"""
import Asset as A


class Stock(A.Asset):
    
    __stock_ISIN = None
    __stock_currency = None
   
    
    def __init__(self,asset_code,asset_cost,asset_price,stock_ISIN,stock_currency):
        A.Asset.__init__(self,asset_cost,asset_price,asset_code)
        self.__asset_code= asset_code
        self.__asset_cost= asset_cost
        self.__asset_price= asset_price
        
        self.__stock_ISIN = stock_ISIN
        self.__stock_currency = stock_currency
        
       
#ACCESSEURS
        
    def get_stock_ISIN(self) :
      return self.__stock_ISIN
    
    def get_stock_currency(self) :
      return self.__stock_currency
    
    def get_stock_flow(self) :
      return self.__stock_flow
    
    def set_stock_ISIN(self,stock_ISIN):
      self.__stock_ISIN = stock_ISIN
    
    def set_stock_currency(self,stock_currency) :
      self.__stock_currency = stock_currency
    
    def set_stock_flow(self,stock_flow) :
      self.__stock_flow = stock_flow
    

