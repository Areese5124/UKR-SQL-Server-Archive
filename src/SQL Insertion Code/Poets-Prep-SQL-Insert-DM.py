# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:16:52 2024

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

All_Poets = UKPP_Dataframe["Author of poem"].unique()
All_Poets = All_Poets.tolist()
  
for i in All_Poets:
    value = i
    query = "INSERT INTO Author (Author_Name) VALUES (%s);"
    cursor.execute(query,(value,))
    print("Inserted",cursor.rowcount,"row(s) of data.")

connection.commit()
cursor.close()
