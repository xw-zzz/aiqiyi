# -*- coding: utf-8 -*-#
# Name:         fire_fox
# Description:  
# Author:       10264
# Date:         2019/11/18
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

sleep_time_second = 0
window_number = 0
show_window = 1
click_ad_interval = 20

click_ad_count = 10

def init():
    cf = configparser.ConfigParser()
    #path = os.path.abspath('config.conf')
    cf.read("config.conf",encoding='utf-8')
    global sleep_time_second
    global window_number
    global show_window
    global click_ad_interval
    global click_ad_count
    sleep_time_second = int(cf.get('config', 'sleep_time_second'))
    window_number = int(cf.get('config', 'window_number'))
    show_window = int(cf.get('config', 'show_window'))
    click_ad_interval = int(cf.get('config', 'click_ad_interval'))
    click_ad_count = int(cf.get('config', 'click_ad_count'))

def get_chrome(proxy):
    return webdriver.Chrome()
    chrome_options = webdriver.ChromeOptions()
    argument = 'proxy-server=%s' % proxy
    print(argument)
    chrome_options.add_argument(argument)
    #return webdriver.Chrome(options=chrome_options)



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


def loop(urls):
    couont = 3
    # try:
    #     return_json = proxy_operation.get_proxy()
    #     proxy = return_json["proxy"]
    #     print("向往-》代理IP%s" % proxy)
    #     browser = get_chrome(proxy)
    #     proxy_operation.delete_proxy(proxy)
    #     # thread.start_new_thread()
    #     open_html(browser, urls[0])
    #     for i in urls:
    #         if urls.index(i) > 0:
    #             js = 'window.open("%s");' % i
    #             browser.execute_script(js)
    #             time.sleep(1)
    #     # for i in urls:
    #     #     print(i)
    #     #     open_html(browser,i)
    #     #     browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'T')
    #     time.sleep(int(sleep_time_second))
    # except Exception as e:
    #     print("线程异常。%s", e)
    # finally:
    #     # browser.close()
    #     if browser is not None:
    #         browser.quit()
    return_json = ''
    #while(1):
    proxy = ''
    browser = get_chrome(proxy)
    #proxy_operation.delete_proxy(proxy)
    # thread.start_new_thread()
    open_html(browser, urls[0])
    # for i in range(0,click_ad_count):
    #     browser.find_element_by_id("flashbox").click()
    #     time.sleep(click_ad_interval)

    for i in urls:
        if urls.index(i) > 0:
            js = 'window.open("%s");' % i
            browser.execute_script(js)

    time.sleep(int(sleep_time_second))
    browser.quit()

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


if __name__ == '__main__':
    init()
    url_list = file.get_request_url()
    #print(show_window)
    # print(url_list)
    # loop(url_list)

    # count = 0
    # print("开始启动，每次设置视频播放时间%s秒" % sleep_time_second)
    # url_list = file.get_request_url()
    # print("请求路径：%s" % url_list)
    # pool = ThreadPoolExecutor(max_workers=4)
    # while (1):
    #     for i in range(1, 4):
    #         count = count + 1
    #         print("已经执行%s次" % count)
    #         pool.submit(loop, url_list)
    #     time.sleep(sleep_time_second + 3)
    print("向往-》启动成功,间隔%s" % sleep_time_second)
    print("向往-》请求路径%s" % url_list)
    print("向往-》任务执行")
    count = 0
    while 1:
        count = count + 1
        print("向往-》执行%s次" % count)
        loop(url_list)
