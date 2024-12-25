def dateFilter(year, month):
    return [
        {
            "$addFields": {
                "published_date_parsed": {
                    "$dateFromString": {
                        "dateString": "$published_date"
                    }
                }
            }
        },
        {
            "$addFields": {
                "year": {"$year": "$published_date_parsed"},
                "month": {"$month": "$published_date_parsed"}
            }
        },
        {
            "$match": {
                "$expr": {
                    "$and": [
                        {"$eq": ["$year", year]},
                        {"$eq": ["$month", month]}
                    ]
                }
            }
        },
        {
            "$project": {"year": 0, "month": 0, "published_date_parsed": 0}
        }
    ]


def countryFilter(country):
    return {
        '$match': {
            'country': country
        }
    }
