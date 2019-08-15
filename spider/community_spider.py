# coding = utf-8
# author: neil shi
# 此代码仅供学习与交流，请勿用于商业用途。
# 爬取小区数据的爬虫派生类

import re
from bs4 import BeautifulSoup
from model.community import *
from spider.base_spider import *
from geo.area import *
from utility.log import *


class CommunityBaseSpider(BaseSpider):
    def collect_area_community_data(self, city_name, district_name, area_name):
        """
        对于每个板块,获得这个板块下所有小区的信息
        :param city_name: 城市
        :param district_name: 区县
        :param area_name: 板块
        :return: community_list: 小区对象列表
        """
        # 开始获得需要的板块数据
        community_list = self.get_community_info(city_name, district_name, area_name)
        # 锁定
        if self.mutex.acquire(1):
            self.total_num += len(community_list)
            # 释放
            self.mutex.release()
        logger.info("Finish crawl area: " + area_name)
        return community_list

    @staticmethod
    def get_community_info(city, district, area):
        total_page = 1
        chinese_district = get_chinese_district(district)
        chinese_area = chinese_area_dict.get(area, "")
        community_list = list()
        page = 'http://{0}.{1}.com/xiaoqu/{2}/'.format(city, SPIDER_NAME, area)
        print(page)
        logger.info(page)

        headers = create_headers()
        response = requests.get(page, timeout=10, headers=headers)
        html = response.content
        soup = BeautifulSoup(html, "lxml")

        # 获得总的页数
        try:
            page_box = soup.find_all('div', class_='page-box')[0]
            matches = re.search('.*"totalPage":(\d+),.*', str(page_box))
            total_page = int(matches.group(1))
        except Exception as e:
            print("\tWarning: only find one page for {0}".format(area))
            print(e)

        # 从第一页开始,一直遍历到最后一页
        for i in range(1, total_page + 1):
            headers = create_headers()
            page = 'http://{0}.{1}.com/xiaoqu/{2}/pg{3}'.format(city, SPIDER_NAME, area, i)
            print(page)  # 打印版块页面地址
            BaseSpider.random_delay()
            response = requests.get(page, timeout=10, headers=headers)
            html = response.content
            soup = BeautifulSoup(html, "lxml")

            # 获得有小区信息的panel
            house_elem_list = soup.find_all('li', class_="xiaoquListItem")
            for house_elem in house_elem_list:
                price = house_elem.find('div', class_="totalPrice")
                name = house_elem.find('div', class_='title')
                on_sale = house_elem.find('div', class_="xiaoquListItemSellCount")

                # 继续清理数据
                price = price.text.strip()
                name = name.text.replace("\n", "")
                on_sale = on_sale.text.replace("\n", "").strip()

                # 作为对象保存
                community = Community(city, chinese_district, chinese_area, name, price, on_sale)
                community_list.append(community)
        return community_list

    def start(self, city, area, district):
        print('City: ', city)
        print('Area: ', area)
        print('District: ', district)

        # 生成中英文对照表
        get_districts(city)
        get_areas(city, district)
        return self.collect_area_community_data(city, district, area)


