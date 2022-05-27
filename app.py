from flask import Flask
from pytrends.request import TrendReq
from json import dumps
import pycountry

app = Flask(__name__)


@app.route('/trending_searches/<string:region>', methods=['GET'])
def trending_searches(region):
    country = pycountry.countries.get(alpha_2=region)
    country_name = country.name.replace(" ", "_").lower()
    if country_name == "russian_federation":
        country_name = "russia"

    pytrends = TrendReq()
    trends = pytrends.trending_searches(pn=country_name)
    trends_list = trends.to_dict(orient='list')[0]
    trends_json = dumps(trends_list, ensure_ascii=False)

    return trends_json


@app.route('/interest_over_time/<string:region>/<string:keyword>', methods=['GET'])
def interest_over_time(region, keyword):
    pytrends = TrendReq()
    pytrends.build_payload([keyword], geo=region, timeframe='today 3-m')
    trends_dict = pytrends.interest_over_time().to_dict(orient="index")
    trends_dict = {time.to_pydatetime().isoformat(): trends_dict[time][keyword] for time in trends_dict}
    trends_json = dumps(trends_dict, ensure_ascii=False)

    return trends_json


if __name__ == '__main__':
    app.run()
