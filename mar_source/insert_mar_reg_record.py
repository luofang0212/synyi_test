#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mar_source.dbPlsql_util_mar import PLSqlMar
from mar_source.dbPlsql_util_system import PLSqlMarSystem
from mar_source.get_data import GetData
import random
import time, datetime

# 挂号主题
mar_sql = PLSqlMar()
system_sql = PLSqlMarSystem()

sql_1 = '''select max(visit_id) from source.reg_record;'''
res_1 = mar_sql.query(sql_1)
max_visit_id = res_1[0][0] + 1

dept_data = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''

dept_res = system_sql.query(dept_data)
print("科室总数量：{0}".format(len(dept_res)))

org_code_data = '''select org_code,org_name from system.organization;'''
org_code_res = system_sql.query(org_code_data)
print("机构总数量：{0}".format(len(org_code_res)))

for i in range(1, 274):
    max_visit_id = max_visit_id + 1

    dept_res = system_sql.query(dept_data)
    dept_id = dept_res[i][0]
    dept_name = dept_res[i][1]
    source_app = dept_res[i][4]

    org_code_res = system_sql.query(org_code_data)
    org_code = org_code_res[i][0]
    org_name = org_code_res[i][1]

    total_cost = random.randint(200000, 730000)
    patient_type_id = random.choice(GetData.patient_type_id)
    pay_kind_code = random.choice(GetData.pay_kind_code)

    visit_type_data = {'I': '住院', 'O': '门诊', 'E': '体检', 'P': '急诊'}
    visit_type_code = random.choice(['O', 'E', 'I', 'P'])
    visit_type = visit_type_data[visit_type_code]

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name

    source_patient_id = '202109' + str(random.randint(1, 250))

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

    # now_time = datetime.datetime.now()
    now_time = '2021-01-21'
    # now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    data_hourse = random.randint(0, 24)
    if 0 <= data_hourse <= 9:
        update_time = str(now_time) + ' 0' + str(data_hourse) + ':00:00.000000'
    elif 9 < data_hourse <= 24:
        update_time = str(now_time) + ' ' + str(data_hourse) + ':00:00.000000'

    age_group_code = random.choice(['18-41', '0-7', '>65', '41-65', '7-18'])
    age_group_data = {'0-7': '0岁-7岁', '7-18': '7岁-18岁', '18-41': '18岁-41岁', '41-65': '41岁-65岁', '>65': '>65岁'}
    age_group_name = age_group_data[age_group_code]

    pay_kind = random.choice(['医保','自费'])
    pay_kind_name = pay_kind + str(random.randint(100, 700))

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

    # now_time = '2021-07-21 09:33:55.000000'

    sql_3 = '''
       INSERT INTO source.reg_record (visit_id, org_code, source_app, source_visit_id, source_patient_id, patient_name, sex_id,
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
                               call_time, book_flag, org_name)
VALUES ({0}, '{4}', '{1}', '6066117', '{11}', '{10}', 24, '女性', 84, '岁', 30804, {20}, '自费7769', 7,
        '{19}', null, '中国', '浙江省', '金华市', null, null, null, {8}, '{9}', null, null, null, '上午',
        '{15}', 4622, '普通号', 4622, '外院中医普诊', '{16}', '{17}', '非疑似新冠', 99, '中医内科', {2}, '{3}', {12}, '{13}',
        4547, '主任医师', 5627, '就诊', 1, null, 12.0000, 12.0000, {14}, '{15}', 1, 0, 1, null, 0,
        null, null, 22.0000, null, null, 1338, '徐唱', {2}, '{3}', 295.0800, '2', '0', '{21}', null, '{7}', null, '13', '7',
        551, 'O', null, '0303', '10117', '211', '2', '64531', '01030002', 96218, '{18}', '{6}', null, '门诊医生|0303', '中医内科',
        null, null, 392.3000, 304069049, 31, '中医科', null, null, null, null, null, null, null, null, null, null, null,
        null, 0, '类型0', null, null, '{5}');
        '''.format(max_visit_id, source_app, dept_id, dept_name, org_code, org_name, age_group_name,
                   book_way_code, book_way_id, book_way_name, patient_name, source_patient_id, doc_id, doc_name,
                   total_cost, update_time, visit_type_code, visit_type,age_group_code,pay_kind_name,patient_type_id,pay_kind_code)
    mar_sql.insert(sql_3)
    print(i)
