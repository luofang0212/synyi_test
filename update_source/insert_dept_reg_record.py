#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb
from util.dbPlsql_util_bi import PlSqlDbBI
import random
import time, datetime
from update_source.get_data import GetData

# 挂号主题 topic=1
mysql1 = PlSqlDbBI()
sql_1 = '''select max(visit_id) from source.reg_record;'''
res_1 = mysql1.query(sql_1)

max_visit_id = res_1[0][0] + 5
print(max_visit_id)

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

for i in range(1, 1210):
    max_visit_id = max_visit_id + 1
    res_2 = mysql.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]
    total_cost = random.randint(200000, 730000)
    patient_type_id = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    pay_kind_code = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    visit_type_code = random.choice(['I', 'O', 'E', 'P'])

    clinic_level = random.choice([1, 2, 3, 4, 5])
    if clinic_level == 1:
        clinic_level_name = "外院西医普诊"
    else:
        clinic_level_name = "西医普诊"

    major_diag_name = random.choice(["健康查体","疑似新冠"])

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

    # now_time = datetime.datetime.now()
    data = random.randint(15, 16)
    now_time = '2021-08-' + str(data)
    # now_time = '2021-' + str(data) + '-02'
    # now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    data_hourse = random.randint(0, 24)
    if 0 <= data_hourse <= 9:
        update_time = str(now_time) + ' 0' + str(data_hourse) + ':00:00.000000'
    elif 9 < data_hourse <= 24:
        update_time = str(now_time) + ' ' + str(data_hourse) + ':00:00.000000'

    settle_data = random.randint(15, 16)
    settle_time = '2021-08-' + str(data)
    # settle_time = '2021-' + str(data) + '-02'
    # now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    settle_hourse = random.randint(0, 24)
    if 0 <= settle_hourse <= 9:
        settle_time = str(settle_time) + ' 0' + str(settle_hourse) + ':00:00.000000'
    elif 9 < settle_hourse <= 24:
        settle_time = str(settle_time) + ' ' + str(settle_hourse) + ':00:00.000000'


    age_group_code = random.choice(['18-41', '0-7', '>65', '41-65', '7-18'])
    if age_group_code == '0-7':
        age_group_name = '0岁-7岁'
    elif age_group_code == '7-18':
        age_group_name = '7岁-18岁'
    elif age_group_code == '18-41':
        age_group_name = '18岁-41岁'
    elif age_group_code == '41-65':
        age_group_name = '41岁-65岁'
    elif age_group_code == '>65':
        age_group_name = '>65岁'

    book_way_code = random.choice(['A', 'Z', '1', '0', 'D'])
    if book_way_code == 'A':
        book_way_id = 4894
        book_way_name = '窗口挂号'
    elif book_way_code == 'Z':
        book_way_id = 4895
        book_way_name = '自助机'
    elif book_way_code == '1':
        book_way_id = 49549
        book_way_name = '预约挂号'
    elif book_way_code == '0':
        book_way_id = 49548
        book_way_name = '现场挂号'
    elif book_way_code == 'D':
        book_way_id = 4893
        book_way_name = '网上预约'
    patient_name = '刘三' + random.choice(['A', 'Z', 'B', 'E', 'D']) + str(random.randint(1, 100))

    # now_time = '2021-07-21 09:33:55.000000'

    sql_3 = '''
        insert into source.reg_record (visit_id, org_code, source_app, source_visit_id, source_patient_id, patient_name, sex_id,
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
                               call_time, book_flag)
values ({0}, '46919134-2', '{1}', '20880|20190618', 03110588, '{14}', 24, '女性', 42, '岁', 15343, {5}, '市医保',
        4603, '医保', '***', '中国', '香港特别行政区', null, null, null, null, {11}, '{12}', null, null, null, '上午',
        '{8}', 4619, '普通号', 4619, '{15}', 0, '门诊', '{17}', 103, '内科门诊', {2}, '{3}', {18}, '{19}',
        4548, '副主任医师', 5627, '就诊', 1, null, 10.0000, 10.0000, {4}, '{16}', 0, 0, 0, null,
        null, null, null, 0.0000, null, null, 2107, '自助001', 221, '门诊收费处', null, 2, 10, {6}, null, '{13}', null, 13, 3, 551,
        '{7}', null, 0307, 9029, 212, 2, 9121, 01030002, 96217, '{9}', '{10}', null, '门诊医生|0307', '内科门诊', null, null,
        10.0000, 300337122, 25, '消化科', null, null, null, null, null, null, null, null, null, null, null, null, 0, '普通',
        '{8}', null);
        '''.format(max_visit_id, source_app, dept_id, dept_name, total_cost, patient_type_id, pay_kind_code,
                   visit_type_code, update_time, age_group_code, age_group_name, book_way_id, book_way_name,
                   book_way_code, patient_name, clinic_level_name,settle_time,major_diag_name,doc_id,doc_name)
    mysql1.insert(sql_3)
    print(i)
