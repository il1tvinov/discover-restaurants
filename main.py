from fastapi import FastAPI

from schemas.discovery import DiscoverRestaurants
from restaurants.restaurants import read_restaurants
from restaurants.discovery import discover_restaurants


app = FastAPI()


@app.post(
    path="/discovery/",
    response_model=DiscoverRestaurants,
    tags=["discovery"],
    summary="Fetch groups of restaurants based on user's location.",
)
def discovery(lat: float, lon: float):
    user_location = [lon, lat]

    restaurants = read_restaurants().get("restaurants")

    discover_payload = discover_restaurants(
        restaurants=restaurants, user_location=user_location
    )
    return DiscoverRestaurants(sections=discover_payload)
