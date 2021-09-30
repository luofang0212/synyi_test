#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb
from util.dbPlsql_util_bi import PlSqlDbBI
import random
from datetime import datetime,timedelta
from update_source.get_data import GetData

''' 手麻主题 topic=8 '''

mysql1 = PlSqlDbBI()
sql_1 = '''select max(operation_record_id) from source.operation_record;'''
res_1 = mysql1.query(sql_1)

max_visit_id = res_1[0][0] + 1

mysql = PlSqlDb()

sql_2 = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''

res_2 = mysql.query(sql_2)
# dept_id = res_2[3][0]
# dept_name = res_2[3][1]
# normalized_dept_name = res_2[3][2]
# normalized_dept_id  = res_2[3][3]
# source_app = res_2[3][4]
print(len(res_2))
print(res_2)

for i in range(1, 1209):
    max_visit_id = max_visit_id + 1
    res_2 = mysql.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    source_app = res_2[i][4]
    operation_name = '左前臂清创、血管神经肌腱修复术' + str(i)
    operation_level_name = random.choice(['一级', '二级', '三级', '四级'])
    pay_kind_code = random.choice([1, 2, 3, 4, 5, 6, 7, 8])

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    operation_doc_name = doc_data[doc_id]

    

    # 指定日期 转换
    # get_time = '2021-08-10 00:00:00.000000'
    # now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')

    # 时间统一用
    now_time = datetime.now()
    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-10, 14), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset

    operation_begin_time = real_time

    hours_data_1 = round(random.uniform(1, 5), 2)
    offset_1 = timedelta(hours=hours_data_1)
    operation_end_time = operation_begin_time + offset_1

    sql_3 = '''
  insert into source.operation_record (operation_record_id, org_code, source_app, source_operation_id, source_visit_id,
                                      visit_type, source_patient_id, patient_name, patient_type_id, patient_type_name,
                                      dept_group_id, dept_group_name, dept_id, dept_name, ward_id, ward_name,
                                      attending_doc_id, attending_doc_name, apply_doc_id, apply_doc_name,
                                      apply_dept_group_id, apply_dept_group_name, apply_dept_id, apply_dept_name,
                                      operation_doc_id, operation_doc_name, surg_dept_group_id, surg_dept_group_name,
                                      surg_dept_id, surg_dept_name, helper1_id, helper2_id, helper3_id,
                                      operation_dept_id, operation_dept_name, oper_dept_group_id, oper_dept_group_name,
                                      trans_dept_id, trans_dept_name, trans_dept_group_id, trans_dept_group_name,
                                      anesthesia_doc_id, anesthesia_doc_name, anes_helper1_id, anes_helper2_id,
                                      anes_helper3_id, prep_nurse1_id, prep_nurse2_id, instru_nurse1_id,
                                      instru_nurse2_id, anesthesia_type_id, anesthesia_type_name, anesthesia_level_name,
                                      anesthesia_complication, anesthesia_begin_time, anesthesia_end_time,
                                      incision_type_id, incision_type_name, operation_name, operation_code,
                                      operation_class_name, operation_level_id, operation_level_name, operation_scale,
                                      pre_diag, post_diag, pre_post_conform, operation_complication1,
                                      operation_complication2, table_num, operation_num, operation_begin_time,
                                      operation_end_time, duration, operation_apply_id, operation_anesthesia_id,
                                      operation_confirm_id, room_name, operation_state, operation_position_name,
                                      body_site, oper_return_fag, oper_48h_flag, plan_return_flag, oper_return_time,
                                      oper_return_reason, steward_score, analgesia_flag, resus_flag, cpr_num,
                                      cpr_succ_flag, uncons_flag, oxysat_flag, anesthesia_death_flag, obstruction_flag,
                                      other_unexpected_flag, first_oper_flag, visit_type_id, visit_type_code,
                                      patient_type_code, dept_code, apply_dept_code, surg_dept_code,
                                      operation_dept_code, trans_dept_code, anesthesia_type_code, anesthesia_level_id,
                                      anesthesia_level_code, incision_type_code, operation_id, operation_class_id,
                                      operation_class_code, operation_level_code, operation_state_id,
                                      operation_state_code, operation_position_id, operation_position_code, cpr_succ_id,
                                      cpr_succ_name, in_pacu_time, out_pacu_time, pacu_temperature, medical_group_code,
                                      medical_group_name, patient_id, normalized_dept_id, normalized_dept_name,
                                      normalized_input_dept_id, normalized_input_dept_name,
                                      normalized_operation_dept_id, normalized_operation_dept_name, str1, str2, str3,
                                      str4, str5, str6, str7, str8, str9, str10)
values ({0}, '46919134-2', '{1}', '03188533|1|1', '03188533|1', '住院', 03188533, '{6}', 8, '市医保', 76, '耳鼻喉科', 148,
        '耳鼻喉科', 147, '五官病区护理单元', null, null, 1292, '朱敬', 76, '耳鼻喉科', {2}, '{3}', null, '{5}', null, null, null, null,
        null, null, null, 410, '门诊手术室', null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, 85023, '静吸复合全麻', 'Ⅰ', null, null, null, null, null, '{9}', 30.0905, '择期', null, '{4}', '中',
        null, null, null, null, null, 1, null, '{7}', '{8}', null, null, null, null, 05,
        '出复苏室', '仰卧位', '仰卧位', null, null, null, null, null, null, null, null, null, null, null, null, 0, null, null,
        null, 552, 'I', 1, 0214, 0214, null, 0358, null, 'C', null, 'Ⅰ', null, null, null, 0, 2, null, 55, null, null,
        null, null, null, '{10}', 0.0000, '病区医生|0214', '耳鼻喉科', 99822, 3, '耳鼻咽喉科', 3, '耳鼻咽喉科', 3, '耳鼻咽喉科',
        null, null, null, null, null, null, null, null, null, null);

        '''.format(max_visit_id, source_app, dept_id, dept_name, operation_level_name,
                   operation_doc_name, patient_name, operation_begin_time, operation_end_time, operation_name, now_time)
    mysql1.insert(sql_3)
    print(i)
