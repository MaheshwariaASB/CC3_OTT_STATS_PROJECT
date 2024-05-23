import json
from typing import Dict, Any
import os

from api_handler import API_Handler


class dataManager:
    def __init__(self, api: API_Handler):
        self.jsonToRead = os.path.join(os.getcwd(), 'data', api.API_Name + ' Response.json')
        self.country_code = api.params['country']

    def createReport(self) -> Dict[str, Any]:
        try:
            final = {}
            with (open(self.jsonToRead, 'r') as file):
                file_json = json.load(file)
                for show in file_json['shows']:
                    services = {}
                    for service in show['streamingOptions'][self.country_code]:
                        services[service['service']['name']] = {
                            "type": service['type'],
                            "link": service['link'],
                            "price": service['price']['formatted'] if 'price' in service else 'N/A'
                        }
                    final[show['title']] = {
                        "id": show['imdbId'],
                        "overview": show['overview'],
                        "rating": show['rating'],
                        "image_link": show['imageSet']['verticalPoster']['w600'],
                        "streaming_options": services
                    }
            i = 1
            while os.path.exists(os.path.join(os.getcwd(), 'data', f"formatted{i}.json")):
                i += 1
            with open(os.path.join(os.getcwd(), 'data', f"formatted{i}.json"), 'w') as file_save:
                json.dump(final, file_save, indent=4)

            return final
        except (IOError, json.JSONDecodeError) as e:
            raise type(e)(f"Error in \033[94m {self.__class__.__name__}\033[0m, read function: \033[91m{str(e)}\033[0m")
