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
import csv


def regist_body():
    n = random.randint(0, 12)
    sur = GetData.sur_name[n]
    m = random.randint(1, 30)
    name = GetData.name[m]
    patient_name = sur + name
    # print(patient_name)

    p = Pinyin()
    result1 = p.get_pinyin(patient_name)
    pinyin = re.sub("[-]+", ',', result1)
    spell_name = re.sub("[-]+", '', result1)
    # code = random.choice([1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.99])
    code = "1.13"
    id_no = str(GetID().get_idnum())
    identifier = str(random.randint(1000, 199999))
    phone = '1312288' + str(random.randint(1000, 9999))
    sex_code = random.choice([1, 2, 9])
    source_patid = 'pid' + str(random.randint(10000, 199990))
    birth_date = GetID().get_birthdata()
    nation_name = random.choice(['汉', '苗族', '瑶族'])
    profession_code = random.randint(10000, 10010)
    ids ='''[{"code":"%s","identifier":"%s"}]'''%(code,identifier)
    contact_name = patient_name
    home_address = "上海某地方"
    temporary_card_no = "1"
    medicare_card_no = "1"
    native_place = "湖南"

    info = '''{"source_patid":"%s","patient_name":"%s","birth_date":"%s","id_no":"%s","spell_name":"%s","contact_name":"%s","nation_name":"%s","home_address":"上海某地方","temporary_card_no":"2","medicare_card_no":"1","sex_code":"%s","phone":"%s","profession_code":"%s","native_place":"湖南","ids":[{"code":"%s","identifier":"%s"}]}
    ''' % (source_patid, patient_name, birth_date, id_no, spell_name, patient_name, nation_name, sex_code, phone,
           profession_code,code,identifier)
    print(info.strip())

    text = "{0}，{1}，{2}，{3}，{4}，{5}，{6}，{7}，{8}，{9}，{10}，{11}，{12}，{13}，{14}，{15}".format(source_patid,patient_name,birth_date,id_no,spell_name,contact_name,nation_name,home_address,temporary_card_no,temporary_card_no,medicare_card_no,sex_code,phone,profession_code,native_place,ids)
    # print(text)
    with open(r"D:\jmeter\jmeter_jmx\empi\regist_text.txt", 'w', encoding='utf-8') as fp:
        fp.write(text+"\n")

if __name__ == '__main__':
    for x in range(1):
        regist_body()

