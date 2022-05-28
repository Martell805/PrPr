from pytrends.request import TrendReq
import pycountry
from wikipediaapi import Wikipedia


wiki = Wikipedia('ru')
pytrends = TrendReq()


def get_trending_searches(region):
    country = pycountry.countries.get(alpha_2=region)
    country_name = country.name.replace(" ", "_").lower()
    if country_name == "russian_federation":
        country_name = "russia"
    if region == "WR":
        country_name = ""

    trends = pytrends.trending_searches(pn=country_name)
    trends_list = trends.to_dict(orient='list')[0]

    return trends_list


def get_interest_over_time(region, keyword):
    if region == "WR":
        region = ""

    interest_pytrends = TrendReq()
    interest_pytrends.build_payload([keyword], geo=region, timeframe='today 3-m')
    trends_dict = interest_pytrends.interest_over_time().to_dict(orient="split")
    print(trends_dict)
    trends_dict = [
        {
            "date": str(trends_dict["index"][q]),
            "popularity": trends_dict["data"][q][0],
        }
        for q in range(len(trends_dict["index"]))]

    return trends_dict


def get_info(keyword):
    page = wiki.page(keyword)

    if not page.exists():
        page_dict = {
            "page_found": False,
        }
    else:
        page_dict = {
            "page_found": True,
            "short": page.summary.split("\n")[0],
            "full": page.summary,
        }

    return page_dict
