import smtplib
import datetime as dt
import random

def send_email(quote):
    my_email = "pyjhen@hotmail.com"
    password = "py123456"

    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="pyjhen@gmail.com",
                            msg=f"Subject:Hello\n\n{quote}"
                            )

with open("quotes.txt") as data:
    data = data.readlines()
    quote = random.choice(data)

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    send_email(quote)
