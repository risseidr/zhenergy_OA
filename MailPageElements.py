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

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
from time import sleep
from win32api import SendMessage
from win32gui import FindWindow, FindWindowEx
from win32con import WM_KEYUP, WM_KEYDOWN, VK_RETURN


def format_time(str_time: str):
    if len(str_time) == 19:
        return datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
    elif len(str_time) == 16:
        return datetime.strptime(str_time, '%Y-%m-%d %H:%M')


class BriefMailPageElements(object):
    def __init__(self, driver: WebDriver):
        driver.implicitly_wait(10)
        self._next_page_button = driver.find_element_by_css_selector(
            'div#intraboxContent > div.panel-footer > nav > div.pageNav > span.nextPage')
        self._pre_page_button = driver.find_element_by_css_selector(
            'div#intraboxContent > div.panel-footer > nav > div.pageNav > span.prePage')
        self._brief_tr = driver.find_elements_by_css_selector('tbody#intrabox_tBody > tr')

    def next_page(self):
        if 'page_ok' in str(self._next_page_button.get_attribute('class')):
            self._next_page_button.click()
            sleep(0.5)
            return True
        else:
            return False

    def pre_page(self):
        if 'page_ok' in str(self._pre_page_button.get_attribute('class')):
            self._pre_page_button.click()
            sleep(0.5)
            return True
        else:
            return False

    def brief_tr(self):
        return self._brief_tr


class BriefInfo(object):
    def __init__(self, tr: WebElement):
        """
        must sent tr

        :param tr:
        """
        self._td_ = tr.find_elements_by_xpath('.//td')
        if 'read_flag' in tr.get_attribute('class'):
            self._read_flag = False
        else:
            self._read_flag = True
        self._checkbox = ''
        self._from = ''
        self._subject = ''
        if self._td_[6].get_attribute('title') == 'Attachment.gif':
            self._attachment_flag = True
        else:
            self._attachment_flag = False
        self._time = datetime.now()

    def open(self):
        sleep(0.1)
        self._td_[4].click()
        sleep(0.5)

    def choose(self):
        self._checkbox = self._td_[0].find_element_by_xpath('.//input')
        if not (self._checkbox.is_selected()):
            sleep(0.1)
            self._checkbox.click()
            sleep(0.1)

    @property
    def read_flag(self):
        return self._read_flag

    @property
    def mail_from(self) -> str:
        self._from = self._td_[2].text
        return self._from

    @property
    def subject(self) -> str:
        self._subject = self._td_[4].text
        return self._subject

    @property
    def time(self):
        self._time = format_time(self._td_[5].text)
        return self._time

    @property
    def attachment_flag(self):
        return self._attachment_flag


class SingleMailPageElements(object):
    def __init__(self, driver: WebDriver, attachment_flag: bool = True):
        self._mail_driver = driver
        self._mail_driver.implicitly_wait(3)
        mail_frame = self._mail_driver.find_element_by_css_selector(
            'div.J_iframe[style="display: block;"] > div > div > iframe')
        self._mail_driver.switch_to.frame(mail_frame)
        self._mail_driver.switch_to.active_element
        self._close_button = self._mail_driver.find_element_by_css_selector(
            'html > body > form > div:nth-of-type(3) > div > a:nth-of-type(1)')
        if attachment_flag:
            self._download_button = self._mail_driver.find_element_by_css_selector('a#dfAll')
        self._from = self._mail_driver.find_element_by_css_selector(
            'html > body > form > div.row-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > '
            'font:nth-child(1)').text
        self._subject = self._mail_driver.find_element_by_css_selector(
            'body > form > div.row-container > table > tbody > tr:nth-child(3) > td:nth-child(2) > b').text
        self._mail = self._mail_driver.find_element_by_css_selector('div.row-container').get_attribute('innerHTML')
        self._time = format_time(self._mail_driver.find_element_by_css_selector(
            'html > body > form > div.row-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > '
            'font:nth-child(4)').text)

    def close(self) -> bool:
        self._close_button.click()
        return True

    def download_all(self):
        sleep(0.2)
        self._download_button.click()
        sleep(0.2)
        hwnd = FindWindow(0, "确定")
        SendMessage(hwnd, WM_KEYDOWN, VK_RETURN, 0)
        SendMessage(hwnd, WM_KEYUP, VK_RETURN, 0)
        sleep(0.2)



    def mail_from(self):
        return self._from

    def subject(self):
        return self._subject

    def mail(self):
        return self._mail

    def mail_time(self):
        return self._time

    def save(self, path: str, save_type='mail_from_first') -> bool:
        """save mail to computer

        :param path:
        :param save_type: 'mail_from_first' or 'time_first'
        :return:
        """
        if save_type == 'mail_from_first':
            return True
        elif save_type == 'time_first':
            return True
        else:
            return False