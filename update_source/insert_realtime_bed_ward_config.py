#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbPlsql_util_system import PlSqlDb
import random
from datetime import datetime, timedelta
from update_source.get_data import GetData

# 移动端 床位使用率-病区

mysql = PlSqlDb()
# sql_1 = '''select max(transfer_general_id) from source.transfer_summary;'''
# res_1 = mysql.query(sql_1)

bed_ward_data = [2401, 2402, 2403, 2404, 2405, 2406, 2407, 2408, 2409, 2410, 2411, 2412, 2413, 2414, 2415, 2416, 2417,
                 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 242601, 2427, 2428, 2429, 2430, 2431, 2432, 2435,
                 2436, 2437, 2438, 2439, 2440, 2446, 2447, 2448, 2449, 2450, 2451, 2452]
sum_ward = len(bed_ward_data)
print(sum_ward)
for i in range(1, sum_ward):
    bed_ward_data = [2401, 2402, 2403, 2404, 2405, 2406, 2407, 2408, 2409, 2410, 2411, 2412, 2413, 2414, 2415, 2416,
                     2417,
                     2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 242601, 2427, 2428, 2429, 2430, 2431, 2432,
                     2435,
                     2436, 2437, 2438, 2439, 2440, 2446, 2447, 2448, 2449, 2450, 2451, 2452]
    bed_ward = bed_ward_data[i]
    kpi_code = "200009"

    calculate = random.randint(25,500)

    sql_2 = '''
            INSERT INTO realops.realtime_bed_ward_config (bed_ward_code, kpi_code, calculate)
            VALUES ('{0}', '{1}', '{2}');
            '''.format(kpi_code,bed_ward,calculate)

    mysql.insert(sql_2)
    print(i)
