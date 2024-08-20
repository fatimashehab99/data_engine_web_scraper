from flask import Flask, jsonify, request

import DataAnalysis.articles_service
import DataAnalysis.authors_service
import DataAnalysis.keywords_service
import DataAnalysis.categories_service

app = Flask(__name__)


@app.route('/articles_by_date', methods=['GET'])
def articles_by_date():
    return DataAnalysis.articles_service.getArticlesCountByDate()


@app.route('/articles_by_word_count', methods=['GET'])
def articles_by_word_count():
    return DataAnalysis.articles_service.getArticlesByWordCount()


@app.route("/top_authors", methods=['GET'])
def top_authors():
    return DataAnalysis.authors_service.getTopAuthors()


@app.route("/top_keywords", methods=['GET'])
def top_keywords():
    return DataAnalysis.keywords_service.getTopKeyword()


@app.route("/articles_by_keyword/<keyword>", methods=['GET'])
def articles_by_keywords(keyword):
    return DataAnalysis.keywords_service.getArticlesByKeyword(keyword)


@app.route("/categories", methods=['GET'])
def categories():
    return DataAnalysis.categories_service.getCategoriesWithArticlesCount()


@app.route("/articles_by_year/<year>", methods=['GET'])
def articles_by_year(year):
    return DataAnalysis.articles_service.getArticlesByYear(year)


@app.route("/longest_articles", methods=['GET'])
def longest_articles():
    return DataAnalysis.articles_service.getLongestArticle()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
