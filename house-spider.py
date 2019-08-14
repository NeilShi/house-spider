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
    community_spider = CommunityBaseSpider()
    community_list = community_spider.start(request)
    response = app.response_class(
        response=json.dumps([community.__dict__ for community in community_list]),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
