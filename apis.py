from pytrends.request import TrendReq
import pycountry
from wikipediaapi import Wikipedia
from json import load


wiki = Wikipedia('RU')
pytrends = TrendReq()


country_list = load(open(pycountry.countries.filename))["3166-1"]
country_list = [
    {
        "name": country["name"].replace(" ", "_").lower() if country["name"] != "Russian Federation" else "russia",
        "code": country["alpha_2"],
    }
    for country in country_list
]
country_list.append({
    "name": "world",
    "code": "WR",
})


def name_from_region(region):
    country = pycountry.countries.get(alpha_2=region)
    country_name = country.name.replace(" ", "_").lower()
    if country_name == "russian_federation":
        country_name = "russia"
    if region == "WR":
        country_name = ""

    return country_name


def get_trending_searches(region):
    country_name = name_from_region(region)

    trends = pytrends.trending_searches(pn=country_name)
    trends_list = trends.to_dict(orient='list')[0]

    return trends_list


def get_interest_over_time(region, keyword, timeframe):
    if region == "WR":
        region = ""

    interest_pytrends = TrendReq()
    interest_pytrends.build_payload([keyword], geo=region, timeframe=timeframe)
    trends_dict = interest_pytrends.interest_over_time().to_dict(orient="split")
    trends_dict = [
        {
            "date": str(trends_dict["index"][q]),
            "popularity": trends_dict["data"][q][0],
        }
        for q in range(len(trends_dict["index"]))
    ]

    return trends_dict


def get_interest_over_time_multiple(region, keywords, timeframe):
    if region == "WR":
        region = ""

    interest_pytrends = TrendReq()
    interest_pytrends.build_payload(keywords, geo=region, timeframe=timeframe)
    trends_dict = interest_pytrends.interest_over_time().to_dict(orient="series")

    trends_dict = {
        keyword: [
            {
                "date": str(date),
                "popularity": trends_dict[keyword].to_dict()[date],
            }
            for date in trends_dict[keyword].to_dict()
        ]
        for keyword in trends_dict
    }

    return trends_dict


def get_related_searches(region, keyword, timeframe):
    if region == "WR":
        region = ""

    related_pytrends = TrendReq()
    related_pytrends.build_payload([keyword], geo=region, timeframe=timeframe)

    related_list = related_pytrends.related_topics()[keyword]["top"].to_dict(orient="records")
    related_list = [
        {
            "keyword": info["topic_title"],
            "type": info["topic_type"],
            "relation": info["value"],
        }
        for info in related_list
    ]

    return related_list


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


def get_all_regions():
    return country_list
