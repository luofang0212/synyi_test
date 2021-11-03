#!/usr/bin/env python
# -*- coding:utf-8 -*-

import psycopg2

# 连接system数据库
class PLSqlSystem:

    def __init__(self):

        # 连接数据库
        # self.conn = psycopg2.connect(database="empi_test", user="postgres", password="postgres", host="172.16.129.172",port="5432")

        # # 连接数据库
        # self.conn = psycopg2.connect(database="empiv4_test", user="luofang",password="p$mKDqBPVc5d", host="172.16.0.20",port="5432")

        # 连接数据库
        self.conn = psycopg2.connect(database="empiv4_test", user="luofang", password="p$mKDqBPVc5d",
                                     host="172.16.0.20", port="5432")

        # 建立游标，用来执行数据库操作
        self.cur = self.conn.cursor()

    def __del__(self):
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()

    # 查询
    def query(self, sql):
        self.cur.execute(sql)
        # 获取select返回的数组，里面数据的组成部分为元组
        rows = self.cur.fetchall()
        # print(rows)

        return rows

    # 插入
    def insert(self, sql):
        mysql = PLSqlSystem()
        self.cur.execute(sql)
        self.conn.commit()

    # 更新
    def update(self, sql):
        mysql = PLSqlSystem()
        self.cur.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    mydb = PLSqlSystem()

    sql = "select * from mdm.code_system"
    res = mydb.query(sql)
    print(res)

