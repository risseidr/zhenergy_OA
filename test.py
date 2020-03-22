from datetime import datetime
from time import sleep

import requests
from requests.cookies import RequestsCookieJar

from MailIndexPage import MailIndexPage
from Settings import settings
from content_main.MailBox import MailBox
from login import login
from startchrome import StartChrome


def test():
    driver = StartChrome().start_chrome()
    print(driver.title)
    driver.set_window_size(1366, 768)

    cookies = driver.get_cookies()
    cookie_jar = RequestsCookieJar()
    cookie_jar.set(cookies[0]['name'], cookies[0]['value'], domain=cookies[0]['domain'])
    r = requests.get(url=url, cookies=cookie_jar)
    if r.status_code == requests.codes.ok:
        data = r.content
        with open("bd_logo1.png", "wb") as f:
            f.write(data)


if __name__ == '__main__':
    test()
