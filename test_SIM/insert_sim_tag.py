#!/usr/bin/env python
# -*- coding:utf-8 -*-

from test_SIM.dbPlsql_util_system import PLSqlSystem
from test_SIM.dbPlsql_util_bi_system import PLSqlSystem as bi_sql

from test_SIM.get_data import GetData

from datetime import datetime, timedelta
import random
import uuid
import re

# 政策指标 造数

sim_system_sql = PLSqlSystem()
bi_system_sql = bi_sql()

tag_data = GetData.uid
for x in range(0, len(tag_data)):

    # 指定日期 转换
    # get_time = '2021-08-10 00:00:00.000000'
    # now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')

    # 时间统一用
    now_time = datetime.now()
    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-10, 14), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset

    update_time = real_time

    policy_data = GetData.policy_data
    tag_id = tag_data[x]
    tag_name = policy_data[tag_id]

    tag_sql = '''INSERT INTO config.indicator_tag (tag_id, tag_name, status, remark, creator, created_time, modifier, modified_time) VALUES ('{0}', '{1}', 1, '', 1, '{2}', 1,'{2}');'''.format(tag_id, tag_name,update_time)

    sim_system_sql.insert(tag_sql)
    print(x)