from article_scraper import getArticleContent
from article_storage import storeToMongoDB


def main():
    url = "https://www.almayadeen.net/news/politics/%D8%AD%D9%85%D8%AF-%D9%84%D9%84%D9%85%D9%8A%D8%A7%D8%AF%D9%8A%D9%86--%D9%86%D8%AA%D9%86%D9%8A%D8%A7%D9%87%D9%88-%D8%A3%D9%81%D8%B4%D9%84-%D8%B5%D9%81%D9%82%D8%A9-%D9%88%D9%82%D9%81-%D8%A5%D8%B7%D9%84%D8%A7%D9%82-%D8%A7%D9%84%D9%86%D8%A7%D8%B1---%D9%88%D9%84%D9%86-%D9%86%D8%AF%D8%AE%D9%84-%D8%A8"
    article_data = getArticleContent(url)
    print(storeToMongoDB(article_data))


if __name__ == "__main__":
    main()
