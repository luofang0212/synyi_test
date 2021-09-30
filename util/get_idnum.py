#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


# 随机生成身份证号
class GetID():
    def get_idnum(self):
        # 43 1021 19880604 1023
        province_id_data = [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46, 50, 51,
                            52, 53, 54, 61, 62, 63, 65, 65, 81, 82, 83]

        middle_num = random.randint(1000, 9999)

        # year = random.randint(1970, 2020)
        # month = random.randint(1, 12)
        # data = random.randint(1, 28)
        #
        # if month <= 9:
        #     month = '0' + str(month)
        # else:
        #     month = month
        #
        # if data <= 9:
        #     data = '0' + str(data)
        # else:
        #     data = data
        #
        # get_birthday = str(year) + str(month) + str(data)
        get_birthday = self.get_birthdata()
        # print(get_birthday)

        final_num = str(random.randint(100, 999))
        final_text = str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 'X']))
        final_data = final_num + final_text

        m = random.randint(0, len(province_id_data) - 1)
        print(m,len(province_id_data))
        province_id = province_id_data[m]

        id_num = str(province_id) + str(middle_num) + get_birthday + final_data

        print(id_num)
        return id_num

    def get_birthdata(self):
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

        get_birthday = str(year) + str(month) + str(data)

        return get_birthday


if __name__ == '__main__':
    for x in range(150):
        GetID().get_idnum()
