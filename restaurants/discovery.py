from .distance import (
    filter_by_distance,
    DISTANCE_LIMIT,
    LocationType,
    get_nearby_restaurants,
)
from .launch_date import get_new_restaurants
from .popularity import get_popular_restaurants
from .restaurants import RestaurantsType


def discover_restaurants(
    restaurants: RestaurantsType, user_location: LocationType
) -> RestaurantsType:
    """Generate payload for '/discovery/' route

    :param restaurants: List of restaurants
    :param user_location: Coordinates of the user's location
    :return: Payload for discovery route
    """

    closest_restaurants = filter_by_distance(
        restaurants=restaurants,
        user_location=user_location,
        distance_limit=DISTANCE_LIMIT,
    )

    sections = [
        get_popular_restaurants(closest_restaurants),
        get_new_restaurants(closest_restaurants),
        get_nearby_restaurants(
            restaurants=closest_restaurants, user_location=user_location
        ),
    ]

    return [section for section in sections if section.get("restaurants")]
