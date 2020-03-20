#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
from datetime import datetime
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from login import login
from MailIndexPage import MailIndexPage
from Settings import Settings
from content_main.MailBox import MailBox

settings = Settings()
options = Options()


def connect_chrome() -> WebDriver:
    def bind_driver() -> WebDriver:
        options.add_experimental_option("debuggerAddress", "127.0.0.1:" + str(settings.remote_debugging_port_id))
        chrome_driver = settings.chromedriver_dir
        return WebDriver(chrome_driver, options=options)

    def start_chrome():
        os.popen(settings.chrome_dir + settings.start_argument)

    with os.popen('netstat -ano|findstr "LISTENING"|findstr "9222"') as f1:
        info1 = f1.read()
        if info1:
            pid = re.split('\\s+', re.split('\\n+', info1)[0])[-1]
            with os.popen('tasklist|findstr "' + pid + '"') as f2:
                info2 = f2.read()
            process = re.split('\\s+', info2)[0]
            if process == 'chrome.exe':
                return bind_driver()
            else:
                raise Exception('remote debugging pid' + ' is occupied')
        else:
            start_chrome()
            return bind_driver()


def main():
    driver = connect_chrome()
    print(driver.title)
    driver.maximize_window()
    index_page = MailIndexPage(login(driver, settings)).inbox
    mailbox = MailBox(index_page)

    print(datetime.now())

    # mailbox.delete_mail()
    mailtag = mailbox.get_mail_info(15).open()
    print(mailtag.mail)
    print(mailtag.attribute_links)
    print(mailtag.attribute_names)

    print(datetime.now())


if __name__ == '__main__':
    main()
