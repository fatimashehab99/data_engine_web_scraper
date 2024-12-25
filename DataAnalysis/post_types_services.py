from flask import Flask, jsonify, request

import helpers
import mongo_connection


# this function is used to get type with count
def getTypeCount(year, month, country):
    pipeline = []
    if year and month:
        pipeline.extend(helpers.dateFilter(year, month))
    if country:
        pipeline.append(helpers.countryFilter(country))
    pipeline.extend([
        {
            '$group': {
                '_id': '$type',
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$project': {
                '_id': 0,
                'type': '$_id',
                'count': '$count'
            }
        }
    ])
    result = list(mongo_connection.collection.aggregate(pipeline))
    return jsonify(result)


# this function is used to get top post types
def getTopPostTypes(year, month, country):
    pipeline = []
    if year and month:
        pipeline.extend(helpers.dateFilter(year, month))
    if country:
        pipeline.append(helpers.countryFilter(country))
    pipeline.extend([
        {
            '$project': {
                'post_type': '$post_type'
            }
        }, {
            '$group': {
                '_id': '$post_type',
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$project': {
                '_id': 0,
                'post_type': '$_id',
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
