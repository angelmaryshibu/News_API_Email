import requests
import send_email

topic="tesla"

api_key="bbdca220f81a4c1bb0e90d00830c9cf4"

url="https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2025-08-17&" \
    "sortBy=publishedAt&apiKey=bbdca220f81a4c1bb0e90d00830c9cf4&" \
    "languane=en"

# Make request
request=(requests.get(url))

# Get a dictionary with data
content = request.json()

message=""

# Access the articles titles and discription
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        message= "Subject:Today's news"+ "\n" + message + article["title"] + "\n" \
            + article["description"] \
            + "\n"+ article["url"] + "\n\n"

message=message.encode("utf-8")

# Send the email
send_email.send_email(message)


    