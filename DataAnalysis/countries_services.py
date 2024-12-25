from flask import Flask, jsonify, request

import helpers
import mongo_connection


# this function is used to get top country
def getCountries(year, month):
    pipeline = []
    if year and month:
        pipeline.extend(helpers.dateFilter(year, month))
    pipeline.extend([
        {
            '$project': {
                'country': '$country'
            }
        }, {

            '$group': {
                '_id': '$country',
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$project': {
                '_id': 0,
                'country': '$_id',
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
