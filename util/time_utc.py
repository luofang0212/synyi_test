#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta

import time

def utc_to_local(utc_st):
    '''UTC时间转本地时间（+8:00）'''
    now_stamp = time.time()
    local_time = datetime.fromtimestamp(now_stamp)
    utc_time = datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st

def local_to_utc(local_st):
   ''' 本地时间转UTC时间（-8:00）'''
   time_struct = time.mktime(local_st.timetuple())
   utc_st = datetime.utcfromtimestamp(time_struct)
   return utc_st

if __name__ == '__main__':

    # utc_time = datetime.now()
    utc_time_bak = '2021-09-07 16:00:00.000000'
    real_time = datetime.strptime(utc_time_bak, '%Y-%m-%d %H:%M:%S.%f')

    # # utc转本地
    # local_time = utc_to_local(time)
    # print (local_time.strftime('%Y-%m-%d %H:%M:%S.%f'))
    # # output：2014-09-18 18:42:16


    # 本地转utc
    utc_tran = local_to_utc(real_time)
    print (utc_tran.strftime("%Y-%m-%d %H:%M:%S.%f"))
