import requests
from Email import send_email

topic = "tesla"

api_key = "302a8e0cf2d44174b70e4666054d7a63"
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&from=2024-04-26&"\
      "sortBy=publishedAt&"\
      "apiKey=302a8e0cf2d44174b70e4666054d7a63&"\
      "language=en"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = "subject:Today's News" + "\n" + body + article["title"] + "\n" \
        + article["description"] \
        + "\n" + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(body)