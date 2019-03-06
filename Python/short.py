# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:16:01 2019

@author: nmace
"""
import pandas as pd
import pylab as plt

data= pd.read_csv("C:/Users/nmace/Documents/GitHub/PPE_GIT/Python/Data/d_historique.txt", header=0, delimiter="\t")
Data= pd.read_csv("C:/Users/nmace/Documents/GitHub/PPE_GIT/Python/Data/CourtierSRD.txt", header=0, delimiter="\t")

plt.plot(data.iloc[:]["Date"],data.NATIXIS_SPOT)

#def short(StockQty,ShortFees):
#    
#    StockPr = data.NATIXIS_SPOT    
#    PnL = 0
#  
#    Delta = StockPr[0] - StockPr[8]
#    PnL = (1 - ShortFees) * Delta * StockQty
#    return PnL
#
#print(short(100,0.03))

def MoyenneMobile(nbPeriode,dateT):
    
    sm = 0
    for k in range(dateT-nbPeriode,dateT):
        sm += data.iloc[k]["NATIXIS_SPOT"]
    
    MM = sm / nbPeriode
    
    return MM

print(MoyenneMobile(50,258))



def stopLossBuy(dateT):
    
    L = []
    for k in range(dateT-50,dateT):
        L.append(data.iloc[k]["NATIXIS_SPOT"])
    
    return min(L)
      
print(stopLossBuy(258))
       
def stopLossSell(dateT):
    
    L = []
    for k in range(dateT-50,dateT):
        L.append(data.iloc[k]["NATIXIS_SPOT"])
    
    return max(L)
      
print(stopLossSell(258))

        
        
        