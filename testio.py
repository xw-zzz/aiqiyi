# -*- coding: utf-8 -*-#
# Name:         testio
# Description:  
# Author:       10264
# Date:         2019/11/26
from json import load
from urllib.request import urlopen
my_ip = load(urlopen('http://jsonip.com'))['ip']
print ('jsonip.com', my_ip)