from flask import Flask, jsonify, request

import mongo_connection


# get articles count by date
def getArticlesCountByDate():
    pipeline = [
        {
            '$addFields': {
                'published_date_as_date': {
                    '$dateFromString': {
                        'dateString': '$published_date'
                    }
                }
            }
        }, {
            '$project': {
                'date': {
                    '$dateToString': {
                        'format': '%Y-%m-%d',
                        'date': '$published_date_as_date'
                    }
                }
            }
        }, {
            '$group': {
                '_id': '$date',
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                'count': -1
            }
        },
        {
            '$project': {
                '_id': 0,
                'date': '$_id',
                'count': '$count'
            }
        }
    ]

    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)


# get articles by word count
def getArticlesByWordCount():
    pipeline = [
        {
            '$addFields': {
                'word_count': {
                    '$toInt': '$word_count'
                }
            }
        }, {
            '$project': {
                'word_count': '$word_count'
            }
        }, {
            '$match': {
                'word_count': {
                    '$ne': 0
                }
            }
        }, {
            '$group': {
                '_id': '$word_count',
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                'count': -1
            }
        }, {
            '$project': {
                '_id': 0,
                'word_count': '$_id',
                'count': '$count'
            }
        }
    ]
    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)


# this function is used to get articles by year
def getArticlesByYear(year):
    pipeline = [
        {
            '$addFields': {
                'published_date': {
                    '$dateFromString': {
                        'dateString': '$published_date'
                    }
                }
            }
        }, {
            '$project': {
                '_id': 0,
                'date': {
                    '$dateToString': {
                        'format': '%Y',
                        'date': '$published_date'
                    }
                }
            }
        }, {
            '$match': {
                'date': year
            }
        }, {
            '$group': {
                '_id': '$date',
                'articles': {
                    '$sum': 1
                }
            }
        }, {
            '$project': {
                '_id': 0,
                'date': '$_id',
                'articles': 1
            }
        }
    ]
    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)
