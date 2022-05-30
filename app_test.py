import requests
import json


if __name__ == '__main__':
    response = requests.get("http://127.0.0.1:5000/trending_searches/RU")
    print(response.content.decode())
    response = requests.get("http://127.0.0.1:5000/interest_over_time/US/Netflix/today 5-y")
    print(response.content.decode())
    response = requests.post("http://127.0.0.1:5000/interest_over_time_multiple/RU/today 12-m",
                             json=json.dumps(["KEK", "LOL"]))
    print(response.content.decode())
    response = requests.get("http://127.0.0.1:5000/info/Netflix")
    print(response.content.decode())
    response = requests.get("http://127.0.0.1:5000/full_info/WR/Netflix/now 7-d")
    print(response.content.decode())
    response = requests.get("http://127.0.0.1:5000/related_searches/RU/ксго/now 7-d")
    print(response.content.decode())
    response = requests.get("http://127.0.0.1:5000/all_regions")
    print(response.content.decode())
