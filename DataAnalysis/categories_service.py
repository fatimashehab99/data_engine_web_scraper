from flask import Flask, jsonify, request

import helpers
import mongo_connection


# this function is used to get top categories
def getTopCategories(year, month, country):
    pipeline = []
    if year and month:
        pipeline.extend(helpers.dateFilter(year, month))
    if country:
        pipeline.append(helpers.countryFilter(country))
    pipeline.extend([
        {
            '$project': {
                'category': '$category'
            }
        }, {
            '$group': {
                '_id': '$category',
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$project': {
                '_id': 0,
                'category': '$_id',
                'count': '$count'
            }
        }, {
            '$sort': {
                'count': -1
            }
        }
    ])
    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)


# this function is used to get categories with articles count
def getCategoriesWithArticlesCount():
    pipeline = [
        {
            '$project': {
                '_id': 0,
                'category': 1
            }
        }, {
            '$match': {
                'category': {
                    '$ne': ''
                }
            }
        }, {
            '$group': {
                '_id': '$category',
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                'count': -1
            }
        }
    ]
    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)
