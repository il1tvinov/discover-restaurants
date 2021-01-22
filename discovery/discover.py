import json

from operator import itemgetter
from typing import List, Dict, Any
from pathlib import Path

from distance import get_distance
from filters import filter_by_distance, DISTANCE_LIMIT


RESTAURANTS = Path.cwd() / "restaurants.json"
FIELD_NAMES = ("title", "restaurants")


def read_restaurants(path: Path):
    with open(path) as restaurants:
        return json.load(restaurants)


def sort_by_distance(restaurants: List[float], user_location: List[float]):
    return sorted(
        restaurants,
        key=lambda restaurant: (
            -restaurant.get(
                "online"
            ),  # workaround to perform descending sorting for this key
            get_distance(
                user_location=user_location,
                restaurant_location=restaurant.get("location"),
            ),
        ),
    )[:10]


def sort_by_popularity(restaurants: List[Dict[str, Any]]):
    return sorted(
        restaurants, key=itemgetter("online", "popularity"), reverse=True
    )[:10]


def sort_by_launch_date(restaurants: List[Dict[str, Any]]):
    return sorted(
        restaurants,
        key=itemgetter("online", "launch_date"),
        reverse=True,
    )[:10]


def build_discover_payload(
    restaurants: List[Dict[str, Any]], user_location: List[float]
):

    closest_restaurants = filter_by_distance(
        restaurants=restaurants,
        user_location=user_location,
        distance_limit=DISTANCE_LIMIT,
    )

    groups = [
        (
            "Popular Restaurants",
            sort_by_popularity(restaurants=closest_restaurants),
        ),
        (
            "New Restaurants",
            sort_by_launch_date(restaurants=closest_restaurants),
        ),
        (
            "Nearby Restaurants",
            sort_by_distance(
                restaurants=closest_restaurants, user_location=user_location
            ),
        ),
    ]

    return [dict(zip(FIELD_NAMES, group)) for group in groups]
