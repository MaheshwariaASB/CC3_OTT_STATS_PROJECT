from api_testing import API_Tester, createNewAPI
from dataManager import dataManager

api = createNewAPI("apis/streaming_availability.json")

query = {
    "country": "in",
    "show_type": "series",
    "genres": "scifi, fantasy",
    "order_by": "rating",
    "order_direction": "desc",
    "genres_relation": "or"
}
api.query(query)

manager = dataManager(api)

manager.createReport()
