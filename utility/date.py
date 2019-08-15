# coding = utf-8
# author: neil shi
# 日期和时间的字符串辅助函数

import time
from datetime import date


def get_time_string():
    """
    获得形如20161010120000这样的年月日时分秒字符串
    :return:
    """
    current = time.localtime()
    return time.strftime("%Y%m%d%H%M%S", current)


def get_date_string():
    """
    获得形如20161010这样的年月日字符串
    :return:
    """
    current = time.localtime()
    return time.strftime("%Y%m%d", current)


def get_year_month_string():
    """
    获得形如201610这样的年月字符串
    :return:
    """
    current = time.localtime()
    return time.strftime("%Y%m", current)


def get_month(price_desc):
    """
    获得爬取数据的月份
    形如 7月二手房均价 的 7
    :return: month
    """
    if price_desc[0].isdecimal():
        month = int(price_desc[0])
    else:
        month = date.today().month - 1
    return month


def get_year(month):
    """
    获得爬取数据的年份
    如果是1月爬取到去年12月的数据
    会有特殊逻辑处理
    :return: year
    """
    real_month = date.today().month
    if month > real_month:
        year = date.today().year - 1
    else:
        year = date.today().year
    return year


if __name__ == "__main__":
    print(get_date_string())
