#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb
from util.dbPlsql_util_bi import PlSqlDbBI
import random
from datetime import datetime,timedelta
from update_source.get_data import GetData

# 出入转主题 topic_code='5

mysql1 = PlSqlDbBI()
sql_1 = '''select max(transfer_general_id) from source.transfer_summary;'''
res_1 = mysql1.query(sql_1)

max_transfer_general_id = res_1[0][0] + 1

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


for i in range(1, 1209):
    max_transfer_general_id = max_transfer_general_id + 1

    res_2 = mysql.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    normalized_dept_name = res_2[i][2]
    normalized_dept_id = res_2[i][3]
    source_app = res_2[i][4]

    actual_bed_days = random.randint(1, 100)
    dis_pat_bed_days = random.randint(1, 100)
    inhos_pat_days = random.randint(1, 100)

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]


    dept_type_code = random.choice(['N', 'ICU'])
    if dept_type_code == 'N':
        dept_type_name = '普通'
    elif dept_type_code == 'ICU':
        dept_type_name = 'ICU'

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
     INSERT INTO source.transfer_summary (transfer_general_id, org_code, source_app, dept_ward_flag, dept_id, dept_name,
                                         ward_id, ward_name, statis_time, original_persons, existing_persons,
                                         actual_existing_persons, in_persons, dis_persons, quit_persons,
                                         transfer_in_persons, transfer_out_persons, dead_persons, critical_persons,
                                         rescue_persons, acco_persons, recovery_presons, imporve_persons,
                                         no_recovery_persons, other_persons, dept_out_persons, dept_in_persons, in_babies,
                                         out_babies, existing_babies, emer_in_persons, dis_same_day, general_op_in_persons,
                                         bed_num, fixed_beds, actual_beds, actual_open_beds, extra_beds, unoccupied_beds,
                                         actual_bed_days, dis_pat_bed_days, inhos_pat_days, statistician, doc_name, doc_id,
                                         dept_group_name, dept_group_id, dept_type, dept_type_name, dept_type_code,
                                         dept_code, str1, str2, str3, str4, str5, str6, str7, str8, str9, str10)
    VALUES ({0}, '46919134-2', '{1}', null, {2}, '{3}', null, null, '{4}', null, null, null,
            0, 0, null, null, 26018, null, null, null, null, null, null, null, null, null, null, 0, 0, null, null, 0, 0,
            300, 300, 300, 300, 0, 293, {9}, {10}, {11}, null, '{7}', {8}, null, null, null, '{5}', '{6}', '0252', null, null,
            null, null, null, null, null, null, null, null);
            '''.format(max_transfer_general_id, source_app, dept_id, dept_name, update_time, dept_type_name,
                       dept_type_code, doc_name, doc_id, actual_bed_days, dis_pat_bed_days, inhos_pat_days)

    mysql1.insert(sql_3)
    print(i)
