from restaurants.popularity import sort_by_popularity, get_popular_restaurants


def test_sort_by_popularity(restaurants_input, popular_restaurants):
    assert sort_by_popularity(restaurants_input) == popular_restaurants.get(
        "restaurants"
    )


def test_get_popular_restaurants(restaurants_input, popular_restaurants):
    assert get_popular_restaurants(restaurants_input) == popular_restaurants
