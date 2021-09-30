#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


# 封装http request请求方式
class HttpRequest:

    def http_request(self, method, url, data=None, headers=None, cookies=None, verify=False):

        if method.lower() == 'get':
            res = requests.get(url, data, headers=headers, cookies=cookies)

        elif method.lower() == 'post':
            res = requests.post(url, data, headers=headers, cookies=cookies)

        elif method.lower() == 'put':
            res = requests.post(url, data, headers=headers, cookies=cookies)
        else:
            try:
                print("不支持该方法")
            except Exception as e:
                print(e)
                raise (e)
        return res


if __name__ == '__main__':
    # post 登陆接口
    login_url = 'https://api.xdclass.net/pub/api/v1/web/web_login'
    login_data = {'phone': '17267723687', 'pwd': 'love920212'}
    res_1 = HttpRequest().http_request('post', login_url, login_data)
    print("登录接口响应信息： ", res_1.json())
    print(100 * '-')
    data = res_1.json()

    # 获取用户token
    user_token = data['data']['token']
    # print(user_token)

    # get  用户信息接口
    user_url = 'https://api.xdclass.net/pub/api/v1/web/user_info'
    user_data = {}
    headers = {
        'token': '{0}'.format(user_token)
    }
    res_2 = HttpRequest().http_request('geT', user_url, headers=headers)
    print("用户信息接口响应信息： ", res_2.json())

    print(res_2.text)
    print(res_2.content)

