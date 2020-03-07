#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   OaMail.py    
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-7 12:01   risseidr   1.0         None
"""

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime


class OaMail(object):
    def __init__(self):
        self._mail_from = ''
        self._to = ['']
        self._cc = ['']
        self._bcc = ['']
        self._subject = ''
        self._body = ''
        self._attachment = ''
        self._read_flag = False
        self._time = datetime.now()
        self._size = 0
        pass

    @property
    def mail_from(self):
        return self._mail_from

    @mail_from.setter
    def mail_from(self, element: WebElement):
        """

        :param element:must be /td with 'title'
        :return:
        """
        self._mail_from = element.get_attribute('title')
        return True

    @property
    def to(self):
        return self._to

    @property
    def cc(self):
        return self._cc

    @property
    def bcc(self):
        return self._bcc

    @property
    def subject(self):
        return self._subject

    @property
    def body(self):
        return self._body

    @property
    def attachment(self):
        return self._attachment

    @property
    def read_flag(self):
        return self._read_flag

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, element: WebElement):

    def get_brief_info(self, element: WebElement):
        """

        :param element: must be element selected by 'tbody#intrabox_tBody > tr'
        :return:
        """
        brief_info = element.find_elements_by_xpath('.//td')
        brief_info[0].get_attribute('title')
        self.body = 0
        return True

    pass


