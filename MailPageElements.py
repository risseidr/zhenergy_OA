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
import win32api
import win32con
import win32gui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from time import sleep

from SingleMail import SingleMail


def format_time(str_time: str):
    if len(str_time) == 19:
        return datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
    elif len(str_time) == 16:
        return datetime.strptime(str_time, '%Y-%m-%d %H:%M')


class MailBox(object):
    def __init__(self, driver: WebDriver):
        """

        :param driver: 浏览器驱动
        """
        self._driver = driver
        self._driver.implicitly_wait(5)
        self._next_page_button = None
        self._pre_page_button = None
        self._mailbox_tr = None

    def next_page(self) -> bool:
        """判断“下一页”能否点击，并点击

        :return:
        """
        self._next_page_button = self._driver.find_element_by_css_selector(
            'div#intraboxContent > div.panel-footer > nav > div.pageNav > span.nextPage')
        if 'page_ok' in str(self._next_page_button.get_attribute('class')):
            self._next_page_button.click()
            sleep(0.5)
            self.mailbox_tr()
            return True
        else:
            return False

    def pre_page(self) -> bool:
        """判断“上一页”能否点击，并点击

        :return:
        """
        self._pre_page_button = self._driver.find_element_by_css_selector(
            'div#intraboxContent > div.panel-footer > nav > div.pageNav > span.prePage')
        if 'page_ok' in str(self._pre_page_button.get_attribute('class')):
            self._pre_page_button.click()
            sleep(0.5)
            self.mailbox_tr()
            return True
        else:
            return False

    def __getitem__(self, item):
        """返回索引BriefInfo

        :param item:
        :return:
        """
        self.mailbox_tr()
        return BriefInfo(self._mailbox_tr[item].find_elements_by_xpath('.//td'))

    def mailbox_tr(self):
        """找到收件箱中的信息元素列表

        :return:
        """
        self._mailbox_tr = self._driver.find_elements_by_css_selector('tbody#intrabox_tBody > tr')


class BriefInfo(object):
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
        sleep(0.5)
        try:
            mail_frame = self._td[0].parent.find_element_by_css_selector(
                'div.J_iframe[style="display: block;"] > div > div > iframe')
        except NoSuchElementException as e:
            self._td[4].find_element_by_xpath('.//a').click()
            sleep(0.5)
            mail_frame = self._td[0].parent.find_element_by_css_selector(
                'div.J_iframe[style="display: block;"] > div > div > iframe')
            print(e)
            print('to slow')
        self._td[0].parent.switch_to.frame(mail_frame)
        return SingleMail(self._td[0].parent, self._attachment_flag)

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
        self._from = self._td[2].text
        return self._from

    @property
    def subject(self) -> str:
        self._subject = self._td[4].text
        return self._subject

    @property
    def time(self):
        self._time = format_time(self._td[5].text)
        return self._time

    @property
    def attachment_flag(self):
        if self._td[6].get_attribute('title') == 'Attachment.gif':
            self._attachment_flag = True
        return self._attachment_flag
