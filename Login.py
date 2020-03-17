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
from selenium.webdriver.chrome.webdriver import WebDriver
from Settings import Settings


class Login(WebDriver):
    def login(self, settings: Settings):
        self.get('http://zntemail.zhenergy.com.cn/mail/znte/U' + settings.mailbox_num + '.nsf/index.html')
        self.implicitly_wait(3)
        sleep(0.5)
        if self.title == '邮件系统-内网邮件':
            return self
        elif self.title == '服务器登录':
            username_element = self.find_element_by_css_selector('input#user-id')
            username_element.clear()
            username_element.send_keys(settings.username)
            username_element.send_keys(Keys.TAB)
            password_element = self.find_element_by_css_selector('input#pw-id')
            password_element.clear()
            password_element.send_keys(settings.password)
            password_element.send_keys(Keys.TAB)
            password_element.send_keys(Keys.ENTER)
            sleep(0.5)
            if self.title == '邮件系统-内网邮件':
                return self
