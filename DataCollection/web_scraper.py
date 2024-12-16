from .article_scraper import getArticleContent, getArticles
from .article_storage import storeToMongoDB


def main():
    i = 0
    article_data = []
    # get articles url
    articles_url = getArticles("https://www.almayadeen.net/sitemaps/all/sitemap-2024-8.xml")
    # get article data ans store it in mongo DB
    for article_url in articles_url:
        article=getArticleContent(article_url)
        storeToMongoDB(article)

if __name__ == "__main__":
    main()
