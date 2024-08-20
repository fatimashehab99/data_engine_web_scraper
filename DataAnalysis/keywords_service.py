from flask import Flask, jsonify, request
import mongo_connection


# this function is used to get top keywords
def getTopKeyword():
    pipeline = [
        {
            '$project': {
                'keywords': 1,
                '_id': 0
            }
        }, {
            '$unwind': {
                'path': '$keywords'
            }
        }, {
            '$group': {
                '_id': '$keywords',
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$project': {
                '_id': 0,
                'keyword': '$_id',
                'count': 1
            }
        }, {
            '$sort': {
                'count': -1
            }
        }, {
            '$limit': 10
        }
    ]
    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)


# this function is used to get articles by keyword
def getArticlesByKeyword(keyword):
    pipeline = [
        {
            '$project': {
                '_id': 0,
                'url': 1,
                'keywords': 1,
                'title': 1
            }
        }, {
            '$unwind': {
                'path': '$keywords'
            }
        }, {
            '$match': {
                'keywords': keyword
            }
        }
    ]
    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)
