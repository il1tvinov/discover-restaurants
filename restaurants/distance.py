from typing import List, Dict, Union

from geopy.distance import geodesic

from .restaurants import RestaurantsType

DISTANCE_LIMIT = 1.5

LocationType = List[float]


def get_distance(
    user_location: LocationType, restaurant_location: LocationType
) -> float:
    """Calculate distance between two given coordinates

    :param user_location: Coordinates of the user's location
    :param restaurant_location: Coordinates of restaurant's location
    :return: Distance between two given coordinates in kilometers
    """
    return geodesic(user_location, restaurant_location).km


def filter_by_distance(
    restaurants: RestaurantsType,
    user_location: LocationType,
    distance_limit: float = DISTANCE_LIMIT,
) -> RestaurantsType:
    """Filter out restaurants which are further than distance limit

    :param restaurants: List of restaurants
    :param user_location: Coordinates of the user's location
    :param distance_limit: Distance limit represented in kilometers
    :return: List of restaurants which don't exceed distance limit
    """
    return [
        restaurant
        for restaurant in restaurants
        if get_distance(
            user_location=user_location,
            restaurant_location=restaurant.get("location"),
        )
        <= distance_limit
    ]


def sort_by_distance(
    restaurants: RestaurantsType, user_location: LocationType
) -> RestaurantsType:
    """Sort restaurants by distance and online status
        - online: descending order
        - location: ascending order

    :param restaurants: List of restaurants
    :param user_location: Coordinates of the user's location
    :return: List of restaurants sorted by distance and online status
    """
    return sorted(
        restaurants,
        key=lambda restaurant: (
            -restaurant.get(
                "online"
            ),  # workaround to perform descending sorting for the first key
            get_distance(
                user_location=user_location,
                restaurant_location=restaurant.get("location"),
            ),
        ),
    )


def get_nearby_restaurants(
    restaurants: RestaurantsType, user_location: LocationType
) -> Dict[str, Union[str, RestaurantsType]]:
    """Get the first 10 nearest restaurants
    and generate payload for nearby restaurants

    :param restaurants: List of restaurants
    :param user_location: Coordinates of the user's location
    :return: Payload for nearby restaurants
    """
    return {
        "title": "Nearby Restaurants",
        "restaurants": sort_by_distance(
            restaurants=restaurants, user_location=user_location
        )[:10],
    }
