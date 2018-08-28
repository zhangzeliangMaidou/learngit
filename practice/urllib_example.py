#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request     # 用于打开和读取URL, 
import urllib.error         # 用于处理前面request引起的异常, 
import urllib.parse        # 用于解析URL, 
import urllib.robotparser    # 用于解析robots.txt文件

with urllib.request.urlopen('http://www.python.org/') as f:
    with open("D:\\work\\python.txt","wb") as f2:
        f2.writelines(f.readlines())
        f2.close()
    f.close()

with open("D:\\work\\python.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()

auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')



