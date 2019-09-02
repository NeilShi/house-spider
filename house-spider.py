import json
from flask import Flask, request
from spider.community_spider import *
from geo.district import get_districts
from geo.area import get_areas

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/community', methods=['POST'])
def get_community():
    # error = None
    city = json.loads(request.get_data())['city']
    area = json.loads(request.get_data())['area']
    district = json.loads(request.get_data())['district']
    community_spider = CommunityBaseSpider()
    community_list = community_spider.start(city, area, district)
    response = app.response_class(
        response=json.dumps([community.__dict__ for community in community_list]),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/district', methods=['POST'])
def get_district():
    district_list = []
    city = json.loads(request.get_data())['city']
    district_cn_dict = get_districts(city, True)
    for item in district_cn_dict.items():
        district_list.append({item[0]: item[1]})
    response = app.response_class(
        response=json.dumps(district_list),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/area', methods=['POST'])
def get_area():
    area_list = []
    city = json.loads(request.get_data())['city']
    district = json.loads(request.get_data())['district']
    area_cn_dict = get_areas(city, district, True)
    for item in area_cn_dict.items():
        area_list.append({item[0]: item[1]})
    response = app.response_class(
        response=json.dumps(area_list),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    # 生产环境中务必去掉debug=True
    app.run(debug=True)
