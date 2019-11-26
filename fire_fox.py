# -*- coding: utf-8 -*-#
# Name:         fire_fox
# Description:  
# Author:       10264
# Date:         2019/11/18
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
    # proxy ="18.136.202.207:1024"
    # chrome_options = webdriver.ChromeOptions()
    # argument = '--proxy-server={%s}' % proxy
    # print(argument)
    # chrome_options.add_argument(argument)
    # return webdriver.Chrome(options=chrome_options)

    # a = proxy.split(":", 1)
    # profile = FirefoxProfile()
    # profile.set_preference('network.proxy.type', 1)
    # profile.set_preference('network.proxy.http', a[0])
    # profile.set_preference('network.proxy.http_port', a[1])
    # profile.set_preference('network.proxy.ssl', a[0])
    # profile.set_preference('network.proxy.ssl_port', a[0])

    # print()
    #print(show_window)
    #print(type(show_window))

    # if show_window == 0:
    #     options = Options()
    #     options.headless = True
    #     return webdriver.Firefox(profile, executable_path=os.getcwd() + "\geckodriver", options=options)
    # else:
    #     return webdriver.Firefox(profile, executable_path=os.getcwd() + "\geckodriver")

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
    if content is not None:
        judge(content)

# try:
    #     return_json = proxy_operation.get_proxy()
    # except Exception as e:
    #     print("获取代理IP失败，重试")
    # print(return_json)
    # if return_json is not None and len(return_json) >0:
    #     break
    # proxy = return_json["proxy"]
    # print("向往-》代理IP%s" % proxy)
def loop(urls):
    while(1):
        proxy =''
        browser = get_chrome(proxy)
        # browser.get("http://httpbin.org/ip")
        # print(browser.page_source)
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
