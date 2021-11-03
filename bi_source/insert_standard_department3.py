#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb
import random

# 新增一级科室
mysql = PlSqlDb()
sql_1 = '''select max(id),max(dept_id),max(sort) from system.standard_department;'''
res_1 = mysql.query(sql_1)
max_id = res_1[0][0]
max_dept_id = 1315
max_sort_id = res_1[0][2]
dept_name = ''
print(max_id, max_dept_id)

for i in range(1,37):
    max_id = max_id+1
    max_dept_id = max_dept_id +1
    max_sort_id = max_sort_id + 1
    dept_name = '业务层级' + str(i)
    dept_type_id = random.choice([1,2,3])
    dept_type_data = {"1":"内科","2":"外科","3":"其他"}
    dept_type_name = dept_type_data[dept_type_id]
    # if dept_type_id == 1:
    #     dept_type_name='内科'
    # elif dept_type_id == 2:
    #     dept_type_name='外科'
    # elif dept_type_id == 3:
    #     dept_type_name='其他'


    sql_2 = '''insert into system.standard_department (id, dept_id, dept_name, dept_type_id, dept_type_name, dept_size_id,
                                            dept_size_name, dept_size_value, icon, org_code, oper_id, oper_time, sort,
                                            parent_dept_id)
    values ({0}, {1}, '{2}', {3}, '{4}', 3, '市级重点专科', 2, 'erke', null, 1, '2021-01-28 03:28:57.698057', {5}, null);'''.format(
        max_id, max_dept_id, dept_name,dept_type_id,dept_type_name,max_sort_id)

    mysql.insert(sql_2)
    print(i)