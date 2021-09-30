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


def regist():
    system_sql = PLSqlSystem()

    n = random.randint(0, 12)
    sur = GetData.sur_name[n]
    m = random.randint(1, 30)
    name = GetData.name[m]
    patient_name = sur + name
    print(patient_name)

    p = Pinyin()
    result1 = p.get_pinyin(patient_name)
    pinyin = re.sub("[-]+",',',result1)
    spell_name = re.sub("[-]+", '', result1)
    # code = random.choice([1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.99])
    code = "1.13"
    id_num = GetID().get_idnum()
    identifier = random.randint(1000, 19999)
    phone = '1312288' + str(random.randint(1000, 9999))
    sex_code = random.choice([1,2,9])
    text_1 = '''
    {"ids": [
        {
          "code": "%s",
          "identifier": "%s"
        }
      ],'''%(code,identifier)
    source_patid = 'pid' + str(random.randint(10000, 199990))
    birth_date = GetID().get_birthdata()
    nation_name = random.choice(['汉','苗族','瑶族'])
    profession_code = random.randint(10000,10010)

    text_2 ='''
      "id_no": "{0}",
      "phone": "{1}",
      "pinyin": "{8}",
      "sex_code": "{2}",
      "birth_date": "{3}",
      "spell_name": "{9}",
      "nation_name": "{4}",
      "contact_name": "{5}",
      "home_address": "上海某地方",
      "native_place": null,
      "patient_name": "{5}",
      "source_patid": "{6}",
      "contact_phone": "{1}",
      "profession_code": "{7}",
      "medicare_card_no": null,
      "temporary_card_no": null
    '''.format(id_num,phone,sex_code,birth_date,nation_name,patient_name,source_patid,profession_code,pinyin,spell_name)

    info = text_1 + text_2 + '}'
    # print(info.strip())
    # 生成euid

    euid = 'EHX0' + str(random.randint(100000,999999))
    # print(euid)

    uid_name = 'taskid'
    namespace = uuid.uuid1()
    taskid = uuid.uuid5(namespace, uid_name)

    now_time = datetime.now()
    update_time = local_to_utc(now_time)

    sql_2 = '''
    INSERT INTO public.patient (is_deleted, created_time, last_updated_time, patient_property, operation_type,
                                hospital_area, euid, taskid)
    VALUES (false, '{0}', '{0}','{1}', 1, null, '{2}', '{3}');
    
    '''.format(update_time, info, euid, taskid)
    system_sql.insert(sql_2)
    print("%s 插入成功" % euid)


if __name__ == '__main__':
    for x in range(50):
        regist()
        print(x)
