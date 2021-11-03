#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import time
import json
from util.HttpRequest import HttpRequest
import requests


def empi_register():
    req = HttpRequest()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        "Authorization": "Bearer C99D66ED9E8EDCCB98134689170075EF391065513F7833B52D079A923A006DFD"
    }

    # biao_url = "http://frontend-469-test.synyi.sy/api/empi/identifierdomains/12"
    # biao_response = req.http_request('get',biao_url,headers=headers)
    # print(biao_response.json())
    ids =[{"code": "1.13", "identifier": "1232334"}]

    register_url = "http://frontend-469-test.synyi.sy/api/empi/patient"
    register_data = {"source_patid":"pid75494","patient_name":"陈成和","birth_date":"20020728","id_no":"45644620200317685X","spell_name":"chenchenghe","contact_name":"陈成和","nation_name":"瑶族","home_address":"上海某地方","temporary_card_no":"2","medicare_card_no":"1","sex_code":"1","phone":"13122885956","profession_code":"10002","native_place":"湖南","ids":[{'code': '1.13', 'identifier': '53178'}]}
    # print(register_data)
    print(register_data)
    register_response = req.http_request('post',register_url,register_data,headers=headers)
    print(register_response.text)


if __name__ == '__main__':
    empi_register()
