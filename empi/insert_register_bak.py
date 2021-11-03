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

    info = '''
    {"ids": [
        {
          "code": "1.12",
          "identifier": "7644"
        }
      ],
      "id_no": "223763197101063508",
      "phone": "13122887145",
      "pinyin": "you,shan,fu",
      "sex_code": "9",
      "birth_date": "20140910",
      "spell_name": "youshanfu",
      "nation_name": "苗族",
      "contact_name": "尤善福",
      "home_address": "上海某地方",
      "native_place": null,
      "patient_name": "尤善福",
      "source_patid": "pid99123",
      "contact_phone": "13122887145",
      "profession_code": "10000",
      "medicare_card_no": null,
      "temporary_card_no": null
    }
    '''
    euid = 'EH20910119'
    # euid = 'EHT0' + str(random.randint(100000, 999999))
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
    regist()
