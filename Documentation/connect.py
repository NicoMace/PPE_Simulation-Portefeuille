# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:16:53 2019

@author: Valentin
"""

def get_histo():
    conn=mysql.connector.connect(user='serveur',password='unic0rn42',database='Server')
    cursor=conn.cursor()
    query="SELECT * FROM website_d_historique;"
    cursor.execute(query)
    string=cursor.fetchall()
    data=pd.DataFrame([string])
    conn.close()
    return data

def get_broker():
    conn=mysql.connector.connect(user='serveur',password='unic0rn42',database='Server')
    cursor=conn.cursor()
    query="SELECT * FROM website_courtiers;"
    cursor.execute(query)
    string=cursor.fetchall()
    data=pd.DataFrame([string])
    conn.close()
    return data

def get_results():
    conn=mysql.connector.connect(user='serveur',password='unic0rn42',database='Server')
    cursor=conn.cursor()
    query="SELECT * FROM website_results;"
    cursor.execute(query)
    string=cursor.fetchall()
    data=pd.DataFrame([string])
    conn.close()
    return data