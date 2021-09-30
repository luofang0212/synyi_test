#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from warnings import filterwarnings

# 忽略mysql警告信息
filterwarnings("ignore", category=pymysql.Warning)

class MysqlDb:

    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="root",db="xd_test_demo",charset="utf8")

        # 使用 cursor() 方法操作游标，得到一个可以执行的sql语句，并且操作结果作为字典返回的游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()

    # 查询
    def query(self, sql, state="all"):

        self.cur.execute(sql)
        if state == "all":
            # 查询全部
            data = self.cur.fetchall()
        else:
            # 查询单个
            data = self.cur.fetchone()

        return data

    # 更新、插入、删除
    def execut(self,sql):

        try:
            # 使用execute() 方法执行sql
            rows = self.cur.execute(sql)

            # 提交事务
            self.conn.commit()

            return rows

        except Exception as e:
            print("数据库操作异常{0}".format(e))
            # 回滚
            self.conn.rollback()

if __name__ == '__main__':

   mydb =  MysqlDb()
   # sql = "select * from test_case"
   # res = mydb.query(sql)
   # print(res)

   # sql = 'INSERT INTO test_case (app) VALUES("test");'
   sql = "delete from test_case where id in(11,12,13);"
   res = mydb.execut(sql)
   print(res)

