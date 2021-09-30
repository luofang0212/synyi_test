#!/usr/bin/env python
# -*- coding:utf-8 -*-



import time
import random
from datetime import datetime, timedelta


# now_time = datetime.now()
# 指定日期 转换
get_time = '2021-08-10 00:00:00.000000'
now_time = datetime.strptime(get_time,'%Y-%m-%d %H:%M:%S.%f')
print(now_time)
# 根据当前时间 去计算便宜时间，随机生成时间
hours_data = random.randint(-10,14)
hours_data = round(random.uniform(-10,14),2)
offset = timedelta(hours=hours_data)
real_time = now_time + offset

print(now_time,real_time,hours_data)