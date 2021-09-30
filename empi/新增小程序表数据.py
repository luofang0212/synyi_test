#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid
import random
import re
from datetime import datetime, timedelta
from xpinyin import Pinyin
from util.time_utc import local_to_utc
from empi.dbPlsql_util_system import PLSqlSystem
from util.dbPlsql_util_bi import PlSqlDbBI
from empi.get_data import GetData
from util.get_idnum import GetID

system_sql = PLSqlSystem()
bi_sql = PlSqlDbBI()


# 患者信息
def patient_identy():
    sql_1 = '''select euid from public.patient where euid like '%EHX%';'''
    euid_data = system_sql.query(sql_1)

    sql_2 = '''select max(regid) from public.patient_identy;'''
    regid_data = system_sql.query(sql_2)

    sql_3 = '''select drug_code,drug_name,diagnosis_code,diagnosis_name from insur_drug_diagnosis_catalog;'''
    drug_data = system_sql.query(sql_3)

    regid = regid_data[0][0] + 1

    for x in range(0, 1):
        regid = regid + 1
        reg_id = regid
        # identy = random.choice(['普通军人', '医保患者', '师级干部'])
        identy = '医保患者'
        euid = 'EHX0940864'
        # euid = euid_data[x][0]
        print("regid: {0} \n euid: {1}".format(regid, euid))

        patient_sql = '''
        INSERT INTO public.patient_identy (regid, identy, eid) VALUES ({0}, '{1}', '{2}');
        '''.format(regid, identy, euid)
        system_sql.insert(patient_sql)

        patient_id = random.randint(1000000, 9999999)

        now_time = datetime.now()
        hours_data = random.randint(-60, 0)
        offset = timedelta(days=hours_data)
        real_time = now_time + offset
        # visit_date = datetime.strftime(real_time, '%Y-%m-%d')
        visit_date = '2021-09-23'

        for j in range(0, 2):
            # 用药信息
            reg_id = regid
            eid = euid

            m = random.randint(0, len(drug_data) - 1)

            drug_code = drug_data[m][0]
            drug_name = drug_data[m][1]

            yao_data = {1: ['0.25g*24片', 3, 20, '盒'], 2: ['0.25g*24片', 5, 10, '盒'], 3: ['0.2g/2ml', 6, 11, '支'],
                        3: ['0.2g/2ml', 7, 5, '支'],
                        4: ['0.236g*12片', 3, 10, '盒'], 5: ['0.3g/2ml', 2, 12, '支'], 6: ['0.15g*12片', 2, 8, '瓶'],
                        7: ['0.6g/2ml', 2, 15, '支'], 8: ['0.15g*12片', 10, 9, '瓶']}
            z = random.randint(1, 8)
            specs = yao_data[z][0]
            qty = yao_data[z][1]
            day_num = yao_data[z][2]
            unit = yao_data[z][3]


            drug_detail_sql = '''
                            INSERT INTO public.drug_detail (reg_id, drug_code, drug_name, specs, qty, day_num, unit, visit_date, patient_id, eid) VALUES ({0}, '{1}', '{2}', '{3}', {4}, {5}, '{6}', '{7}', '{8}', '{9}');
                            '''.format(reg_id, drug_code, drug_name, specs, qty, day_num, unit, visit_date, patient_id,
                                       eid)
            system_sql.insert(drug_detail_sql)

            visitdate = visit_date
            # 诊断详情 诊断正确
            diagcode = drug_data[m][2]
            diagname = drug_data[m][3]

            # 诊断详情 诊断错误
            # diagcode = drug_data[m][2] + '999'
            # diagname = drug_data[m][3] + '999'

            diagnose_detail_sql = '''
                            INSERT INTO public.diagnose_detail (reg_id, diagcode, diagname, visitdate, eid) VALUES ({0}, '{1}', '{2}', '{3}', '{4}');
                            '''.format(reg_id, diagcode, diagname, visitdate, eid)
            system_sql.insert(diagnose_detail_sql)
            print("插入成功")


if __name__ == '__main__':
    patient_identy()
