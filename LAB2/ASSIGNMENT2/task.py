import requests

# Function to retrieve news articles from News API
def get_news(api_key):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "country": "us"  # You can change the country based on your preference
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data["articles"]
        return articles
    else:
        print("Error retrieving news:", response.status_code)
        return None

# Function to generate a group chat with different agents
def generate_group_chat(agents, news_articles):
    print("Group Chat:")
    for article in news_articles:
        print("Article Title:", article["title"])
        for agent in agents:
            print(agent + ":", "What are your thoughts on this news?")
        print("\n")

# API key from News API
news_api_key = "44655c0d1eb54b7ab32d9264f37b922a"

# Retrieve news articles
news_articles = get_news(news_api_key)

if news_articles:
    agents = ["user_proxy", "critic", "writer", "planner"]
    generate_group_chat(agents, news_articles)