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

policy_sql = '''
select policy_kpi_code,policy_kpi_name,policy,exposition,policy_kpi_level1,
       policy_kpi_level2,policy_kpi_level3,formula,policy_kpi_guide,
       unit,data_source
from system.policy_kpi where unit is not null and policy is not null limit 50;
'''

sim_system_sql = PLSqlSystem()
bi_system_sql = bi_sql()

policy_data = bi_system_sql.query(policy_sql)
# print(policy_data)
nums = len(policy_data)


indicator_sql = '''select indicator_name from config.indicator;'''
indicator_data = sim_system_sql.query(indicator_sql)
print(indicator_data)
indicator_data_text = []
for i in range(0, len(indicator_data)):
    indicator_data_text.append(indicator_data[i][0])
print(indicator_data_text)

for x in range(1, nums):
    policy_kpi_code = policy_data[x][0]
    policy_kpi_name = policy_data[x][1]
    policy = policy_data[x][2]
    exposition = policy_data[x][3]
    policy_kpi_level1 = policy_data[x][4]
    policy_kpi_level2 = policy_data[x][5]
    policy_kpi_level3 = policy_data[x][6]
    formula = policy_data[x][7]
    policy_kpi_guide = policy_data[x][8]
    unit = policy_data[x][9]
    data_source = policy_data[x][10]
    print(policy_kpi_code, policy_kpi_name, policy, policy_kpi_level1,
          policy_kpi_level2, policy_kpi_level3, formula, policy_kpi_guide, unit, data_source)

    indicator_alias = "我是别名" + str(random.randint(10, 2000))

    name = 'indicator_id'
    namespace = uuid.uuid1()
    indicator_id = uuid.uuid5(namespace, name)

    random_data = GetData.random_data
    zimu1 = str(random.randint(1, 9))
    zimu2 = random.choice(random_data)
    zimu3 = random.choice(random_data)
    zimu4 = random.choice(random_data)
    zimu5 = random.choice(random_data)
    zimu6 = random.choice(random_data)
    zimu7 = random.choice(random_data)
    code = zimu1 + zimu2 + zimu3 + zimu4 + zimu5 + zimu6 + zimu7
    indicator_code = "Z" + code
    # print(indicator_code)
    #

    guide = random.randint(0,3)
    #
    unit_res = policy_data[x][9]
    if unit_res == '':
        unit = ''
    else:
        unit = unit_res

    dept_data = GetData.dept_data
    responsible_person = random.choice(GetData.dept_name)
    responsible_dept = dept_data[responsible_person]

    content = policy_data[x][3]
    formula = policy_data[x][7]

    description = policy_data[x][4]
    meaning = policy_data[x][5]
    remark = "我是remark" + str(random.randint(10, 2000))
    #
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
    #
    indicator_name = policy_data[x][1]
    indicator_sql = '''
        INSERT INTO config.indicator (indicator_id, indicator_code, indicator_name, indicator_alias, source_type, guide,
                                  unit, responsible_person, responsible_dept, content, formula, description, meaning,
                                  status, remark, creator, created_time, modifier, modified_time)
    VALUES ('{0}', '{1}', '{2}', '{3}', 1, '{4}', '{5}', '{6}', '{7}', '{8}', '{9}',
            '{10}', '{11}', 1, '{12}', 1, '{13}', 1, '{13}');
        '''.format(indicator_id, indicator_code, indicator_name, indicator_alias, guide, unit, responsible_person,
                   responsible_dept, content, formula, description, meaning, remark, update_time)

    if indicator_name in indicator_data_text:
        print("{0} 已存在".format(indicator_name))
    else:
        sim_system_sql.insert(indicator_sql)
        print("indicator_sql 插入成功")

    policy_data_1 = GetData.policy_data
    tag_id = random.choice(GetData.uid)
    tag_name = policy_data_1[tag_id]

    tag_detail_sql = '''INSERT INTO config.indicator_tag_detail (tag_id, indicator_id, creator, created_time, modifier, modified_time)  VALUES ('{0}', '{1}', 1,'{2}', 1, '{2}'); '''.format(
        tag_id, indicator_id, update_time)

    sim_system_sql.insert(tag_detail_sql)
    print("tag_detail_sql 插入成功")

    print(x)