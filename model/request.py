# coding = utf-8
# author: neil shi


class Request(object):
    def __init__(self, city, district, area):
        self.form = dict()
        self.form['city'] = city
        self.form['district'] = district
        self.form['area'] = area
