from flask import Flask, jsonify, request

import helpers
import mongo_connection


# get article count
def getArticleCount(year, month, country):
    pipeline = []
    if year and month:
        pipeline.extend(helpers.dateFilter(year, month))
    if country:
        pipeline.append(helpers.countryFilter(country))
    pipeline.extend([
        {
            '$count': 'articles_count'
        }
    ])
    result = list(mongo_connection.collection.aggregate(pipeline))
    return result[0].get("articles_count") if result else None


# get articles by word count
def getArticlesByWordCount(year, month, country):
    pipeline = []
    if year and month:
        pipeline.extend(helpers.dateFilter(year, month))
    if country:
        pipeline.append(helpers.countryFilter(country))
    pipeline.extend([{
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
            'articles_count': '$count'
        }
    }
    ])
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


# this function is used to get the longest article
def getLongestArticles(year, month, country):
    pipeline = []
    if year and month:
        pipeline.extend(helpers.dateFilter(year, month))
    if country:
        pipeline.append(helpers.countryFilter(country))
    pipeline.extend([
        {
            '$project': {
                'word_count': '$word_count',
                '_id': 0,
                'url': '$url',
                'post_id': '$postId',
                'title': '$title'
            }
        }, {
            '$sort': {
                'word_count': -1
            }
        }, {
            '$limit': 10
        }
    ])
    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)


# this function is used to get recent 10 articles
def getRecentArticles(year, month, country):
    pipeline = []
    if year and month:
        pipeline.extend(helpers.dateFilter(year, month))
    if country:
        pipeline.append(helpers.countryFilter(country))
    pipeline.extend([
        {
            '$sort': {
                'published_date': 1
            }
        }, {
            '$project': {
                '_id': 0,
                'url': '$url',
                'post_id': '$postId',
                'title': '$title'
            }
        }, {
            '$limit': 10
        }
    ])
    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)
