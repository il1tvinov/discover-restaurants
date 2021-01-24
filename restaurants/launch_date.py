from operator import itemgetter
from datetime import datetime
from typing import Dict, Union

from .restaurants import RestaurantsType

MONTHS_LIMIT = 4
DATE_FORMAT = "%Y-%m-%d"


def get_launch_duration(launch_date: str) -> int:
    """Calculate how many months have passed since launch date

    :param launch_date: Launch date
    :return: Number of months passed since launch date
    """
    current_date = datetime.date(datetime.now())
    launch_date = datetime.strptime(launch_date, DATE_FORMAT)
    return (current_date.year - launch_date.year) * 12 + (
        current_date.month - launch_date.month
    )


def filter_by_date(
    restaurants: RestaurantsType, months_limit: int = MONTHS_LIMIT
) -> RestaurantsType:
    """Filter out restaurants which are older than months limit

    :param restaurants: List of restaurants
    :param months_limit: A number used as months limit
    :return: List of restaurants which aren't older than months limit
    """
    return [
        restaurant
        for restaurant in restaurants
        if get_launch_duration(restaurant.get("launch_date")) <= months_limit
    ]


def sort_by_launch_date(restaurants: RestaurantsType) -> RestaurantsType:
    """Sort restaurants by launch date and online status in descending order

    :param restaurants: List of restaurants
    :return: List of restaurants sorted by launch date and online status
    """
    return sorted(
        restaurants,
        key=itemgetter("online", "launch_date"),
        reverse=True,
    )


def get_new_restaurants(
    restaurants: RestaurantsType,
) -> Dict[str, Union[str, RestaurantsType]]:
    """Get the first 10 newest restaurants
    and generate payload for new restaurants

    :param restaurants: List of restaurants
    :return: Payload for new restaurants
    """
    new_restaurants = filter_by_date(
        restaurants=restaurants, months_limit=MONTHS_LIMIT
    )
    return {
        "title": "New Restaurants",
        "restaurants": sort_by_launch_date(new_restaurants)[:10],
    }
