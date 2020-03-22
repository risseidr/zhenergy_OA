#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MailInfo.py
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-7 12:01   risseidr   1.0         None
"""

from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
from time import sleep

from MailTag import MailTag


def format_time(str_time: str):
    return datetime.strptime(str_time, '%Y/%m/%d %H:%M')


class MailInfo(object):
    def __init__(self, td: [WebElement]):
        self._td = td
        self._checkbox = ''
        self._from = ''
        self._subject = ''
        self._read_flag = False
        self._attachment_flag = False
        self._time = datetime.now()

    def open(self):
        self._td[4].find_element_by_xpath('.//a').click()
        sleep(0.2)

        return MailTag(self._td[0].parent)

    def choose(self):
        self._checkbox = self._td[0].find_element_by_xpath('.//input')
        while not (self._checkbox.is_selected()):
            self._checkbox.click()
            sleep(0.1)

    @property
    def read_flag(self):
        if self._td[1].get_attribute('title') == 'Attachment.gif':
            self._attachment_flag = True
        return self._read_flag

    @property
    def mail_from(self) -> str:
        self._from = self._td[2].get_attribute('title')
        return self._from

    @property
    def subject(self) -> str:
        self._subject = self._td[4].get_attribute('title')
        return self._subject

    @property
    def time(self):
        self._time = format_time(self._td[5].get_attribute('title'))
        return self._time

    @property
    def attachment_flag(self):
        if self._td[6].get_attribute('title') == 'Attachment.gif':
            self._attachment_flag = True
        return self._attachment_flag
