#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbPlsql_util_system import PlSqlDb


# 更新normalized_department、standard_department 的sort
mysql = PlSqlDb()

dept_id = 1279
for i in range(1316,1351):
    dept_id = dept_id + 1
    sql_2 = '''update system.standard_department set parent_dept_id={0} where dept_id = {1};'''.format(dept_id,i)
    mysql.update(sql_2)
    print(i)





