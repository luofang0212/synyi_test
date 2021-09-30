#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import time
import json
from util.HttpRequest import HttpRequest
import requests


def empi_register():
    token = "Bearer 0D4169F5752F89844B7FBDE7C2C54C10B5166567DC459CBC98F291E6D5D456DE"
    http_rq = HttpRequest()
    # 患者标识符接口
    identifierdomains = 3
    identifierdomains_url = "http://frontend-469-test.synyi.sy/api/empi/identifierdomains/3"
    headers = {
        "Authorization": token
    }
    response = http_rq.http_request('get', identifierdomains_url, headers=headers)

    info = response.json()
    print(info)
    code = info['identifierCode']
    identifier = '38288' + str(random.randint(10000, 300000))
    print(code)
    time.sleep(0.5)

    patient_url = "http://frontend-469-test.synyi.sy/api/empi/patient"
    patient_data = {"source_patid": "122223", "patient_name": "2212", "birth_date": "12", "id_no": "2",
                    "spell_name": "2", "contact_name": "22", "nation_name": "322", "home_address": "2",
                    "temporary_card_no": "2", "medicare_card_no": "123222", "sex_code": "2", "phone": "2",
                    "profession_code": "12", "native_place": "133332332", "contact_phone": ["232"],
                    "ids": [{"code": code, "identifier": identifier}]}

    headers = {
        "Authorization": token
    }
    response_2 = http_rq.http_request('post', patient_url, data=patient_data, headers=headers)
    print(response_2.json())


if __name__ == '__main__':
    empi_register()
