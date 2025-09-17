import requests

api_key="bbdca220f81a4c1bb0e90d00830c9cf4"

url="https://newsapi.org/v2/everything?q=tesla&from=2025-08-17&" \
    "sortBy=publishedAt&apiKey=bbdca220f81a4c1bb0e90d00830c9cf4"

# Make request
request=(requests.get(url))

# Get a dictionary with data
content = request.json()

# Access the articles titles and discription
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    