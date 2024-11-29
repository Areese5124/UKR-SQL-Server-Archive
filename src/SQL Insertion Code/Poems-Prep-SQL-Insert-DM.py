# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:57:39 2024

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

All_Poems = UKPP_Dataframe["Poem full text (copy and paste)"].dropna().unique()
Unique3 =UKPP_Dataframe.drop_duplicates(subset=['Poem full text (copy and paste)'])



All_Poems = All_Poems.tolist()

for i in All_Poems:
    value = i
    query = "INSERT INTO Poem (Poem_Full_Text) VALUES (%s);"
    cursor.execute(query,(value,))
    print("Inserted",cursor.rowcount,"row(s) of data.")

connection.commit()
