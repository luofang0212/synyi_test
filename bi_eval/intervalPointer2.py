#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bi_eval.score_color import to_color
'''
区间指标-情况2
    当 实际值<参考值下限,  则 指标得分=0分，
    当 实际值>参考值上限, 则 指标得分=分值权重满分*150%,
    当 参考值下限<=实际值<=参考值上限，则指标得分= (实际值-参考值下限)/(参考值上限-参考值下限)*分值权重满分*150%
'''

# 实际值
actual_value = 76000.79

# 参考值
reference_value = 70000
# 浮动范围
domain_of_walker = -5000
referenceValueMin = 0
referenceValueMax = 0

print("区间值[{0},{1}]".format(referenceValueMin,referenceValueMax))

# 分值
score = 1000
# 分值权重
score_weight = 0.3
# 分值权重满分:指标分值
full_score = score * score_weight
print("实际值：{0}  参考值：[{1},{2}]  分值权重满分(指标分值)：{3}".format(actual_value,referenceValueMin,referenceValueMax,full_score))

# 指标得分
index_score = 0

# 实际值<参考值下限
if (actual_value < referenceValueMin):
    # 指标得分=0分
    index_score = 0
    print("1指标得分= {0}".format(index_score))
    to_color(index_score,score,full_score)
# 实际值>参考值上限
elif (actual_value > referenceValueMax):
    # 指标得分=分值权重满分*150%
    index_score = full_score * 1.5
    print("2指标得分= {0}".format(index_score))
    to_color(index_score,score,full_score)
# 参考值下限<=实际值<=参考值上限
elif (referenceValueMin <= actual_value <= referenceValueMax):
    # 指标得分= (实际值-参考值下限)/(参考值上限-参考值下限)*分值权重满分*150%
    index_score = (actual_value - referenceValueMin) / (referenceValueMax - referenceValueMin) * full_score * 1.5
    print("3指标得分= {0}".format(index_score))
    to_color(index_score,score,full_score)
