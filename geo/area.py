# coding = utf-8
# author: neil shi
# 板块信息相关函数

from geo.district import *
from const.xpath import *
from request.headers import *
from spider.base_spider import SPIDER_NAME


def get_district_url(city, district):
    """
    拼接指定城市的区县url
    :param city: 城市
    :param district: 区县
    :return:
    """
    return "http://{0}.{1}.com/xiaoqu/{2}".format(city, SPIDER_NAME, district)


def get_areas(city, district, for_dict):
    """
    通过城市和区县名获得下级板块名
    :param city: 城市
    :param district: 区县
    :param for_dict: 是否返回中英字典
    :return: 区县列表
    """
    page = get_district_url(city, district)
    areas = list()
    try:
        headers = create_headers()
        response = requests.get(page, timeout=10, headers=headers)
        html = response.content
        root = etree.HTML(html)
        links = root.xpath(DISTRICT_AREA_XPATH)

        # 针对a标签的list进行处理
        for link in links:
            relative_link = link.attrib['href']
            # 去掉最后的"/"
            relative_link = relative_link[:-1]
            # 获取最后一节
            area = relative_link.split("/")[-1]
            # 去掉区县名,防止重复
            if area != district:
                chinese_area = link.text
                chinese_area_dict[area] = chinese_area
                # print(chinese_area)
                areas.append(area)
        if for_dict:
            return chinese_area_dict
        else:
            return areas
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print(get_areas("cq", "yubei", False))

