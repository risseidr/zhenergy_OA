#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   OaMail.py
@Contact :   riseidr@hotmail.com
@License :   (C)Copyright 2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-3-7 12:01   risseidr   1.0         None
"""

import win32api
import win32gui
import win32con


def click_ENTER():
    hwnd_now = win32gui.GetForegroundWindow()
    print('%x' % hwnd_now)
    hwnd_mail = win32gui.FindWindow(0, "邮件系统-内网邮件 - Internet Explorer")
    print('%x' % hwnd_mail)
    hwnd_download = win32gui.FindWindow(0, "浏览文件夹")
    print('%x' % hwnd_download)
    win32gui.ShowWindow(hwnd_mail, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd_download)
    win32api.keybd_event(0x0D, 0, 0, 0)
    win32api.keybd_event(0x0D, win32con.KEYEVENTF_KEYUP, 0)
    win32gui.ShowWindow(hwnd_now, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd_now)
    return True
