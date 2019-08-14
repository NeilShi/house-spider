import unittest
from flask import jsonify
from model.request import *
from spider.community_spider import *


class TestSpider(unittest.TestCase):
    def test_community_spider(self):
        req = Request('cq', 'yubei', 'zhaomushan')
        spider = CommunityBaseSpider()
        result = spider.start(req)
        jsonify(result)
        print(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
