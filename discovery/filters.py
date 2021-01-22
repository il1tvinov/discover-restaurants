from typing import List, Dict, Any

from discover import get_distance


DISTANCE_LIMIT = 1.5


def filter_by_distance(
    restaurants: List[Dict[str, Any]],
    user_location: List[float],
    distance_limit: float,
):
    return [
        restaurant
        for restaurant in restaurants
        if get_distance(
            user_location=user_location,
            restaurant_location=restaurant.get("location"),
        )
        <= distance_limit
    ]
