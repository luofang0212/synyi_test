#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb
from util.dbPlsql_util_bi import PlSqlDbBI
import random
import time
from datetime import timedelta,datetime
from update_source.get_data import GetData

# 医师出诊表 topic=xxx
mysql1 = PlSqlDbBI()
sql_1 = '''select max(id) from source.outpatient_doc;'''
res_1 = mysql1.query(sql_1)

max_id = res_1[0][0] + 1
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

for i in range(1, 1208):
    max_id = max_id + 1
    res_2 = mysql.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]
    normalized_dept_name = res_2[i][2]
    normalized_dept_id = res_2[i][3]



    clinic_type_data = {0: '门诊', 1: '急诊', 2: '住院', 3: '其他'}
    clinic_type_code = random.choice([0, 3])
    clinic_type_name = clinic_type_data[clinic_type_code]

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

    # 诊室
    clinic_room_data = {"1001": "诊室一", "1002": "诊室二", "1003": "诊室三", "1004": "诊室四", "1005": "诊室五", "1006": "诊室六"}
    clinic_room_code = random.choice(["1001", "1002", "1003", "1004", "1005", "1006"])
    clinic_room_name = clinic_room_data[clinic_room_code]

    # 诊区
    clinic_ward_data = {1: "血液净化中心诊区", 2: "中医内科诊区", 3: "内分泌科诊区", 4: "中医内科诊区", 5: "皮肤科诊区", 6: "急诊外科诊区", 7: "耳鼻喉科诊区",
                       8: "儿科病区诊区", 9: "产科门诊诊区", 10: "神经外科诊区", 11: "口腔科诊区", 12: "新生儿专科门诊诊区", 13: "感染管理科诊区"}
    clinic_ward_code = random.randint(1, 13)
    clinic_ward_name = clinic_ward_data[clinic_ward_code]

    room_type_data = {0: '专科', 1: '专病', 2: '普病'}
    room_type_code = random.choice([0, 1, 2])
    room_type_name = room_type_data[room_type_code]

    room_status_data = {0: '未开诊', 1: '开诊'}
    room_status_code = random.choice([0, 1])
    room_status_name = room_status_data[room_status_code]

    doc_title_data = {1: '主治医师', 2: '主任医师', 3: '高级工程师', 4: '助理研究员', 5: '副主任技师', 6: '副主任中药师', 7: '副主任护师', 8: '中药师'}
    doc_title_id = random.randint(1, 8)
    doc_title_code = doc_title_id
    doc_title_name = doc_title_data[doc_title_id]

    clinic_days = random.choice([0.5, 1.0])

    # 指定日期 转换
    data = random.randint(19,22)
    get_time = '2021-08-{0} 10:00:00.000000'.format(data)
    now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')

    # 时间统一用
    # now_time = datetime.now()

    data_new_time = datetime.strftime(now_time,'%Y-%m-%d')
    time_scope_data = {0: ['上午', ' 08:00:00', ' 08:05:00', ' 12:00:00'],
                       1: ['下午', ' 13:00:00', ' 13:05:00', ' 16:30:00']}
    time_scope_code = int(random.choice([0, 1]))
    time_scope_name = time_scope_data[time_scope_code][0]
    begin_service_time = data_new_time + time_scope_data[time_scope_code][1] + '.000000'
    first_input_time = data_new_time + time_scope_data[time_scope_code][2] + '.000000'
    end_service_time = data_new_time + time_scope_data[time_scope_code][3] + '.000000'

    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-10, 14), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset

    update_time = real_time

    sql_3 = '''
       INSERT INTO source.outpatient_doc (id, doc_code, doc_name, dept_code, dept_name, check_in_time, clinic_type_code,
                                   clinic_type_name, source_app, clinic_ward_code, clinic_ward_name, clinic_room_code,
                                   clinic_room_name, room_type_code, room_type_name, room_status_code, room_status_name,
                                   doc_id, doc_title_id, doc_title_code, doc_title_name, dept_id, begin_service_time,
                                   first_input_time, end_service_time, time_scope_code, time_scope_name, clinic_days,
                                   str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, statis_time)
VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{23}', {24}, '{25}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}',
        '{11}', {12}, '{13}', {1}, {14}, '{15}', '{16}', {3}, '{20}', '{21}', '{22}', {17}, '{18}', {19}, null, null, null, null,
        null, null, null, null, null, null, '{23}');

        '''.format(max_id, doc_id, doc_name, dept_id, dept_name, source_app, clinic_ward_code, clinic_ward_name,
                   clinic_room_code,
                   clinic_room_name, room_type_code, room_type_name, room_status_code, room_status_name, doc_title_id,
                   doc_title_code, doc_title_name,time_scope_code, time_scope_name, clinic_days,begin_service_time,
                                   first_input_time, end_service_time,update_time,clinic_type_code,
                                   clinic_type_name)
    mysql1.insert(sql_3)
    print(i)
