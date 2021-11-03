#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbPlsql_util_system import PlSqlDb


# 更新normalized_department、standard_department 的sort
mysql = PlSqlDb()


# dept_id = 1
# for i in range(1,1203):
#     dept_id = dept_id + 1
#     sql_2 = '''update system.standard_department set sort={0} where dept_id={1};'''.format(i, dept_id)
#     mysql.update(sql_2)
#     print(i)
#

dept_id = 1
sort = 38
for i in range(1,50):
    dept_id = dept_id + 1
    sort = sort + 1
    sql_2 = '''update system.standard_department set sort={0} where dept_id={1};'''.format(sort, i)
    mysql.update(sql_2)
    print(sort)



