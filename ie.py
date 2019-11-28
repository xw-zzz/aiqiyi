# -*- coding: utf-8 -*-#
# Name:         fire_fox
# Description:  
# Author:       10264
# Date:         2019/11/18
import time
import file

import configparser
import os
import webbrowser

sleep_time_second = 0
window_number = 0
show_window = 1

from json import load


def init():
    # cf = configparser.ConfigParser()
    # cf.read("config.conf", encoding='ascii')
    global sleep_time_second
    global window_number
    global show_window
    global click_ad_interval
    global click_ad_count
    # sleep_time_second = int(cf.get('config', 'sleep_time_second'))
    # window_number = int(cf.get('config', 'window_number'))
    # show_window = int(cf.get('config', 'show_window'))
    sleep_time_second = 50
    window_number = 1
    show_window = 1


def judge(content):
    if '未连接到互联网' in content:
        print('代理不好使啦')
    if 'anti_Spider-checklogin&' in content:
        print('被anti_Spider check啦')


def open_html(browser, url):
    """
     打开指定界面
    """
    content = browser.get(url)
    # time.sleep(sleep_time_second)
    if content is not None:
        judge(content)


def getIP():
    from urllib.request import urlopen
    my_ip = load(urlopen('http://httpbin.org/ip'))['origin']
    print("当前IP %s" % my_ip)


def bohao():
    while True:
        os.system('@Rasdial 宽带连接 /DISCONNECT')  # 先断开宽带连接（这个宽带连接是你的网络名字，可以叫做别的）
        # 然后重新拨号
        os.system('@Rasdial 宽带连接 051685874292 1MPRYA70')
        res = os.system('ping 8.8.8.8')
        # 没有网络的时候res为True
        if res:
            print("准备重新连接")
            time.sleep(2)
        # 有网络 什么都不做
        else:
            break
        # 每隔 5分钟进行一次检测
    getIP()


def loop(urls):
    for i in urls:
        webbrowser.open(i)
    # browser.quit()
    time.sleep(int(sleep_time_second))
    os.system('taskkill /IM chrome.exe /F')
    bohao()


if __name__ == '__main__':
    init()
    url_list = file.get_request_url()
    print("向往-》启动成功,间隔%s" % sleep_time_second)
    count = 0
    while 1:
        count = count + 1
        print("向往-》执行%s次" % count)
        loop(url_list)
