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
      self.__ptf_PnL = 0
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
      
    def add_ptf_investment(self,ptf_investment,data):
        if ptf_investment.get_investment_asset().get_asset_price() != None:
            if ptf_investment.comp_investment_price(self.__ptf_broker)< self.__ptf_capital:
                self.__ptf_list_investments.append(ptf_investment)
                self.__ptf_capital=self.__ptf_capital-ptf_investment.comp_investment_cost(self.__ptf_broker)
                print(True)
            else:
                print(False)
        elif ptf_investment.get_investment_asset().get_asset_price() == None:
            ptf_investment.get_investment_asset().set_asset_price(data.iloc[0][ptf_investment.get_investment_asset().get_asset_ISIN()])
            if ptf_investment.comp_investment_price(self.__ptf_broker)< self.__ptf_capital:
                self.__ptf_list_investments.append(ptf_investment)
                self.__ptf_capital=self.__ptf_capital-ptf_investment.comp_investment_cost(self.__ptf_broker)
                print(True)
            else:
                print(False)
      
    def comp_ptf_line_cost(self,index):
        return self.__ptf_list_investments[index].get_investment_cost()*\
    self.__ptf_list_investments[index].get_investment_quantity() #+ \
   # self.__ptf_list_investments[index].comp_investment_broker_fees(self.__ptf_broker)
    
    def comp_ptf_line_price(self, index):
        return self.__ptf_list_investments[index].comp_investment_price(self.__ptf_broker)#-\
       # self.__ptf_list_investments[index].comp_investment_broker_fees(self.__ptf_broker)
    
    def comp_ptf_line_broker_fees(self, index):
        return self.__ptf_list_investments[index].comp_investment_broker_fees(self.__ptf_broker)
    
    def comp_ptf_PnL(self):
        PnL=0
        for index in range(len(self.__ptf_list_investments)):
            PnL=PnL + self.comp_ptf_line_price(index)-self.comp_ptf_line_cost(index)- 2*self.comp_ptf_line_broker_fees(index)
        self.__ptf_PnL= PnL
    
    def comp_ptf_value(self):
        value=0
        for index in range(len(self.__ptf_list_investments)):
            value+= self.comp_ptf_line_price(index) 
            
        return value+self.__ptf_capital
    
    def comp_max_drawdown(self,m_PnL):
        mdd = 0
        peak = m_PnL[0]
        for x in m_PnL:
            if x > peak: 
                peak = x
            dd = (peak - x) / peak
            if dd > mdd:
                mdd = dd
        self.__ptf_real_risk =  mdd
        
# METHODE BUY SELL ASSETS According to their index and Quanity
    def sell_ptf(self, index, investment_quantity):
        broker_fees= self.__ptf_broker.comp_broker_fees(investment_quantity,self.__ptf_list_investments[index].get_investment_asset().get_asset_price())
        
        cash_flow=investment_quantity*\
        self.__ptf_list_investments[index].get_investment_asset().get_asset_price()
        
        if self.__ptf_capital>broker_fees:
            self.__ptf_capital=self.__ptf_capital+cash_flow-broker_fees
            self.__ptf_list_investments[index].set_investment_quantity(self.__ptf_list_investments[index].get_investment_quantity()-investment_quantity)
            print(str(True)+ " sold :"+ str(investment_quantity))
        else:
            print(False)
        
    def buy_ptf(self, index, investment_quantity):
        broker_fees= self.__ptf_broker.comp_broker_fees(investment_quantity,self.__ptf_list_investments[index].get_investment_asset().get_asset_price())
        
        cash_flow=investment_quantity*\
        self.__ptf_list_investments[index].get_investment_asset().get_asset_price()
        
        if self.__ptf_capital>broker_fees+cash_flow:
            self.__ptf_capital=self.__ptf_capital-cash_flow-broker_fees
            self.__ptf_list_investments[index].set_investment_quantity(self.__ptf_list_investments[index].get_investment_quantity()+investment_quantity)
            print(str(True)+ " Bought :" +str(investment_quantity))
        else:
            print(False)
        
       
        
            
    
        
        
        
        
        
    

