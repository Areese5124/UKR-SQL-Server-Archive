# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:31:11 2024

@author: Arees
"""

import os
import pandas as pd

import sys
sys.path.insert(0, 'C:/Users/Arees/OneDrive/UKPP SQL/.config')
from ukpp_connector import create_connection_UKPP

connection = create_connection_UKPP()
cursor = connection.cursor()

os.chdir("C:/Users/Arees/OneDrive/UKPP SQL/dep")

UKPP_Dataframe = pd.read_excel("UKPP-Dataframe.xlsx")

All_Posters = UKPP_Dataframe["Author of post"].unique()
All_Posters = All_Posters.tolist()

for i in All_Posters:
    value = i
    query = "INSERT INTO Poster (Poster_Name) VALUES (%s);"
    cursor.execute(query,(value,))
    print("Inserted",cursor.rowcount,"row(s) of data.")
    
connection.commit()
cursor.close()
