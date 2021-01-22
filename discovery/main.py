from fastapi import FastAPI

from schemas.discover import UserLocation, DiscoverRestaurants
from discover import read_restaurants, RESTAURANTS, build_discover_payload


app = FastAPI()


@app.post("/discover", response_model=DiscoverRestaurants)
def discover(
    user_location: UserLocation,
):
    user_location = [user_location.lat, user_location.lon]

    restaurants = read_restaurants(RESTAURANTS).get("restaurants")

    discover_page = build_discover_payload(
        restaurants=restaurants, user_location=user_location
    )
    discover_page = DiscoverRestaurants(sections=discover_page)
    return discover_page
