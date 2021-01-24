from restaurants.distance import (
    get_distance,
    filter_by_distance,
    DISTANCE_LIMIT,
    sort_by_distance,
    get_nearby_restaurants,
)


def test_get_distance(
    user_location, restaurant_location, distance_between_user_and_restaurant
):
    assert (
        get_distance(user_location, restaurant_location)
        == distance_between_user_and_restaurant
    )


def test_filter_by_distance(
    restaurants_input, user_location, restaurants_filtered_by_distance
):
    assert (
        filter_by_distance(
            restaurants=restaurants_input,
            user_location=user_location,
            distance_limit=DISTANCE_LIMIT,
        )
        == restaurants_filtered_by_distance
    )


def test_sort_by_distance(
    restaurants_input, user_location, restaurants_sorted_by_distance
):
    assert sort_by_distance(
        restaurants_input, user_location
    ) == restaurants_sorted_by_distance.get("restaurants")


def test__nearby_restaurants(
    restaurants_input, user_location, restaurants_sorted_by_distance
):
    assert (
        get_nearby_restaurants(restaurants_input, user_location)
        == restaurants_sorted_by_distance
    )
