#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MailTag.py
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-14 19:46   risseidr   1.0         None

"""
import os
import urllib
from datetime import datetime
from time import sleep
from urllib import parse

from selenium.webdriver.ie.webdriver import WebDriver

from MailFolder import MailFolder


def format_time(str_time: str):
    return datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')


class MailTag(object):
    def __init__(self, driver: WebDriver, subject):
        self._mail_driver = driver
        self._mail_driver.switch_to.window(driver.window_handles[-1])
        self._from = None
        self._subject = None
        self._mail = None
        self._time = None
        self._attachment_links = []
        self._attachment_names = []
        self._attachment_size = ''
        self._get_attachments()

    def close(self):
        self._mail_driver.close()

    def download_all(self):
        mail_folder = MailFolder(self)
        mail_folder.create_mail_folder()
        mail_folder.transfer_mail_to_html()
        for link in self.attachment_links:
            self.download_attachment(link)
        sleep(5)
        mail_folder.move_attachments_to_mail_folder()

    @property
    def mail_from(self) -> str:
        self._from = self._mail_driver.find_element_by_css_selector(
            'html > body > form > div.row-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > '
            'font:nth-child(1)').text
        return self._from

    @property
    def subject(self) -> str:
        self._subject = self._mail_driver.find_element_by_css_selector(
            'body > form > div.row-container > table > tbody > tr:nth-child(3) > td:nth-child(2) > b').text
        return self._subject

    @property
    def mail(self) -> str:
        self._mail = self._mail_driver.find_element_by_css_selector(
            'html > body > form > div.row-container').get_attribute('innerHTML')
        self.mail_local()
        return self._mail

    @property
    def mail_time(self) -> datetime:
        self._time = format_time(self._mail_driver.find_element_by_css_selector(
            'html > body > form > div.row-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > '
            'font:nth-child(4)').text)
        return self._time

    def _get_attachments(self):
        links = self._mail_driver.find_elements_by_css_selector('div#divLinks > a')
        for a in links:
            path = urllib.parse.unquote(os.path.join(a.get_attribute('href')))
            self._attachment_names.append(path[path.rfind(r'/') + 1:])
            self._attachment_links.append(path)

    @property
    def attachment_links(self):
        return self._attachment_links

    @property
    def attachment_names(self):
        return self._attachment_names

    @property
    def attachment_size(self):
        return self._attachment_size

    def mail_local(self):
        for name in self._attachment_names:
            self._mail = self._mail.replace(r"javascript:getFile('" + name + "')", '.\\' + name)

    def download_attachment(self, link):
        self._mail_driver.get(link)
