#!/usr/bin/env python
# -*- coding:utf-8 -*-


from test_SIM.dbPlsql_util_system import PLSqlSystem
from test_SIM.dbPlsql_util_bi_system import PLSqlSystem as bi_sql

from datetime import datetime,timedelta
import random
import uuid

# topic
sim_system_sql = PLSqlSystem()
bi_system_sql = bi_sql()

topic_sql = '''
select topic_name,topic_from,topic_table from system.topic;
'''
topic_data= bi_system_sql.query(topic_sql)
nums = len(topic_data)
# print(topic_data)

id_sql = '''
select max(id) from config.indicator_topic;
'''
res_id= sim_system_sql.query(id_sql)
max_id = res_id[0][0] + 1

for i in range(0,nums):
    max_id = max_id + 1
    topic_name = topic_data[i][0]
    topic_table = topic_data[i][1]

    print(topic_name,topic_table)

    name = 'test_name'
    namespace = uuid.uuid1()
    guid_text = uuid.uuid5(namespace, name)


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


    sql_3 = '''INSERT INTO config.indicator_topic (id,topic_id, topic_name, topic_table, source_id, status, remark, creator,
                                    created_time, modifier, modified_time)
VALUES ({0},'{1}', '{2}', '{3}', 'a6871da0-6ae3-434c-cf51-2e0fd314b303',
        1, '', 1, '{4}', 1, '{4}');
        '''.format(max_id,guid_text,topic_name,topic_table,update_time)

    sim_system_sql.insert(sql_3)
    print(i)

