import requests


if __name__ == '__main__':
    response = requests.get("http://127.0.0.1:5000/trending_searches/RU")
    print(response.content.decode())
    response = requests.get("http://127.0.0.1:5000/interest_over_time/US/Netflix")
    print(response.content.decode())
    response = requests.get("http://127.0.0.1:5000/info/Netflix")
    print(response.content.decode())
    response = requests.get("http://127.0.0.1:5000/full_info/WR/Netflix")
    print(response.content.decode())
    response = requests.get("http://127.0.0.1:5000/related_searches/RU/ксго")
    print(response.content.decode())
