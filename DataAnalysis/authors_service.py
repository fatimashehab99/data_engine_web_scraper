from flask import Flask, jsonify, request
import mongo_connection


# this function is used to get top authors
def getTopAuthors():
    pipeline = [
        {
            '$project': {
                'author': '$author'
            }
        }, {
            '$group': {
                '_id': '$author',
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$project': {
                '_id': 0,
                'author': '$_id',
                'count': '$count'
            }
        }, {
            '$sort': {
                'count': -1
            }
        }
    ]
    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)
