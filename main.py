from fastapi import FastAPI

from schemas.discover import DiscoverRestaurants
from restaurants.restaurants import read_restaurants
from restaurants.discover import discover_restaurants


app = FastAPI()


@app.post(
    path="/discover/",
    response_model=DiscoverRestaurants,
    tags=["discover"],
    summary="Fetch groups of restaurants based on user's location.",
)
def discover(lat: float, lon: float):
    user_location = [lon, lat]

    restaurants = read_restaurants().get("restaurants")

    discover_payload = discover_restaurants(
        restaurants=restaurants, user_location=user_location
    )
    return DiscoverRestaurants(sections=discover_payload)
