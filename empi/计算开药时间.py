#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta

# 指定日期 转换
get_time = '2021-08-29'
now_time = datetime.strptime(get_time,'%Y-%m-%d')

# 用药天数
days_1 = 34
offset_1 = timedelta(days=days_1)
real_time = now_time + offset_1

# 可提前开药天数
days_2 = -4
offset_2 = timedelta(days=days_2)
ke_time = real_time + offset_2

system_time_1 = datetime.now()
system_time_2 = datetime.strftime(system_time_1,'%Y-%m-%d')
system_time = datetime.strptime(system_time_2,'%Y-%m-%d')

ying_day = ke_time - system_time
real_time = datetime.strftime(real_time,'%Y-%m-%d')
ke_time = datetime.strftime(ke_time,'%Y-%m-%d')

print("下次实际可开药时间：{0}\n可提前开药时间：{1}\n距离下次应开药时间：{2}".format(real_time,ke_time,ying_day))