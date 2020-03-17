#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Mail_Box.py
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-17 14:28   risseidr   1.0         None
"""
from time import sleep

from selenium.webdriver.remote.webelement import WebElement

from MailPageElements import MailInfo


class MailBox(WebElement):
    def __init__(self, div: WebElement):
        """
        override

        :param div:
        """
        self._sort_btn = None
        self._sort_flag = 0
        self._next_page_button = None
        self._pre_page_button = None
        self._tr = [WebElement]
        super().__init__(div.parent, div.id_, div.w3c)

    def delete(self):
        self.find_element_by_xpath('.//div/div[1]/div/div[1]/div[button="删除"]/button').click()
        self.click_btn_ok()

    def delete_completely(self):
        self.find_element_by_xpath('.//div/div[1]/div/div[1]/div[button="彻底删除"]/button').click()
        self.click_btn_ok()

    def restore(self):
        self.find_element_by_xpath('.//div/div[1]/div/div[1]/div[button="还原"]/button').click()
        self.click_btn_ok()

    def click_btn_ok(self):
        sleep(0.1)
        self.find_element_by_xpath('*//div[a="确定"]/a[1]').click()
        sleep(1)
        self._fresh_tr()

    def sort_by_time(self, flag: str):
        self._sort_btn = self.find_element_by_xpath(
            './/a/img[@src="/static_new/image/sortDesc.gif" or @src="/static_new/image/sortAsc.gif"]')
        if self._sort_btn.get_attribute('src') == '/static_new/image/sortAsc.gif':
            self._sort_flag = 1
        if self._sort_flag != flag:
            self._sort_btn.click()
            sleep(1)
            self._fresh_tr()

    def next_page(self) -> bool:
        """判断“下一页”能否点击，并点击

        :return:
        """
        self._next_page_button = self.find_element_by_css_selector(
            'div#intraboxContent > div.panel-footer > nav > div.pageNav > span.nextPage')
        if 'page_ok' in str(self._next_page_button.get_attribute('class')):
            self._next_page_button.click()
            sleep(0.5)
            self._fresh_tr()
            return True
        else:
            return False

    def pre_page(self) -> bool:
        """判断“上一页”能否点击，并点击

        :return:
        """
        self._pre_page_button = self.find_element_by_css_selector(
            'div#intraboxContent > div.panel-footer > nav > div.pageNav > span.prePage')
        if 'page_ok' in str(self._pre_page_button.get_attribute('class')):
            self._pre_page_button.click()
            sleep(2)
            self._fresh_tr()
            return True
        else:
            return False

    def _fresh_tr(self):
        self._tr = self.find_elements_by_xpath('.//table/tbody/tr')

    @property
    def tr(self):
        return self._tr

    def get_mail_info(self, item) -> MailInfo:
        return MailInfo(self.tr[item].find_elements_by_xpath('.//td'))
