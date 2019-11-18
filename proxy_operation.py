# -*- coding: utf-8 -*-#
# Name:         proxy_operation
# Description:  
# Author:       10264
# Date:         2019/11/18
import requests
import json
def get_proxy():
    """
     获取代理地址
    :return:
    """
    return_json = requests.get("http://129.204.148.18:5010/get/").json()
    if return_json is not None and return_json != "":
        return  return_json
    else:
        return ""


def delete_proxy(proxy):
    """
     删除
    :param proxy:
    :return:
    """
    requests.get("http://129.204.148.18:5010/delete/?proxy={}".format(proxy))


if __name__ == '__main__':

    get_proxy()