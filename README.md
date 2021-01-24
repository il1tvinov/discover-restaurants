# discover-restaurants
Backend tech-assignment for Wolt.  
The application is implemented as a single endpoint providing restaurants suggestions based on user's location.

## Getting started
Install the requirements and run the application
```shell script
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
**OR**

Build the image and fire up the container
```shell script
docker-compose build
docker-compose up -d
```

Go to `http://127.0.0.1:8000/docs` to open API documentation and test the endpoint.

## Assignment description

### Restaurant-object
Both frontend and backend tasks use restaurant objects which represent **fictive** restaurants in Helsinki.  Each object has a set of fields providing more information about the restaurant, like *name* and *location*.

Example:
```
{
   "blurhash":"UAPp-JsCNbr[UQagn*V^p-bYjIjtL?kSo]bG",
   "location":[
      24.933257,
      60.171263
   ],
   "name":"Charming Cherry House",
   "online": true,
   "launch_date":"2020-09-20",
   "popularity":0.665082352909038
}
```


#### Fields:
- **blurhash**: image representation (type: string)
- **location**: Restaurant's location as latitude and longitude coordinates. First element in the list is the longitude (type: a list containing two decimal elements)
- **name**: The name of the restaurant (type: string)
- **launch_date**: the date when the restaurant was added to Wolt app (type: string, ISO 8601 date)
- **online**: if *true*, the restaurant is accepting orders. If *false*, the restaurant is closed (type: boolean)
- **popularity**: the higher the number, the more popular the restaurant is in Wolt app (type: a float between 0-1, where 1 is the - most popular restaurant)

### Backend assignment
*restaurants.json* in the repository contains one hundred restaurants from the Helsinki area. 

Your task is to create an **API endpoint** */discovery* that takes coordinates of the customer as an input and then **returns a page (JSON response)** containing *most popular, newest and nearby* restaurants (based on given coordinates). 

Location of a customer needs to be provided as **request parameters** *lat* (latitude) and *lon* (longitude), e.g. */discovery?lat=60.1709&lon=24.941*. Both parameters accept float values.

A JSON object returned by the */discovery* -endpoint must have the following structure:
```
{
   "sections": [
      {
           "title": "Popular Restaurants",
           "restaurants": [.. add max 10 restaurant objects..]
      },
      {
           "title": "New Restaurants",
           "restaurants": [..add max 10 restaurant objects..]
      },
 	{
           "title": "Nearby Restaurants",
           "restaurants": [.. add max 10 restaurant objects..]
      }

   ]
}
```

For each *restaurants*-list you need to add **maximum 10** restaurant objects. A list can also contain fewer restaurants (or even be empty) if there are not enough objects matching given conditions. A section with an empty *restaurants*-list should be removed from the response.

**So how do you know which restaurants to add to each list?** 

There are two main rules to follow:
- All restaurants returned by the endpoint must be **closer than 1.5 kilometers** from given coordinates, measured as a straight line between coordinates and the location of the restaurant.
- Open restaurants (*online=true*) are **more important** than closed ones. Every list must be first populated with open restaurants, and only adding closed ones if there is still capacity left.

In addition each list has a specific **sorting rule**:
- “Popular Restaurants”: highest *popularity* value first (descending order)
- “New Restaurants”: Newest *launch_date* first (descending). This list has also a special rule: *launch_date* must be no older than 4 months.
- “Nearby Restaurants”: Closest to the given location first (ascending).

Remember to **cap each list to max. 10** best matching restaurants. The same restaurant can obviously be in multiple lists (if it matches given criteria).