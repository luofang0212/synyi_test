#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb
from util.dbPlsql_util_bi import PlSqlDbBI
import random
import time
from datetime import datetime,timedelta
from update_source.get_data import GetData
from util.time_utc import *

# 门诊号源 topic=xxx
mysql1 = PlSqlDbBI()
sql_1 = '''select max(id) from source.outpatient_source;'''
res_1 = mysql1.query(sql_1)

max_id = res_1[0][0] +1
print(max_id)

mysql = PlSqlDb()

sql_2 = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''

res_2 = mysql.query(sql_2)
# dept_id = res_2[3][0]
# dept_name = res_2[3][1]
# normalized_dept_name = res_2[3][2]
# normalized_dept_id  = res_2[3][3]
# source_app = res_2[3][4]
print(len(res_2))
print(res_2)

for i in range(1, 400):
    max_id = max_id + 1
    res_2 = mysql.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]
    normalized_dept_name = res_2[i][2]
    normalized_dept_id = res_2[i][3]

    reg_level_data = {0: 'IMC急诊科', 1: '主任专家', 2: '急诊挂号', 3: '西医专科', 4: '免费挂号', 5: '副主任专家'}
    reg_level_id = random.randint(0, 5)
    reg_level_code = reg_level_id
    reg_level_name = reg_level_data[reg_level_id]

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

    doc_title_data = {1: '主治医师', 2: '主任医师', 3: '高级工程师', 4: '助理研究员', 5: '副主任技师', 6: '副主任中药师', 7: '副主任护师', 8: '中药师'}
    doc_title_id = random.randint(1, 8)
    doc_title_code = doc_title_id
    doc_title_name = doc_title_data[doc_title_id]

    source_amount = random.randint(1, 5)
    is_extra_flag = random.randint(0, 1)


    # 指定日期 转换
    data = random.randint(2, 2)
    get_time = '2021-09-0{0} 10:00:00.000000'.format(data)
    now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')

    # 时间统一用
    # now_time = datetime.now()
    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-8, 13), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset
    res = local_to_utc(real_time)
    update_time = local_to_utc(real_time)

    # time_scope_data = {0: '上午', 1: '下午'}
    # time_scope_code = int(random.choice([0, 1]))
    # time_scope_name = time_scope_data[time_scope_code]

    compare_time = '2021-09-0{0} 12:00:00.000000'.format(data)
    compare_time_new = datetime.strptime(compare_time, '%Y-%m-%d %H:%M:%S.%f')

    # print(now_time, real_time, compare_time_new)
    if real_time <= compare_time_new:
        # 上午
        time_scope_data = [0, '上午']

    elif real_time > compare_time_new:
        # 下午
        time_scope_data = [1, '下午']

    time_scope_code = time_scope_data[0]
    time_scope_name = time_scope_data[1]



    sql_3 = '''
       INSERT INTO source.outpatient_source (id, org_code, source_app, dept_id, dept_code, dept_name, dept_type_code,
                                      dept_type_name, reg_level_id, reg_level_code, reg_level_name, doc_id, doc_code,
                                      doc_name, doc_title_id, doc_title_code, doc_title_name, source_amount,
                                      is_extra_flag, time_scope_code, time_scope_name, release_time, statis_time, str1,
                                      str2, str3, str4, str5, str6, str7, str8, str9, str10)
VALUES ({0}, '46919134-2', '{1}', {2}, '{2}', '{3}', '{2}', '{3}', {4}, '{5}', '{6}', {7}, '{7}', '{8}', {9}, '{10}',
         '{11}', {12}, {13},
           {14}, '{15}', '{16}', '{16}', null, null, null, null, null, null, null, null, null, null);
        '''.format(max_id, source_app, dept_id, dept_name, reg_level_id, reg_level_code, reg_level_name, doc_id,
                   doc_name, doc_title_id, doc_title_code, doc_title_name, source_amount, is_extra_flag,
                   time_scope_code, time_scope_name,update_time)
    mysql1.insert(sql_3)
    print(i)
