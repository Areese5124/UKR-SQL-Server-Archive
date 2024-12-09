# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:57:39 2024

@author: Arees
"""

import os
import pandas as pd

os.chdir("C:/Users/Arees/OneDrive/Repositorys/UKR-SQL-Server-Archive/dep")

UKPP_Dataframe = pd.read_excel("UKPP-Dataframe.xlsx")
UKPP_Dataframe = UKPP_Dataframe.drop_duplicates(subset=['Poem full text (copy and paste)'])

sql_df = pd.DataFrame()
sql_df['Poem_Full_Text'] = UKPP_Dataframe["Poem full text (copy and paste)"].dropna()



import sys
sys.path.insert(0, 'C:/Users/Arees/OneDrive/Repositorys/UKR-SQL-Server-Archive/.config')
from ukpp_connector import create_connection_UKPP
connection = create_connection_UKPP()
cursor = connection.cursor()

cursor.execute("SELECT * FROM Original_Language;")
results = cursor.fetchall()
SQL_Og_Lang_Dict = {value: key for key, value in results}

UKPP_Dataframe['Original language (if post is a translation)'] = UKPP_Dataframe[
    'Original language (if post is a translation)'].str.strip()
UKPP_Dataframe['Language'] = UKPP_Dataframe[
    'Language'].str.strip()

for index, row in UKPP_Dataframe.iterrows():
    if pd.notnull(row["Original language (if post is a translation)"]):
        UKPP_Dataframe.at[index, "Language"] = row["Original language (if post is a translation)"]

sql_df['Poem_Original_Language'] = UKPP_Dataframe[
    'Language'].map(SQL_Og_Lang_Dict)

from ukpp_connector import create_engine_UKPP
engine = create_engine_UKPP()
sql_df.to_sql(name='Poem', con=engine, if_exists='append', chunksize = 1000, index= False)
connection.commit()
