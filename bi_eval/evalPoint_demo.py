#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bi_eval.score_color import to_color

'''
 score分值,score_weight分值权重,domain_of_walker浮动范围,actual_value实际值,reference_value参考值
'''

'''
正向指标-情况1
    当（实际值/参考值)>=150% ，则 指标分值=分值权重满分*150%
    否则 指标分值=(实际值/参考值)*分值权重满分
'''


def forwrd_1(score, score_weight, actual_value, reference_value):
    print("\n-------------正向指标-情况1------------------")
    # 分值权重满分（指标分值）
    full_score = score * score_weight
    print("实际值：{0}  参考值：{1}  分值权重满分(指标分值)：{2}".format(actual_value, reference_value, full_score))

    # 比率：实际值/参考值
    result = actual_value / reference_value
    print("比率：{0}".format(result))

    # （实际值/参考值)>=150%
    if (result >= 1.5):
        # 指标得分=分值权重满分*150%
        index_score = full_score * 1.5
        print("1指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)
    else:
        # 指标得分=(实际值/参考值)*分值权重满分
        index_score = (actual_value / reference_value) * full_score
        print("2指标得分= {0}".format(index_score))
        # index_score1 = actual_value  * full_score / reference_value
        # print("2-1指标得分= {0}".format(index_score1))
        to_color(index_score, score, full_score)


'''
正向指标-情况2
    当实际值<10, 则 指标分值=0分，
    当实际值>=10 ，则
       当（实际值/参考值)>=150%
           则 指标分值=分值权重满分*150%，
           否则：指标分值= (实际值/参考值)*分值权重满分）
'''


def forwrd_2(score, score_weight, actual_value, reference_value):
    print("\n-------------正向指标-情况2------------------")

    # 分值权重满分：指标分值
    full_score = score * score_weight
    print("实际值：{0}  参考值：{1}  分值权重满分(指标分值)：{2}".format(actual_value, reference_value, full_score))

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
            to_color(index_score, score, full_score)
        else:
            # 指标分值= (实际值/参考值)*分值权重满分
            index_score = (actual_value / reference_value) * full_score
            print("3指标得分= {0}".format(index_score))
            to_color(index_score, score, full_score)


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


def forwrd_3(score, score_weight, actual_value, reference_value):
    print("\n-------------正向指标-情况3------------------")

    # 分值权重满分：指标分值
    full_score = score * score_weight
    print("实际值：{0}  参考值：{1}  分值权重满分(指标分值)：{2}".format(actual_value, reference_value, full_score))

    # 当实际值>=65%
    if (actual_value >= 0.65):
        # 实际值/参考值
        result = actual_value / reference_value
        print("比率：{0}".format(result))

        if (result >= 1.5):
            # 指标得分=分值权重满分*150%
            index_score = full_score * 1.5
            print("1指标得分= {0}".format(index_score))
            to_color(index_score, score, full_score)
        else:
            # 指标得分=(实际值/参考值)*分值权重满分
            index_score = (actual_value / reference_value) * full_score
            print("2指标得分= {0}".format(index_score))
            to_color(index_score, score, full_score)

    # 当实际值<65%
    elif (actual_value < 0.65):
        # 实际值<参考值
        if (actual_value < reference_value):
            # 指标分值= (实际值/参考值)*分值权重满分/2
            index_score = (actual_value / reference_value) * full_score / 2
            print("3指标得分= {0}".format(index_score))
            to_color(index_score, score, full_score)
        else:
            # 实际值>=2*参考值
            if (actual_value >= (2 * reference_value)):
                # 指标分值=分值权重满分
                index_score = full_score
                print("4指标得分= {0}".format(index_score))
                to_color(index_score, score, full_score)
            else:
                # 指标分值= (实际值/参考值)*分值权重满分/2)
                index_score = (actual_value / reference_value) * full_score / 2
                print("5指标得分= {0}".format(index_score))
                to_color(index_score, score, full_score)


'''
正向指标-情况4
    当实际值<=-100%, 则 指标得分=0分，
    否则，
        当 实际值>50%，则指标得分=分值权重满分*150%
                    否则指标得分=分值权重*(100%+实际值)

'''


def forwrd_4(score, score_weight, actual_value, reference_value):
    print("\n-------------正向指标-情况4------------------")
    # 分值权重满分：指标分值
    full_score = score * score_weight
    print("实际值：{0}  参考值：{1}  分值权重满分(指标分值)：{2}".format(actual_value, reference_value, full_score))

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


'''
负向指标-情况1
    当(参考值/实际值)>=150% ，
        则指标得分=分值权重满分*150%
        否则指标得分= (参考值/实际值)*分值权重满分
'''


def negative_1(score, score_weight, actual_value, reference_value):
    print("\n-------------负向指标-情况1------------------")
    # 分值权重满分：指标分值
    full_score = score * score_weight
    print("实际值：{0}  参考值：{1}  分值权重满分(指标分值)：{2}".format(actual_value, reference_value, full_score))

    result = reference_value / actual_value
    print("比率：{0}".format(result))

    if (result >= 1.5):
        # 指标得分=分值权重满分*150%
        index_score = full_score * 1.5
        print("1指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)
    else:
        # 则指标得分= (参考值/实际值)*分值权重满分
        index_score = (reference_value / actual_value) * full_score
        print("2指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)


'''
区间指标-情况1
    当实际值在区间范围内，则指标得分=分值权重满分，
        否则 (分值权重满分-偏离值）>=0,
        则 指标得分= (分值权重满分-偏离值），否则 指标得分=0。
'''


def interval_1(score, score_weight, actual_value, referenceValueMin, referenceValueMax):
    print("\n-------------区间指标-情况1------------------")
    # 分值权重满分：指标分值
    full_score = score * score_weight
    print("实际值：{0}  参考值：[{1},{2}]  分值权重满分(指标分值)：{3}".format(actual_value, referenceValueMin, referenceValueMax,
                                                            full_score))

    # 实际值在区间范围内
    if (referenceValueMin <= actual_value <= referenceValueMax):
        # 指标得分=分值权重满分
        index_score = full_score
        print("1指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)

    else:
        # 实际值<参考值下限
        if (actual_value < referenceValueMin):
            # 偏离值=（实际值-参考值）的绝对值
            off_center = abs(actual_value - referenceValueMin)
            print("1偏离值：{0}".format(off_center))
        elif (actual_value > referenceValueMax):
            # 偏离值=（实际值-参考值）的绝对值
            off_center = abs(actual_value - referenceValueMax)
            print("2偏离值：{0}".format(off_center))

        if ((full_score - off_center) >= 0):
            # 指标得分 = (分值权重满分 - 偏离值）
            index_score = full_score - off_center
            print("2指标得分= {0}".format(index_score))
            to_color(index_score, score, full_score)
        else:
            # 指标得分 = 0
            index_score = 0
            print("3指标得分= {0}".format(index_score))
            to_color(index_score, score, full_score)


'''
区间指标-情况2
    当 实际值<参考值下限,  则 指标得分=0分，
    当 实际值>参考值上限, 则 指标得分=分值权重满分*150%,
    当 参考值下限<=实际值<=参考值上限，则指标得分= (实际值-参考值下限)/(参考值上限-参考值下限)*分值权重满分*150%
'''


def interval_2(score, score_weight, actual_value, referenceValueMin, referenceValueMax):
    print("\n-------------区间指标-情况2------------------")
    # 分值权重满分：指标分值
    full_score = score * score_weight

    print("实际值：{0}  参考值：[{1},{2}]  分值权重满分(指标分值)：{3}".format(actual_value, referenceValueMin, referenceValueMax,
                                                            full_score))

    # 实际值<参考值下限
    if (actual_value < referenceValueMin):
        # 指标得分=0分
        index_score = 0
        print("1指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)
    # 实际值>参考值上限
    elif (actual_value > referenceValueMax):
        # 指标得分=分值权重满分*150%
        index_score = full_score * 1.5
        print("2指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)
    # 参考值下限<=实际值<=参考值上限
    elif (referenceValueMin <= actual_value <= referenceValueMax):
        # 指标得分= (实际值-参考值下限)/(参考值上限-参考值下限)*分值权重满分*150%
        index_score = (actual_value - referenceValueMin) / (referenceValueMax - referenceValueMin) * full_score * 1.5
        print("3指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)


'''
适中指标-情况1
    当  实际值<参考值，
        则 指标得分 = (实际值/参考值)*分值权重满分，
         否则 指标得分 = (参考值/实际值)*分值权重满分
'''


def middle_1(score, score_weight, actual_value, reference_value):
    print("\n-------------适中指标-情况1------------------")
    # 分值权重满分：指标分值
    full_score = score * score_weight
    print("实际值：{0}  参考值：{1}  分值权重满分(指标分值)：{2}".format(actual_value, reference_value, full_score))

    # 实际值<参考值下限
    if (actual_value < reference_value):
        # 指标得分 = (实际值/参考值)*分值权重满分
        index_score = (actual_value / reference_value) * full_score
        print("1指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)
    else:
        # 指标得分 = (参考值/实际值)*分值权重满分
        index_score = (reference_value / actual_value) * full_score
        print("2指标得分= {0}".format(index_score))
        to_color(index_score, score, full_score)
