#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:16:51 2019

@author: mithurangajendran
"""
class Portfolio:
    
    __ptf_broker = None
    __ptf_expected_return = None
    __ptf_expected_risk = None
    __ptf_real_return = None
    __ptf_real_risk = None

    ptf_list_investments = list()
    
    def __init__(self,ptf_broker,ptf_expected_return, ptf_expected_risk):
      self.__ptf_broker= ptf_broker
      self.__ptf_expected_return = ptf_expected_return
      self.__ptf_expected_risk = ptf_expected_risk
      
      self.__ptf_real_return = None
      self.__ptf_real_risk = None

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
      self.__ptf_list_investments= self.__ptf_list_investments.append(ptf_investment)
    

