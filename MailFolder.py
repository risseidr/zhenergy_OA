#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MailFolder
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-12-16:42   risseidr   1.0         None
"""

import os, shutil
from time import sleep

from Settings import settings


class MailFolder(object):
    def __init__(self, mail):
        self._mail_from = mail.mail_from
        self._time = mail.mail_time
        self._subject = mail.subject
        self._mail = mail.mail
        self._attachment_names = mail.attachment_names
        self._mail_path = None

    def subject_to_folder_name(self):
        return self._subject.replace(':', '：').replace('?', '？').replace('"', "'")

    def create_mail_folder(self):
        mail_path = os.path.join(settings.save_root_path, self._mail_from,
                                 self._time.strftime('%Y%m%d %H%M%S') + ' ' + self.subject_to_folder_name())
        if not os.path.isdir(mail_path):
            os.makedirs(mail_path)
        self._mail_path = mail_path

    def move_attachments_to_mail_folder(self):
        if self._attachment_names:
            for f in self._attachment_names:
                while True:
                    if f in os.listdir(settings.temp_download_path):
                        file_path = os.path.join(settings.temp_download_path, f)
                        shutil.move(file_path, self._mail_path)
                        break
                    sleep(0.05)

    def transfer_mail_to_html(self):
        html = os.path.join(self._mail_path, '邮件.html')
        try:
            with open(html, 'x') as file:
                file.write(self._mail)
            file.close()
        except FileExistsError as e:
            print(e)
