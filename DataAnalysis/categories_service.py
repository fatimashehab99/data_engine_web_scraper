from flask import Flask, jsonify, request
import mongo_connection


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
