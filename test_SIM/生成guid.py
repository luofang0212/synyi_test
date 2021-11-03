#!/usr/bin/env python
# -*- coding:utf-8 -*-


import random
import uuid

# bc2db0ac-9344-3829-4801-89438df4225b

def get_guid():

    name = 'test_name2'
    namespace = uuid.uuid1()
    # print(namespace)
    # print(uuid.uuid3(namespace, name))  # namespace 必须是UUID
    # print(uuid.uuid4())
    print(uuid.uuid5(namespace, name))


if __name__ == '__main__':
    for x in range(10):
         get_guid()