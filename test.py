#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r'C:\Users\risseidr\AppData\Local\Programs\Python\Python38-32\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)
