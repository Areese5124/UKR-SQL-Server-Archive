# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:15:49 2024

@author: Arees
"""
import pandas as pd

import os
os.chdir("C:/Users/Arees/OneDrive/UKPP SQL/dep")
UKPP_Dataframe = pd.read_excel("UKPP-Dataframe.xlsx")

import sys
sys.path.insert(0, 'C:/Users/Arees/OneDrive/UKPP SQL/.config')
from ukpp_connector import create_connection_UKPP

connection = create_connection_UKPP()
cursor = connection.cursor()
cursor.execute("SELECT * FROM Poem;")
results = cursor.fetchall()

SQL_Poem_Id_Dict = {value: key for key, value in results}
UKPP_Dataframe['Poem full text (copy and paste)'] = UKPP_Dataframe[
    'Poem full text (copy and paste)'].map(SQL_Poem_Id_Dict)

UKPP_Dataframe = UKPP_Dataframe.drop_duplicates(subset=['Poem full text (copy and paste)'])
UKPP_Dataframe['Original language (if post is a translation)'] = UKPP_Dataframe[
    'Original language (if post is a translation)'].str.strip()
UKPP_Dataframe['Language'] = UKPP_Dataframe[
    'Language'].str.strip()

for index, row in UKPP_Dataframe.iterrows():
    if pd.notnull(row["Original language (if post is a translation)"]):
        UKPP_Dataframe.at[index, "Language"] = row["Original language (if post is a translation)"]
        
Org_Languages = list(UKPP_Dataframe["Language"].dropna().unique())

for i in Org_Languages:
    value = i
    query = "INSERT INTO Original_Language (Original_Language) VALUES (%s);"
    cursor.execute(query,(value,))
    print("Inserted",cursor.rowcount,"row(s) of data.")

connection.commit()
cursor.close()