#-*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:02:45 2024

@author: Arees
"""
import xlsxwriter
import gspread
import pandas as pd

gc = gspread.service_account()
sh = gc.open("UkrPoetry database")

worksheet = sh.get_worksheet(5)
UKPP_Database = worksheet.get_all_values()
name = UKPP_Database[0]
UKPP_Dataframe = pd.DataFrame(data = UKPP_Database[1:], columns = name)


UKPP_Dataframe['Author of poem'] = UKPP_Dataframe['Author of poem'].replace(
    'kateryna mikhalitsyna', 'Kateryna Mikhalitsyna'
    )


UKPP_Dataframe['Author of post'] = UKPP_Dataframe['Author of post'].str.strip()
UKPP_Dataframe['Author of post'] = UKPP_Dataframe['Author of post'].replace(
    ['Alessandro Achillei', 'Alessandro Achili'
      ],'Alessandro Achilli'
    )  
UKPP_Dataframe['Author of post'] = UKPP_Dataframe['Author of post'].replace(
    ['Aneta Kaminsky', 'Aneta Kaminska'
      ],'Aneta Kamińska'
    )  
UKPP_Dataframe['Author of post'] = UKPP_Dataframe['Author of post'].replace(
    ['Boris Humeniuk', 'Boris Humanyuk'
      ],'Borys Humeniuk'
    )
UKPP_Dataframe['Author of post'] = UKPP_Dataframe['Author of post'].replace(
    "Ol'ha Chukashkyna", "Ol'ga Chukashkyna"
    )
UKPP_Dataframe['Author of post'] = UKPP_Dataframe['Author of post'].replace(
    "Stanislav Belsky", "Stanislav Belskiy"
    )
UKPP_Dataframe['Author of post'] = UKPP_Dataframe['Author of post'].replace(
    "Váno Krueger", "Vano Krueger"
    )


UKPP_Dataframe['Your name'] = UKPP_Dataframe['Your name'].fillna(
    "Name Not Recorded")


UKPP_Dataframe['Translator of poem (if poem is a translation)'] = UKPP_Dataframe[
    'Translator of poem (if poem is a translation)'].replace(
    "Stalislav Belsky", "Stanislav Belskiy"
    )
UKPP_Dataframe['Translator of poem (if poem is a translation)'] = UKPP_Dataframe[
    'Translator of poem (if poem is a translation)'].replace(
    "Stanislav Belsky", "Stanislav Belskiy"
    )

UKPP_Dataframe['Original language (if post is a translation)'] = UKPP_Dataframe[
    'Original language (if post is a translation)'].replace(
    "Ukranian", "Ukrainian"
    )

        
        
out_path = "C:/Users/Arees/OneDrive/UKPP SQL/dep/UKPP-Dataframe.xlsx"
writer = pd.ExcelWriter(out_path , engine='xlsxwriter')
UKPP_Dataframe.to_excel(writer, sheet_name='Public Authors')
writer.close()
