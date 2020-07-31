#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Licensed under WTFPL or the Unlicense or CC0.
# This uses Python 3, but it's easy to port to Python 2 by changing
# strings to u'xx'.

"""
"""
import itertools

def num2chinese(num, big=False, simp=True, o=False, twoalt=False):
    """
    Converts numbers to Chinese representations.

    `big`   : use financial characters.
    `simp`  : use simplified characters instead of traditional characters.
    `o`     : use 〇 for zero.
    `twoalt`: use 两/兩 for two when appropriate.

    Note that `o` and `twoalt` is ignored when `big` is used, 
    and `twoalt` is ignored when `o` is used for formal representations.
    """
    # check num first
    nd = str(num)
    if abs(float(nd)) >= 1e48:
        raise ValueError('number out of range')
    elif 'e' in nd:
        raise ValueError('scientific notation is not supported')
    c_symbol = '正负点' if simp else '正負點'
    if o:  # formal
        twoalt = False
    if big:
        c_basic = '零壹贰叁肆伍陆柒捌玖' if simp else '零壹貳參肆伍陸柒捌玖'
        c_unit1 = '拾佰仟'
        c_twoalt = '贰' if simp else '貳'
    else:
        c_basic = '〇一二三四五六七八九' if o else '零一二三四五六七八九'
        c_unit1 = '十百千'
        if twoalt:
            c_twoalt = '两' if simp else '兩'
        else:
            c_twoalt = '二'
    c_unit2 = '万亿兆京垓秭穰沟涧正载' if simp else '萬億兆京垓秭穰溝澗正載'
    revuniq = lambda l: ''.join(k for k, g in itertools.groupby(reversed(l)))
    nd = str(num)
    result = []
    if nd[0] == '+':
        result.append(c_symbol[0])
    elif nd[0] == '-':
        result.append(c_symbol[1])
    if '.' in nd:
        integer, remainder = nd.lstrip('+-').split('.')
    else:
        integer, remainder = nd.lstrip('+-'), None
    if int(integer):
        splitted = [integer[max(i - 4, 0):i]
                    for i in range(len(integer), 0, -4)]
        intresult = []
        for nu, unit in enumerate(splitted):
            # special cases
            if int(unit) == 0:  # 0000
                intresult.append(c_basic[0])
                continue
            elif nu > 0 and int(unit) == 2:  # 0002
                intresult.append(c_twoalt + c_unit2[nu - 1])
                continue
            ulist = []
            unit = unit.zfill(4)
            for nc, ch in enumerate(reversed(unit)):
                if ch == '0':
                    if ulist:  # ???0
                        ulist.append(c_basic[0])
                elif nc == 0:
                    ulist.append(c_basic[int(ch)])
                elif nc == 1 and ch == '1' and unit[1] == '0':
                    # special case for tens
                    # edit the 'elif' if you don't like
                    # 十四, 三千零十四, 三千三百一十四
                    ulist.append(c_unit1[0])
                elif nc > 1 and ch == '2':
                    ulist.append(c_twoalt + c_unit1[nc - 1])
                else:
                    ulist.append(c_basic[int(ch)] + c_unit1[nc - 1])
            ustr = revuniq(ulist)
            if nu == 0:
                intresult.append(ustr)
            else:
                intresult.append(ustr + c_unit2[nu - 1])
        result.append(revuniq(intresult).strip(c_basic[0]))
    else:
        result.append(c_basic[0])
    if remainder:
        result.append(c_symbol[2])
        result.append(''.join(c_basic[int(ch)] for ch in remainder))
    return ''.join(result)



import re


def cjk_detect(texts):
    # korean
    if re.search("[\uac00-\ud7a3]", texts):
        return "ko"
    # japanese
    if re.search("[\u3040-\u30ff]", texts):
        return "ja"
    # chinese
    if re.search("[\u4e00-\u9FFF]", texts):
        return "zh"
    return None


def test_cjk_detect():
    # Pure English
    assert cjk_detect(
        "Is Obstruction an Impeachable Offense? History Says Yes") is None
    # Pure French
    assert cjk_detect(
        "Damian Lillard a réussi un nouveau shoot de la victoire"
        " au buzzer à très longue distance") is None
    # Simplified Chinese
    assert cjk_detect(
        "2009年，波音公司(Boeing)在查尔斯顿附近的新厂破土动工时，曾宣扬这里是最先进的制造中心"
        "，将制造一款世界上最先进的飞机。但在接下来的十年里，这家生产787梦想客机的工厂一直受到做"
        "工粗糙和监管不力的困扰，危及航空安全。") == "zh"
    # Traditional Chinese
    assert cjk_detect(
        "北查爾斯頓工廠的安全漏洞已經引起了航空公司和監管機構的密切關注。") == "zh"
    # Japanese
    assert cjk_detect(
        "日産自動車は24日、2019年3月期の連結業績予想を下方修正した。") == "ja"
    # Korean
    assert cjk_detect(
        "투서로 뜨고 투서에 지나") == "ko"
    # Korean with a Chinese character
    assert cjk_detect(
        "北 외무성 간부 총살설 주민들 사이서 확산…하노이 회담 실패 때문") == "ko"


def print_incorrect_cases():
    # Japanese
    texts = "日産自動車、営業益45%減　前期下方修正"
    print(texts, "expected: ja actual:", cjk_detect(texts))
    # Traditional Chinese with Japanese hiragana
    texts = "健康の油切 好吃の涼麵"
    print(texts, "expected: zh actual:", cjk_detect(texts))
    # Traditional Chinese with Japanese katakana punctuation
    texts = "鐵腕・都鐸王朝（五）：文藝復興最懂穿搭的高富帥——亨利八世"
    print(texts, "expected: zh actual:", cjk_detect(texts))


if __name__ == "__main__":
    # Correct cases
    test_cjk_detect()
    # Incorrect cases
    print_incorrect_cases()

    print(num2chinese(3456))