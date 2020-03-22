#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LoginWeb.py
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-14 17:29   risseidr   1.0         None
"""
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from Settings import Settings


def login(driver: WebDriver, settings: Settings):
    driver.get('http://zntemail.zhenergy.com.cn/mail/znte/U' + settings.mailbox_num + '.nsf/index.html')
    # driver.get('http://dmoa.zhenergy.com.cn/')
    driver.implicitly_wait(3)
    sleep(0.5)
    if driver.title == '邮件系统-内网邮件':
        return driver
    else:
        username_element = driver.find_element_by_css_selector('input#user-id')
        username_element.clear()
        username_element.send_keys(settings.username)
        username_element.send_keys(Keys.TAB)
        password_element = driver.find_element_by_css_selector('input#pw-id')
        password_element.clear()
        password_element.send_keys(settings.password)
        password_element.send_keys(Keys.TAB)
        password_element.send_keys(Keys.ENTER)
        sleep(0.5)
        if driver.title == '邮件系统-内网邮件':
            return driver
