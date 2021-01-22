from typing import List

from geopy.distance import geodesic


def get_distance(
    user_location: List[float], restaurant_location: List[float]
) -> float:
    return geodesic(user_location, restaurant_location).km
