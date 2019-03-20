# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:35:14 2019

@author: Valentin
"""

def connect():
    conn=mysql.connector.connect(user='serveur',password='unic0rn42',database='Server')
    cursor=conn.cursor()
    query="SELECT * FROM website_d_historique;"
    cursor.execute(query)
    string=cursor.fetchall()
    data=[string]
    df=pd.DataFrame(string)

    return df.iloc[0,1]