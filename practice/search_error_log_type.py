#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re

class FindErrorLog():

    def __init__(self, file_pattern, error_log_pattern):
        self.file_pattern = re.compile(file_pattern)
        self.error_log_pattern = re.compile(error_log_pattern)

    def find_error_log_in_file(self, filename):
        if os.path.isdir(filename):
            for subfilename in os.listdir(filename):
                subfilepath = os.path.join(filename, subfilename)
                self.find_error_log_in_file(subfilepath)
        else:
            if not os.path.exists(filename):
                print("%s does not Exist")
                return
            if os.path.isfile(filename):
                #if filename.split(".")[-1] in ["txt","py","log","error","xml","db"]:
                if filename.split(".")[-1] in ["py"]:
                    with open(os.path.abspath(filename), mode="r", encoding='UTF-8') as f:
                        lines = f.readlines()
                        for line in lines:
                            m = self.error_log_pattern.search(line)
                            if m:
                                print(m.group(0))
                                print("%%"*100)
                                return True
