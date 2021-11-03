#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbPlsql_util_system import PlSqlDb
import random
from datetime import datetime, timedelta
from bi_source.get_data import GetData

# 血液使用率

mysql = PlSqlDb()
sql_1 = '''select max(id) from realops.realtime_blood;'''
res = mysql.query(sql_1)
max_id = res[0][0] + 1


for i in range(1, 100):

    max_id = max_id + 1
    patient_id = max_id
    inp_no = random.randint(100,10000)

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    name = sur_name + s_name

    bed = random.choice([1001,1002,1003,1004,1005,1006])
    age = random.randint(1, 100)
    ward = random.choice(['心血管病区','二十九病区','骨科病区','十五病区','十五病区','十五病区','十五病区','心血管病区','神经中心病区'])
    dept_data = {'2716': '呼吸与危重症医学科', '2710': '肾脏内科', '2702': '神内2区', '2722': '消化科', '2720': '内分泌科', '2717': '神内18区', '2722': '消化科', '2723': '放疗科', '2713': '产科'}

    dept_code = random.choice(['2716','2710','2702','2722','2720','2717','2722','2723','2713'])
    dept_name = dept_data[dept_code]

    diag=random.choice(['血液病一','血液病二','血液病三','血液病四','血液病五','血液病六'])
    result=random.choice(['通过','未通过'])

    sex = random.choice(['男','女'])


    now_time = datetime.now()
    # 根据当前时间 去计算便宜时间，随机生成时间
    hours_data = round(random.uniform(-15, 9), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset
    etl_time = real_time


    sql_2 = '''
            INSERT INTO realops.realtime_blood (patient_id, inp_no, name, bed, age, ward, dept_code, dept_name, diag, result, etl_time,id)
VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', {11});
            '''.format(patient_id, inp_no, name, bed, age, ward, dept_code, dept_name, diag, result, etl_time,id)

    mysql.insert(sql_2)
    print(i)
