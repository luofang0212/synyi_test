#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mar_source.dbPlsql_util_mar import PLSqlMar
from mar_source.dbPlsql_util_system import PLSqlMarSystem
from mar_source.get_data import GetData
import random
from datetime import datetime,timedelta

# 收入主题
mar_sql = PLSqlMar()
system_sql = PLSqlMarSystem()

sql_1 = '''select max(fee_detail_id) from source.fee_detail;'''
res_1 = mar_sql.query(sql_1)
max_fee_detail_id= res_1[0][0] + 1

dept_data = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''
dept_res = system_sql.query(dept_data)
print("科室总数量：{0}".format(len(dept_res)))

org_code_data = '''select org_code,org_name from system.organization;'''
org_code_res = system_sql.query(org_code_data)
print("机构总数量：{0}".format(len(org_code_res)))

for i in range(1, 1210):
    max_fee_detail_id = max_fee_detail_id + 1
    res_2 = system_sql.query(dept_data)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]

    org_code_res = system_sql.query(org_code_data)
    org_code = org_code_res[i][0]
    org_name = org_code_res[i][1]

    total_cost = random.randint(10000, 200000)
    source_fee_detail_id = '020|3|2042|' + str(random.randint(1, 20000)) + str(i)
    patient_type_id = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    pay_kind_code = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    # visit_type_code = 'O'

    visit_type_data = {'I': '住院', 'O': '门诊', 'E': '体检', 'P': '急诊'}
    visit_type_code = random.choice(['O', 'E', 'I', 'P'])
    visit_type = visit_type_data[visit_type_code]

    adjust_sub_class_code = random.choice(['135152', '135148', '135149', '135169', '135147', '135168'])

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

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

    sql_3 = '''
    insert into source.fee_detail (fee_detail_id, org_code, source_app, source_fee_detail_id, source_visit_id,
                               source_patient_id, patient_name, patient_type_id, patient_type_name, pay_kind_id,
                               pay_kind_name, visit_type, order_type_id, order_type_name, recipe_id, order_item_id,
                               item_name, usage_id, usage_name, unit, unit_price, qty, total_cost, dept_group_id,
                               dept_group_name, dept_id, dept_name, ward_id, ward_name, bed_name, doc_id, doc_name,
                               input_dept_id, input_dept_name, input_doc_id, input_doc_name, input_dept_group_id,
                               input_dept_group_name, exec_dept_id, exec_dept_name, exec_oper_id, exec_oper_name,
                               exec_dept_group_id, exec_dept_group_name, order_time, bill_time, settle_time,
                               accrual_basis_time, order_sub_class_id, order_sub_class_name, fee_sub_class_id,
                               fee_sub_class_name, invoice_class_id, invoice_class_name, invoice_sub_class_id,
                               invoice_sub_class_name, phar_class_id, phar_class_name, phar_sub_class_id,
                               phar_sub_class_name, accounting_sub_class_id, accounting_sub_class_name,
                               adjust_sub_class_id, adjust_sub_class_name, outpat_sub_class_id, outpat_sub_class_name,
                               inpat_sub_class_id, inpat_sub_class_name, mr_sub_class_id, mr_sub_class_name,
                               dose_model_id, dose_model_name, charge_oper_id, charge_oper_name, bed_id,
                               patient_type_code, pay_kind_code, visit_type_id, visit_type_code, order_type_code,
                               usage_code, dept_code, ward_code, bed_code, doc_code, input_dept_code, input_doc_code,
                               exec_dept_code, exec_oper_code, antibac_flag, adjust_sub_class_code, dose_model_code,
                               charge_oper_code, reg_level_code, reg_level_name, reg_time, medical_group_code,
                               medical_group_name, regular_name, oper_flag_code, oper_flag_name, patient_id,
                               normalized_dept_id, normalized_dept_name, normalized_input_dept_id,
                               normalized_input_dept_name, normalized_exec_dept_id, normalized_exec_dept_name, str1,
                               str2, str3, str4, str5, str6, str7, str8, str9, str10,org_name)
values ({0}, '{15}', '{1}', '{5}', '03246163|4', 03246163, '{12}', {6}, '电子现金', 7, '电子现金', '{11}',
        null, null, null, null, '奥曲肽注射液(0.2mg)', null, null, null, 59.1800, 2.0000, {4}, null, null, 257, '感染病区',
        null, null, 77, {13}, '{14}', {2}, '{3}', {13}, '{14}', 257, '感染病区', 242, '病区药房', {13}, '{14}', 235, '药剂科', null,
        '{10}', '{10}', null, 4629, '西药', 4629, '西药', null, null, null,
        null, null, null, null, null, 135101, '西药费', 135149, '西药费', null, null, 135031, '西药费', 135216, '西药', null, null,
        null, null, 1014, 7, {8}, 552, '{7}', null, null, 0201, null, 77, 0183, 0201, 0183, 01070208, 0183, 0, {9}, null,
        0426, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null,'{16}');

        '''.format(max_fee_detail_id, source_app, dept_id, dept_name, total_cost, source_fee_detail_id, patient_type_id,
                   visit_type_code, pay_kind_code, adjust_sub_class_code, update_time, visit_type, patient_name, doc_id,
                   doc_name, org_code, org_name)

    mar_sql.insert(sql_3)
    print(i)
