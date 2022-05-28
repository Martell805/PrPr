# VERSION 1.1

from flask import Flask
from json import dumps
from apis import *


app = Flask(__name__)


@app.route('/trending_searches/<string:region>', methods=['GET'])
def trending_searches(region):
    trends_list = get_trending_searches(region)
    trends_json = dumps(trends_list, ensure_ascii=False)

    return trends_json


@app.route('/interest_over_time/<string:region>/<string:keyword>', methods=['GET'])
def interest_over_time(region, keyword):
    trends_list = get_interest_over_time(region, keyword)
    trends_json = dumps(trends_list, ensure_ascii=False)

    return trends_json


@app.route('/info/<string:keyword>', methods=['GET'])
def info(keyword):
    page_dict = get_info(keyword)

    page_json = dumps(page_dict, ensure_ascii=False)

    return page_json


@app.route('/full_info/<string:region>/<string:keyword>')
def full_info(region, keyword):
    full_dict = get_info(keyword)

    full_dict["graph"] = get_interest_over_time(region, keyword)

    return dumps(full_dict, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
