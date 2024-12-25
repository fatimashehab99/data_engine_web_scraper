from flask import Flask, jsonify, request
from spacy.lang.en.tokenizer_exceptions import string

import DataAnalysis.articles_service
import DataAnalysis.authors_service
import DataAnalysis.keywords_service
import DataAnalysis.categories_service
import DataAnalysis.countries_services
import DataAnalysis.post_types_services

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


@app.route("/top_countries", methods=['GET'])
def top_countries():
    year = request.args.get('year', default=None, type=int)
    month = request.args.get('month', default=None, type=int)
    return DataAnalysis.countries_services.getCountries(year, month)


@app.route("/top_post_type", methods=['GET'])
def top_post_type():
    year = request.args.get('year', default=None, type=int)
    month = request.args.get('month', default=None, type=int)
    country = request.args.get('country', default=None, type=str)
    return DataAnalysis.post_types_services.getTopPostTypes(year, month, country)


# @app.route("/articles_by_keyword/<keyword>", methods=['GET'])
# def articles_by_keywords(keyword):
#     return DataAnalysis.keywords_service.getArticlesByKeyword(keyword)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
