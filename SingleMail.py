#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SingleMail.py
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-14 19:46   risseidr   1.0         None

"""
from datetime import datetime
from time import sleep

import win32api
import win32con
import win32gui
from selenium.webdriver.ie.webdriver import WebDriver


def format_time(str_time: str):
    if len(str_time) == 19:
        return datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
    elif len(str_time) == 16:
        return datetime.strptime(str_time, '%Y-%m-%d %H:%M')


class SingleMail(object):
    def __init__(self, driver: WebDriver, attachment_flag: bool = False):
        self._mail_driver = driver
        self._mail_driver.implicitly_wait(3)
        self._close_button = self._mail_driver.find_element_by_css_selector(
            'html > body > form > div:nth-of-type(3) > div > a:nth-of-type(1)')
        self._attachment_flag = attachment_flag
        if attachment_flag:
            self._download_button = self._mail_driver.find_element_by_css_selector('a#dfAll')
        self._from = self._mail_driver.find_element_by_css_selector(
            'html > body > form > div.row-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > '
            'font:nth-child(1)').text
        self._subject = self._mail_driver.find_element_by_css_selector(
            'body > form > div.row-container > table > tbody > tr:nth-child(3) > td:nth-child(2) > b')
        self._mail = self._mail_driver.find_element_by_css_selector('div.row-container')
        self._time = format_time(self._mail_driver.find_element_by_css_selector(
            'html > body > form > div.row-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > '
            'font:nth-child(4)').text)

    def close(self) -> bool:
        self._close_button.click()
        return True

    def download_all(self):
        hwnd_now = win32gui.GetForegroundWindow()
        print('%x' % hwnd_now)
        hwnd_mail = win32gui.FindWindow(0, "邮件系统-内网邮件 - Internet Explorer")
        print('%x' % hwnd_mail)
        shell = win32con.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.ShowWindow(hwnd_mail, win32con.SW_SHOWNA)
        win32gui.SetForegroundWindow(hwnd_mail)
        sleep(0.1)
        self._download_button.click()
        sleep(0.1)
        win32api.keybd_event(0x0D, 0, 0, 0)
        win32api.keybd_event(0x0D, win32con.KEYEVENTF_KEYUP, 0)
        win32gui.ShowWindow(hwnd_now, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd_now)

    @property
    def mail_from(self) -> str:
        return self._from

    @property
    def subject(self) -> str:
        return self._subject.text

    @property
    def mail(self) -> str:
        return self._mail.get_attribute('innerHTML')

    @property
    def mail_time(self) -> datetime:
        return format_time(self._time.text)

    @property
    def attachment_flag(self) -> bool:
        return self._attachment_flag
