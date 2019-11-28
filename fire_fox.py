# -*- coding: utf-8 -*-#
# Name:         fire_fox
# Description:  
# Author:       10264
# Date:         2019/11/18
import random
from concurrent.futures.thread import ThreadPoolExecutor
from json import load

from selenium import webdriver
import time
import proxy_operation
import file
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
import configparser
import os
import _thread as thread

import win32ras
sleep_time_second = 0
window_number = 0
show_window = 1
account = ''
password = ''


def init():

    global sleep_time_second
    global window_number
    global show_window
    global account
    global password
    account, password = file.get_account()
    try:
        cf = configparser.ConfigParser()
        path = os.path.abspath('config.conf')
        cf.read("config.conf", encoding='utf-8')
        sleep_time_second = int(cf.get('config', 'sleep_time_second'))
        window_number = int(cf.get('config', 'window_number'))
        show_window = int(cf.get('config', 'show_window'))
    except Exception as e:
        print("解析失败")
        sleep_time_second = 53
        window_number = 2
        show_window = 1


def get_chrome(proxy):
    # proxy ="18.136.202.207:1024"
    chrome_options = webdriver.ChromeOptions()
    # argument = '--proxy-server={%s}' % proxy
    # print(argument)
    # chrome_options.add_argument(argument)
    # chrome_options.add_argument('--headless')  # 无头模式
    chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速
    chrome_options.add_argument('--start-maximized')  # 浏览器最大化
    chrome_options.add_argument('--window-size=1280x1024')  # 设置浏览器分辨率（窗口大小）
    chrome_options.add_argument('log-level=3')
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_options.add_argument('--ignore-certificate-errors')  # 禁用扩展插件并实现窗口最大化
    chrome_options.add_argument('--incognito')  # 隐身模式（无痕模式）
    chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--window-size=800,800')
    chrome_options.add_argument('--disable-javascript')  # 禁用javascript
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=chrome_options)

    a = proxy.split(":", 1)
    # profile = FirefoxProfile()
    # profile.set_preference('network.proxy.type', 1)
    # profile.set_preference('network.proxy.http', a[0])
    # profile.set_preference('network.proxy.http_port', a[1])
    # profile.set_preference('network.proxy.ssl', a[0])
    # profile.set_preference('network.proxy.ssl_port', a[0])
    # profile.set_preference('browser.link.open_newwindow', 3)
    # print()
    # print(show_window)
    # print(type(show_window))
    if show_window == 0:
        options = Options()
        options.headless = True
        return webdriver.Firefox(executable_path=os.getcwd() + "\geckodriver", options=options)
    else:
        return webdriver.Firefox(executable_path=os.getcwd() + "\geckodriver")


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
    # if content is not None:
    #     judge(content)


def loop(urls):
    try:
        # return_json = proxy_operation.get_proxy()
        # proxy = return_json["proxy"]
        # print("向往-》代理IP%s" % proxy)
        proxy = ''
        browser = get_chrome(proxy)

        # proxy_operation.delete_proxy(proxy)
        # thread.start_new_thread()
        open_html(browser, urls[0])
        for i in urls:
            if urls.index(i) > 0:
                js = 'window.open("%s");' % i
                browser.execute_script(js)
                time.sleep(1)
        # for i in urls:
        #     print(i)
        #     open_html(browser,i)
        #     browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'T')
        time.sleep(int(sleep_time_second))
    except Exception as e:
        print("线程异常。%s", e)
    finally:
        # browser.close()
        browser.delete_all_cookies()
        browser.quit()
        bohao1()


def getIP():
    from urllib.request import urlopen
    my_ip = load(urlopen('http://httpbin.org/ip'))['origin']
    print("当前IP %s" % my_ip)


def bohao():
    while True:
        os.system('@Rasdial 宽带连接 /DISCONNECT')  # 先断开宽带连接（这个宽带连接是你的网络名字，可以叫做别的）
        # 然后重新拨号
        s = '@Rasdial 宽带连接 ' + account + ' ' + password
        os.system(s)
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



def bohao1():
    DialBroadband()
    getIP()

def Connect(dialname, account, passwd):
    dial_params = (dialname, '', '', account, passwd, '')
    return win32ras.Dial(None, None, dial_params, None)


def DialBroadband():
    dialname = u'宽带连接'  # just a name
    try:
        # handle is a pid, for disconnect or showipadrress, if connect success return 0.
        # account is the username that your ISP supposed, passwd is the password.
        handle, result = Connect(dialname, account, password)
        if result == 0:
            print
            "Connection success!"
            return handle, result
        else:
            print
            "Connection failed, wait for 2 seconds and try again..."
            time.sleep(2)
            DialBroadband()
    except:
        print
        "Can't finish this connection, please check out."


if __name__ == '__main__':
    init()
    url_list = file.get_request_url()

    # print(show_window)
    # print(url_list)
    # loop(url_list)

    count = 0
    print("开始启动，每次设置视频播放时间%s秒" % sleep_time_second)
    # url_list = file.get_request_url()

    # pool = ThreadPoolExecutor(max_workers=2)
    # pool.submit(loop,url_list[0:7])
    # pool.submit(loop, url_list[7:14])
    # while (1):
    #     for i in range(1, 4):
    #         count = count + 1
    #         print("已经执行%s次" % count)
    #         pool.submit(loop, url_list)
    #     time.sleep(sleep_time_second + 3)
    # print("向往-》启动成功,间隔%s" % sleep_time_second)
    # print("向往-》请求路径%s" % url_list)
    # print("向往-》任务执行")
    # count = 0
    while (1):
        #xxx_list = [url_list[random.randint(0, len(url_list))]]
        #print("请求路径：%s" % xxx_list)
        count = count + 1
        print("执行%s次" % count)
        loop(url_list)
    # print(url_list[0:7])
    # print(type(url_list[0:7]))
    # thread.start_new_thread(loop, ('Thread-1',url_list[0:7],))
    # thread.start_new_thread(loop, ('Thread-2',url_list[7:14],))
