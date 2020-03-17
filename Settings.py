#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Settings.py    
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-17 12:42   risseidr   1.0         None
"""


class Settings(object):
    def __init__(self):
        self._mailbox_num = 'U14411'
        self._username = 'zhubinyuan'
        self._password = '12345678'
        self._save_root_path_ = r'%temp%'
        self._save_type = 0

    @property
    def mailbox_num(self):
        return self._mailbox_num

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def save_root_path(self):
        return self._save_root_path_

    @property
    def save_type(self):
        return self._save_type
