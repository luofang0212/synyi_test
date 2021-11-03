#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_bi import PlSqlDbBI
from util.dbPlsql_util_system import PlSqlDb
import random
from bi_source.get_data import GetData
from datetime import datetime,timedelta
from util.time_utc import *

'''入院记录主题	 topic=150 '''

mysql_bi = PlSqlDbBI()
sql_1 = '''select max(visit_id) from source.discharge_record_in;'''
res_1 = mysql_bi.query(sql_1)
# print(res_1)

max_visit_id = res_1[0][0] + 1


mysql_2 = PlSqlDb()

sql_2 = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''
res_2 = mysql_2.query(sql_2)
print(len(res_2))
# print(res_2)

for i in range(1, 1208):
    max_visit_id = max_visit_id + 1


    res_2 = mysql_2.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

    # 指定日期 转换
    # get_time = '2021-08-10 00:00:00.000000'
    # now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')

    # # 时间统一用
    # now_time = datetime.now()
    # # 根据当前时间 去计算便宜时间，随机生成时间
    # # hours_data = random.randint(-10,14)
    # hours_data = round(random.uniform(-10, 14), 2)
    # offset = timedelta(hours=hours_data)
    # real_time = now_time + offset

    # 指定日期 转换
    data = random.randint(8, 9)
    get_time = '2021-10-{0} 08:00:00.000000'.format(data)
    now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')

    hours_data = round(random.uniform(-2, 14), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset

    update_time = local_to_utc(real_time)

    sql_3 = '''
    INSERT INTO source.discharge_record_in (visit_id, org_code, source_app, source_visit_id, source_patient_id, patient_id,
                                        patient_name, age, in_time, in_dept_id, in_dept_name, in_ward_id, in_ward_name,
                                        in_doc_id, in_doc_name, patient_type_id, patient_type_name, patient_type_code,
                                        in_type_id, in_type_code, in_type_name, in_diag_id, in_diag_code, in_diag_name,
                                        str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, dept_type_code,
                                        dept_type_name, address, country, province, city, district)
VALUES ({0}, '46919134-2', '{1}', '11925811', 'AG3274352', null, '{6}', null, '{7}', {2},
        '{3}', 1, '观察病房', {4}, '{5}', null, null, null, null, null, '急诊', null, null, null, 'B6东区', '神经内科住院',
        '神经内科住院', '5', '出院结算', '23002', 3.0000, null, null, null, 0, '类型1', '新区万科金域华府一期1期8栋6-902', '中国', '广东', '赤坎区',
        null);

        '''.format(max_visit_id,source_app,dept_id,dept_name,doc_id,doc_name,patient_name,update_time)

    mysql_bi.insert(sql_3)
    print(i)
