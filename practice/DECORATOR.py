#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
装饰器使用方法
"""

import time


# 不带参数的装饰器
def deco(func):
    def wrapper():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        secs = end_time - start_time
        m,s = divmod(secs,60)
        h,m = divmod(m,60)
        print("%s小时%s分钟%s秒" % (h,m,s))
    return wrapper

@deco
def func():
    print("Start...")
    time.sleep(2)
    print("End...")


# 带参数的装饰器
def deco2(func):
    def wrapper(a,b):
        start_time = time.perf_counter()
        func(a,b)
        end_time = time.perf_counter()
        secs = end_time - start_time
        m, s = divmod(secs, 60)
        h, m = divmod(m, 60)
        print("%s小时%s分钟%s秒" % (h, m, s))
    return wrapper

@deco2
def func2(a,b):
    print (a+b)

#带不确定参数的装饰器

def deco3(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        secs = end_time - start_time
        m, s = divmod(secs, 60)
        h, m = divmod(m, 60)
        print("%s小时%s分钟%s秒" % (h, m, s))
    return wrapper

@deco3
def func30(a,b):
    print (a + b)

@deco3
def func31(a):
    time.sleep(3)
    print(a)

@deco3
def func32(a):
    time.sleep(3)
    for i in a:
        print (i)

@deco3
def func33(a):
    time.sleep(3)
    for i in a.items():
        print (i)

@deco3
def func34(b,a,c):
    time.sleep(3)
    for i in a:
        print (i)
    for i in b.items():
        print (i)
    print (c)

#func34(a=[1,2,3],b={"a":1,"b":2},c="hello world")

