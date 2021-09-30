#!/usr/bin/env python
# -*- coding:utf-8 -*-

from clickhouse_driver import Client


class ClickHouseDb:

    def __init__(self):
        # host = '172.16.1.18'  # 服务器地址
        host = '172.16.129.55'  # 服务器地址
        # host = '172.16.1.22'  # 服务器地址
        port = 9000  # 端口
        user = 'default'  # 用户名
        password = '123456789'  # 密码
        database = 'default'  # 数据库
        send_receive_timeout = 30  # 超时时间

        # 连接数据库
        self.client = Client(host=host, port=port, user=user, password=password, database=database,
                             send_receive_timeout=send_receive_timeout)

    # 查询，返回的是一个list，list里面是一个元组
    def query(self, sql):
        data = self.client.execute(sql)
        return data


if __name__ == '__main__':
    mydb = ClickHouseDb()

    sql = '''select *
              from default.fee_detail fee_detail
              where bill_time >= '2021-04-01 00:00:00'
                and bill_time < '2021-05-01 00:00:00' limit 10;'''
    res = mydb.query(sql)
    print(res)
