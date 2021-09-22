# A REST API contains information about food outlets across multiple cities. Given the city name, and maximum
# cost for 2 persons, the goal is to use the API to get the list of food outlets that belong to this city and have
# an estimated cost less than or equal to given cost. The API returns paginated data.
# To access the information, perform an HTTP GET request to
# http://jsonmock.hackerrank.com/api/food_outlets?city=<city>&page=<pageNumber>
# where <city> is the city to get the food outlets and <pageNumber> is an integer that denotes the page
# of the results to return. For example, a GET request to
# http://jsonmock.hackerrank.com/api/food_outlets?city=Seattle&page=2 returns data associated with city Seattle,
# and on the second page of the results. Similarly, a GET request to
# http://jsonmock.hackerrank.com/api/food_outlets?city=Houston&page=1 returns data associated with city Houston,
# and on the first page of the results.
# The response to such a request is a JSON with the following 5 fields:
# page: The current page of the results.
# per_page: The maximum number of records returned per page.
# total: The total number of records in the database.
# total_pages: The total number of pages with results.
# data: Either an empty array or an array of outlet objects. Each object has the following schema:
# - city: city we queried for where the outlet is located [STRING]
# - name: name of the outlet [STRING]
# - estimated_cost: estimated cost for 2 persons [INTEGER]
# - user_rating:
#       - average_rating: average rating of the outlet [FLOAT]
#       - votes: total votes for the outlet [INTEGER]
# - id: unique identifier of the outlet [INTEGER]
# Below is an example of an outlet object:
# {
#      "city": "Houston",
#      "name": "Cocoa Tree",
#      "estimated_cost": 10,
#      "user_rating": {
#          "average_rating": 4.5,
#          "votes": 969,
#      },
#      "id": 938
# }
# Given a string city, numerical maximum cost for 2 persons maxCost, return the list of food outlet names that
# are located in this city and have an estimated cost less than or equal to given maxCost.
import requests


def getRelevantFoodOutlets(city, maxCost):
    result = []
    baseUrl = "http://jsonmock.hackerrank.com/api/food_outlets?city=" + city
    total_pages = requests.get(baseUrl).json()["total_pages"]

    for page in range(total_pages):
        url = baseUrl + "&page=" + str(page + 1)
        data = requests.get(url).json()["data"]

        for i in range(len(data)):
            if data[i]["estimated_cost"] <= maxCost:
                result.append(data[i]["name"])

    return result


print(getRelevantFoodOutlets('Denver', 50))  # BKC DIVE, Vedge
print(getRelevantFoodOutlets('Houston', 30))
# Nasi And Mee
# Zaatar Arabic Restaurant
# Milano Ice Cream
# Thaal Kitchen
# Alakapuri
# Nawras Seafood Restaurant
# Brindhavan Vegetarian Restaurant
# Mustake Multicuisine Restaurant
# Cocoa Tree
