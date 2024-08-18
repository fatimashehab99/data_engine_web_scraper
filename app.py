from flask import Flask, jsonify, request

import DataAnalysis.articles_services

app = Flask(__name__)


@app.route('/articles_by_date', methods=['GET'])
def articles_by_date():
    return DataAnalysis.articles_services.getArticlesCountByDate()


@app.route('/articles_by_word_count', methods=['GET'])
def articles_by_word_count():
    return DataAnalysis.articles_services.getArticlesByWordCount()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
