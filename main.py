#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import datetime
from Login import LoginWeb

ie = LoginWeb()
mailbox = ie.login(14411, 'zhubinyuan', '12345678')
print(datetime.now())

try:
    while True:
        j = 0
        while j < 50:
            for i in range(j, 50):
                inbox = mailbox.get_briefinfo(i)
                j += 1
                if '收到： ' in inbox.subject:
                    inbox.choose()
                    j -= 1
            if j < 50:
                mailbox.delete_choosed()
                mailbox.refresh_tr()
        if mailbox.next_page():
            pass
        else:
            break
except IndexError:
    if IndexError.args[0] == 'list index out of range':
        pass

print(datetime.now())
# inbox = BriefMailPageElements(driver)
# for tr in inbox.brief_tr():
#     mail_info = BriefInfo(tr)
#     if mail_info.subject().find('收到： ') == 0:
#         mail_info.set_del_tag()
