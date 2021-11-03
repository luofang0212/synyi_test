#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_bi import PlSqlDbBI
from util.dbPlsql_util_system import PlSqlDb
import random
from datetime import datetime, timedelta
from bi_source.get_data import GetData

mysql_bi = PlSqlDbBI()
sql_1 = '''select max(id),max(stat_date_id) from source.std_dws_emp_distribution_month;'''
res_1 = mysql_bi.query(sql_1)

max_id = res_1[0][0] + 1
stat_date_id = res_1[0][1] + 1

mysql_2 = PlSqlDb()

sql_2 = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''
res_2 = mysql_2.query(sql_2)

print(len(res_2))
# print(res_2)

for i in range(1, 1209):
    max_id = max_id + 1
    stat_date_id = stat_date_id + 1
    res_2 = mysql_2.query(sql_2)

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

    doc_title_data = {1: '副主治医生', 2: '主任医生', 3: '高级医生', 4: '助理医生', 5: '副主任护士', 6: '副主任中药护士', 7: '副主任护士', 8: '中药医生', 9: '护士', 10: '主治医生',11:'中医医生',12:'中医护士'}
    doc_title_id = random.randint(11, 12)
    doc_title_code = doc_title_id
    doc_title_name = doc_title_data[doc_title_id]

    at_dept_data = {1: '感染管理科', 2: '儿科', 3: '鼻科', 4: '妇产科', 5: '孕妇科', 6: '普外科', 7: '血液科', 8: '急诊', 9: '感染性疾病',
                    10: '重症医学',11: '中医',12: '麻醉',13: '康复'}
    at_dept_code = random.randint(11, 13)
    at_dept_name = at_dept_data[at_dept_code]

    emp_type_data = {1: '副主治医生', 2: '主任医生', 3: '高级医生', 4: '助理医生', 5: '副主任护士', 6: '副主任中药护士', 7: '副主任护士', 8: '中药医生', 9: '护士', 10: '主治医生',11: '主治医师',12: '主治护师'}
    emp_type_code = random.randint(10, 11)
    emp_type_name = emp_type_data[emp_type_code]

    emp_num = random.randint(1, 200)

    # 指定日期 转换
    data = random.randint(1, 12)
    get_time = '2021-{0}-05 08:00:00.000000'.format(data)
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
    INSERT INTO source.std_dws_emp_distribution_month (id, stat_date_id, stat_date, org_id, org_code, org_name,
                                                    hosp_area_id, hosp_area_code, hosp_area_name, at_dept_id,
                                                    at_dept_code, at_dept_name, fixed_dept_id, fixed_dept_code,
                                                    fixed_dept_name, gendor_code, gendor_name, education_code,
                                                    education_name, graduate_school, emp_type_code, emp_type_name,
                                                    title_code, title_name, position_code, position_name, emp_num,
                                                    etl_time_1, update_time)
VALUES ({0}, {1}, '{2}', 7733, '46919132', '森亿国际机构', 3, '3', '东院区', 6464, '{6}', '{7}', {6}, '{6}',
        '{7}', '1', '男', '2', '学历2', '国防科技大学', '{8}', '{9}', '{3}', '{4}', '5', '岗位7', {5}, '{2}',
        '{2}');
    
        '''.format(max_id, stat_date_id, update_time, doc_title_code, doc_title_name, emp_num, at_dept_code,
                   at_dept_name, emp_type_code, emp_type_name)

    mysql_bi.insert(sql_3)
    print(i)
