#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 08:27:45 2019

@author: mithurangajendran
"""
#P######################################## PATH
import os
os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    #Mithuran
#os.chdir('D:/Users/Pierre/Documents/8 - Scolarite/ECE/PPE/PPE_GIT/Python')    #Pierre
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    'Mithuran
#os.chdir('/Users/nmace/Documents/GitHub/PPE_GIT/Python')          #Nicolas


######################################### INISTIALISATION ######################@
from Classes import *



        
def strat_EC_1(treshold, portfolio,b_date,e_date, periode, data):
    value=[]
    capital=[]
    m_PnL=[]
    for i in range(len(portfolio.get_ptf_list_investments())):
        m_PnL.append([0])
    m_PnL.append([0])
    start= data.loc[data["Date"] == b_date].index[0]
    end= data.loc[data["Date"] == e_date].index[0]   
    
    for jour in range(start, end+1, periode):
        for investment in portfolio.get_ptf_list_investments():
        #print(jour)
            investment.get_investment_asset().set_asset_price(data.iloc[jour][investment.get_investment_asset().get_asset_ISIN()])
            lower_qty= treshold// investment.get_investment_asset().get_asset_price()
            upper_qty=lower_qty+1
            #print(investment.get_investment_quantity())
            
            if investment.get_investment_asset().comp_asset_cost(abs(lower_qty-investment.get_investment_quantity()),portfolio.get_ptf_broker())<10:
            
                if investment.get_investment_asset().comp_asset_cost(lower_qty,portfolio.get_ptf_broker())<investment.get_investment_asset().comp_asset_cost(upper_qty,portfolio.get_ptf_broker()):
                    if lower_qty-investment.get_investment_quantity()<0:
                    
                        portfolio.sell_ptf(portfolio.get_ptf_list_investments().index(investment),abs(lower_qty-investment.get_investment_quantity()))
                        
                        
                    elif lower_qty-investment.get_investment_quantity()>0:
                        portfolio.buy_ptf(portfolio.get_ptf_list_investments().index(investment),abs(lower_qty-investment.get_investment_quantity()))
                        
                
                elif investment.get_investment_asset().comp_asset_cost(lower_qty,portfolio.get_ptf_broker())>investment.get_investment_asset().comp_asset_cost(upper_qty,portfolio.get_ptf_broker()):
                    if upper_qty-investment.get_investment_quantity()<0:
                        portfolio.sell_ptf(portfolio.get_ptf_list_investments().index(investment),abs(upper_qty-investment.get_investment_quantity()))
                    
                    elif upper_qty-investment.get_investment_quantity()>0:
                        portfolio.buy_ptf(portfolio.get_ptf_list_investments().index(investment),abs(upper_qty-investment.get_investment_quantity()))
            m_PnL[portfolio.get_ptf_list_investments().index(investment)].append(investment.comp_investment_PnL(portfolio.get_ptf_broker()))
        portfolio.comp_ptf_PnL()
        capital.append(portfolio.get_ptf_capital())
        m_PnL[-1].append(portfolio.get_ptf_PnL())
        value.append(portfolio.comp_ptf_value())
            #print("Investment Quantity :"+ str(investment.get_investment_quantity())+" Price night :"+ str(investment.comp_investment_price(b1)))
            #print("PnL :"+ str(p1.get_ptf_PnL())+"\n")
            
    return ([data.loc[start:end].Date],value, capital, m_PnL)


