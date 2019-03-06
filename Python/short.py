# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:16:01 2019

@author: nmace
"""
import pandas as pd
import pylab as plt

data= pd.read_csv("C:/Users/nmace/Documents/GitHub/PPE_GIT/Python/Data/d_historique.txt", header=0, delimiter="\t")
#Data= pd.read_csv("C:/Users/nmace/Documents/GitHub/PPE_GIT/Python/Data/CourtierSRD.txt", header=0, delimiter="\t")

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

def MoyenneMobile(nbPeriode,dateEntry):
    
    sm = 0
    for k in range(dateEntry-nbPeriode,dateEntry):
        sm += data.iloc[k]["NATIXIS_SPOT"]
    
    MM = sm / nbPeriode
    
    return MM

#print("Moyenne Mobile : " + str(MoyenneMobile(50,258)))



def stopLossBuy(dateEntry):
    
    L = []
    for k in range(dateEntry-50,dateEntry):
        L.append(data.iloc[k]["NATIXIS_SPOT"])
    
    return min(L)
      
#print("SL buy : " + str(stopLossBuy(258)))
       
def stopLossSell(dateEntry):
    
    L = []
    for k in range(dateEntry-50,dateEntry):
        L.append(data.iloc[k]["NATIXIS_SPOT"])
    
    return max(L)
      
#print("SL sell : " + str(stopLossSell(258)))


def MaxDrawDown(dateEntry,dateSorty):
    
    L = []

    for k in range(dateEntry,dateSorty):
        if((data.iloc[k]["NATIXIS_SPOT"] > data.iloc[k-1]["NATIXIS_SPOT"] and data.iloc[k]["NATIXIS_SPOT"] < data.iloc[k+1]["NATIXIS_SPOT"]) or (data.iloc[k]["NATIXIS_SPOT"] < data.iloc[k-1]["NATIXIS_SPOT"] and data.iloc[k]["NATIXIS_SPOT"] > data.iloc[k+1]["NATIXIS_SPOT"])):
            L.append(data.iloc[k]["NATIXIS_SPOT"])
    
    Max=L[0]
    Min=L[1]
    
    if(L[0]>L[1]):
        for i in range(0,len(L)-1):
            if(L[i] > L[i+1]):
                if(L[i] > Max):
                    Max = L[i]
                elif(L[i+1] < Min):
                    Min = L[i+1]

    else:
        for i in range(1,len(L)-1):
            if(L[i] > L[i+1]):
                if(L[i] > Max):
                    Max = L[i]
                elif(L[i+1] < Min):
                    Min = L[i+1]
    
    risk = (Max - Min)/Max * 100
    
    return risk


print("Risk : " + str(MaxDrawDown(4,55)) + " %")