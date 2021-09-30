#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bi_eval.score_color import to_color
'''
区间指标-情况1
    当实际值在区间范围内，则指标得分=分值权重满分，
        否则 (分值权重满分-偏离值）>=0,
        则 指标得分= (分值权重满分-偏离值），否则 指标得分=0。
'''

# 实际值
actual_value = 106.59
# print("实际值：{0}".format(actual_value))actual_value

# 参考值
reference_value = 94.50
# # 浮动范围
# domain_of_walker = 8.5

referenceValueMin = 0
referenceValueMax = 0
# print("区间值[{0},{1}]".format(referenceValueMin, referenceValueMax))

# 分值
score = 100
# 分值权重
score_weight = 0.2
# 分值权重满分：指标分值
full_score = score * score_weight
print("实际值：{0}  参考值：[{1},{2}]  分值权重满分(指标分值)：{3}".format(actual_value,referenceValueMin,referenceValueMax,full_score))

# 指标得分
index_score = 0

# 指定比率 150%
mack = 1.5


# 实际值在区间范围内
if (referenceValueMin <= actual_value <= referenceValueMax):
    #指标得分=分值权重满分
    index_score = full_score
    print("1指标得分= {0}".format(index_score))
    to_color(index_score,score,full_score)

else:
    # 实际值<参考值下限
    if(actual_value<referenceValueMin):
         # 偏离值=（实际值-参考值）的绝对值
        off_center = abs(actual_value-referenceValueMin)
        print("1偏离值：{0}".format(off_center))
    elif (actual_value > referenceValueMax):
        # 偏离值=（实际值-参考值）的绝对值
        off_center = abs(actual_value - referenceValueMax)
        print("2偏离值：{0}".format(off_center))

    if((full_score-off_center) >= 0 ):
        #指标分值= (分值权重满分-偏离值）
        index_score = full_score - off_center
        print("2指标得分= {0}".format(index_score))
        to_color(index_score,score,full_score)
    else:
        # 指标得分 = 0
        index_score = 0
        print("3指标得分= {0}".format(index_score))
        to_color(index_score,score,full_score)