#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Settings.py    
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-17 12:42   risseidr   1.0         None
"""
import os

from selenium import webdriver


class Settings(object):
    def __init__(self):
        self._chrome_dir = os.path.join(
            os.getenv('USERPROFILE'), r'AppData\Local\Google\Chrome\Application\chrome.exe')
        self._remote_debugging_port_id = 9222
        self._start_argument = r' --remote-debugging-port=' + str(self._remote_debugging_port_id) + \
                               ' --user-data-dir="C:\selenum\AutomationProfile"'
        self._chromedriver_dir = os.path.join(
            os.getenv('USERPROFILE'), r'AppData\Local\Programs\Python\Python38-32\chromedriver.exe')
        self._mailbox_num = '14411'
        self._username = 'zhubinyuan'
        self._password = '12345678'
        self._save_root_path_ = os.getenv('USERPROFILE')
        self._save_type = 0

    @property
    def chrome_dir(self):
        return self._chrome_dir

    @property
    def remote_debugging_port_id(self):
        return self._remote_debugging_port_id

    @property
    def start_argument(self):
        return self._start_argument

    @property
    def chromedriver_dir(self):
        return self._chromedriver_dir

    @property
    def mailbox_num(self):
        return self._mailbox_num

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def save_root_path(self):
        return self._save_root_path_

    @property
    def save_type(self):
        return self._save_type
