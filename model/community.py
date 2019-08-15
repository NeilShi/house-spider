# coding=utf-8
# author: neil shi
# 小区信息的数据结构


class Community(object):
    def __init__(self, city, district, area, name, price, on_sale, month, year):
        self.city = city
        self.district = district
        self.area = area
        self.price = price
        self.name = name
        self.on_sale = on_sale
        self.month = month
        self.year = year

    def text(self):
        return self.city + "," + \
                self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.price + "," + \
                self.on_sale + "," + \
                self.month + "," + \
                self.year
