#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb
from util.dbPlsql_util_bi import PlSqlDbBI
import random
import time
from update_source.get_data import GetData
from datetime import datetime, timedelta
from util.time_utc import *

# 挂号主题 topic=1
mysql1 = PlSqlDbBI()
sql_1 = '''select max(visit_id) from data.pg_reg_record;'''
res_1 = mysql1.query(sql_1)

max_visit_id = res_1[0][0] + 1
# max_visit_id = 1
print(max_visit_id)

mysql = PlSqlDb()

sql_2 = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''

res_2 = mysql.query(sql_2)

print(len(res_2))

for i in range(1, 400):
    max_visit_id = max_visit_id + 1
    res_2 = mysql.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]

    total_cost = random.randint(200000, 730000)
    patient_type_id = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    pay_kind_code = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    visit_type_code = random.choice(['I', 'O', 'E', 'P'])

    clinic_level_data = {1:'外院西医普诊',2:'西医普诊',3:'中医普诊',4:'中医专诊',5:'内院中医专诊'}
    clinic_level_code = random.choice([1, 2, 3, 4, 5])
    clinic_level_name = clinic_level_data[clinic_level_code]


    major_diag_name = random.choice(["健康查体", "疑似新冠"])

    age_group_code = random.choice(['18-40', '0-7', '>65', '41-65', '7-18'])
    # age_group_code = random.choice(['18-41', '0-7', '>65', '41-65'])
    age_group_data = {'0-7': '0岁-7岁', '7-18': '7岁-18岁', '18-40': '18岁-41岁', '41-65': '41岁-65岁', '>65': '>65岁'}
    age_group_name = age_group_data[age_group_code]

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name

    # 0:未预约 1:预约
    book_flag = random.choice([0, 1, 1, 1, 0, 1])

    # 0: 未拿号 1: 候诊 2: 就诊 3:就诊完成
    visit_state_data = {0: ["0", "未拿号"], 1: ["1", "候诊"], 2: ["2", "就诊"], 3: ["3", "就诊完成"]}
    visit_state_id = random.choice([0, 1, 2, 3])
    visit_state_code = visit_state_data[visit_state_id][0]
    visit_state_name = visit_state_data[visit_state_id][1]

    # 诊区
    visit_ward_data = {1: "血液净化中心诊区", 2: "中医内科诊区", 3: "内分泌科诊区", 4: "中医内科诊区", 5: "皮肤科诊区", 6: "急诊外科诊区", 7: "耳鼻喉科诊区",
                       8: "儿科病区诊区", 9: "产科门诊诊区", 10: "神经外科诊区", 11: "口腔科诊区", 12: "新生儿专科门诊诊区", 13: "感染管理科诊区"}
    visit_ward_id = random.randint(1, 13)
    visit_ward_code = str(visit_ward_id)
    visit_ward_name = visit_ward_data[visit_ward_id]

    book_way_data = {'A': [4894, "窗口挂号"], 'Z': [4895, "自助机"], '1': [49549, "预约挂号"], '0': [49548, "现场挂号"],
                     'D': [4893, "网上预约"], }
    book_way_code = random.choice(['A', 'Z', '1', '0', 'D'])
    book_way_id = book_way_data[book_way_code][0]
    book_way_name = book_way_data[book_way_code][1]

    # 指定日期 转换
    data = random.randint(1, 9)
    get_time = '2021-{0}-10 08:00:00.000000'.format(data)
    now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')


    # now_time = datetime.now()
    # 根据当前时间 去计算偏移时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-2, 14), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset

    call_time = local_to_utc(real_time)
    call_time_bak = real_time

    hours_data_2 = round(random.uniform(0, 0.15), 2)
    offset_2 = timedelta(hours=hours_data_2)

    hours_data_3 = round(random.uniform(0, 0.2), 2)
    offset_3 = timedelta(hours=hours_data_3)

    arrive_time = local_to_utc(call_time_bak - offset_3)

    end_time = local_to_utc(call_time_bak + offset_2)

    compare_time = '2021-{0}-10 12:00:00.000000'.format(data)
    compare_time_new = datetime.strptime(compare_time, '%Y-%m-%d %H:%M:%S.%f')

    # print(now_time, real_time, compare_time_new)
    if real_time <= compare_time_new:
        visit_data = {'1001': ['诊室一', '7001', '何运浩'], "1002": ['诊室二', '7002', '陈鸿德'], "1003": ['诊室三', '7003', '孙德运'],
                      "1004": ['诊室四', '7005', '杨朗'],
                      "1005": ['诊室五', '7006', '吕轩'], "1006": ['诊室六', '7013', '尤彦昌']}
    elif real_time > compare_time_new:
        visit_data = {'1001': ['诊室一', '7001', '何运浩'], "1002": ['诊室二', '7022', '赵清杰'], "1003": ['诊室三', '7003', '孙德运'],
                      "1004": ['诊室四', '7016', '朱运凯'],
                      "1005": ['诊室五', '7006', '吕轩'], "1006": ['诊室六', '7019', '李浩宕'], "1007": ['诊室七', '8019', '晨小小']}

    visit_room_code = random.choice(["1001", "1002", "1003", "1004", "1005", "1006"])
    visit_room_name = visit_data[visit_room_code][0]
    doc_code = visit_data[visit_room_code][1]
    doc_name = visit_data[visit_room_code][2]

    sql_3 = '''
        insert into data.pg_reg_record(visit_id, org_code, source_app, source_visit_id, source_patient_id, patient_name, sex_id,
                               sex_name, age, age_unit, age_day, patient_type_id, patient_type_name, pay_kind_id,
                               pay_kind_name, address, country, province, city, district, profession_id,
                               profession_name, book_way_id, book_way_name, arrive_situation_id, arrive_situation_name,
                               holiday_service, time_scope, reg_time, reg_level_id, reg_level_name, clinic_level_id,
                               clinic_level_name, is_again, visit_type, major_diag_name, dept_group_id, dept_group_name,
                               dept_id, dept_name, doc_id, doc_name, doc_title_id, doc_title_name, visit_state_id,
                               visit_state_name, reg_num, reg_cost, reg_diag_cost, reg_total_cost, total_cost,
                               settle_time, west_medicine_flag, cnmedicine_flag, herb_flag, tcm_non_drug_flag,
                               antibac_flag, injection_flag, infusion_flag, drug_kinds, observation_flag,
                               transfer_inpat_flag, oper_id, oper_name, oper_dept_id, oper_dept_name, drug_cost,
                               sex_code, patient_type_code, pay_kind_code, profession_code, book_way_code,
                               arrive_situation_code, reg_level_code, clinic_level_code, visit_type_id, visit_type_code,
                               dept_group_code, dept_code, doc_code, doc_title_code, visit_state_code, oper_code,
                               oper_dept_code, age_group_id, age_group_code, age_group_name, basic_drug_kinds,
                               medical_group_code, medical_group_name, pub_cost, own_cost, pay_cost, patient_id,
                               normalized_dept_id, normalized_dept_name, major_diag_code, referral_flag, str1, str2,
                               str3, str4, str5, str6, str7, str8, str9, str10, dept_type_code, dept_type_name,
                               call_time, book_flag,arrive_time, end_time, visit_ward_code, visit_ward_name,
                               visit_room_code, visit_room_name)
values ({0}, '46919134-2', '{1}', '20880|20190618', 03110588, '{14}', 24, '女性', 42, '岁', 15343, {5}, '市医保',
        4603, '医保', '***', '中国', '香港特别行政区', null, null, null, null, {11}, '{12}', null, null, null, '上午',
        '{8}', 4619, '普通号', 4619, '{15}', 0, '门诊', '{17}', 103, '内科门诊', {2}, '{3}', {18}, '{19}',
        4548, '副主任医师', {21}, '{23}', 1, null, 10.0000, 10.0000, {4}, '{16}', 0, 0, 0, null,
        null, null, null, 0.0000, null, null, 2107, '自助001', 221, '门诊收费处', null, 2, 10, {6}, null, '{13}', null, 13, {29}, 551,
        '{7}', null, 0307, '{18}', 212, {22}, 9121, 01030002, 96217, '{9}', '{10}', null, '门诊医生|0307', '内科门诊', null, null,
        10.0000, 300337122, 25, '消化科', null, null, null, null, null, null, null, null, null, null, null, null, 0, '普通',
        '{8}', {20}, '{16}', '{26}', '{27}', '{28}', '{24}', '{25}');
        '''.format(max_visit_id, source_app, dept_id, dept_name, total_cost, patient_type_id, pay_kind_code,
                   visit_type_code, call_time, age_group_code, age_group_name, book_way_id, book_way_name,
                   book_way_code, patient_name, clinic_level_name, arrive_time, major_diag_name, doc_code, doc_name,
                   book_flag, visit_state_id, visit_state_code, visit_state_name, visit_room_code, visit_room_name,
                   end_time, visit_ward_code, visit_ward_name,clinic_level_code)
    mysql1.insert(sql_3)
    print(i)
