# -*- coding: utf-8 -*-#
# Name:         fire_fox
# Description:  
# Author:       10264
# Date:         2019/11/18
from selenium import webdriver
import time
from config import *
import urllib.request
import requests
import proxy_operation
import threading
from concurrent.futures import ThreadPoolExecutor


def init():
    """
     浏览器信息初始化
    :return:
    """
    # PROXY = "115.29.3.37:80"
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
    browser = webdriver.Chrome()


def get_chrome(proxy):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server={0}'.format(proxy))
    return webdriver.Chrome()


def open_html(browser, url):
    """
     打开指定界面
    """
    browser.get(url)
    # time.sleep(sleep_time_second)


def loop():
    couont = 3
    try:

        return_json = proxy_operation.get_proxy()
        proxy = return_json["proxy"]
        print("代理地址%s" % proxy)
        browser = get_chrome(proxy)
        proxy_operation.delete_proxy(proxy)
        open_html(browser, "https://www.iqiyi.com/v_19rvcuttls.html")
        js = 'window.open("https://www.iqiyi.com/v_19rvcupjg0.html");'
        browser.execute_script(js)
        time.sleep(1)

        # js = 'window.open("https://www.iqiyi.com/v_19rvcvpfic.html");'
        # browser.execute_script(js)
        # time.sleep(50)
        print("222")
        time.sleep(sleep_time_second)
        print("111")

    # except:
    #    print("线程异常。")
    finally:
        browser.close()


if __name__ == '__main__':
    count = 0
    print("开始启动，每次设置视频播放时间%s秒" % sleep_time_second)
    pool = ThreadPoolExecutor(max_workers=4)
    while (1):
        # for i in (1,5):
        #         #     count = count + 1
        #         #     print("已经执行%s次" % count)
        #         #     pool.submit(loop)
        count = count + 1
        print("已经执行%s次" % count)
        pool.submit(loop)
        count = count + 1
        print("已经执行%s次" % count)
        pool.submit(loop)
        count = count + 1
        print("已经执行%s次" % count)
        pool.submit(loop)
        count = count + 1
        print("已经执行%s次" % count)
        pool.submit(loop)
        time.sleep(sleep_time_second * 4)
