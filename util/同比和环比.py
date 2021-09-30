#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 同比增长率=(本期值 - 同期值)/同期值*100
def tongbi(benqiValue, tongqiValue):
    print("\n-------同比增长率----------")
    tongbi_rate = (benqiValue - tongqiValue) / tongqiValue * 100
    tonbi = benqiValue - tongqiValue
    print("本期值：{0}   同期值：{1}  同比增长：{2}  同比率：{3}".format(benqiValue, tongqiValue,tonbi, tongbi_rate))

    return tongbi_rate


# 环比增长率 = (本期值 - 上期值) / 上期值 * 100
def huanbi(benqiValue, shangqiValue):
    print("\n-------环比增长率----------")
    huanbi_rate = (benqiValue - shangqiValue) / shangqiValue * 100
    huanbi = benqiValue - shangqiValue
    print("本期值：{0}  上期值：{1}  环比增长：{2}  环比率：{3}".format(benqiValue, shangqiValue, huanbi,huanbi_rate))

    return huanbi_rate

if __name__ == '__main__':

    tongbi(417, 434)
    huanbi(417, 434)