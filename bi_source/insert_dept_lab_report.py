#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb
from util.dbPlsql_util_bi import PlSqlDbBI
from bi_source.get_data import GetData
import random
from datetime import datetime,timedelta

# 检查检验主题 topic=21
mysql1 = PlSqlDbBI()
sql_1 = '''select max(report_id) from source.lab_report;'''
res_1 = mysql1.query(sql_1)

max_report_id = res_1[0][0] + 1

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

    max_report_id = max_report_id + 1

    # 对应normalized_department表科室数据
    res_2 = mysql.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]


    source_fee_detail_id = 'MY0077' + str(round(random.uniform(1, 200),4)) + '|' + str(random.randint(1, 200))

    total_cost = random.randint(200000, 730000)
    patient_type_id = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    pay_kind_code = random.choice([1, 2, 3, 4, 5, 6, 7, 8])

    random_data = random.choice(['A', 'B', 'C', 4, 5, 6, 7, 8])
    report_class_name = 'Abbott - i4000sr' + str(random_data)

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name
    # print(patient_name)
    visit_type_data = {'I': '住院', 'O': '门诊', 'E': '体检', 'P': '急诊'}
    visit_type_code = random.choice(['I', 'O', 'E', 'P'])
    visit_type = visit_type_data[visit_type_code]


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

    test_time = real_time

    hours_data_1 = round(random.uniform(1, 15), 2)
    offset_1 = timedelta(hours=hours_data_1)
    apply_time = test_time + offset_1

    sql_3 = '''
       INSERT INTO source.lab_report (report_id, source_report_id, org_code, source_app, visit_type, visit_type_code,
                               source_visit_id, source_patient_id, patient_name, sex_code, sex_name, age, age_unit,
                               age_day, bed_code, bed_name, report_class_code, report_class_name, report_name,
                               test_instrument_code, test_instrument_name, apply_bill_no, apply_ward_code,
                               apply_ward_name, apply_dept_code, apply_dept_name, apply_oper_code, apply_oper_name,
                               apply_time, barcode, sample_code, sample_name, sampling_oper_code, sampling_oper_name,
                               sampling_time, receive_oper_code, receive_oper_name, receive_time, test_dept_code,
                               test_dept_name, test_oper_code, test_oper_name, test_time, report_oper_code,
                               report_oper_name, report_time, abnormal_flag_code, abnormal_flag_name, report_state_code,
                               report_state_name, patient_id, normalized_apply_dept_id, normalized_apply_dept_name,
                               normalized_test_dept_id, normalized_test_dept_name, str1, str2, str3, str4, str5, str6,
                               str7, str8, str9, str10, source_apply_id, lab_status_code, lab_status_name,
                               apply_type_code, apply_type_name, report_dept_code, report_dept_name)
VALUES ({0}, '{1}', '46919134-2', '{2}', '{7}', '{6}', '100035904', '2761612', '{8}', '2', '女性', 52,
        '岁', 18799, '25', '25', 'MY', '{5}', '肿瘤筛查（卵巢筛查）', null, null, '1902131683', '0246H', '妇科②护理单元',
        '{3}', '{4}', '0408', '陈国英', '{9}', '0780014253', '32', '静脉血', null, null,
        '{9}', 'hluyi', null, '{9}', '{3}', '{4}', null, null,
        '{10}', '8998', '高正洪', '{10}', null, null, '1', '正常', 57506, null,
        '妇科二', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        '{3}', '{4}');
        '''.format(max_report_id, source_fee_detail_id, source_app, dept_id, dept_name, report_class_name,
                   visit_type_code, visit_type, patient_name, test_time, apply_time)
    mysql1.insert(sql_3)
    print(i)
