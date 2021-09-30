#!/usr/bin/env python
# -*- coding:utf-8 -*-

from test_SIM.dbPlsql_util_system import PLSqlSystem
from test_SIM.dbPlsql_util_bi_system import PLSqlSystem as bi_sql
from test_SIM.dbPlsql_util_rha_system import RHAPLSqlSystem as rha_sql
from test_SIM.get_data import GetData


from datetime import datetime, timedelta
import random
import uuid
import re

# 政策指标 造数

sim_system_sql = PLSqlSystem()
rha_system_sql = rha_sql()

kpi_data_sql = '''
select t.tag_name,i.indicator_id,indicator_code,i.indicator_name
from config.indicator_tag t
         right join config.indicator_tag_detail td on t.tag_id = td.tag_id
         right join config.indicator i on td.indicator_id = i.indicator_id
where i.status=1
and t.tag_name in('新病案手术','新病案首页','病例分组结果','床位分布情况日报','RHA填报主题','人员分布情况月报');
'''
kpi_data = sim_system_sql.query(kpi_data_sql)
# print(kpi_data)
num = len(kpi_data)
for x in range(0, num):

    indicator_id = kpi_data[x][1]
    indicator_code = kpi_data[x][2]
    indicator_name = kpi_data[x][3]
    tips = "我是tips:" + indicator_name
    remarks = "我是remarks:" + indicator_name

    # print(indicator_code)

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

    rha_sql = '''
     INSERT INTO system.indicator_config (indicator_name, indicator_id, indicator_code, group_by, order_by, top, creator,
                                     created_time, modifier, modified_time, extension_config, tips, color, remarks,
                                     is_fixed)
VALUES ('{0}', '{1}', '{2}', null, null, null, 1, '{3}', null, '{3}', null, '{4}', null, '{5}', default);
    '''.format(indicator_name, indicator_id, indicator_code,update_time,tips,remarks)
    rha_system_sql.insert(rha_sql)
    print(x)