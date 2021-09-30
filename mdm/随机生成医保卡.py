#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random


# 随机生成身份证号
def get_yibao_id():
    # 43 1021 19880604 1023
    province_id_data = [22, 33, 44, 55, 11, 66, 77, 88, 99, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    middle_num = random.randint(1000, 9999)

    year = random.randint(1970, 2020)
    month = random.randint(1, 12)
    data = random.randint(1, 28)

    if month <= 9:
        month = '0' + str(month)
    else:
        month = month

    if data <= 9:
        data = '0' + str(data)
    else:
        data = data

    get_birthday = str(month) + str(data)
    # print(get_birthday)

    final_num = str(random.randint(100, 999))
    final_text = str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    final_data = final_num + final_text

    id = random.randint(0,len(province_id_data))
    province_id = province_id_data[id]

    id_num = 'YB' + str(province_id) + str(middle_num) + get_birthday + final_data

    print(id_num)


if __name__ == '__main__':
    get_yibao_id()
