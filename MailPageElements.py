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
import time


def format_time(str_time: str):
    if 'AM' in str_time or 'PM' in str_time:
        return datetime.strptime(str_time, '%m/%d/%Y %I:%M:%S %p')
    else:
        return datetime.strptime(str_time, '%Y/%m/%d %H:%M')


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
            return True
        else:
            return False

    def pre_page(self):
        if 'page_ok' in str(self._pre_page_button.get_attribute('class')):
            self._pre_page_button.click()
            return True
        else:
            return False

    def brief_tr(self):
        return self._brief_tr


class BriefInfo(object):
    def __init__(self, tr: WebElement):
        # if tr.find_element_by_xpath('.//td[2]').get_attribute('title') == 'Mail.gif':
        #     self._read_flag = True
        # else:
        #     self._read_flag = False
        self._checkbox = tr.find_element_by_xpath('.//td[1]/input')
        # self._from = tr.find_element_by_xpath('.//td[3]').get_attribute('title')
        self._subject = tr.find_element_by_xpath('.//td[5]').get_attribute('title')
        # self._time = format_time(tr.find_element_by_xpath('.//td[6]').get_attribute('title'))
        # if tr.find_element_by_xpath('.//td[7]').get_attribute('title') == 'Attachment.gif':
        #     self._attachment_flag = True
        # else:
        #     self._attachment_flag = False

    def open(self):
        self._subject.click()

    def set_del_tag(self):
        if not (self._checkbox.is_selected()):
            self._checkbox.click()

    def read_flag(self):
        return self._read_flag

    def mail_from(self) -> str:
        return self._from

    def subject(self) -> str:
        return self._subject

    def time(self):
        return self._time

    def attachment_flag(self):
        return self._attachment_flag


class SingleMailPageElements(object):
    def __init__(self, driver: WebDriver, attachment_flag: bool):
        driver.implicitly_wait(10)
        self._close_button = driver.find_element_by_css_selector(
            'html > body > form > div:nth-of-type(3) > div > a:nth-of-type(1)')
        if attachment_flag:
            self._download_button = driver.find_element_by_css_selector('a#dfAll')

        self._from = driver.find_element_by_css_selector(
            'html > body > form > div.row-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > '
            'font:nth-child(1)').text
        self._subject = driver.find_element_by_css_selector(
            'body > form > div.row-container > table > tbody > tr:nth-child(4) > td:nth-child(2) > b').text
        self._mail = driver.find_element_by_css_selector('div.row-container').get_attribute('innerHTML')
        self._time = format_time(driver.find_element_by_css_selector(
            'html > body > form > div.row-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > '
            'font:nth-child(4)').text)

    def close(self) -> bool:
        self._close_button.click()
        return True

    def download_all(self):
        self._download_button.click()
        time.sleep(0.5)
        self._download_button.send_keys(Keys.ENTER)

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
