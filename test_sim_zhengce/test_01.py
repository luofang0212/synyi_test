#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.do_excel import DoExcel
from dbPlsql_util_system import PLSqlSystem
import re

excel = DoExcel(r'D:\python_work\synyi_test\test_sim_zhengce\需要导入的政策指标集.xlsx', 'Sheet1').get_data()

# print(excel)

system_mysql = PLSqlSystem()

for x in range(1,len(excel)):

    name = excel[x]['col2']
    name = re.sub(r"\s","",name).strip()
    print(name)

    guide_data = {'逐步降低':0,'逐步提高':1,'监测比较':2,'监测达标':3}
    guide_name = excel[x]['col4']
    print(guide_name)
    if guide_name == None:
        guide = 0
    else:
        guide = guide_data[guide_name]

    unit = excel[x]['col3']
    content = excel[x]['col5']
    formula = excel[x]['col6']

    sql = '''
    update config.indicator set guide='{0}',unit='{1}', content='{2}', formula='{3}' where indicator_name = '{4}';
    '''.format(guide,unit,content,formula,name)

    system_mysql.update(sql)
    print("{0} 更新成功".format(name))
    print(x)