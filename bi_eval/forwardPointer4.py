#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bi_eval.score_color import to_color

'''
正向指标-情况4
    当实际值<=-100%, 则 指标得分=0分，
    否则，
        当 实际值>50%，则指标得分=分值权重满分*150%
                    否则指标得分=分值权重*(100%+实际值)

'''

# 实际值
actual_value = 0.23
# 参考值
reference_value = 0

# 分值
score = 100
# 分值权重
score_weight = 1
# 分值权重满分：指标分值
full_score = score * score_weight
print("分值权重满分(指标分值)：{0}".format(full_score))

# 浮动范围
domain_of_walker = 0

# 指标得分
index_score = 0

# 指定比率 150%
mack = 1.5

print("实际值：{0}".format(actual_value))

# 当实际值<=-100%, 则 指标得分=0分，
if (actual_value <= -1):
    # 指标得分=0
    index_score = 0
    print("1指标得分= {0}".format(index_score))
    to_color(index_score, score, full_score)
else:
    # 实际值 > 50 %
    if (actual_value > 0.5):
        # 指标得分 = 分值权重满分 * 150 %
        index_score = full_score * 1.5
        print("2指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)
    else:
        # 指标得分 = 分值权重满分 * (100 % +实际值)
        index_score = full_score * (1 + actual_value)
        print("3指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)
