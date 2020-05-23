# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser
import time
import Inputhandler as Inputhandler
import requests

config = configparser.RawConfigParser()
config.read('interview.properties')

options = Options()
#options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--disable-infobars')
options.add_argument('--start-fullscreen')
options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(chrome_options=options)

'''
Assignment 1
'''


url = config.get('assignment1', 'url')
driver.get(url)
org_zip = config.get('assignment1', 'org.input')
dst_zip = config.get('assignment1', 'dst.input')
org_xpath = config.get('assignment1', 'org')
dst_xpath = config.get('assignment1', 'dst')
submit_xpath = config.get('assignment1', 'submit')
result_xpath = config.get('assignment1', 'result')
accept_cookies_xpath  = config.get('assignment1', 'accept_cookies')

Inputhandler.mouseClick(driver,accept_cookies_xpath)
Inputhandler.sendKey(driver,org_xpath,org_zip)
Inputhandler.mouseClickSendKeyandEnter(driver,dst_xpath,dst_zip)
Inputhandler.mouseClick(driver,submit_xpath)
time.sleep(1)
Inputhandler.mouseClick(driver,accept_cookies_xpath)
result = Inputhandler.readText(driver,result_xpath)
try:
    with open('result.txt','w') as f:
        f.write(result)
except Exception as e:
    print('no service availabel on weekends/holidays.')
"""
Output will be saved in result.txt file
"""


'''
Assignment 2
'''


url = config.get('assignment2', 'url')
driver.get(url)
search_xpath = config.get('assignment2', 'search')
search_key = [config.get('assignment2', 'input')]

search_suggestion = config.get('assignment2', 'search_bar')

required_results = dict()
def suggestion_extract(key):
    try:
        Inputhandler.sendKey(driver,search_xpath,key[:-1])
        time.sleep(5)
        result = Inputhandler.readText(driver,search_suggestion)
        driver.get(url)
        temp = [print(key,'  ',search_sug) for search_sug in result.split('\n') if key in search_sug]
        return [search_sug for search_sug in result.split('\n') if key in search_sug]
    except Exception as e:
        return []


search_results = suggestion_extract(search_key[0])
search_key.extend(search_results)
required_results[search_key[0]] = search_results


for index,key in enumerate(set(search_key[1:])):
    search_results = suggestion_extract(key)
    search_key.extend(search_results)
    required_results[key] = search_results
    if index==5:
        break


print("required_results",required_results)

driver.close()

"""
Output will be printed in dict format, and can be changed to any required format
"""

"""
log will be saved in selenium.log file
"""