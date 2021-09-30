#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid
import random
import re
from datetime import datetime,timedelta
from util.time_utc import local_to_utc
from mdm.dbPlsql_util_system import PLSqlSystem



max_code = 699
def insert_data():
    mdm_sql = PLSqlSystem()

    # sql_1 = '''
    #     select max("Code") from mdm.concept where "CodeSystemId"='709f878b-db90-4c98-bfa8-76610f62080b';
    #     '''
    # res_1 = mdm_sql.query(sql_1)
    # max_code = int(res_1[0][0]) + 1
    # print(max_code)

    global max_code
    max_code = max_code + 1
    code_new = 'bigg' + str(max_code)
    print(code_new)

    sql_2 = '''
    select "Code","Display" from mdm.concept where "CodeSystemId"='bc6f698b-46e7-42ef-81b3-0b8871e913db';
    '''
    res_2 = mdm_sql.query(sql_2)
    n = random.randint(0,47350)
    code_id=res_2[n][0]
    code_name = res_2[n][1]
    code_name = re.sub(r"[\\]",'',code_name)
    display =str(random.randint(10000,200000)) + code_name
    # print(code_name)

    name = 'bigg大数据2'
    namespace = uuid.uuid1()
    guid = uuid.uuid5(namespace, name)
    # print(guid)

    type = random.choice(['启用','停用'])
    reference_code = random.choice(['A','B','C','D']) + str(random.randint(10000,200000))
    active = random.choice(['启用','停用'])
    prefer_ch = random.choice(['cf', 'bf','af','gf','lf'])
    reference_code_system = random.choice(['A','B','C','D']) + str(random.randint(10000,200000)) + str(random.randint(100,200000))

    data_info = '''
   [{"code": "isActive", "value": true}, {"code": "ConceptParentCode", "value": {"code": "%s", "display": "%s"}}, {"code": "active", "value": "%s"}, {"code": "type", "value": "%s"}, {"code": "prefer_ch", "value": "%s"}, {"code": "reference_code_system", "value": "%s"}, {"code": "reference_code", "value": "%s"}]
    '''%(code_id,code_name,active,type,prefer_ch,reference_code_system,reference_code)

    now_time = datetime.now()
    update_time = local_to_utc(now_time)
    # print(update_time)

    sql_3 = """
    INSERT INTO mdm.concept ("Id", "CreateTime", "LastUpdateTime", "VersionId", "Code", "Display", "Values", "ParentId", "CodeSystemId") VALUES ('{0}', '{1}', '{1}', 1, '{2}', '{3}', '{4}', '00000000-0000-0000-0000-000000000000', '709f878b-db90-4c98-bfa8-76610f62080b');
    """.format(guid,update_time,code_new,display,data_info)

    mdm_sql.insert(sql_3)
    print("插入成功")

if __name__ == '__main__':
    for x in range(1,5000):
         insert_data()