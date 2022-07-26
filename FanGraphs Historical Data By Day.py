#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:17:23 2022

@author: dylanelder
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}

output = {
        'Rank': [],
        'Team': [],
        'K/9': [],
        'BB/9': [],
        'K/BB': [],
        'HR/9': [],
        'K%': [],
        'BB%': [],
        'K_BB%': [],
        'AVG': [],
        'WHIP': [],
        'BABIP': [],
        'LOB%': [],
        'ERA-': [],
        'FIP-': [],
        'xFIP-': [],
        'ERA': [],
        'FIP': [],
        'E-F': [],
        'xFIP':[],
        'SIERA': [],
        'Date': [],
        
        }


def getFanGraphs(month, day):

    url = f'https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=1&season=2021&month=1000&season1=2021&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2021-04-01&enddate=2021-{month}-{day}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    for x in range (0,30):
        x = url
        x = x.split('&enddate=2021-')
        y = x[1]
        z = y.replace('-','')
        z1 = (z[1:])

        output['Date'].append(z1)
    
    table = soup.find('table', class_ = 'rgMasterTable')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    
    for td in rows:
        td = td.find_all('td')
                
        output['Rank'].append(td[0].text)
        output['Team'].append(td[1].text)
        output['K/9'].append(td[2].text)
        output['BB/9'].append(td[3].text)
        output['K/BB'].append(td[4].text)
        output['HR/9'].append(td[5].text)
        output['K%'].append(td[6].text)
        output['BB%'].append(td[7].text)
        output['K_BB%'].append(td[8].text)
        output['AVG'].append(td[9].text)
        output['WHIP'].append(td[10].text)
        output['BABIP'].append(td[11].text)
        output['LOB%'].append(td[12].text)
        output['ERA-'].append(td[13].text)
        output['FIP-'].append(td[14].text)
        output['xFIP-'].append(td[15].text)
        output['ERA'].append(td[16].text)
        output['FIP'].append(td[17].text)
        output['E-F'].append(td[18].text)
        output['xFIP'].append(td[19].text)
        output['SIERA'].append(td[20].text)
        
    return




month = oct(4)

for month in range (4, 10):
    
    month = ("{:02d}".format(month))

    date = oct(1)
    
    
    if  month == '04':

        for date in range (10, 31):
            date = ("{:02d}".format(date))
            getFanGraphs(month, date)
            
    elif  month == '05':

        for date in range (1, 32):
            date = ("{:02d}".format(date))
            getFanGraphs(month, date)
            
    elif  month == '06':

        for date in range (1, 31):
            date = ("{:02d}".format(date))
            getFanGraphs(month, date)
            
    elif  month == '07':

        for date in range (1, 32):
            date = ("{:02d}".format(date))
            getFanGraphs(month, date)
            
    elif  month == '08':

        for date in range (1, 32):
            date = ("{:02d}".format(date))
            getFanGraphs(month, date)
            
    elif  month == '09':

        for date in range (1, 31):
            date = ("{:02d}".format(date))
            getFanGraphs(month, date)

          




FG_Data = pd.DataFrame(output)

FG_Data.to_excel('FG_Data.xlsx')









