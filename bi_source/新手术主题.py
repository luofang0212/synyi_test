#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_bi import PlSqlDbBI
from util.dbPlsql_util_system import PlSqlDb
import random
from datetime import datetime, timedelta
from bi_source.get_data import GetData

mysql_bi = PlSqlDbBI()
sql_1 = '''select max(id) from source.new_case_operation;'''
res_1 = mysql_bi.query(sql_1)

max_id= res_1[0][0] + 1
# max_case_id =  1
mysql_2 = PlSqlDb()

sql_2 = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''
res_2 = mysql_2.query(sql_2)
# print(len(res_2))


operation_sql = '''select operation_code, operation_name
from source.operation_record
where operation_code is not null
  and operation_name is not null
group by operation_code, operation_name;'''
operation_data = mysql_bi.query(operation_sql)
print(len(operation_data))

for i in range(1, 1209):
    max_id = max_id + 1
    res_2 = mysql_2.query(sql_2)

    n = random.randint(1,50)
    operation_code = operation_data[n][0]
    operation_name = operation_data[n][1]

    anesthesia_type_name = random.choice(['全麻','局部麻','不麻醉'])

    # 指定日期 转换
    data = random.randint(1, 12)
    get_time = '2021-{0}-05 08:00:00.000000'.format(data)
    now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')

    # # 时间统一用
    # now_time = datetime.now()
    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-10, 14), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset

    update_time = real_time

    sql_3 = '''
        INSERT INTO source.new_case_operation (id, org_code, source_app, source_id, source_visit_id, visit_type_id, visit_type,
                                       visit_type_code, source_patient_id, patient_name, case_id, operation_time,
                                       main_flag, operation_level_id, operation_level_code, operation_level_name,
                                       operation_id, operation_code, operation_name, operation_doc_id,
                                       operation_doc_name, helper1_id, helper1_name, helper2_id, helper2_name,
                                       anesthesia_type_id, anesthesia_type_code, anesthesia_type_name, incision_heal_id,
                                       incision_heal_name, anesthesia_doc_id, anesthesia_doc_name, incision_type_id,
                                       incision_type_code, incision_type_name, preoper_2h_drug_flag, forward_flag,
                                       anesthesia_level_code, anesthesia_level_name, duration, table_num, nnis_level_id,
                                       nnis_level_code, nnis_level_name, site_infec_flag, preoper_days,
                                       material_check_cost, material_treat_cost, oper_material_cost, oper_return_flag,
                                       oper_48h_flag, plan_retrun_flag, steward_score, analgesia_flag, resus_flag,
                                       out_dept_id, out_dept_code, out_dept_name, oper_dept_id, oper_dept_name,
                                       bed_doc_id, bed_doc_name, main_operation_class_name, operation_complication1,
                                       operation_complication2, str1, str2, str3, str4, str5, str6, str7, str8, str9,
                                       str10)
VALUES ({0}, '46919132', 'tj_his3', '2', '7512|20210902', 1, '住院', 'I', '410', '徐喕', 899, '{3}', 4,
        1, '3', '手术2级', 4, '{1}', '{2}', 674, '张斳', 510, null, 149, null, 1, '2', '{4}', 1, '愈合方式3', 876, '王苦', 6, '4',
        '切口类型8', 3, 3, '3', '麻醉等级5', 1.00, 4, 6, '2', 'NNIS等级5', 2, 1.0, 1000.0000, 1000.0000, 1000.0000, 3, 2, 2, 4.2,
        3, 3, 939, '636', '出院科室2135', 2424, '手术科室1389', 505, '黄懲', '手术类型2', '76', '术后并发症121', null, null, null, null,
        null, null, null, null, null, null);
        '''.format(max_id,operation_code,operation_name,update_time,anesthesia_type_name)

    mysql_bi.insert(sql_3)
    print(i)
