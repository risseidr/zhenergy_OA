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
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BriefMailPageElements(object):
    def __init__(self, driver: WebDriver):
        self._next_page_button = driver.find_element_by_css_selector('tbody#intraboxContent > div.panel-footer > nav '
                                                                     '> div.pageNav > span.nextPage')
        self._pre_page_button = driver.find_element_by_css_selector('tbody#intraboxContent > div.panel-footer > nav '
                                                                    '> div.pageNav > span.prePage')
        self._brief_tr = driver.find_elements_by_css_selector('tbody#intrabox_tBody > tr')

    def next_page(self):
        if str(self._next_page_button.get_attribute('class')).find('page_ok'):
            self._next_page_button.click()
            return True
        else:
            return False

    def pre_page(self):
        if str(self._pre_page_button.get_attribute('class')).find('page_ok'):
            self._pre_page_button.click()
            return True
        else:
            return False

    @property
    def brief_tr(self):
        return self._brief_tr


class SingleMailPageElements(object):
    def __init__(self, driver: WebDriver, attachment_flag: bool):
        self._close_button = driver.find_element_by_css_selector('html > body > form > div:nth-of-type(3) > div > '
                                                                 'a:nth-of-type(1)')
        if attachment_flag:
            self._download_button = driver.find_element_by_css_selector('a#dfAll')
            # driver.find_element_by_css_selector('html > body > form > div:nth-of-type(5) > table > tbody >
            # tr:nth-of-type(4) > td:nth-of-type(2) > div:nth-of-type(2) > a:nth-of-type(2)')

        self._from = driver.find_element_by_css_selector('html > body > form > div.row-container > table > tbody > '
                                                         'tr:nth-child(1) > td:nth-child(2) > font:nth-child(1)')
        self._to = driver.find_element_by_css_selector('div#SendTodiv')
        self._subject = driver.find_element_by_css_selector('body > form > div.row-container > table > tbody > '
                                                            'tr:nth-child(3) > td:nth-child(2) > b')
        # get_attribute('innerHTML')