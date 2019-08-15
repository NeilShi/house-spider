import unittest
from flask import jsonify
from spider.community_spider import *


class TestSpider(unittest.TestCase):
    def test_community_spider(self):
        spider = CommunityBaseSpider()
        result = spider.start('cq', 'yubei', 'zhaomushan')
        jsonify(result)
        print(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
