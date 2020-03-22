#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
from datetime import datetime
from time import sleep

from login import login
from MailIndexPage import MailIndexPage
from Settings import Settings, settings
from content_main.MailBox import MailBox
from startchrome import StartChrome


def main():
    driver = StartChrome().start_chrome()
    print(driver.title)
    driver.set_window_size(1366, 768)
    index_page = MailIndexPage(login(driver, settings)).inbox
    mailbox = MailBox(index_page)

    print(datetime.now())

    # mailbox.delete_mail()
    mailbox.sort_by_time(1)
    mailbox.download_mail()
    sleep(5)

    print(datetime.now())


if __name__ == '__main__':
    main()
