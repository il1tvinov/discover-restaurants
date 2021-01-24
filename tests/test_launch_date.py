from freezegun import freeze_time

from restaurants.launch_date import (
    get_launch_duration,
    filter_by_date,
    MONTHS_LIMIT,
    sort_by_launch_date,
    get_new_restaurants,
)


@freeze_time("2021-01-24")
def test_get_launch_duration():
    launch_date = "2020-04-01"
    months_duration = 9
    assert get_launch_duration(launch_date) == months_duration


@freeze_time("2021-01-24")
def test_filter_by_date(
    restaurants_input, restaurants_filtered_by_launch_date
):
    assert (
        filter_by_date(
            restaurants=restaurants_input, months_limit=MONTHS_LIMIT
        )
        == restaurants_filtered_by_launch_date
    )


def test_sort_by_launch_date(
    restaurants_input, restaurants_sorted_by_launch_date
):
    assert (
        sort_by_launch_date(restaurants_input)
        == restaurants_sorted_by_launch_date
    )


def test_get_new_restaurants(restaurants_input, nearby_restaurants):
    assert get_new_restaurants(restaurants_input) == nearby_restaurants
