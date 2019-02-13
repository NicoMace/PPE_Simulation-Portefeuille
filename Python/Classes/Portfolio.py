#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:16:51 2019

@author: mithurangajendran
"""
class Portfolio:
    
    #__ptf_broker = None
    #__ptf_expected_return = None
    #__ptf_expected_risk = None
    #__ptf_real_return = None
    #__ptf_real_risk = None
    #__ptf_list_investments= list()

    ptf_list_investments = list()
    
    def __init__(self,ptf_broker,ptf_expected_return, ptf_expected_risk):
      self.__ptf_broker= ptf_broker
      self.__ptf_expected_return = ptf_expected_return
      self.__ptf_expected_risk = ptf_expected_risk
      
      self.__ptf_real_return = None
      self.__ptf_real_risk = None
      
      self.__ptf_list_investments= list()
      
    def __repr__(self):
        return '{ptf_broker: '+self.__ptf_broker+\
        ', ptf_expected_return: '+str(self.__ptf_expected_return)+\
        ', ptf_expected_risk: '+str(self.__ptf_expected_risk)+\
        ', ptf_real_return: '+str(self.__ptf_real_return)+\
        ', ptf_real_risk:'+str(self.__ptf_real_risk)+\
        ', ptf_list_investments: '+str(self.__ptf_list_investments)+'}'
  

#ACCESSEURS
      
    def get_ptf_broker(self):
      return self.__ptf_broker
    
    def get_ptf_list_investments(self):
      return self.__ptf_list_investments
    
    def get_ptf_expected_return(self): 
      return self.__ptf_expected_return
    
    def get_ptf_expected_risk(self):
      return self.__ptf_expected_risk
    
    def get_ptf_real_return(self): 
      return self.__ptf_real_return
    
    def get_ptf_real_risk(self): 
      return self.__ptf_real_risk
  
    
    def set_ptf_broker(self,ptf_broker):
      self.__ptf_broker= ptf_broker
    
    def set_ptf_list_investments(self,ptf_list_investments):
      self.__ptf_list_investments= ptf_list_investments
    
    def set_ptf_expected_return(self,ptf_expected_return):
      self.__ptf_expected_return = ptf_expected_return
    
    def set_ptf_expected_risk(self,ptf_expected_risk):
      self.__ptf_expected_risk = ptf_expected_risk
    
    def set_ptf_real_return(self,ptf_real_return):
      self.__ptf_real_return = ptf_real_return
    
    def set_ptf_real_risk(self,ptf_real_risk):
      self.__ptf_real_risk = ptf_real_risk

    
#METHODES
      
    def add_ptf_investment(self,ptf_investment):
      self.__ptf_list_investments.append(ptf_investment)
      
    def comp_ptf_line_cost(self,index):
        return self.__ptf_list_investments[index].get_investment_cost()*\
    self.__ptf_list_investments[index].get_investment_quantity()
    
    def comp_ptf_line_price(self, index):
        return self.__ptf_list_investments[index].get_investment_quantity()*\
                    self.__ptf_list_investments[index].get_investment_asset().get_asset_price()
    
    def comp_ptf_PnL(self):
        PnL=0
        for index in range(len(self.__ptf_list_investments)):
            PnL=PnL + self.comp_ptf_line_price(index)-self.comp_ptf_line_cost(index)
        return PnL
            
    
            
        
        
        
        
    

