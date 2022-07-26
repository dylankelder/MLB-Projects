#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:40:46 2022

@author: dylanelder
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ChromeDriverManager:
    pass


driver = webdriver.Chrome(executable_path='/Users/dylanelder/Desktop/Python-SL/chromedriver')

#Lines 22-23 contain login information for FanGraphs.com. I recommend supporting FanGraphs yourself by purchasing your own subscription :)
username = 'dke5'
password = 'ZyyWwodFKfMa'

#Lines 26-31 login to a password protected version of the FanGraphs website
log_url = 'https://blogs.fangraphs.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.fangraphs.com%2Fleaders.aspx%3Fpos%3Dall%26stats%3Dbat%26lg%3Dall%26qual%3Dy%26type%3D8%26season%3D2021%26month%3D0%26season1%3D2021%26ind%3D0'
driver.get(log_url)
driver.find_element_by_name('log').send_keys(username)
driver.find_element_by_name('pwd').send_keys(password)
driver.find_element_by_css_selector('#wp-submit').click()
print('success')

#Lines 34-38 download starting pitcher data
driver.get('https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=1&season=2022&month=0&season1=2022&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="LeaderBoard1_dg1_ctl00__29"]/td[22]')))
link = driver.find_element_by_link_text('Export Data')
link.click()

#Lines 41-45 download splits data vs LHP
driver.get('https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=1&splitArrPitch=&position=B&autoPt=false&splitTeams=false&statType=team&statgroup=2&startDate=2022-03-01&endDate=2022-11-01&players=&filter=&groupBy=season&wxTemperature=&wxPressure=&wxAirDensity=&wxElevation=&wxWindSpeed=&sort=23,1')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-drop-test"]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[30]/td[17]')))
link1 = driver.find_element_by_link_text('Export Data')
link1.click()

#Lines 48-52 download splits data vs RHP
driver.get('https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=2&splitArrPitch=&position=B&autoPt=false&splitTeams=false&statType=team&statgroup=2&startDate=2022-03-01&endDate=2022-11-01&players=&filter=&groupBy=season&wxTemperature=&wxPressure=&wxAirDensity=&wxElevation=&wxWindSpeed=&sort=23,1')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-drop-test"]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[30]/td[17]')))
link2 = driver.find_element_by_link_text('Export Data')
link2.click()

print('Fin!')
#After this program runs, the program titled "MLB_daily_data_collection" uses the local CSV downloads to access the starting pitcher and splits data
