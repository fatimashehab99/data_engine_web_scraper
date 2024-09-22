from article_scraper import getArticleContent
from article_storage import storeToMongoDB
from article_scraper import getArticles
from google.cloud import bigquery

# Create a BigQuery client
client = bigquery.Client()

# Specify your BigQuery table (project.dataset.table)
table_id = "apt-nebula-425921-i1.data_engine.articles"


def main():
    i = 0
    article_data = []
    # get articles url
    articles_url = getArticles("https://www.almayadeen.net/sitemaps/all/sitemap-2024-8.xml")
    # get article data ans store it in mongo DB
    for article_url in articles_url:
        i+=1
        gcp = (getArticleContent(article_url))
        errors=client.insert_rows_json(table_id, [gcp])
        print(i)
        if errors:
            print(f"Encountered errors while inserting rows: {errors}")
        else:
            print("Row successfully inserted.")

    # storeToMongoDB(article_data)


if __name__ == "__main__":
    main()
