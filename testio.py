# -*- coding: utf-8 -*-#
# Name:         testio
# Description:  
# Author:       10264
# Date:         2019/11/26

 #!/usr/bin/python
 # -*- coding:utf8 -*-
from json import load
from urllib.request import urlopen
import urllib
import re

my_ip = load(urlopen('http://httpbin.org/ip'))['origin']
print(my_ip)