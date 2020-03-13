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

import os, shutil, io
from MailPageElements import SingleMailPageElements

DOWNLOAD_DIR = r'C:\Users\zhubinyuan.ZHENERGY'
ROOT_DIR = r'E:\98 邮件附件'


class MailFolder(object):
    _download_dir = DOWNLOAD_DIR
    _root_dir = ROOT_DIR

    def __init__(self, mail: SingleMailPageElements):
        self._mail_from = mail.mail_from
        self._time = mail.mail_time
        self._subject = mail.subject
        self._mail = mail.mail
        self._attachment_flag = mail.attachment_flag
        self._attachments_name = mail._attachments_name
        self._mail_path = None

    def subject_to_folder_name(self):
        return self._subject.replace(':', '：').replace('?', '？').replace('"', "'")

    def create_mail_folder(self):
        mail_path = os.path.join(self._root_dir, self._mail_from,
                                 self._time.strftime('%y-%m-%d %H：%M：%S') + ' ' + self._subject)
        if not os.path.isdir(mail_path):
            os.mkdir(mail_path)
            self._mail_path = mail_path

    def move_attachments_to_mail_folder(self):
        if self._attachment_flag:
            for f in self._attachments_name:
                file_path = os.path.join(self._download_dir, f)
                shutil.move(file_path, self._mail_path)

    def transfer_mail_to_html(self):
        html = os.path.join(self._mail_path, '邮件.html')
        with open('html', 'x') as file:
            file.writable(self._mail)
        file.close()
