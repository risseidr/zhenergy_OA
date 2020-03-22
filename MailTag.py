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

import requests
from requests.cookies import RequestsCookieJar
from selenium.webdriver.ie.webdriver import WebDriver

from Settings import settings


def format_time(str_time: str):
    return datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')


class MailTag(object):
    def __init__(self, driver: WebDriver):
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
        self._mail_path = None

    @property
    def mail_from(self) -> str:
        self._from = self._mail_driver.find_element_by_css_selector(
            'html > body > form > div.row-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > '
            'font:nth-child(1)').text
        return self._from

    @property
    def subject(self) -> str:
        self._subject = self._mail_driver.find_element_by_css_selector(
            'body > form > div.row-container > table > tbody > tr:nth-last-child(2) > td:nth-child(2) > b').text
        return self._subject

    @property
    def mail(self) -> str:
        self._mail = self._mail_driver.find_element_by_css_selector(
            'html > body > form > div.row-container').get_attribute('innerHTML')
        for name in self._attachment_names:
            self._mail = self._mail.replace(r"javascript:getFile('" + name + "')", '.\\' + name)
        return self._mail

    @property
    def mail_time(self) -> datetime:
        self._time = format_time(self._mail_driver.find_element_by_css_selector(
            'html > body > form > div.row-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > '
            'font:nth-child(4)').text)
        return self._time

    @property
    def attachment_size(self):
        return self._attachment_size

    def _get_attachments(self):
        self._mail_driver.implicitly_wait(0.2)
        links = self._mail_driver.find_elements_by_css_selector('div#divLinks > a')
        self._mail_driver.implicitly_wait(3)
        for a in links:
            path = urllib.parse.unquote(os.path.join(a.get_attribute('href')))
            self._attachment_names.append(path[path.rfind(r'/') + 1:])
            self._attachment_links.append(path)

    def _download_attachments(self):
        cookies = self._mail_driver.get_cookies()
        cookie_jar = RequestsCookieJar()
        cookie_jar.set(cookies[0]['name'], cookies[0]['value'], domain=cookies[0]['domain'])
        for (url, filename) in zip(self._attachment_links, self._attachment_names):
            r = requests.get(url=url, cookies=cookie_jar)
            if r.status_code == requests.codes.ok:
                data = r.content
                file_path = os.path.join(self._mail_path, filename)
                with open(file_path, "xb") as f:
                    f.write(data)

    def _subject_to_folder_name(self):
        return self.subject.replace(':', '：').replace('?', '？').replace('"', "'").replace('\\', '-').replace('/', '-')

    def _create_mail_folder(self):
        mail_path = os.path.join(settings.save_root_path, self.mail_from,
                                 self.mail_time.strftime('%Y%m%d %H%M%S') + ' ' + self._subject_to_folder_name())
        mail_path = os.path.abspath(mail_path)
        if not os.path.isdir(mail_path):
            os.makedirs(mail_path)
        self._mail_path = mail_path

    def _transfer_mail_to_html(self):
        html = os.path.join(self._mail_path, '邮件.html')
        try:
            with open(html, 'x', encoding='utf-8') as file:
                file.write(self.mail)
            file.close()
        except FileExistsError as e:
            print(e)

    def close(self):
        self._mail_driver.close()
        self._mail_driver.switch_to.window(self._mail_driver.window_handles[0])

    def download_all(self):
        self._create_mail_folder()
        self._transfer_mail_to_html()
        self._download_attachments()
