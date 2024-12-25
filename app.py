from flask import Flask, jsonify, request
from spacy.lang.en.tokenizer_exceptions import string

import DataAnalysis.articles_service
import DataAnalysis.authors_service
import DataAnalysis.keywords_service
import DataAnalysis.categories_service

app = Flask(__name__)


@app.route('/articles_by_date', methods=['GET'])
def articles_by_date():
    return DataAnalysis.articles_service.getArticlesCountByDate()


@app.route("/top_authors", methods=['GET'])
def top_authors():
    year = request.args.get('year', default=None, type=int)
    month = request.args.get('month', default=None, type=int)
    country = request.args.get('country', default=None, type=str)
    return DataAnalysis.authors_service.getTopAuthors(year, month, country)


@app.route("/top_keywords", methods=['GET'])
def top_keywords():
    year = request.args.get('year', default=None, type=int)
    month = request.args.get('month', default=None, type=int)
    country = request.args.get('country', default=None, type=str)
    return DataAnalysis.keywords_service.getTopKeyword(year, month, country)


@app.route("/top_categories", methods=['GET'])
def top_categories():
    year = request.args.get('year', default=None, type=int)
    month = request.args.get('month', default=None, type=int)
    country = request.args.get('country', default=None, type=str)
    return DataAnalysis.categories_service.getTopCategories(year, month, country)


# @app.route("/articles_by_keyword/<keyword>", methods=['GET'])
# def articles_by_keywords(keyword):
#     return DataAnalysis.keywords_service.getArticlesByKeyword(keyword)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
