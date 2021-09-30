#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_bi import PlSqlDbBI
from util.dbPlsql_util_system import PlSqlDb
import random
from datetime import datetime, timedelta
from update_source.get_data import GetData

mysql_bi = PlSqlDbBI()
sql_1 = '''select max(id),max(out_date_id),max(case_id) from source.std_dwd_pay_case_group;'''
res_1 = mysql_bi.query(sql_1)

max_id = res_1[0][0] + 1
out_date_id = res_1[0][1] + 1
case_id = int(res_1[0][2]) + 1
# max_id =  1
# out_date_id =  1

mysql_2 = PlSqlDb()

sql_2 = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''
res_2 = mysql_2.query(sql_2)

print(len(res_2))
# print(res_2)

drgs_sql = '''select in_diag_name,in_diag_code  from source.case_base where in_diag_name is not null  group by in_diag_name,in_diag_code;'''
drgs_data = mysql_bi.query(drgs_sql)
print(len(drgs_data))

for i in range(1, 1209):
    max_id = max_id + 1
    out_date_id = out_date_id + 1
    case_id = case_id + 1
    res_2 = mysql_2.query(sql_2)

    n = random.randint(1,30)
    out_dept_code=res_2[n][0]
    out_dept_name=res_2[n][1]

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

    diag_code_group = round(random.uniform(1, 20), 2)

    doc_title_data = {1: '副主治医生', 2: '主任医生', 3: '高级医生', 4: '助理医生', 5: '副主任护士', 6: '副主任中药护士', 7: '副主任护士', 8: '中药医生',
                      9: '护士', 10: '主治医生'}
    doc_title_id = random.randint(1, 10)
    doc_title_code = doc_title_id
    doc_title_name = doc_title_data[doc_title_id]

    dept_data = {1: '感染管理科', 2: '儿科', 3: '鼻科', 4: '妇产科', 5: '孕妇科', 6: '普外科', 7: '血液科', 8: '急诊', 9: '感染性疾病',
                 10: '重症医学', 11: '中医', 12: '麻醉', 13: '康复'}
    dept_code = random.randint(1, 13)
    dept_name = dept_data[dept_code]

    bed_data = random.randint(1, 49)
    bed_num = random.randint(50, 200)
    actual_open_beds = bed_num - bed_data
    actual_used_beds = bed_num - actual_open_beds
    extra_beds = random.randint(0, 50)

    out_way_name = random.choice(['死亡', '危重', '正常'])
    risk_level = random.choice(['中高风险', '中风险', '高风险', '低风险','中低风险'])

    in_days = random.randint(1, 50)
    in_total_cost = random.randint(1000, 250000)
    medicine_cost = random.randint(1000, 250000)
    west_medicine_cost = random.randint(1000, 250000)
    cnmedicine_cost = random.randint(1000, 250000)
    cnmedicine_herbs_cost = random.randint(1000, 250000)
    material_cost = random.randint(1000, 250000)
    material_check_cost = random.randint(1000, 250000)
    material_treat_cost = random.randint(1000, 250000)
    material_operation_cost = random.randint(1000, 250000)
    ralated_weight = round(random.uniform(0, 1), 3)
    in_num = random.randint(1, 50)
    days_rate =  round(random.uniform(0, 0.01), 2)
    cost_rate = round(random.uniform(0, 0.01), 2)

    m = random.randint(1,50)
    drgs_name = drgs_data[m][0]
    drgs_id = random.randint(1,1000)

    # 指定日期 转换
    data = random.randint(1, 12)
    get_time = '2020-{0}-16 08:00:00.000000'.format(data)
    now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')

    # # 时间统一用
    # now_time = datetime.now()
    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-10, 14), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset

    update_time = real_time

    sql_3 = '''
    INSERT INTO source.std_dwd_pay_case_group (id, out_date_id, out_date, case_id, in_num, patient_id, patient_code,
                                            patient_name, patient_age, gendor_code, gendor_name, in_date, out_way_code,
                                            out_way_name, org_id, org_code, org_name, hosp_area_id, hosp_area_code,
                                            hosp_area_name, out_dept_id, out_dept_code, out_dept_name, out_main_diag_id,
                                            out_main_diag_code, out_main_diag_name, out_main_oper_id,
                                            out_main_oper_code, out_main_oper_name, doctor_id, doctor_code, doctor_name,
                                            in_days, in_total_cost, medicine_cost, west_medicine_cost, cnmedicine_cost,
                                            cnmedicine_herbs_cost, material_cost, material_check_cost,
                                            material_treat_cost, material_operation_cost, drgs_version, drgs_id,
                                            drgs_code, drgs_name, ralated_weight, cost_rate, risk_level, etl_time1,
                                            update_time, days_rate)
VALUES ({0}, {1}, '{2}', '{23}', {18}, 5185, 3372, '徐謩', 20, '2', '女', '{2}', '1', '{3}',
        6168, '46919132', '森亿国际机构', 3, '1', '东院区', {20}, '{20}', '{21}', 1, '4', '测试出院诊断', 4, '4', '测试手术操作', 4786,
        '9893', '郑薪', {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13},
           {14}, 'CHS_DRG', {22}, '{15}', '{15}', {16}, {19}, '{4}', '{2}', '{2}',{17});
        '''.format(max_id, out_date_id, update_time, out_way_name, risk_level, in_days, in_total_cost, medicine_cost,
                   west_medicine_cost, cnmedicine_cost, cnmedicine_herbs_cost, material_cost, material_check_cost,
                   material_treat_cost, material_operation_cost, drgs_name,ralated_weight,days_rate,in_num,cost_rate,out_dept_code, out_dept_name,drgs_id,case_id)

    mysql_bi.insert(sql_3)
    print(i)
