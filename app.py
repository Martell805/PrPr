# VERSION 1.5

from flask import Flask, request
from json import dumps, loads
from apis import *


app = Flask(__name__)


@app.route('/trending_searches/<string:region>', methods=['GET'])
def trending_searches(region):
    trends_list = get_trending_searches(region)
    trends_json = dumps(trends_list, ensure_ascii=False)

    return trends_json


@app.route('/interest_over_time/<string:region>/<string:keyword>/<string:timeframe>', methods=['GET'])
def interest_over_time(region, keyword, timeframe):
    trends_list = get_interest_over_time(region, keyword, timeframe)
    trends_json = dumps(trends_list, ensure_ascii=False)

    return trends_json


@app.route('/interest_over_time_multiple/<string:region>/<string:timeframe>', methods=['POST'])
def interest_over_time_multiple(region, timeframe):
    trends_list = get_interest_over_time_multiple(region, loads(request.json), timeframe)
    trends_json = dumps(trends_list, ensure_ascii=False)

    return trends_json


@app.route('/related_searches/<string:region>/<string:keyword>/<string:timeframe>', methods=['GET'])
def related_searches(region, keyword, timeframe):
    relation_list = get_related_searches(region, keyword, timeframe)
    relation_json = dumps(relation_list, ensure_ascii=False)

    return relation_json


@app.route('/info/<string:keyword>', methods=['GET'])
def info(keyword):
    page_dict = get_info(keyword)
    page_json = dumps(page_dict, ensure_ascii=False)

    return page_json


@app.route('/full_info/<string:region>/<string:keyword>/<string:timeframe>')
def full_info(region, keyword, timeframe):
    full_dict = get_info(keyword)
    full_dict["graph"] = get_interest_over_time(region, keyword, timeframe)
    full_json = dumps(full_dict, ensure_ascii=False)

    return full_json


@app.route('/all_regions')
def all_regions():
    regions_list = get_all_regions()
    regions_json = dumps(regions_list, ensure_ascii=False)

    return regions_json


if __name__ == '__main__':
    app.run()
