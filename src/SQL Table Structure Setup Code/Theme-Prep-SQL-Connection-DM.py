# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:55:32 2024

@author: Arees
"""

Themes = ['War', 'Religion', 'Ukraine', 'Death', 'Time', 'Russia', 'Geography', 
     'Seasons', 'Family', 'Language', 'Animals', 'Memory', 'Maidan', 'Nature', 
     'Protest', 'Poetry', 'Love', 'Psychology', 'Fruit', 'Gender', 
     'Mythology', 'Dreams']

import sys
sys.path.insert(0, 'C:/Users/Arees/OneDrive/UKPP SQL/.config')
from ukpp_connector import create_connection_UKPP

connection = create_connection_UKPP()
cursor = connection.cursor()

for i in Themes:
    query = f"ALTER TABLE Themes ADD COLUMN {i} TINYINT(1);"
    cursor.execute(query)
    
connection.commit()
cursor.close()