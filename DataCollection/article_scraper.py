import json
from bs4 import BeautifulSoup
import requests


def getArticles(month_url):
    # fetch and parse month articles page
    response = requests.get(month_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    loc_tags = soup.find_all('loc')  # get articles url tag
    loc_contents = [loc.text for loc in loc_tags]  # get articles url
    return loc_contents


# this function is used to get the article data content
def getArticleContent(url):
    try:

        # fetch and parse article web page
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        # extract JSON metadata
        script_tag = soup.find('script', {'id': 'tawsiyat-metadata'})
        if not script_tag or not script_tag.string:
            return {"status": "error", "message": "Metadata not found"}

        article_data = json.loads(script_tag.string.strip())

        # Extract specific fields
        category, country, post_type = "", "", ""

        # looping over the classes fields to be able to get the country , post_type and category attributes
        for class_item in article_data.get('classes', []):
            mapping = class_item.get("mapping")  # mapping let
            value = class_item.get("value")
            if mapping == "category":
                category = value
            elif mapping == "country":
                country = value
            elif mapping == "posttype":
                post_type = value

        return {
            "post_id": article_data.get("postid"),
            "type": article_data.get("type"),
            "title": article_data.get("title"),
            "url": url,
            "keywords": [keyword.strip() for keyword in article_data["keywords"].split(",")],
            "thumbnail": article_data.get("thumbnail"),
            "video_duration": article_data.get("video_duration"),
            "word_count": article_data.get("word_count"),
            "published_date": article_data.get("published_time"),
            "updated_date": article_data.get("last_updated"),
            "description": article_data.get("description"),
            "author": article_data.get("author"),
            "classes": article_data.get("classes", []),
            "category": category,
            "country": country,
            "post_type": post_type
        }
    except (requests.exceptions.RequestException, ValueError) as e:
        return f"Error occurred: {e}"
