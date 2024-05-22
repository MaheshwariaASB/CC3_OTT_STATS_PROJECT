from api_testing import API_Tester, createNewAPI
from dataManager import dataManager

api = createNewAPI("apis/streaming_availability.json")

query = {
    "country": "in",
    "show_type": "movie",
    "genres": "scifi",
    "order_by": "rating",
    "order_direction": "desc"
}
api.query(query)

manager = dataManager(api)

manager.createReport()
