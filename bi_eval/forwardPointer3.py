#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bi_eval.score_color import to_color

'''
正向指标-情况3
    当实际值>=65%,
         当 (实际值/参考值)>150%，
             则 指标分值=分值权重满分*150%，
             否则 指标分值=(实际值/参考值)*分值权重满分)
    当实际值<65%,
     当 (实际值<参考值)，
            则 指标分值= (实际值/参考值)*分值权重满分/2， 
         否则:
                当实际值>=2*参考值,
                    则 指标分值=分值权重满分，
                    否则目标分值= (实际值/参考值)*分值权重满分/2)
'''

# 实际值
actual_value = 56.59
# 参考值
reference_value = 64.66

# 分值
score = 100
# 分值权重
score_weight = 0.5
# 分值权重满分:指标分值
full_score = score * score_weight
print("实际值：{0}  参考值：{1}  分值权重满分(指标分值)：{2}".format(actual_value, reference_value, full_score))

# 浮动范围
domain_of_walker = 0

# 指标得分
index_score = 0

# 指定比率 150%
mack = 1.5

print("实际值：{0}".format(actual_value))

# 当实际值>=65%
if (actual_value >= 0.65):
    # 实际值/参考值
    result = actual_value / reference_value
    print("比率：{0}".format(result))

    if (result >= 1.5):
        # 指标得分=分值权重满分*150%
        index_score = full_score * 1.5
        print("1指标得分= {0}".format(index_score))
        to_color(index_score,score,full_score)
    else:
        # 指标得分=(实际值/参考值)*分值权重满分
        index_score = (actual_value / reference_value) * full_score
        print("2指标得分= {0}".format(index_score))
        to_color(index_score,score,full_score)

# 当实际值<65%
elif (actual_value < 0.65):
    # 实际值<参考值
    if (actual_value < reference_value):
        # 指标分值= (实际值/参考值)*分值权重满分/2
        index_score = (actual_value / reference_value) * full_score / 2
        print("3指标得分= {0}".format(index_score))
        to_color(index_score,score,full_score)
    else:
        # 实际值>=2*参考值
        if (actual_value >= (2 * reference_value)):
            # 指标分值=分值权重满分
            index_score = full_score
            print("4指标得分= {0}".format(index_score))
            to_color(index_score,score,full_score)
        else:
            # 指标分值= (实际值/参考值)*分值权重满分/2)
            index_score = (actual_value / reference_value) * full_score / 2
            print("5指标得分= {0}".format(index_score))
            to_color(index_score,score,full_score)
