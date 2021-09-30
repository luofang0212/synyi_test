#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mar_source.dbPlsql_util_mar import PLSqlMar
from mar_source.dbPlsql_util_system import PLSqlMarSystem
from mar_source.get_data import GetData
import random
import time, datetime

# 病案主题
mar_sql = PLSqlMar()
system_sql = PLSqlMarSystem()



sort_no = 1

for i in range(1,277):
    sort_no = sort_no + 1
    org_code_data = '''update system.organization set sort_no={0} where org_id={1};'''.format(sort_no,i)
    org_code_res = system_sql.update(org_code_data)

    print(i)