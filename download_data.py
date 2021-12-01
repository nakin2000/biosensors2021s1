# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 22:29:48 2021

@author: kin45
"""

import requests,pandas as pd
url = "https://covid19.ddc.moph.go.th/"
url_province_daily = "https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-by-provinces"
# above url api json

req = requests.get(url_province_daily)
url_content = req.content
file_tmp = open('download_province_daily.json','wb')
file_tmp.write(url_content)
file_tmp.close()

df_json = pd.read_json('download_province_daily.json')
df_json.to_csv('download_province_timeline.csv' ,encoding='utf-8-sig')
df_json.to_excel('download_province_timeline.xlsx')