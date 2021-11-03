#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid
import random
import re
from datetime import datetime, timedelta
from xpinyin import Pinyin
from util.time_utc import local_to_utc
from empi.dbPlsql_util_system import PLSqlSystem
from empi.get_data import GetData
from util.get_idnum import GetID
import uuid

system_sql = PLSqlSystem()


# 患者信息
def patient_identy():
    # sql_1 = '''select euid from public.patient where euid like '%EH%';'''
    # euid_data = system_sql.query(sql_1)

    sql_2 = '''select max(regid) from public.patient_identy;'''
    regid_data = system_sql.query(sql_2)

    sql_3 = '''select drug_code,drug_name,diagnosis_code,diagnosis_name from insur_drug_diagnosis_catalog;'''
    drug_data = system_sql.query(sql_3)

    # regid = regid_data[0][0] + 1
    # regid=0

    for x in range(0, 1):
        # regid = regid + 1
        # # regid = 0
        # reg_id = regid
        data_num = random.randint(0, 6)
        yard_data = {0: '上海浦东新区人民外院', 1: '上海浦东新区人民外院', 2: '上海黄浦区中心人民外院', 3: '北京六中心人民外院', 4: '深圳六中心人民外院', 5: "本院", 6: ""}
        yard = yard_data[data_num]

        if data_num >= 5:
            regid = regid_data[0][0] + 1
        else:
            regid = 0
        print(data_num, regid, yard)
        # 普通患者
        # identy = random.choice(['普通军人', '医保患者', '师级干部'])
        identy = '普通患者'
        euid = 'EH00987243'
        # euid = euid_data[x][0]
        print("regid: {0} \n euid: {1}".format(regid, euid))
        print("*"*50)
        visit_date = '2021-10-29'
        print(visit_date)

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
        # day = '0' + str(x)

        for j in range(0, 1):
            # 用药信息
            reg_id = regid
            eid = euid
            # print(len(drug_data) - 1) 4414
            m = random.randint(301, 590)
            # m = 3801
            drug_code = drug_data[m][0]
            drug_name = drug_data[m][1]
            print(drug_code, drug_name)

            yao_data = {1: ['0.25g*24片', 3, 20, '盒'], 2: ['0.25g*24片', 5, 10, '盒'], 3: ['0.2g/2ml', 6, 11, '支'],
                        3: ['0.2g/2ml', 7, 5, '支'],
                        4: ['0.236g*12片', 3, 10, '盒'], 5: ['0.3g/2ml', 2, 12, '支'], 6: ['0.15g*12片', 2, 8, '瓶'],
                        7: ['0.6g/2ml', 2, 15, '支'], 8: ['0.15g*12片', 10, 9, '瓶']}
            z = random.randint(1, 8)
            # z = 8
            specs = yao_data[z][0]
            qty = yao_data[z][1]
            day_num = yao_data[z][2]
            unit = yao_data[z][3]

            drug_detail_sql = '''
                            INSERT INTO public.drug_detail (reg_id, drug_code, drug_name, specs, qty, day_num, unit, visit_date, patient_id, eid,yard) VALUES ({0}, '{1}', '{2}', '{3}', {4}, {5}, '{6}', '{7}', '{8}', '{9}','{10}');
                            '''.format(reg_id, drug_code, drug_name, specs, qty, day_num, unit, visit_date, patient_id,
                                       eid,yard)
            system_sql.insert(drug_detail_sql)

            visitdate = visit_date
            # 诊断详情 诊断正确
            diagcode = drug_data[m][2]
            diagname = drug_data[m][3]

            # 诊断详情 诊断错误
            diagcode = drug_data[m][2] + '999'
            diagname = drug_data[m][3] + '999'
            print("诊断名称：",diagcode,diagname)
            print("*" * 50)
            diagnose_detail_sql = '''
                            INSERT INTO public.diagnose_detail (reg_id, diagcode, diagname, visitdate, eid) VALUES ({0}, '{1}', '{2}', '{3}', '{4}');
                            '''.format(reg_id, diagcode, diagname, visitdate, eid)
            system_sql.insert(diagnose_detail_sql)
            # print("插入成功")

        name = 'test_name3'
        namespace = uuid.uuid1()
        guid = uuid.uuid5(namespace, name)

        text1 = "12岁时曾患肺结核，经系统治疗一年半，现已痊愈"
        text2 = "1995年在阜外医院做房间隔缺损修补术，术后恢复良好，体育已达标。"
        text3 = "严重心脏病，但先天性心脏病经手术治愈，或房室间隔缺损却分流量少，动脉导管未闭但返流血量少，经二级以上医院专科检查确定无需手术者除外"
        text4 = "严重的血液病、内分泌及代谢系统疾病、风湿性疾病。慢性肝炎病人并且肝功能不正常者，其中，肝炎病原携带者但肝功能正常者除外。结核病，但原发型肺结核、浸润性肺结核已硬结稳定，结核型胸膜炎已治愈或治愈后遗有胸膜肥厚者除外"
        text5 = "无"
        text6 = ""
        bin_text = random.choice([text1, text2, text3, text4, text5, text6])
        original_txt_content_1 = '''【主诉】右眼球突出1个月
【既往史】无特殊
【家庭史】无特殊
【个人史】无
【月经史】无
简要病史:{0}
查体:右眼0.3，左眼1.2
【诊断】右眶肿瘤
【嘱咐】'''.format(bin_text)

        original_txt_content_2 = '''【主诉】右眼球突出1个月
【既往史】无特殊
【家庭史】无特殊
【个人史】无
【月经史】无
【简要病史】{0}
【查体】右眼0.3，左眼1.2
【诊断】右眶肿瘤
【嘱咐】'''.format(bin_text)

        original_txt_content = random.choice([original_txt_content_1, original_txt_content_2])
        # print(original_txt_content)

        outpat_medical_record_sql = '''
            INSERT INTO public.outpat_medical_record (id, reg_id, original_txt_content, create_time) VALUES ('{0}', {1}, '{2}', '{3} 14:25:25.000000');
        '''.format(guid, regid, original_txt_content, visit_date)
        system_sql.insert(outpat_medical_record_sql)
        print("表都插入成功")


if __name__ == '__main__':
    patient_identy()
