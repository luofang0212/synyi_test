#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_bi import PlSqlDbBI
from util.dbPlsql_util_system import PlSqlDb
import random
from datetime import datetime,timedelta
from update_source.get_data import GetData


mysql_bi = PlSqlDbBI()
sql_1 = '''select max(id),max(stat_date_id) from source.std_dws_bed_distribute_day;'''
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
    visit_type_code = random.choice(['O','E','I','P'])
    visit_type = visit_type_data[visit_type_code]

    adjust_sub_class_code = random.choice(['135152', '135148', '135149', '135169', '135147', '135168'])

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

    diag_code_group = round(random.uniform(1,20),2)

    doc_title_data = {1: '副主治医生', 2: '主任医生', 3: '高级医生', 4: '助理医生', 5: '副主任护士', 6: '副主任中药护士', 7: '副主任护士', 8: '中药医生',9: '护士',10: '主治医生'}
    doc_title_id = random.randint(1, 10)
    doc_title_code = doc_title_id
    doc_title_name = doc_title_data[doc_title_id]

    dept_data = {1: '感染管理科', 2: '儿科', 3: '鼻科', 4: '妇产科', 5: '孕妇科', 6: '普外科', 7: '血液科', 8: '急诊', 9: '感染性疾病',
                    10: '重症医学',11: '中医',12: '麻醉',13: '康复'}
    dept_code = random.randint(1, 13)
    dept_name = dept_data[dept_code]

    bed_data = random.randint(1, 49)
    bed_num = random.randint(50,200)
    actual_open_beds = bed_num - bed_data
    actual_used_beds = bed_num - actual_open_beds
    extra_beds = random.randint(0, 50)


    # 指定日期 转换
    data = random.randint(1, 12)
    get_time = '2019-{0}-05 08:00:00.000000'.format(data)
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
    INSERT INTO source.std_dws_bed_distribute_day (id, stat_date_id, stat_date, org_id, org_code, org_name, hosp_area_id,
                                               hosp_area_name, dept_id, dept_code, dept_name, bed_num, actual_open_beds,
                                               actual_used_beds, extra_beds, etl_time1, update_time)
VALUES ({0}, {1}, '{2}', 1032, '46919132', '森亿国际机构', 2, '东院区', 7469, '{7}', '{8}', {3}, {4},
           {5}, {6}, '{2}', '{2}');
        '''.format(max_id,stat_date_id,update_time,bed_num, actual_open_beds,actual_used_beds,extra_beds,dept_code, dept_name)

    mysql_bi.insert(sql_3)
    print(i)
