import requests
from datetime import datetime
import smtplib

MY_LAT = -48.0166
MY_LONG = -54.625

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(f"Lat: {iss_latitude}, Long: {iss_longitude}")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(f"Current time: {time_now}\nSunrise: {sunrise}")

if iss_latitude > MY_LAT - 5 and iss_latitude < MY_LAT + 5:
    if iss_longitude >  MY_LONG - 5 and iss_longitude < MY_LONG + 5:
        if  time_now.hour < sunrise or  time_now.hour > sunset:         
            my_email = "yourmail@gmail.com"
            my_password = "password"
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            message = f"""\
            Subject: Look Up! The ISS Is Near You!\n\nThe International Space Station (ISS) is passing by your location right now! It's {time_now}.
            Look up at the sky and see our beautiful planet from this unique perspective.
                                            """
            connection.sendmail(from_addr=my_email, to_addrs="receiver@gmail.com", msg= "Subject: Look Up! The ISS Is Near You!\n\nThe International Space Station (ISS) is passing by your location right now! It's {time_now}.Look up at the sky and see our beautiful planet from this unique perspective.")
            connection.close()
            print("Message sent!")
              


