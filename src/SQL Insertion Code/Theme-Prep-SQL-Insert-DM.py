# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:08:45 2024

@author: Arees
"""
import pandas as pd
import sys

sys.path.insert(0, 'C:/Users/Arees/OneDrive/UKPP SQL/.config')
from ukpp_connector import create_connection_UKPP

connection = create_connection_UKPP()
cursor = connection.cursor()
query = "SELECT * FROM Themes"
sql_df = pd.read_sql_query(query, connection)

import os
os.chdir("C:/Users/Arees/OneDrive/UKPP SQL/dep")

UKPP_Dataframe_Mapped = pd.read_excel("UKPP-SQL-Dataframe-Mapped.xlsx")

Theme_List = ['War', 'Religion', 'Ukraine', 'Death', 'Time', 'Russia', 'Geography', 
     'Seasons', 'Family', 'Language', 'Animals', 'Memory', 'Maidan', 'Nature', 
     'Protest', 'Poetry', 'Love', 'Psychology', 'Fruit', 'Gender', 
     'Mythology', 'Dreams']


UKPP_Dataframe_Mapped = UKPP_Dataframe_Mapped.drop_duplicates(subset=['Poem full text (copy and paste)'])

sql_df['idTheme_Poem'] = UKPP_Dataframe_Mapped['Poem full text (copy and paste)'].unique()

for theme in Theme_List:
    column_name = f'{theme}'
    sql_df[column_name] = UKPP_Dataframe_Mapped.iloc[:, 9].str.contains(theme, case=False)
sql_df.replace({False: 0, True: 1}, inplace=True)


from ukpp_connector import create_engine_UKPP
engine = create_engine_UKPP()
sql_df.to_sql(name='Themes', con=engine, if_exists='append', chunksize = 1000, index= False)
connection.commit()
