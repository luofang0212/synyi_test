#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bi_eval.score_color import to_color
'''
适中指标-情况1
    当  实际值<参考值，
        则 指标得分 = (实际值/参考值)*分值权重满分，
         否则 指标得分 = (参考值/实际值)*分值权重满分
'''

# 实际值
actual_value = 1000

# 参考值
reference_value = 1500
# 浮动范围
domain_of_walker = 0

# 分值
score = 100
# 分值权重
score_weight = 0.3
# 分值权重满分：指标分值
full_score = score * score_weight
print("实际值：{0}  参考值：{1}  分值权重满分(指标分值)：{2}".format(actual_value, reference_value, full_score))

# 指标分值
index_score = 0


# 实际值<参考值下限
if (actual_value < reference_value):
    # 指标得分 = (实际值/参考值)*分值权重满分
    index_score = (actual_value / reference_value) * full_score
    print("1指标得分= {0}".format(index_score))
    to_color(index_score,score,full_score)
else:
    # 指标得分 = (参考值/实际值)*分值权重满分
    index_score = (reference_value / actual_value) * full_score
    print("2指标得分= {0}".format(index_score))
    to_color(index_score,score,full_score)
