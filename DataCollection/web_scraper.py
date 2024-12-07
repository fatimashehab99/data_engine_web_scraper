from article_scraper import getArticleContent
from article_storage import storeToMongoDB
from article_scraper import getArticles


def main():
    i = 0
    article_data = []
    # get articles url
    articles_url = getArticles("https://www.almayadeen.net/sitemaps/all/sitemap-2024-8.xml")
    # get article data ans store it in mongo DB
    for article_url in articles_url:
        article_data.append(getArticleContent(article_url))
    storeToMongoDB(article_data)


if __name__ == "__main__":
    main()
