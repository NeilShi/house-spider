import json
from flask import Flask, request
from spider.community_spider import *

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


if __name__ == '__main__':
    # 生产环境中务必去掉debug=True
    app.run(debug=True)
