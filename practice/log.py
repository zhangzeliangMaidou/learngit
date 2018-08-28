#!/usr/bin/env python
#-*- coding:utf-8 -*-

import logging
import time
import os
import sys
import os.path

class Logger():
    
    def __init__(self, log_name=None, logger_name=None):

        #设置日志文件名称：time.time()取得当前时间；time.localtime()取得本地时间；time.strftime()格式化日期；
        time_str = time.strftime("%Y_%m_%d_%H", time.localtime(time.time()))
        if not log_name:
            logname = time_str + '.log'
        else:
            logname = time_str + '_' + log_name + '.log'
        if not logger_name:
            self.logger_name = sys._getframe(1).f_code.co_name
        else:
            self.logger_name = logger_name
        print (logname)
        #设置日志文件所在的路径
        log_filedir = sys.path[0]+os.sep+'Logs'
        if not os.path.isdir(log_filedir):
            print("日志文件夹 %s 不存在，已创建该文件夹" %log_filedir)
            os.mkdir(log_filedir)
        current_day_log_filedir = log_filedir+os.sep+time.strftime("%Y_%m_%d", time.localtime(time.time()))
        if not os.path.isdir(current_day_log_filedir):
            print("日志文件夹 %s 不存在，已创建该文件夹" %current_day_log_filedir)
            os.mkdir(current_day_log_filedir)
            
        self.logfile = current_day_log_filedir + os.sep + logname

    def logger(self):
        #创建一个logger以及设置日志级别
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(logging.DEBUG)
        
        #创建文件handler，用于写入日志文件并设置文件日志级别
        file_handler = logging.FileHandler(self.logfile, "a")
        file_handler.setLevel(logging.DEBUG)
        
        #创建控制端输出handler，用于输出到控制端并设置输出日志级别
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        
        ##在控制端handler添加过滤器，将含有chat或者gui的handler信息输出
        #filter = logging.Filter("chat.gui")
        #console_handler.addFilter(filter)
        
        #定义handler的输出格式并将格式应用到handler
        #formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        formatter = logging.Formatter('%(asctime)s [%(levelname)s][%(module)s][%(funcName)s][%(lineno)-5d] %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        #将handler加入到logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        #将handler从logger中移除
        #self.logger.removeHandler(file_handler)
        #self.logger.removeHandler(console_handler)
        return self.logger

