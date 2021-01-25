import json

from typing import Dict, Any, List
from pathlib import Path


RESTAURANTS_PATH = Path(__file__).parent.absolute() / "restaurants.json"


RestaurantType = Dict[str, Any]
RestaurantsType = List[RestaurantType]


def read_restaurants(
    input_file: Path = RESTAURANTS_PATH,
) -> RestaurantsType:
    """Read input file containing restaurants data

    :param input_file: Path to the input file containing restaurants data
    :return: List of restaurants
    """
    with open(input_file) as restaurants:
        return json.load(restaurants).get("restaurants")
