# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:49:50 2024

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

UKPP_Dataframe['Original language (if post is a translation)'] = UKPP_Dataframe[
    'Original language (if post is a translation)'].str.strip()
UKPP_Dataframe['Language'] = UKPP_Dataframe[
    'Language'].str.strip()

for index, row in UKPP_Dataframe.iterrows():
    if pd.notnull(row["Original language (if post is a translation)"]):
        UKPP_Dataframe.at[index, "Original language (if post is a translation)"] = row[
            "Language"]

Translation_Languages = UKPP_Dataframe["Original language (if post is a translation)"].dropna().unique()
Translation_Languages = Translation_Languages.tolist()

for i in Translation_Languages:
    value = i
    query = "INSERT INTO Translation_Languages (Languages) VALUES (%s);"
    cursor.execute(query,(value,))
    print("Inserted",cursor.rowcount,"row(s) of data.")

connection.commit()
cursor.close()