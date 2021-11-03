#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb
from util.dbPlsql_util_bi import PlSqlDbBI
import random
import time
from datetime import timedelta, datetime
from bi_source.get_data import GetData
from util.time_utc import *

# 门诊预约 topic=xxx
mysql1 = PlSqlDbBI()
sql_1 = '''select max(book_id) from source.outpatient_appointment;'''
res_1 = mysql1.query(sql_1)

max_book_id = res_1[0][0] + 1
# max_book_id=1
print(max_book_id)

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
    max_book_id = max_book_id + 1
    res_2 = mysql.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]
    normalized_dept_name = res_2[i][2]
    normalized_dept_id = res_2[i][3]

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name

    sex_data = {'0': '女', '1': '男'}
    sex_code = random.choice(['0', '1'])
    sex_name = sex_data[sex_code]
    age = random.randint(1, 100)

    age_group_data = {'0-7': '0岁-7岁', '7-18': '7岁-18岁', '18-41': '18岁-41岁', '41-65': '41岁-65岁', '>65': '>65岁'}
    age_group_code = random.choice(['18-41', '0-7', '>65', '41-65', '7-18'])
    age_group_name = age_group_data[age_group_code]

    patient_type_data = {1: '军人', 2: '军人', 3: '军人', 4: '军人', 5: '群众', 6: '群众', 7: '群众', 8: '群众', }
    patient_type_code = random.randint(1, 8)
    patient_type_name = patient_type_data[patient_type_code]

    pay_kind_data = {0: '自费', 1: '医保', 2: '商保'}
    pay_kind_code = random.randint(0, 2)
    pay_kind_name = pay_kind_data[pay_kind_code]

    book_way_data = {'A': [4894, "窗口挂号"], 'Z': [4895, "自助机"], '1': [49549, "预约挂号"], '0': [49548, "现场挂号"],
                     'D': [4893, "网上预约"], }
    book_way_code = random.choice(['A', 'Z', '1', '0', 'D'])
    book_way_id = book_way_data[book_way_code][0]
    book_way_name = book_way_data[book_way_code][1]

    # 普通门诊、专家门诊、特需门诊
    book_class_data = {0: '普通门诊', 1: '专家门诊', 2: '特需门诊'}
    book_class_code = random.randint(0, 2)
    book_class_name = book_class_data[book_class_code]

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

    book_num = random.choice([1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    # 指定日期 转换
    data = random.randint(26, 26)
    get_time = '2021-10-{0} 10:00:00.000000'.format(data)
    now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')
    # now_time = datetime.now()
    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-8, 13), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset

    update_time = local_to_utc(real_time)

    compare_time = '2021-10-{0} 12:00:00.000000'.format(data)
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
       INSERT INTO source.outpatient_appointment (book_id, org_code, source_app, source_appointment_id, source_visit_id,
                                           source_patient_id, patient_name, sex_code, sex_name, age, age_unit, age_day,
                                           age_group_code, age_group_name, patient_type_code, patient_type_name,
                                           pay_kind_code, pay_kind_name, address, country, province, city, district,
                                           profession_code, profession_name, book_way_code, book_way_name, book_time,
                                           appointment_time, source_appointment_time, reg_time, book_class_code,
                                           book_class_name, dept_code, dept_name, doc_code, doc_name, book_num,
                                           patient_id, normalized_dept_id, normalized_dept_name, str1, str2, str3, str4,
                                           str5, str6, str7, str8, str9, str10, dept_id,time_scope_code,time_scope_name)
VALUES ({0}, '46919134-2', '{1}', '1', '1', '1', '{4}', '{5}', '{6}', {7}, '天', 10, '{8}', '{9}', '{10}', '{11}',
         '{12}', '{13}', '浦东新区亮景路', '上海',
         '上海', '上海', '一区', null, null, '{14}', '{15}', '{23}', '{23}', null, '{23}', '{16}', '{17}', '{2}', '{3}', '{18}',
         '{19}', {20},
           {0}, {21}, '{22}', null, null, null, null, null, null, null, null, null, null, {2},{24},'{25}');
        '''.format(max_book_id, source_app, dept_id, dept_name, patient_name, sex_code, sex_name, age, age_group_code,
                   age_group_name, patient_type_code, patient_type_name, pay_kind_code, pay_kind_name, book_way_code,
                   book_way_name, book_class_code, book_class_name, doc_id, doc_name, book_num, normalized_dept_id,
                   normalized_dept_name, update_time, time_scope_code, time_scope_name)
    mysql1.insert(sql_3)
    print(i)
