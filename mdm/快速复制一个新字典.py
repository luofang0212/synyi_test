#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mdm.dbPlsql_util_system import PLSqlSystem
import uuid

mysql = PLSqlSystem()

def copy_dict():

    sql_1 = '''select * from mdm.property where "CodeSystemId"='23f6e2de-6444-430e-837f-6b78b076c65e';
            '''
    property_data = mysql.query(sql_1)
    print(property_data[0])

    for x in range(len(property_data[0])):
        name = 'test_name1'
        namespace = uuid.uuid1()
        guid = uuid.uuid5(namespace, name)

        CodeSystemId='78783cf0-1245-5cb5-b6b1-3b30f8b5bd1a'
        Code = property_data[x][4]
        Type = property_data[x][6]
        Name = property_data[x][7]
        RowNo = property_data[x][9]
        Extension = str(property_data[x][8])
        print(Extension)


        sql_2 = '''
        INSERT INTO mdm.property ("Id", "CreateTime", "LastUpdateTime", "VersionId", "Code", "Uri", "Type", "Name", "CodeSystemId", "Extension", "RowNo") VALUES ('%s', '2021-10-09 11:36:53.154771', '2021-10-11 08:43:00.295325', 1, '%s', null, 2, '%s', '%s', '%s', %s);
        '''%(guid,CodeSystemId,Code,Type,Name,Extension,RowNo)
        mysql.insert(sql_2)
        print(x)


if __name__ == '__main__':
    copy_dict()