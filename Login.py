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
from selenium.webdriver.chrome.options import Options
from MailPageElements import MailBox


class LoginWeb(WebDriver):
    def __init__(self, executable_path="chromedriver", port=0, options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None, chrome_options=None, keep_alive=True):
        self.__chrome_options = chrome_options
        self.__chrome_options = Options()
        self.__chrome_options.binary_location = r'C:\Program Files\ntko controls\ntkochrome.exe'
        super().__init__(executable_path, port, options, service_args, desired_capabilities, service_log_path,
                         self.__chrome_options, keep_alive)

    def login(self, mailbox_num: int, username: str, password: str) -> MailBox:
        self.get('http://zntemail.zhenergy.com.cn/mail/znte/U' + str(mailbox_num) + '.nsf/index.html')
        self.implicitly_wait(5)
        sleep(0.5)
        if self.title == '邮件系统-内网邮件':
            return MailBox(self)
        elif self.title == '服务器登录':
            username_element = self.find_element_by_css_selector('input#user-id')
            username_element.clear()
            username_element.send_keys(username)
            username_element.send_keys(Keys.TAB)
            password_element = self.find_element_by_css_selector('input#pw-id')
            password_element.clear()
            password_element.send_keys(password)
            password_element.send_keys(Keys.TAB)
            password_element.send_keys(Keys.ENTER)
            sleep(0.5)
            return MailBox(self)
