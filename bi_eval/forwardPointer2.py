#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bi_eval.score_color import to_color

'''
正向指标-情况2
    当实际值<10, 则 指标分值=0分，
    当实际值>=10 ，则
       当（实际值/参考值)>=150%
           则 指标分值=分值权重满分*150%，
           否则：指标分值= (实际值/参考值)*分值权重满分）
'''

# 实际值
actual_value = 119.00
# 参考值
reference_value = 350.08

# 分值
score = 100
# 分值权重
score_weight = 0.3
# 分值权重满分：指标分值
full_score = score * score_weight
print("实际值：{0}  参考值：{1}  分值权重满分(指标分值)：{2}".format(actual_value, reference_value, full_score))

# 浮动范围
domain_of_walker = 0

# 指标得分
index_score = 0


print("实际值：{0}".format(actual_value))


# 当实际值<10, 则 指标分值=0分
if (actual_value < 10):
    # 指标分值=0分
    index_score = 0
    print("1指标得分= {0}".format(index_score))
    to_color(index_score, score, full_score)
# 当实际值 >= 10
elif (actual_value >= 10):
    # 实际值/参考值
    result = actual_value / reference_value
    print("比率：{0}".format(result))
    # （实际值 / 参考值) >= 150 %
    if (result >= 1.5):
        # 指标分值=分值权重满分*150%，
        index_score = full_score * 1.5
        print("2指标得分= {0}".format(index_score))
        to_color(index_score,score,full_score)
    else:
        # 指标分值= (实际值/参考值)*分值权重满分
        index_score = (actual_value / reference_value) * full_score
        print("3指标得分= {0}".format(index_score))
        to_color(index_score,score,full_score)