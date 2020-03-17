#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import datetime

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from login import login
from MailIndexPage import MailIndexPage
from Settings import Settings
from content_main.MailBox import MailBox

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r'C:\Users\risseidr\AppData\Local\Programs\Python\Python38-32\chromedriver.exe'
driver = WebDriver(chrome_driver, chrome_options=options)
# driver = WebDriver(options=options)
print(driver.title)
driver.maximize_window()
settings = Settings()
index_page = MailIndexPage(login(driver, settings)).inbox
mailbox = MailBox(index_page)

print(datetime.now())

mailbox.delete_mail()

print(datetime.now())
# td = BriefMailPageElements(driver)
# for tr in td.brief_tr():
#     mail_info = MailInfo(tr)
#     if mail_info.subject().find('收到： ') == 0:
#         mail_info.set_del_tag()
