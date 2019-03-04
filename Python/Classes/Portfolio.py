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
    
    def __init__(self,ptf_broker,ptf_expected_return, ptf_expected_risk, ptf_capital):
      self.__ptf_broker= ptf_broker
      self.__ptf_expected_return = ptf_expected_return
      self.__ptf_expected_risk = ptf_expected_risk
      self.__ptf_capital = ptf_capital
      self.__ptf_PnL = None
      self.__ptf_real_return = None
      self.__ptf_real_risk = None
      
      self.__ptf_list_investments= list()
      
    def __repr__(self):
        return '{ptf_broker: '+str(self.__ptf_broker)+\
        ', ptf_expected_return: '+str(self.__ptf_expected_return)+\
        ', ptf_expected_risk: '+str(self.__ptf_expected_risk)+\
        ', ptf_capital: '+str(self.__ptf_capital)+\
        ', ptf_PnL: '+str(self.__ptf_PnL)+\
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

    def get_ptf_capital(self):
        return self.__ptf_capital
    
    def get_ptf_PnL(self):
        return self.__ptf_PnL
    
  
    
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
      
    def set_ptf_capital(self, ptf_capital):
        self.__ptf_capital = ptf_capital
    
    def set_ptf_PnL(self, ptf_PnL):
        self.__ptf_PnL= ptf_PnL

    
#METHODES
      
    def add_ptf_investment(self,ptf_investment):
        if ptf_investment.comp_investment_price()< self.__ptf_capital:
            self.__ptf_list_investments.append(ptf_investment)
            self.__ptf_capital=self.__ptf_capital-ptf_investment.comp_investment_price()
            print(True)
        else:
            print(False)
      
    def comp_ptf_line_cost(self,index):
        return self.__ptf_list_investments[index].get_investment_cost()*\
    self.__ptf_list_investments[index].get_investment_quantity() + \
    self.__ptf_list_investments[index].comp_investment_broker_fees(self.get_ptf_broker())
    
    def comp_ptf_line_price(self, index):
        return self.__ptf_list_investments[index].comp_investment_price()-\
        self.__ptf_list_investments[index].comp_investment_broker_fees(self.get_ptf_broker())
    
    def comp_ptf_PnL(self):
        PnL=0
        for index in range(len(self.__ptf_list_investments)):
            PnL=PnL + self.comp_ptf_line_price(index)-self.comp_ptf_line_cost(index) 
        self.__ptf_PnL= PnL
    
    
            
    
        
        
        
        
        
    

