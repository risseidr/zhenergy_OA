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

    def _create_download_path(self):
        try:
            os.makedirs(self._settings.temp_download_path)
        except FileExistsError or WinError as e:
            print(e)

    def _set_download_path(self):
        dlg = win32gui.FindWindow('#32770', '位置')
        text = win32gui.FindWindowEx(dlg, 0, 'Edit', None)
        win32api.SendMessage(text, win32con.WM_SETTEXT, 0, os.path.abspath(self._settings.temp_download_path))
        win32gui.PostMessage(dlg, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.PostMessage(dlg, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    def _options_init(self):
        self._options.add_experimental_option(
            "debuggerAddress", "127.0.0.1:" + str(self._settings.remote_debugging_port_id))

    def _bind_driver(self):
        return WebDriver(self._settings.chromedriver_dir, options=self._options)

    def _click_path_setting_button(self):
        self._driver.get('chrome://settings/downloads')
        print(self._driver.text)
        a = self._driver.find_element_by_xpath('//*[@id="changeDownloadsPath"]//cr-button')
        a.click()

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
        self._create_download_path()
        # self._click_path_setting_button()
        # self._set_download_path()
        return self._driver
