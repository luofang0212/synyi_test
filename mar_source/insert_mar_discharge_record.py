#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mar_source.dbPlsql_util_mar import PLSqlMar
from mar_source.dbPlsql_util_system import PLSqlMarSystem
from mar_source.get_data import GetData
import random
from datetime import datetime,timedelta


# 住院主题
mar_sql = PLSqlMar()
system_sql = PLSqlMarSystem()

sql_1 = '''select max(visit_id) from source.discharge_record;'''
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
    res_2 = system_sql.query(dept_data)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]

    org_code_res = system_sql.query(org_code_data)
    org_code = org_code_res[i][0]
    org_name = org_code_res[i][1]

    pay_cost = random.randint(1300000, 6030000)
    in_total_cost = random.randint(10000, 130000)
    patient_type_id = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    in_days = random.choice([3.0000, 5.0000, 7.0000, 10.0000, 11.0000, 15.0000])
    pay_kind_code = random.choice([1, 2, 3, 4, 5, 6, 7, 8])

    visit_type_data = {'I': '住院', 'O': '门诊', 'E': '体检', 'P': '急诊'}
    visit_type_code = random.choice(['I', 'O', 'E', 'P'])
    visit_type = visit_type_data[visit_type_code]

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name=doc_data[doc_id]


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
   insert into source.discharge_record (visit_id, org_code, source_app, source_visit_id, source_patient_id, patient_name,
                                      visit_type, in_time, in_dept_id, in_dept_name, in_ward_id, in_ward_name,
                                      bed_doc_id, bed_doc_name, out_time, out_dept_id, out_dept_name, out_ward_id,
                                      out_ward_name, out_bed_id, out_bed_name, patient_type_id, patient_type_name,
                                      pay_kind_id, pay_kind_name, in_num, in_days, in_total_cost, drug_cost, drug_kinds,
                                      antibac_kinds, antibac_flag, antibac_cost, ddd_value, spe_ddd_value,
                                      basic_drug_flag, spe_antibac_flag, injection_flag, inject_usage_flag,
                                      injection_cost, infusion_flag, oral_drug_flag, oral_drug_cost, i_incision_flag,
                                      preoper_antibio_flag, preoper_2h_antibio_flag, postoper_antibio_flag,
                                      preven_antibio_flag, treat_antibio_flag, eti_flag, treat_eti_flag,
                                      treat_res_antibac_eti_flag, treat_spe_antibac_eti_flag, treat_res_antibac_flag,
                                      treat_spe_antibac_flag, antibac_union_flag, material_cost, check_cost, lab_cost,
                                      treat_cost, major_diag, critical_flag, serious_flag, is_rescue, outcome_id,
                                      outcome_name, preoper_days, inten_presons, inten_days, create_id, create_name,
                                      create_time, in_dept_group_id, in_dept_group_name, out_dept_group_id,
                                      out_dept_group_name, country, province, city, district, disease_name, disease_id,
                                      visit_type_id, visit_type_code, in_dept_code, out_dept_code, patient_type_code,
                                      pay_kind_code, in_diag_id, in_diag_code, in_diag_name, out_diag_id, out_diag_code,
                                      out_diag_name, major_diag_id, major_diag_code, outcome_code, settle_time,
                                      medical_group_code, medical_group_name, presc_com_flag, oper_flag_code, pub_cost,
                                      own_cost, pay_cost, oper_flag_name, patient_id, normalized_in_dept_id,
                                      normalized_in_dept_name, normalized_out_dept_id, normalized_out_dept_name, str1,
                                      str2, str3, str4, str5, str6, str7, str8, str9, str10, dept_type_code,
                                      dept_type_name,org_name)
values ({0}, '{14}', '{1}', 10159817, 3577370, '{11}', '{10}', '{9}', null, '胃肠外科住院', 86, '观察病房',
        {12}, '{13}', '{9}', {2}, '{3}', 22, '观察病房', 393, 811421, {6}, '深圳医保7157', 49509, '深圳医保7157', 1, {8},
        {16}, 619.1000, 1, 1, 1, 28.2200, null, null, 0, null, 1, 1, 65.6400, 0, 1, 0.5700, null, null, null, null,
        null, null, null, null, null, null, null, null, null, 557.3600, 421.0000, 1284.0000, 61.2000, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, '中国', '广东省', '深圳市', null, null,
        null, null, '{7}', 1050, 1050, 5, {5}, null, null, '慢性阑尾炎', null, null, null, null, null, null,
        '{9}', null, null, null, null, 0.0000, 7084.1600, {4}, null, 903879, null, null, null, null,
        'AK3022915', null, null, null, null, null, null, null, null, null, 0, '类型1','{15}');

        '''.format(max_visit_id, source_app, dept_id, dept_name, pay_cost, pay_kind_code, patient_type_id,
                   visit_type_code, in_days, update_time,visit_type,patient_name,doc_id,doc_name,org_code,org_name,in_total_cost)
    mar_sql.insert(sql_3)
    print(i)
