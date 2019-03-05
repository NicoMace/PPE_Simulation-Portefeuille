# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:19:41 2019

@author: Pierre
"""

from Asset import Asset


class Bond(Asset):
    
    #__bond_nominal = None
    #__bond_currency = None
    #__bond_yield = None
    #__bond_market_price = None
   
    
    def __init__(self,asset_code,asset_price,bond_ISIN,bond_currency):
        Asset.__init__(self,asset_code,asset_price)
        self.__bond_ISIN = bond_ISIN
        self.__bond_currency = bond_currency

    def __repr__(self):
        return '{asset_code: '+self.get_asset_code()+\
        ', asset_price: '+str(self.get_asset_price())+\
        ', bond_ISIN: '+str(self.__bond_ISIN)+\
        ', bond_currency:'+str(self.__bond_currency)+'}'

        
       
    # Assesseurs.
        
    def get_bond_ISIN(self) :
      return self.__bond_ISIN
    
    def get_bond_currency(self) :
      return self.__bond_currency
    
    def get_bond_flow(self) :
      return self.__bond_flow
    
    def set_bond_ISIN(self,bond_ISIN):
      self.__bond_ISIN = bond_ISIN
    
    def set_bond_currency(self,bond_currency) :
      self.__bond_currency = bond_currency
    
    def set_bond_flow(self,bond_flow) :
      self.__bond_flow = bond_flow
    

