import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 24.713552
MY_LONG = 46.675297

# Set up email credentials
MY_EMAIL = "ramisassaf132@gmail.com"
PASSWORD = "dmwe xrhh emmd nofs"

# BONUS: run the code every 60 seconds.
def every_60_seconds():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    def iss_overhead():
        if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True

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

    # If the ISS is close to my current position
    if iss_overhead() and (time_now.hour > sunset or time_now.hour < sunrise):
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Start TLS encryption
            connection.starttls()
            # Log in to the email account
            connection.login(user=MY_EMAIL, password=PASSWORD)
            # Send the email with the selected letter contents
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look up! \n\nThe ISS is above you in the sky!".encode("utf-8"))


while True:
    every_60_seconds()
    time.sleep(60)


