#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import os
import sys

f = open("qconncom.txt","r")
lines = f.readlines()

for line in lines:
    match_realse_version = re.match(r'(.*)Release:.*', line, re.M | re.I)
    if match_realse_version:
        print(match_realse_version.group())
        target = match_realse_version.group()
        realse_number = target.split(":")[1].split(".")[0].split("r")[1]
        print(realse_number)
    match_target_number = re.match(r'(.*)LA\.UM\.(.*)-(.*)-(.*)-(.*)\*', line, re.M | re.I)
    if match_target_number:
        print(match_target_number.group())
        target = match_target_number.group()
        target_number = target.split("-")[1]
        print(target_number)


