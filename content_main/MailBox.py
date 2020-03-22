#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MailBox.py
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-17 14:28   risseidr   1.0         None
"""
from time import sleep

from selenium.webdriver.remote.webelement import WebElement

from MailInfo import MailInfo
from MailTag import MailTag


class MailBox(object):
    def __init__(self, div: WebElement):
        """
        override

        :param div:
        """
        self._div = div
        self._sort_btn = None
        self._sort_flag = 0
        self._next_page_button = None
        self._pre_page_button = None
        self._tr = None
        self._fresh_tr()

    def delete(self):
        self._div.find_element_by_xpath('.//div/div[1]/div/div[1]/div[button="删除"]/button').click()
        self.click_btn_ok()

    def delete_completely(self):
        self._div.find_element_by_xpath('.//div/div[1]/div/div[1]/div[button="彻底删除"]/button').click()
        self.click_btn_ok()

    def restore(self):
        self._div.find_element_by_xpath('.//div/div[1]/div/div[1]/div[button="还原"]/button').click()
        self.click_btn_ok()

    def click_btn_ok(self):
        sleep(0.5)
        self._div.parent.find_element_by_xpath('*//div[a="确定"]/a[1]').click()
        self._fresh_tr()

    def sort_by_time(self, flag: int):
        """

        :param flag: 0:时间倒序 or 1时间顺序
        :return:
        """
        self._sort_btn = self._div.find_element_by_xpath(
            './/a/img[@src="/static_new/image/sortDesc.gif" or @src="/static_new/image/sortAsc.gif"]')
        if self._sort_btn.get_attribute('src') == '/static_new/image/sortAsc.gif':
            self._sort_flag = 1
        if self._sort_flag != flag:
            self._sort_btn.click()
            self._fresh_tr()

    def next_page(self) -> bool:
        """判断“下一页”能否点击，并点击

        :return:
        """
        self._next_page_button = self._div.find_element_by_css_selector(
            'div#intraboxContent > div.panel-footer > nav > div.pageNav > span.nextPage')
        if 'page_ok' in str(self._next_page_button.get_attribute('class')):
            self._next_page_button.click()
            self._fresh_tr()
            return True
        else:
            return False

    def pre_page(self) -> bool:
        """判断“上一页”能否点击，并点击

        :return:
        """
        self._pre_page_button = self._div.find_element_by_css_selector(
            'div#intraboxContent > div.panel-footer > nav > div.pageNav > span.prePage')
        if 'page_ok' in str(self._pre_page_button.get_attribute('class')):
            self._pre_page_button.click()
            self._fresh_tr()
            return True
        else:
            return False

    def _fresh_tr(self):
        sleep(2)
        self._tr = self._div.find_elements_by_xpath('.//table/tbody/tr')
        sleep(0.2)

    def get_mail_info(self, item) -> MailInfo:
        return MailInfo(self._tr[item].find_elements_by_xpath('.//td'))

    def delete_mail(self):
        try:
            while True:
                j = 0
                while j < len(self._tr):
                    for i in range(j, len(self._tr)):
                        td = self.get_mail_info(i)
                        j += 1
                        if '收到： ' in td.subject:
                            td.choose()
                            j -= 1
                    if j < len(self._tr):
                        self.delete()
                if self.next_page():
                    pass
                else:
                    break
        except IndexError as e:
            print(e)

    def download_mail(self):
        try:
            while True:
                for i in range(0, len(self._tr)):
                    td = self.get_mail_info(i)
                    td.open()
                    mailtag = MailTag(self._div.parent)
                    mailtag.download_all()
                    sleep(0.5)
                    mailtag.close()
                if self.next_page():
                    pass
                else:
                    break
        except IndexError as e:
            print(e)
