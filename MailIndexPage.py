#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MailIndexPage.py
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-17 12:53   risseidr   1.0         None
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class MailIndexPage(object):
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.implicitly_wait(3)
        self._inbox = None
        self._send_box = None
        self._draft_box = None
        self._trash_box = None
        self._favorites_box = None

    @property
    def inbox(self) -> WebElement:
        """
        click and then return element_div of inbox

        :return:element_div of inbox
        """
        self._driver.find_element_by_css_selector('#nav-list > li:nth-child(1)').click()
        self._inbox = self._driver.find_element_by_id('#intraboxBody')
        return self._inbox

    @property
    def draft_box(self) -> WebElement:
        """
        click and then return element_div of draft_box

        :return:element_div of draft_box
        """
        self._driver.find_element_by_css_selector('#nav-list > li:nth-child(1)').click()
        self._draft_box = self._driver.find_element_by_id('#draftBody')
        return self._draft_box

    @property
    def send_box(self) -> WebElement:
        """
        click and then return element_div of send_box

        :return:element_div of send_box
        """
        self._driver.find_element_by_css_selector('#nav-list > li:nth-child(3)').click()
        self._send_box = self._driver.find_element_by_id('#sentBody')
        return self._send_box

    @property
    def trash_box(self) -> WebElement:
        """
        click and then return element_div of trash_box

        :return:element_div of trash_box
        """
        self._driver.find_element_by_css_selector('#nav-list > li:nth-child(4)').click()
        self._trash_box = self._driver.find_element_by_id('#trashBody')
        return self._trash_box

    @property
    def favorites_box(self) -> WebElement:
        """
        click and then return element_div of favorites_box

        :return:element_div of favorites_box
        """
        pass
        return self._favorites_box

    def close_sent_box(self):
        self._driver.find_element_by_css_selector('#sentHead > i').click()

    def close_draft_box(self):
        self._driver.find_element_by_css_selector('#draftHead > i').click()

    def close_trash_box(self):
        self._driver.find_element_by_css_selector('#trashHead > i').click()

    def close_favorites_box(self):
        pass
