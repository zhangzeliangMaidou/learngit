#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

# Python 字典类型数据转换为JSON对象
data = {
    "no":1,
    "name":"Runoob",
    "url":"http://www.baidu.com"
    }

json_str = json.dumps(data)
print("Python origin data:",repr(data))
print("JSON Object:",json_str)

data2 = json.loads(json_str)
print(type(data2))

with open("data.json","w") as f:
    json.dump(data,f)

with open("data.json","r") as f:
    data=json.load(f)
    print (data)
