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
    sql_2 = '''select max(regid) from public.patient_identy;'''
    euid_data = system_sql.query(sql_1)
    regid_data = system_sql.query(sql_2)

    regid = regid_data[0][0] + 1

    for x in range(0, len(euid_data)):
        regid = regid + 1
        identy = random.choice(['普通军人', '医保患者', '师级干部'])
        euid = euid_data[x][0]

        patient_sql = '''
        INSERT INTO public.patient_identy (regid, identy, eid) VALUES ({0}, '{1}', '{2}');
        '''.format(regid, identy, euid)
        system_sql.insert(patient_sql)
        print(x, "{0}插入成功".format(euid))


# 用药信息
def drug_detail():
    sql_1 = '''select drug_code,drug_name from public.drug_detail group by drug_code,drug_name;'''
    drug_data = system_sql.query(sql_1)

    sql_2 = '''select regid,eid from public.patient_identy where eid like '%EHX%';'''
    patient_data = system_sql.query(sql_2)

    for x in range(0, len(patient_data)-1):
        reg_id = patient_data[x][0]
        eid = patient_data[x][1]

        m = random.randint(0, len(drug_data) - 1)
        drug_code = drug_data[m][0]
        drug_name = drug_data[m][1]

        yao_data = {1: ['0.25g*24片', '盒'], 2: ['0.25g*24片', '盒'], 3: ['0.2g/2ml', '支'], 3: ['0.2g/2ml', '支'],
                    4: ['0.236g*12片', '盒'], 5: ['0.3g/2ml', '支'], 6: ['0.15g*12片', '瓶'],
                    7: ['0.6g/2ml', '支'], 8: ['0.15g*12片', '瓶']}
        z = random.randint(1, 8)
        specs = yao_data[z][0]
        unit = yao_data[z][1]
        qty = random.randint(1, 9)
        day_num = random.randint(1, 20)

        now_time = datetime.now()
        hours_data = random.randint(-60, 0)
        offset = timedelta(days=hours_data)
        real_time = now_time + offset
        visit_date = datetime.strftime(real_time, '%Y-%m-%d')

        sql_3 = '''select patient_property from public.patient where euid = '{0}';'''.format(eid)
        patient_property = system_sql.query(sql_3)
        # print(patient_property)
        patient_id = patient_property[0][0]['source_patid']
        # print(patient_id)

        drug_detail_sql = '''
        INSERT INTO public.drug_detail (reg_id, drug_code, drug_name, specs, qty, day_num, unit, visit_date, patient_id, eid) VALUES ({0}, '{1}', '{2}', '{3}', {4}, {5}, '{6}', '{7}', '{8}', '{9}');
        '''.format(reg_id, drug_code, drug_name, specs, qty, day_num, unit, visit_date, patient_id, eid)
        system_sql.insert(drug_detail_sql)
        print(x)


# 诊断详情
def diagnose_detail():
    sql_1 = '''select diagcode,diagname from public.diagnose_detail where diagcode is not null group by diagcode,diagname;'''
    sql_2 = '''select regid,eid from public.patient_identy where eid like '%EHX%';'''
    diag_data = system_sql.query(sql_1)
    patient_data = system_sql.query(sql_2)

    for x in range(0, len(patient_data) - 1):
        m = random.randint(0, len(patient_data) - 1)
        reg_id = patient_data[x][0]
        eid = patient_data[x][1]

        n = random.randint(0, len(diag_data) - 1)
        diagcode = diag_data[n][0]
        diagname = diag_data[n][1]

        now_time = datetime.now()
        hours_data = random.randint(-60, 0)
        offset = timedelta(days=hours_data)
        real_time = now_time + offset
        visitdate = datetime.strftime(real_time, '%Y-%m-%d')
        # print(visitdate)

        diagnose_detail_sql = '''
        INSERT INTO public.diagnose_detail (reg_id, diagcode, diagname, visitdate, eid) VALUES ({0}, '{1}', '{2}', '{3}', '{4}');
        '''.format(reg_id, diagcode, diagname, visitdate, eid)
        system_sql.insert(diagnose_detail_sql)
        print(eid, x)


# 诊断信息
def insur_drug_diagnosis_catalog():

    sql_1='''select drug_code,drug_name from public.drug_detail group by drug_code,drug_name;'''
    drug_data = system_sql.query(sql_1)

    sql_2 = '''select in_diag_code ,in_diag_name  from source.case_base
    where in_diag_code is not null and in_diag_name  is not null
    group by in_diag_code ,in_diag_name limit 100;'''
    in_diag_data = bi_sql.query(sql_2)

    for x in range(1,len(drug_data)-1):

        drug_code = drug_data[x][0]
        drug_name = drug_data[x][1]

        n = random.randint(1,90)
        diagnosis_code = in_diag_data[n][0]
        diagnosis_name = in_diag_data[n][1]

        diagnosis_catalog_sql = '''
        INSERT INTO public.insur_drug_diagnosis_catalog (drug_code, diagnosis_code, drug_name, diagnosis_name) VALUES ('{0}', '{1}', '{2}', '{3}');
        '''.format(drug_code, diagnosis_code, drug_name, diagnosis_name)
        system_sql.insert(diagnosis_catalog_sql)
        print(x)

if __name__ == '__main__':
    # patient_identy()
    # diagnose_detail()
    # drug_detail()
    insur_drug_diagnosis_catalog()
    # pass
