import os
from api_handler import API_Handler, createNewAPI
from dataManager import dataManager

# Colored Output Testing
print(f"Error in\033[94m Class\033[0m, writeToFile function: \033[91m \nerror")  # Success

# Full test of report
api = createNewAPI("apis/streaming_availability.json")
query = {
    "country": "in",
    "show_type": "series",
    "genres": "action, comedy",
    "order_by": "rating",
    "order_direction": "desc",
    "genres_relation": "and"
}
api.query(query)
manager = dataManager(api)
manager.createReport()

