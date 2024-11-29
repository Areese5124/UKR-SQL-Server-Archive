# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:47:39 2024

@author: Arees
"""
import os
os.chdir("C:/Users/Arees/OneDrive/UKPP SQL/dep")

import pandas as pd
import sys
sys.path.insert(0, 'C:/Users/Arees/OneDrive/UKPP SQL/.config')
from ukpp_connector import create_connection_UKPP

connection = create_connection_UKPP()
cursor = connection.cursor()
UKPP_Dataframe = pd.read_excel("UKPP-Dataframe.xlsx")

cursor.execute("SELECT * FROM Poem;")
results = cursor.fetchall()
SQL_Poem_Id_Dict = {value: key for key, value in results}
UKPP_Dataframe['Poem full text (copy and paste)'] = UKPP_Dataframe[
    'Poem full text (copy and paste)'].map(SQL_Poem_Id_Dict)

cursor.execute("SELECT * FROM Author;")
results = cursor.fetchall()
SQL_Author_Id_Dict = {value: key for key, value in results}
UKPP_Dataframe['Author of poem'] = UKPP_Dataframe[
    'Author of poem'].map(SQL_Author_Id_Dict)

cursor.execute("SELECT * FROM Archivist;")
results = cursor.fetchall()
SQL_Archivist_Id_Dict = {value: key for key, value in results}
UKPP_Dataframe['Your name'] = UKPP_Dataframe[
    'Your name'].map(SQL_Archivist_Id_Dict)

cursor.execute("SELECT * FROM Poster;")
results = cursor.fetchall()
SQL_Poster_Id_Dict = {value: key for key, value in results}
UKPP_Dataframe['Author of post'] = UKPP_Dataframe[
    'Author of post'].map(SQL_Poster_Id_Dict)

cursor.execute("SELECT * FROM Translator;")
results = cursor.fetchall()
SQL_Translator_Id_Dict = {value: key for key, value in results}
UKPP_Dataframe['Translator of poem (if poem is a translation)'] = UKPP_Dataframe[
    'Translator of poem (if poem is a translation)'].map(SQL_Translator_Id_Dict)



UKPP_Dataframe = UKPP_Dataframe.iloc[:, 1:]

import xlsxwriter

out_path = "C:/Users/Arees/OneDrive/UKPP SQL/dep/UKPP-SQL-Dataframe-Mapped.xlsx"
writer = pd.ExcelWriter(out_path , engine='xlsxwriter')
UKPP_Dataframe.to_excel(writer, sheet_name='Public Authors')
writer.close()
