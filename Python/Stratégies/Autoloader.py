"""
Created on Wed Jan 16 15:44:49 ù


@author: mithurangajendran
"""
import sys
sys.path.append("/Users/mithurangajendran/Documents/PPE_GIT/Python/Classes")

import pandas as pd
from User import User
from Portfolio import Portfolio
from Stock import Stock
from Broker import Broker
from Investment import Investment
d_broker= pd.read_csv("/Users/mithurangajendran/Documents/PPE_GIT/Python/Data/Courtiers.txt",header=0, delimiter=" ")
data= pd.read_csv("/Users/mithurangajendran/Documents/PPE_GIT/Python/Data/d_historique.txt", header=0, delimiter="\t")