#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MyWebDriver(webdriver.chrome):
    pass


options = Options()
options.binary_location = r'C:\Program Files\ntko controls\ntkochrome.exe'
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r'C:\Users\risseidr\AppData\Local\Programs\Python\Python38-32\chromedriver.exe'
driver = MyWebDriver(chrome_options=options)
print(driver.title)
