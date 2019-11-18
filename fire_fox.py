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

browser = None;

def init():
    """
     浏览器信息初始化
    :return:
    """
    browser = webdriver.Chrome()



def open_html(url):
    """
     打开指定界面
    """
    browser.get(url)
    time.sleep(sleep_time_second)





if __name__ == '__main__':
    init()