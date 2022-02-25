# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:14:49 2022

@author: IrisTerpstra
@organisation: GlobeScope BV
"""

import pandas as pd

df = pd.read_excel (r'C:\Users\IrisTerpstra\Documents\Tenderned_gunningenZS-DMS-VTH_2021.xlsx')

df.drop(0)

df['ZS'] = df['systemen'].str.contains('ZS', regex = False)
df['DMS'] = df['systemen'].str.contains('DMS', regex = False)
df['KCS'] = df['systemen'].str.contains('KCS', regex = False)
df['VTH'] = df['systemen'].str.contains('VTH', regex = False)

df = df[['uitvrager', 'organisatie_code', 'ZS', 'DMS', 'VTH', 
         'KCS', 'datum_aankondiging', 'contractant', 'bedrag', 'systemen']]

print(df)

df.to_excel(r'C:\Users\IrisTerpstra\Documents\Tenderned_gunningen2021_aangepast.xlsx')
