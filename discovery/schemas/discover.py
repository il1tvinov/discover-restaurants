from typing import List

from pydantic import BaseModel


class UserLocation(BaseModel):
    lat: float
    lon: float


class Restaurant(BaseModel):
    blurhash: str
    launch_date: str
    location: List[float]
    name: str
    online: bool
    popularity: float


class Section(BaseModel):
    title: str
    restaurants: List[Restaurant]


class DiscoverRestaurants(BaseModel):
    sections: List[Section]
