#!/usr/bin/env python
# -*- coding:utf-8 -*-

import psycopg2


class PlSqlDb:

    def __init__(self):
        # 连接数据库
        # self.conn = psycopg2.connect(database="bi_3.14.1", user="postgres", password="postgres", host="172.16.129.172",
        #                              port="5432")

        # self.conn = psycopg2.connect(database="bi_test", user="luofang", password="p$mKDqBPVc5d", host="172.16.0.20",
        #                              port="5432")
        # self.conn = psycopg2.connect(database="bi_3.19.0", user="postgres", password="postgres", host="172.16.129.172",
        #                              port="5432")
        self.conn = psycopg2.connect(database="bi", user="postgres", password="postgres", host="172.16.129.172",
                                     port="5432")

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
        ## 获取SELECT返回的元组
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

        return rows

    # 插入
    def insert(self, sql):
        mysql = PlSqlDb()
        self.cur.execute(sql)
        self.conn.commit()

    # 更新
    def update(self, sql):
        mysql = PlSqlDb()
        self.cur.execute(sql)
        self.conn.commit()


if __name__ == '__main__':

   mydb =  PlSqlDb()

   sql = "select * from system.system_dictionary"
   res = mydb.query(sql)
   print(res)


