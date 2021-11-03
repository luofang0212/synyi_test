#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_bi import PlSqlDbBI
from util.dbPlsql_util_system import PlSqlDb
import random
from datetime import datetime,timedelta
from bi_source.get_data import GetData

'''新冠主题 topic=151 '''

mysql_bi = PlSqlDbBI()

sql_1 = '''select max(record_id),max(sample_id),max(report_id) from source.covid19_record covid19_record;'''
res_1 = mysql_bi.query(sql_1)
print(res_1)

max_record_id = int(res_1[0][0]) + 1
max_sample_id = int(res_1[0][1]) + 1
max_report_id = int(res_1[0][2]) + 1

mysql_2 = PlSqlDb()

sql_2 = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''
res_2 = mysql_2.query(sql_2)

print(len(res_2))
print(res_2)

for i in range(1, 1209):
    max_record_id = max_record_id + 1
    max_sample_id = max_sample_id + 1
    max_report_id = max_report_id + 1

    res_2 = mysql_2.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]

    total_cost = random.randint(10000, 200000)
    age = random.randint(0, 100)

    sex_data = {'1': '男性', '2': '女性'}
    sex_code = random.choice(['1', '2'])
    sex_name = sex_data[sex_code]

    test_result_data = {'0': '阳性', '1': '阴性'}
    test_result_code = random.choice(['0', '1'])
    test_result_name = test_result_data[test_result_code]

    sample_source_data = {'0': '院内标本', '1': '口岸标本'}
    sample_source_code = random.choice(['0', '1'])
    sample_source_name = test_result_data[test_result_code]

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

    # 指定日期 转换
    data = random.randint(22, 23)
    get_time = '2021-08-{0} 16:00:00.000000'.format(data)
    now_time = datetime.strptime(get_time,'%Y-%m-%d %H:%M:%S.%f')
    # now_time = datetime.now()
    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-15, 9), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset
    update_time = real_time

    sql_3 = '''
    INSERT INTO source.covid19_record (record_id, org_code, source_app, report_id, sample_id, pat_id, pat_name, sex_code,
                                   sex_name, age, age_unit, pat_source_code, pat_source_name, dept_code, dept_name,
                                   apply_doc_id, apply_doc_name, apply_time, sample_time, test_time, report_time,
                                   test_result_code, test_result_name, item_resullt_code, item_resullt_name,
                                   sample_source_code, sample_source_name, sample_type_code, sample_type_name)
VALUES ({0}, '46919132', '{1}', '{5}', '{6}', '5788788', '{4}', '{14}', '{15}', {9}, '岁', 0, '门诊', '{2}',
            '{3}', {7}, '{8}', '{13}', '{13}', '{13}',
        '{13}', {16}, '{10}', null, null, {11}, '{12}', 7, '拭子-咽喉2076');

        '''.format(max_record_id, source_app, dept_id, dept_name, patient_name, max_report_id, max_sample_id, doc_id,
                   doc_name, age,  test_result_name, sample_source_code, sample_source_name,
                   update_time, sex_code, sex_name,test_result_code)

    mysql_bi.insert(sql_3)
    print(i)
