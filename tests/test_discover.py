from restaurants.discover import discover_restaurants


def test_discover_restaurants(
    restaurants_input, user_location, discover_restaurants_fixture
):
    assert (
        discover_restaurants(restaurants_input, user_location)
        == discover_restaurants_fixture
    )
