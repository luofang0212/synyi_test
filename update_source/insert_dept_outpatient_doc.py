#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb
from util.dbPlsql_util_bi import PlSqlDbBI
import random
import time
from datetime import timedelta, datetime
from update_source.get_data import GetData
from util.time_utc import *

# 医师出诊表 topic=xxx
mysql1 = PlSqlDbBI()
sql_1 = '''select max(id) from source.outpatient_doc;'''
res_1 = mysql1.query(sql_1)

# max_id = 1
max_id = res_1[0][0] + 1
print(max_id)

mysql = PlSqlDb()

clinic_ward_data = {1: "血液净化中心诊区", 2: "中医内科诊区", 3: "内分泌科诊区", 4: "西医外科诊区", 5: "皮肤科诊区", 6: "急诊外科诊区", 7: "耳鼻喉科诊区",
                    8: "儿科病区诊区", 9: "产科门诊诊区", 10: "神经外科诊区", 11: "口腔科诊区", 12: "新生儿专科门诊诊区", 13: "感染管理科诊区"}

for i in range(1, 14):
    max_id = max_id + 1
    # print(i)
    clinic_type_data = {0: '门诊', 1: '急诊', 2: '住院', 3: '其他'}
    clinic_type_code = random.choice([0, 3])
    clinic_type_name = clinic_type_data[clinic_type_code]

    room_status_data = {0: '未开诊', 1: '开诊'}
    room_status_code = random.choice([0, 1])
    room_status_name = room_status_data[room_status_code]

    clinic_days = 0.5

    clinic_ward_id = i
    clinic_ward_code = str(i)
    clinic_ward_name = clinic_ward_data[clinic_ward_id]

    # 指定日期 转换
    data = random.randint(2, 2)
    get_time = '2021-09-0{0} 08:00:00.000000'.format(data)
    # get_time = '2021-08-{0} 16:00:00.000000'.format(data)
    now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')

    # 时间统一用
    # now_time = datetime.now()

    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-8,4)
    hours_data = round(random.uniform(-0.5, 0.5), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset
    utc_time = local_to_utc(real_time)

    # print('now_time: {0}\nreal_time: {2}\nutc_time: {1} '.format(now_time,real_time, utc_time))

    update_time = local_to_utc(real_time)

    compare_time = '2021-09-0{0} 12:00:00.000000'.format(data)
    compare_time_new = datetime.strptime(compare_time, '%Y-%m-%d %H:%M:%S.%f')

    # print(now_time, real_time, compare_time_new)
    if real_time <= compare_time_new:
        # 上午
        visit_data = {'1001': ['诊室一', '7001', '何运浩', 10, '儿科普通门诊', 'tj_his3', 1, '主治医师', 0, '专科'],
                      "1002": ['诊室二', '7002', '陈鸿德', 198, '耳鼻喉科主任门诊', 'tj_his3', 2, '主任医师', 1, '专病'],
                      "1003": ['诊室三', '7003', '孙德运', 325, '普外科门诊', 'tj_his3', 3, '高级工程师', 0, '专科'],
                      "1004": ['诊室四', '7005', '杨朗', 117, '心电图室', 'Oa', 4, '助理研究员', 1, '专病'],
                      "1005": ['诊室五', '7006', '吕轩', 89, '血液内科', 'Oa', 1, '主治医师', 0, '专科'],
                      "1006": ['诊室六', '7013', '尤彦昌', 102, '影像科(MRI)', 'Oa', 5, '副主任技师', 2, '普病']}
        time_scope_data = [0, '上午', ' 08:00:00', ' 08:05:00', ' 12:00:00']

    elif real_time > compare_time_new:
        # 下午
        visit_data = {'1001': ['诊室一', '7001', '何运浩', 10, '儿科普通门诊', 'tj_his3', 1, '主治医师', 0, '专科'],
                      "1002": ['诊室二', '7022', '赵清杰', 107, '手足外科', 'tj_his3', 1, '主治医师', 0, '专科'],
                      "1003": ['诊室三', '7003', '孙德运', 325, '普外科门诊', 'tj_his3', 1, '主治医师', 0, '专科'],
                      "1004": ['诊室四', '7016', '朱运凯', 388, '神经内科（二）', 'Oa', 1, '主治医师', 0, '专科'],
                      "1005": ['诊室五', '7006', '吕轩', 389, '神经内科（一）', 'Oa', 1, '主治医师', 0, '专科'],
                      "1006": ['诊室六', '7019', '李浩宕', 172, '放疗门诊', 'tj_his3', 1, '主治医师', 0, '专科'],
                      "1007": ['诊室七', '8019', '晨小小', 172, '放疗门诊', 'tj_his3', 1, '主治医师', 0, '专科']
                      }

        time_scope_data = [1, '下午', ' 13:00:00', ' 13:05:00', ' 16:30:00']

    # clinic_room_code = random.choice(["1001", "1002", "1003", "1004", "1005", "1006"])
    clinic_room_code = str(1006)
    clinic_room_name = visit_data[clinic_room_code][0]
    doc_code = visit_data[clinic_room_code][1]
    doc_name = visit_data[clinic_room_code][2]
    dept_id = visit_data[clinic_room_code][3]
    dept_name = visit_data[clinic_room_code][4]
    source_app = visit_data[clinic_room_code][5]
    doc_title_id = visit_data[clinic_room_code][6]
    doc_title_code = visit_data[clinic_room_code][6]
    doc_title_name = visit_data[clinic_room_code][7]
    room_type_code = visit_data[clinic_room_code][8]
    room_type_name = visit_data[clinic_room_code][9]

    data_new_time = datetime.strftime(real_time, '%Y-%m-%d')
    time_scope_code = time_scope_data[0]
    time_scope_name = time_scope_data[1]

    begin_service_time_1 = data_new_time + time_scope_data[2] + '.000000'
    begin_service_time = str(
        local_to_utc(datetime.strptime(begin_service_time_1, '%Y-%m-%d %H:%M:%S.%f'))) + '.000000'
    # print(begin_service_time)
    first_input_time_1 = data_new_time + time_scope_data[3] + '.000000'
    first_input_time = str(local_to_utc(datetime.strptime(first_input_time_1, '%Y-%m-%d %H:%M:%S.%f'))) + '.000000'

    end_service_time_1 = data_new_time + time_scope_data[4] + '.000000'
    end_service_time = str(local_to_utc(datetime.strptime(end_service_time_1, '%Y-%m-%d %H:%M:%S.%f'))) + '.000000'

    sql_3 = '''
   INSERT INTO source.outpatient_doc (id, doc_code, doc_name, dept_code, dept_name, check_in_time, clinic_type_code,
                               clinic_type_name, source_app, clinic_ward_code, clinic_ward_name, clinic_room_code,
                               clinic_room_name, room_type_code, room_type_name, room_status_code, room_status_name,
                               doc_id, doc_title_id, doc_title_code, doc_title_name, dept_id, begin_service_time,
                               first_input_time, end_service_time, time_scope_code, time_scope_name, clinic_days,
                               str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, statis_time)
VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{23}', {24}, '{25}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}',
    '{11}', {12}, '{13}', {1}, {14}, '{15}', '{16}', {3}, '{20}', '{21}', '{22}', {17}, '{18}', {19}, null, null, null, null,
    null, null, null, null, null, null,'{23}');

    '''.format(max_id, doc_code, doc_name, dept_id, dept_name, source_app, clinic_ward_code, clinic_ward_name,
               clinic_room_code,
               clinic_room_name, room_type_code, room_type_name, room_status_code, room_status_name, doc_title_id,
               doc_title_code, doc_title_name, time_scope_code, time_scope_name, clinic_days, begin_service_time,
               first_input_time, end_service_time, update_time, clinic_type_code,
               clinic_type_name)
    mysql1.insert(sql_3)
    print(i)
