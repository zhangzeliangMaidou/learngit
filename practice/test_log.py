#!/usr/bin/env python
# -*- coding:utf-8 -*-

from log import Logger

Log= Logger()

class Test():
    
    def __init__(self):
        self.logger = Log.logger()

    def test(self):
        self.logger.debug('this is a logger debug message')
        self.logger.info('this is a logger info message')
        self.logger.warning('this is a logger warning message')
        self.logger.error('this is a logger error message')
        self.logger.critical('this is a logger critical message')

print(__file__)
Test = Test()
Test.test()
