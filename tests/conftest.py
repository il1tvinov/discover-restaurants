from pytest import fixture


@fixture()
def user_location():
    return [24.941244, 60.171987]


@fixture()
def restaurant_location():
    return [24.942143, 60.172142]


@fixture()
def distance_between_user_and_restaurant():
    return 0.10080699251016557


@fixture()
def restaurants_input():
    return [
        {
            "blurhash": "UME,}O}zIwJXTsTGnjs*I{OHbYsRMoi~xnbI",
            "launch_date": "2020-11-11",
            "location": [24.938247, 60.181390],
            "name": "Relish Place",
            "online": False,
            "popularity": 0.6696615083382598,
        },
        {
            "blurhash": "UGHdYc]|EmNdYjJW$doe57J7bcxZ8$xBbYW-",
            "launch_date": "2020-03-16",
            "location": [24.993325, 60.151355],
            "name": "Outside of zone",
            "online": False,
            "popularity": 0.57347340947833162,
        },
        {
            "blurhash": "UCO;.s:bO%r_yWXlORbbC?TFvobaVDi_t9nS",
            "launch_date": "2020-02-19",
            "location": [24.938245, 60.181388],
            "name": "Tender Lettuce",
            "online": True,
            "popularity": 0.8919633748546864,
        },
        {
            "blurhash": "UH9DE2+hKKsCO-X5r]n*3#GAw3Sx+hr]OnX5",
            "launch_date": "2020-05-22",
            "location": [24.938246, 60.181389],
            "name": "Mustard",
            "online": True,
            "popularity": 0.70907452479616846,
        },
        {
            "blurhash": "UKFGw4^KM}$$x@X8N1kB10R+xEWWR8Rlt4o0",
            "launch_date": "2018-02-23",
            "location": [24.938244, 60.181387],
            "name": "Ketchup XL",
            "online": True,
            "popularity": 0.90706741877410304,
        },
    ]


@fixture()
def restaurants_filtered_by_distance():
    return [
        {
            "blurhash": "UME,}O}zIwJXTsTGnjs*I{OHbYsRMoi~xnbI",
            "launch_date": "2020-11-11",
            "location": [24.938247, 60.181390],
            "name": "Relish Place",
            "online": False,
            "popularity": 0.6696615083382598,
        },
        {
            "blurhash": "UCO;.s:bO%r_yWXlORbbC?TFvobaVDi_t9nS",
            "launch_date": "2020-02-19",
            "location": [24.938245, 60.181388],
            "name": "Tender Lettuce",
            "online": True,
            "popularity": 0.8919633748546864,
        },
        {
            "blurhash": "UH9DE2+hKKsCO-X5r]n*3#GAw3Sx+hr]OnX5",
            "launch_date": "2020-05-22",
            "location": [24.938246, 60.181389],
            "name": "Mustard",
            "online": True,
            "popularity": 0.70907452479616846,
        },
        {
            "blurhash": "UKFGw4^KM}$$x@X8N1kB10R+xEWWR8Rlt4o0",
            "launch_date": "2018-02-23",
            "location": [24.938244, 60.181387],
            "name": "Ketchup XL",
            "online": True,
            "popularity": 0.90706741877410304,
        },
    ]


@fixture()
def restaurants_sorted_by_distance():
    return {
        "title": "Nearby Restaurants",
        "restaurants": [
            {
                "blurhash": "UKFGw4^KM}$$x@X8N1kB10R+xEWWR8Rlt4o0",
                "launch_date": "2018-02-23",
                "location": [24.938244, 60.181387],
                "name": "Ketchup XL",
                "online": True,
                "popularity": 0.907067418774103,
            },
            {
                "blurhash": "UCO;.s:bO%r_yWXlORbbC?TFvobaVDi_t9nS",
                "launch_date": "2020-02-19",
                "location": [24.938245, 60.181388],
                "name": "Tender Lettuce",
                "online": True,
                "popularity": 0.8919633748546864,
            },
            {
                "blurhash": "UH9DE2+hKKsCO-X5r]n*3#GAw3Sx+hr]OnX5",
                "launch_date": "2020-05-22",
                "location": [24.938246, 60.181389],
                "name": "Mustard",
                "online": True,
                "popularity": 0.7090745247961685,
            },
            {
                "blurhash": "UME,}O}zIwJXTsTGnjs*I{OHbYsRMoi~xnbI",
                "launch_date": "2020-11-11",
                "location": [24.938247, 60.18139],
                "name": "Relish Place",
                "online": False,
                "popularity": 0.6696615083382598,
            },
            {
                "blurhash": "UGHdYc]|EmNdYjJW$doe57J7bcxZ8$xBbYW-",
                "launch_date": "2020-03-16",
                "location": [24.993325, 60.151355],
                "name": "Outside of zone",
                "online": False,
                "popularity": 0.5734734094783316,
            },
        ],
    }


@fixture()
def restaurants_filtered_by_launch_date():
    return [
        {
            "blurhash": "UME,}O}zIwJXTsTGnjs*I{OHbYsRMoi~xnbI",
            "launch_date": "2020-11-11",
            "location": [24.938247, 60.18139],
            "name": "Relish Place",
            "online": False,
            "popularity": 0.6696615083382598,
        }
    ]


@fixture()
def restaurants_sorted_by_launch_date():
    return [
        {
            "blurhash": "UH9DE2+hKKsCO-X5r]n*3#GAw3Sx+hr]OnX5",
            "launch_date": "2020-05-22",
            "location": [24.938246, 60.181389],
            "name": "Mustard",
            "online": True,
            "popularity": 0.7090745247961685,
        },
        {
            "blurhash": "UCO;.s:bO%r_yWXlORbbC?TFvobaVDi_t9nS",
            "launch_date": "2020-02-19",
            "location": [24.938245, 60.181388],
            "name": "Tender Lettuce",
            "online": True,
            "popularity": 0.8919633748546864,
        },
        {
            "blurhash": "UKFGw4^KM}$$x@X8N1kB10R+xEWWR8Rlt4o0",
            "launch_date": "2018-02-23",
            "location": [24.938244, 60.181387],
            "name": "Ketchup XL",
            "online": True,
            "popularity": 0.907067418774103,
        },
        {
            "blurhash": "UME,}O}zIwJXTsTGnjs*I{OHbYsRMoi~xnbI",
            "launch_date": "2020-11-11",
            "location": [24.938247, 60.18139],
            "name": "Relish Place",
            "online": False,
            "popularity": 0.6696615083382598,
        },
        {
            "blurhash": "UGHdYc]|EmNdYjJW$doe57J7bcxZ8$xBbYW-",
            "launch_date": "2020-03-16",
            "location": [24.993325, 60.151355],
            "name": "Outside of zone",
            "online": False,
            "popularity": 0.5734734094783316,
        },
    ]


@fixture()
def nearby_restaurants():
    return {
        "title": "New Restaurants",
        "restaurants": [
            {
                "blurhash": "UME,}O}zIwJXTsTGnjs*I{OHbYsRMoi~xnbI",
                "launch_date": "2020-11-11",
                "location": [24.938247, 60.18139],
                "name": "Relish Place",
                "online": False,
                "popularity": 0.6696615083382598,
            },
        ],
    }


@fixture()
def popular_restaurants():
    return {
        "title": "Popular Restaurants",
        "restaurants": [
            {
                "blurhash": "UKFGw4^KM}$$x@X8N1kB10R+xEWWR8Rlt4o0",
                "launch_date": "2018-02-23",
                "location": [24.938244, 60.181387],
                "name": "Ketchup XL",
                "online": True,
                "popularity": 0.907067418774103,
            },
            {
                "blurhash": "UCO;.s:bO%r_yWXlORbbC?TFvobaVDi_t9nS",
                "launch_date": "2020-02-19",
                "location": [24.938245, 60.181388],
                "name": "Tender Lettuce",
                "online": True,
                "popularity": 0.8919633748546864,
            },
            {
                "blurhash": "UH9DE2+hKKsCO-X5r]n*3#GAw3Sx+hr]OnX5",
                "launch_date": "2020-05-22",
                "location": [24.938246, 60.181389],
                "name": "Mustard",
                "online": True,
                "popularity": 0.7090745247961685,
            },
            {
                "blurhash": "UME,}O}zIwJXTsTGnjs*I{OHbYsRMoi~xnbI",
                "launch_date": "2020-11-11",
                "location": [24.938247, 60.18139],
                "name": "Relish Place",
                "online": False,
                "popularity": 0.6696615083382598,
            },
            {
                "blurhash": "UGHdYc]|EmNdYjJW$doe57J7bcxZ8$xBbYW-",
                "launch_date": "2020-03-16",
                "location": [24.993325, 60.151355],
                "name": "Outside of zone",
                "online": False,
                "popularity": 0.5734734094783316,
            },
        ],
    }


@fixture()
def discover_restaurants_fixture():
    return [
        {
            "title": "Popular Restaurants",
            "restaurants": [
                {
                    "blurhash": "UKFGw4^KM}$$x@X8N1kB10R+xEWWR8Rlt4o0",
                    "launch_date": "2018-02-23",
                    "location": [24.938244, 60.181387],
                    "name": "Ketchup XL",
                    "online": True,
                    "popularity": 0.907067418774103,
                },
                {
                    "blurhash": "UCO;.s:bO%r_yWXlORbbC?TFvobaVDi_t9nS",
                    "launch_date": "2020-02-19",
                    "location": [24.938245, 60.181388],
                    "name": "Tender Lettuce",
                    "online": True,
                    "popularity": 0.8919633748546864,
                },
                {
                    "blurhash": "UH9DE2+hKKsCO-X5r]n*3#GAw3Sx+hr]OnX5",
                    "launch_date": "2020-05-22",
                    "location": [24.938246, 60.181389],
                    "name": "Mustard",
                    "online": True,
                    "popularity": 0.7090745247961685,
                },
                {
                    "blurhash": "UME,}O}zIwJXTsTGnjs*I{OHbYsRMoi~xnbI",
                    "launch_date": "2020-11-11",
                    "location": [24.938247, 60.18139],
                    "name": "Relish Place",
                    "online": False,
                    "popularity": 0.6696615083382598,
                },
            ],
        },
        {
            "title": "New Restaurants",
            "restaurants": [
                {
                    "blurhash": "UME,}O}zIwJXTsTGnjs*I{OHbYsRMoi~xnbI",
                    "launch_date": "2020-11-11",
                    "location": [24.938247, 60.18139],
                    "name": "Relish Place",
                    "online": False,
                    "popularity": 0.6696615083382598,
                }
            ],
        },
        {
            "title": "Nearby Restaurants",
            "restaurants": [
                {
                    "blurhash": "UKFGw4^KM}$$x@X8N1kB10R+xEWWR8Rlt4o0",
                    "launch_date": "2018-02-23",
                    "location": [24.938244, 60.181387],
                    "name": "Ketchup XL",
                    "online": True,
                    "popularity": 0.907067418774103,
                },
                {
                    "blurhash": "UCO;.s:bO%r_yWXlORbbC?TFvobaVDi_t9nS",
                    "launch_date": "2020-02-19",
                    "location": [24.938245, 60.181388],
                    "name": "Tender Lettuce",
                    "online": True,
                    "popularity": 0.8919633748546864,
                },
                {
                    "blurhash": "UH9DE2+hKKsCO-X5r]n*3#GAw3Sx+hr]OnX5",
                    "launch_date": "2020-05-22",
                    "location": [24.938246, 60.181389],
                    "name": "Mustard",
                    "online": True,
                    "popularity": 0.7090745247961685,
                },
                {
                    "blurhash": "UME,}O}zIwJXTsTGnjs*I{OHbYsRMoi~xnbI",
                    "launch_date": "2020-11-11",
                    "location": [24.938247, 60.18139],
                    "name": "Relish Place",
                    "online": False,
                    "popularity": 0.6696615083382598,
                },
            ],
        },
    ]
