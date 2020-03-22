#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   startchrome.py
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-21 15:04   risseidr   1.0         None
"""
import os
import re
from ctypes import WinError

import win32api
import win32con
import win32gui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from Settings import settings


class StartChrome(object):
    def __init__(self, s=settings):
        self._options = Options()
        self._driver = None
        self._settings = s
        self._options_init()

    def _open_chrome(self):
        os.popen(self._settings.chrome_dir + self._settings.start_argument)

    def _options_init(self):
        self._options.add_experimental_option(
            "debuggerAddress", "127.0.0.1:" + str(self._settings.remote_debugging_port_id))

    def _bind_driver(self):
        return WebDriver(self._settings.chromedriver_dir, options=self._options)

    def start_chrome(self):
        with os.popen('netstat -ano|findstr "LISTENING"|findstr "9222"') as f1:
            info1 = f1.read()
            if info1:
                pid = re.split('\\s+', re.split('\\n+', info1)[0])[-1]
                with os.popen('tasklist|findstr "' + pid + '"') as f2:
                    info2 = f2.read()
                process = re.split('\\s+', info2)[0]
                if process == 'chrome.exe':
                    self._driver = self._bind_driver()
                else:
                    raise Exception('remote debugging pid' + ' is occupied')
            else:
                self._open_chrome()
                self._driver = self._bind_driver()
        return self._driver
