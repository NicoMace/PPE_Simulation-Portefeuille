#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:32:19 2019

@author: mithurangajendran
"""

#P######################################## PATH
import os
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    #Mithuran
os.chdir('D:/Users/Pierre/Documents/8 - Scolarite/ECE/PPE/PPE_GIT/Python')    #Pierre
#os.chdir('/Users/mithurangajendran/Documents/PPE_GIT/Python')    'Mithuran
#os.chdir('/Users/nmace/Documents/GitHub/PPE_GIT/Python')          #Nicolas

######################################### INISTIALISATION ######################@
import tensorflow as tf
import numpy as np
from Classes.IA_Process import DataProcessing


def create_model():
    pass

def train_model(data,asset_name):
    
    df=data.loc[:,['Date',asset_name]]
    process = DataProcessing(df, 0.9,2)
    process.gen_test(10)
    process.gen_train(10)
    X_train = process.X_train / 200
    Y_train = process.Y_train / 200
    
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(1, activation=tf.nn.relu))
    model.compile(optimizer="adam", loss="mean_squared_error")
    model.fit(X_train, Y_train, epochs=100, verbose=0)
    #model.save_weights(str(asset_name+"_my_model"+".h5"))
    return model

#model=train_model(data,"NATIXIS_SPOT")

def forecast_next_value(data,jour,asset_name, model):
    #model = tf.keras.models.Sequential()
    #model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu,input_dim=10))
    #model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
    #model.add(tf.keras.layers.Dense(1, activation=tf.nn.relu))
    #model.load_weights(str(asset_name+"_my_model"+".h5"))
    
    stock=data.iloc[jour-10:jour][asset_name]
    X_predict = np.array(stock).reshape((1, 10)) / 200
    out=model.predict(X_predict)*200
    return(out[0][0])

#forecast_next_value(data, 70,"NATIXIS_SPOT",model,10)

def strat_forecast(portfolio,b_date,e_date, periode,quantity_percent,data,if_model=False):#PERIODE DE 10 car BATCH DE 10
    
    value=[]
    capital=[]
    m_PnL=[]
    for i in range(len(portfolio.get_ptf_list_investments())):
        m_PnL.append([])
    m_PnL.append([])
    
    if if_model==False:
        model=[]
        for investment in portfolio.get_ptf_list_investments():
            model.append(train_model(data,investment.get_investment_asset().get_asset_ISIN()))
    else:
        model=if_model
        

    start= data.loc[data["Date"] == b_date].index[0]
    end= data.loc[data["Date"] == e_date].index[0]
    
    for jour in range(start+10,end+1,periode):
        #print("\nJour :" +str(jour))

        for investment in portfolio.get_ptf_list_investments():
        
            investment.set_investment_cost(data.iloc[start][investment.get_investment_asset().get_asset_ISIN()])
            prix_actif= data.iloc[jour][investment.get_investment_asset().get_asset_ISIN()]
            investment.get_investment_asset().set_asset_price(prix_actif)
            investment_quantity= investment.get_investment_quantity()
            
            next_asset_price=forecast_next_value(data,jour,investment.get_investment_asset().get_asset_ISIN(), model[portfolio.get_ptf_list_investments().index(investment)])
            #print(str(investment.get_investment_asset().get_asset_ISIN())+" : "+str(next_asset_price))
            if next_asset_price >prix_actif:
                 portfolio.buy_ptf(portfolio.get_ptf_list_investments().index(investment),int(quantity_percent*investment_quantity))
            
            elif next_asset_price < prix_actif and investment_quantity-int(quantity_percent*investment_quantity)>0 and next_asset_price!=-0:
                portfolio.sell_ptf(portfolio.get_ptf_list_investments().index(investment),int(quantity_percent*investment_quantity))

            portfolio.comp_ptf_PnL()
            m_PnL[portfolio.get_ptf_list_investments().index(investment)].append(investment.comp_investment_PnL(portfolio.get_ptf_broker()))
        portfolio.comp_ptf_PnL()
        capital.append(portfolio.get_ptf_capital())
        m_PnL[-1].append(portfolio.get_ptf_PnL())
        value.append(portfolio.comp_ptf_value())
    portfolio.comp_max_drawdown(m_PnL[-1])
    
    return ([data.loc[start:end].Date],value, capital, m_PnL,model)




