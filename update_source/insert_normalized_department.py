#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb

# 映射业务科室一级科室
mysql1 = PlSqlDb()
sql = '''select max(id),max(dept_id),max(sort) from system.normalized_department;'''
res = mysql1.query(sql)
max_id = res[0][0]
max_dept_id = res[0][1]
max_sort = res[0][2]
print(res)

sql_1 = '''select dept_id,dept_name from system.standard_department where dept_name like '%业务层级%';'''
res_1 = mysql1.query(sql_1)
print(res_1)

for i in range(0, 36):
    max_id = max_id + 1
    max_dept_id = max_dept_id + 1
    max_sort = max_sort + 1
    dept_name = res_1[i][1]

    normalized_dept_id = res_1[i][0]
    normalized_dept_name = res_1[i][1]

    sql_2 = '''insert into system.normalized_department (id, dept_id, dept_name, normalized_dept_id, normalized_dept_name, source_app,
                                           org_code, dept_type_id, dept_type_name, dept_size_id, dept_size_name,
                                           dept_size_value, str1, str2, oper_id, oper_time, last_update_time,sort)
    values ({0}, {1}, '{2}', {3}, '{4}', 'tj_his3', '46919134-2', 2, '外科', 4, '非重点专科', 1, null, null, 1,
            '2020-07-13 11:34:40.000000', '2020-09-09 09:41:34.000000',{5});
            '''.format(max_id, max_dept_id,dept_name,normalized_dept_id,normalized_dept_name,max_sort)
    mysql1.insert(sql_2)
    print(i)