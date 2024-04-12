import requests
import json
import math
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

direction = "🔺"
worth = False

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + STOCK_NAME + '&interval=5min&apikey=your_api'
r = requests.get(url)
data = r.json()["Time Series (Daily)"]

with open("data.json", "w") as file:
    json.dump(data, file)

data_list = [value for (key, value) in data.items()]
yesterday_closing = data_list[0]["4. close"]
print(f"yesterday closing: {yesterday_closing}")

day_before_yesterday_closing = data_list[1]["4. close"]
print(f"day before yesterday closing: {day_before_yesterday_closing}")


positive_difference = float(yesterday_closing) - float(day_before_yesterday_closing)
if positive_difference < 0:
    positive_difference *= -1
    direction = "🔻"


percent_difference = (positive_difference / float(yesterday_closing)) * 100
print(percent_difference)

api_key = "your_api"

if percent_difference >= 5: 
    url = "https://newsapi.org/v2/everything?q=tesla&from=2024-03-12&sortBy=publishedAt&apiKey=" + api_key
    r = requests.get(url)
    data = r.json()

    with open("news.json", "w") as file:
        json.dump(data, file)

    articles = data["articles"][:3]

    with open("articles.json", "w") as file:
        json.dump(articles, file)

    worth = True


article_desc = []
for i in range(3):
    article_desc.append((articles[i]["title"], articles[i]["description"]))

print(article_desc)

msgs = []

for i in range(3):
    msg = f"""
    {STOCK_NAME}: {direction}{math.floor(percent_difference)}%
    Headline: {article_desc[i][0]}
    Brief: {article_desc[i][1]}
    """
    msgs.append(msg)


my_email = "mail@gmail.com"
my_password = "password"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)

if worth:
    for i in range(3):
        connection.sendmail(from_addr=my_email, to_addrs="mail@gmail.com", msg= f"Subject: Stock News!\n\n{msgs[i]}")

connection.close()
print("Msgs sent!")
