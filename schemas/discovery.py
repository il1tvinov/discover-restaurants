from typing import List

from pydantic import BaseModel

from restaurants.distance import LocationType


class Restaurant(BaseModel):
    blurhash: str
    launch_date: str
    location: LocationType
    name: str
    online: bool
    popularity: float


class Section(BaseModel):
    title: str
    restaurants: List[Restaurant]


class DiscoverRestaurants(BaseModel):
    sections: List[Section]

    class Config:
        schema_extra = {
            "example": {
                "sections": [
                    {
                        "title": "Restaurants",
                        "restaurants": [
                            {
                                "blurhash": "UAN=8k?LS~M:ErJFs%t0MDMWRqo@%BxSV{RX",
                                "launch_date": "2020-04-20",
                                "location": [24.938082, 60.17626],
                                "name": "Sea Chain",
                                "online": True,
                                "popularity": 0.956990414084132,
                            },
                        ],
                    }
                ]
            }
        }
