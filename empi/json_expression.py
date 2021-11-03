#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json
from jsonpath_ng import jsonpath,parse

json_string = '''
[{
    "key":"2",
    "value":"自费卡"
},
{
    "key":"14",
    "value":"体检患者标识"
},
{
    "key":"1",
    "value":"患者主索引号"
},
{
    "key":"12",
    "value":"住院号"
},
{
    "key":"8",
    "value":"驾驶证"
},
{
    "key":"13",
    "value":"港澳居民来往内地通行证"
},
{
    "key":"9",
    "value":"军官证"
},
{
    "key":"5",
    "value":"医保卡"
},
{
    "key":"7",
    "value":"居民户口簿"
},
{
    "key":"6",
    "value":"台湾居民来往内地通行证"
},
{
    "key":"10",
    "value":"护照"
},
{
    "key":"4",
    "value":"其他法定有效证件"
},
{
    "key":"3",
    "value":"门诊号"
}]
'''
json_data = json.loads(json_string)

json_expression = parse('json_data[0].$.key')

match = json_expression.find(json_data)

print(match[0].value)