# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:33:37 2024

@author: Arees
"""
import pandas as pd
import os
import numpy as np

os.chdir("C:/Users/Arees/OneDrive/UKPP SQL/dep")
UKPP_Dataframe_Mapped = pd.read_excel("UKPP-SQL-Dataframe-Mapped.xlsx")

import sys
sys.path.insert(0, 'C:/Users/Arees/OneDrive/UKPP SQL/.config')
from ukpp_connector import create_connection_UKPP

connection = create_connection_UKPP()
cursor = connection.cursor()
query = "SELECT * FROM UKPP_Poem_Details"
sql_df = pd.read_sql_query(query, connection)

sql_df[["Poem",
        "Author_Name",
        "Archivist_Name",
        "Post_Url",
        "Poster_Name",
        "Translator",
        "Date_Posted",
        "Poems_In_Comments",
        "Suggestions_Or_Corrections",
        "Comments",
        "Number_Of_Likes",
        "Number_Of_Comments",
        "Number_Of_Shares"
        ]] = UKPP_Dataframe_Mapped[["Poem full text (copy and paste)",
                                    "Author of poem",
                                    "Your name",
                                    "url of facebook post",
                                    "Author of post",
                                    "Translator of poem (if poem is a translation)",
                                    "Date posted",
                                    "Poem(s) in comment field?",
                                    "Suggestion/correction in comment field? ",
                                    "Comments (copy and paste)",
                                    "Number of likes",
                                    "Number of comments",
                                    "Number of shares"
                                    ]]

sql_df['Date_Posted'] = pd.to_datetime(sql_df['Date_Posted'], errors='coerce')
sql_df['Translated_Post'] = sql_df['Translator'].notna() & (sql_df['Translator'] != '')



for index, row in UKPP_Dataframe_Mapped.iterrows():
    if pd.notnull(row["Original language (if post is a translation)"]):
        UKPP_Dataframe_Mapped.at[index, "Original language (if post is a translation)"] = row[
            "Language"]

cursor.execute("SELECT * FROM Translation_Languages;")
results = cursor.fetchall()
SQL_Translation_Lang_Id_Dict = {value: key for key, value in results}
sql_df['Translation_Language'] = UKPP_Dataframe_Mapped[
    'Original language (if post is a translation)'].map(SQL_Translation_Lang_Id_Dict)
sql_df['Translation_Language'] = sql_df['Translation_Language'].where(sql_df['Translated_Post'], np.nan)

sql_df.Poems_In_Comments.fillna("No", inplace=True)
sql_df.Poems_In_Comments.replace({'Yes': True, 'No': False}, inplace=True)
sql_df.Suggestions_Or_Corrections.fillna("No", inplace=True)
sql_df.Suggestions_Or_Corrections.replace({'Yes': True, 'No': False}, inplace=True)
sql_df.Number_Of_Likes.fillna(0, inplace=True)
sql_df.Number_Of_Comments.fillna(0, inplace=True)
sql_df.Number_Of_Shares.fillna(0, inplace=True)









