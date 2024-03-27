import requests
import json
import smtplib

#use PythonAnywhere to automate
#use twilio to use the paid api service

api_key = "db3b1ed117dc4300ec6904ca5bd2149f"
latitude = "33.68"
longitude = "73.04"

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?cnt=4&lat=33.68&lon=73.04&appid=db3b1ed117dc4300ec6904ca5bd2149f")
response.raise_for_status()
data = response.json()

json_object = json.dumps(data, indent=4)
 
# Writing to sample.json
with open("weather.json", "w") as outfile:
    outfile.write(json_object)

rain = False
clouds = False
clear = False

for i in range(4):
    list_length = len(data["list"][i]["weather"])
    for j in range(list_length):
        if (data["list"][i]["weather"][j]["id"]) < 700:
            rain = True
        if (data["list"][i]["weather"][j]["id"]) == 800:
            clear = True
        if (data["list"][i]["weather"][j]["id"]) > 800:
            clouds = True


Subject = ""
message = ""

if rain:
    message = "Bring an umbrella today!"
    Subject = "Rainy Weather ⛈️"
elif clouds:
    message = "Umbrella recommended!"
    Subject = "Cloudy Weather ☁️"
elif clear:
    message = "Clear skies today. No umbrella needed!"
    Subject = "Clear Weather"



my_email = "sender@gmail.com"
my_password = "password"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="receiver@gmail.com", msg=f"Subject:{Subject}\n\n{message}")
connection.close()

