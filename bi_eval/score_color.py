#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
    指标得分>=指标分值，则为绿色。
    指标分值*60%<=指标得分<=指标分值,则为蓝色。
    指标得分<指标分值*60%,则为黄色。
'''


# 指标得分
# index_score = 0
#
# # 分值
# score = 0
# # 分值权重
# score_weight = 0
# # 分值权重满分:指标分值
# full_score = score * score_weight

def to_color(index_score, score, full_score):

    # 指标得分>=指标分值，则为绿色
    if (index_score >= full_score):
        print("指标得分>=指标分值： 显示绿色")

    # 指标分值*60%<=指标得分<=指标分值,则为蓝色
    elif (full_score * 0.6 <= index_score <= full_score):
        print("指标分值*60%<=指标得分<=指标分值： 显示蓝色")

    # 指标得分<指标分值*60%,则为黄色
    elif (index_score < full_score * 0.6):
        print("指标得分<指标分值*60%： 显示黄色")
