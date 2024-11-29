# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:42:17 2024

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

All_Archivists = UKPP_Dataframe["Your name"].unique()
All_Archivists = All_Archivists.tolist()

for i in All_Archivists:
    value = i
    query = "INSERT INTO Archivist (Archivist_Name) VALUES (%s);"
    cursor.execute(query,(value,))
    print("Inserted",cursor.rowcount,"row(s) of data.")

connection.commit()
cursor.close()