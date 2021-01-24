from operator import itemgetter
from typing import Dict, Union

from .restaurants import RestaurantsType


def sort_by_popularity(restaurants: RestaurantsType) -> RestaurantsType:
    """Sort restaurants by popularity and online status in descending order

    :param restaurants: List of restaurants
    :return: List of restaurants sorted by popularity
    """
    return sorted(
        restaurants, key=itemgetter("online", "popularity"), reverse=True
    )


def get_popular_restaurants(
    restaurants: RestaurantsType,
) -> Dict[str, Union[str, RestaurantsType]]:
    """Get the first 10 most popular restaurants
    and generate payload for popular restaurants

    :param restaurants: List of restaurants
    :return: Payload for popular restaurants
    """
    return {
        "title": "Popular Restaurants",
        "restaurants": sort_by_popularity(restaurants)[:10],
    }
