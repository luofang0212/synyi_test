#!/usr/bin/env python
# -*- coding:utf-8 -*-


from clickhouse_driver import Client

def db_clickhouse():
    # host='172.16.1.18' #服务器地址
    host = '172.16.1.22'  # 服务器地址
    port =9000 #端口
    user='default' #用户名
    password='123456789' #密码
    database='default' #数据库
    send_receive_timeout = 30 #超时时间

    client = Client(host=host, port=port, user=user, password=password, database=database,send_receive_timeout=send_receive_timeout)


    sql = '''select round(sum(fee_detail.total_cost) / 10000, 2) as "医疗总收入(万元)"
              from default.fee_detail fee_detail
              where bill_time >= '2021-04-01 00:00:00'
                and bill_time < '2021-05-01 00:00:00' '''
    data = client.execute(sql)
    print(data)

db_clickhouse()