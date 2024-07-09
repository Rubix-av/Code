import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Joe", "views":10000},
        {"likes": 10000, "name": "How to make REST APIs", "views":80000},
        {"likes": 35, "name": "Tim", "views":2000},
        {"likes": 23487234, "name": "How to fly dog", "views": 13413413}]


for i in range(len(data)):
    response = requests.put(BASE + f"video/{i}", json=data[i])
    print(response.json())
input()
response = requests.get(BASE + "video/0")
print(response.json())
input()
response = requests.get(BASE + "video/1")
print(response.json())
input()
response = requests.get(BASE + "video/2")
print(response.json())
input()
response = requests.get(BASE + "video/3")
print(response.json())