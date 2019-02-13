#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 17:39:23 2019

@author: mithurangajendran
"""



def comp_find_cheapest_broker(list_brokers,Investement):
    investment_quantity= Investment.get_investment_quantity()
    asset_price= Investment.get_asset_price()
    
    for i in range(0, len(list_brokers)):
        L.append(list_brokers[i].comp_broker_fees(asset_quantity, asset_price))
        
    return list_brokers[argmin(L)].get_broker_name()