from config import key
import requests
import time
import csv
url = f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2021-04-01/2022-04-01?adjusted=true&sort=asc&limit=300&apiKey={key}"

response = requests.get(url)
data = response.json()
results = data["results"]
lst = []
for day in results:
    print(day)
    price = day['c']
    temps = day['t']
    print(price)
    print(temps)
    date = time.strftime('%Y-%m-%d', time.localtime(temps/1000))
    print(date)

    dtdc = {"date": date,"price" : price}
    lst.append(dtdc)
print(lst)

with open("aapl.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile,fieldnames=["date", "price"])
    writer.writeheader()
    writer.writerows(lst)

url = f"https://api.polygon.io/v2/aggs/ticker/NFLX/range/1/day/2021-04-01/2022-04-01?adjusted=true&sort=asc&limit=300&apiKey={key}"

response = requests.get(url)
data = response.json()
results = data["results"]
lst = []
for day in results:
    print(day)
    price = day['c']
    temps = day['t']
    print(price)
    print(temps)
    date = time.strftime('%Y-%m-%d', time.localtime(temps/1000))
    print(date)

    dtdc = {"date": date,"price" : price}
    lst.append(dtdc)
print(lst)

with open("NFLX.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile,fieldnames=["date", "price"])
    writer.writeheader()
    writer.writerows(lst)

url = f"https://api.polygon.io/v2/aggs/ticker/COUR/range/1/day/2021-04-01/2022-04-01?adjusted=true&sort=asc&limit=300&apiKey={key}"

response = requests.get(url)
data = response.json()
results = data["results"]
lst = []
for day in results:
    print(day)
    price = day['c']
    temps = day['t']
    print(price)
    print(temps)
    date = time.strftime('%Y-%m-%d', time.localtime(temps/1000))
    print(date)

    dtdc = {"date": date,"price" : price}
    lst.append(dtdc)
print(lst)

with open("COUR.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile,fieldnames=["date", "price"])
    writer.writeheader()
    writer.writerows(lst)

url = f"https://api.polygon.io/v2/aggs/ticker/AMZN/range/1/day/2021-04-01/2022-04-01?adjusted=true&sort=asc&limit=300&apiKey={key}"

response = requests.get(url)
data = response.json()
results = data["results"]
lst = []
for day in results:
    print(day)
    price = day['c']
    temps = day['t']
    print(price)
    print(temps)
    date = time.strftime('%Y-%m-%d', time.localtime(temps/1000))
    print(date)

    dtdc = {"date": date,"price" : price}
    lst.append(dtdc)
print(lst)

with open("AMZN.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile,fieldnames=["date", "price"])
    writer.writeheader()
    writer.writerows(lst)

url = f"https://api.polygon.io/v2/aggs/ticker/GOOG/range/1/day/2021-04-01/2022-04-01?adjusted=true&sort=asc&limit=300&apiKey={key}"

response = requests.get(url)
data = response.json()
results = data["results"]
lst = []
for day in results:
    print(day)
    price = day['c']
    temps = day['t']
    print(price)
    print(temps)
    date = time.strftime('%Y-%m-%d', time.localtime(temps/1000))
    print(date)

    dtdc = {"date": date,"price" : price}
    lst.append(dtdc)
print(lst)

with open("GOOG", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile,fieldnames=["date", "price"])
    writer.writeheader()
    writer.writerows(lst)
