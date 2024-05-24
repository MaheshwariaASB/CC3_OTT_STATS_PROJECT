import json
from typing import Dict, Any
import os
import datetime
from api_handler import API_Handler


class dataManager:
    def __init__(self, api: API_Handler):
        self.jsonToRead = os.path.join(os.getcwd(), 'data', api.API_Name + ' Response.json')
        self.country_code = api.params['country']

    def createReport(self, overwrite: bool) -> Dict[str, Any]:
        try:
            final = {}
            with (open(self.jsonToRead, 'r') as file):
                file_json = json.load(file)
                for show in file_json['shows']:
                    services = {}
                    for service in show['streamingOptions'][self.country_code]:
                        services[service['service']['name']] = {
                            "service": service['service']['name'],
                            "type": service['type'],
                            "link": service['link'],
                            "price": service['price']['formatted'] if 'price' in service else 'N/A'
                        }
                    genres = []
                    for genre in show['genres']:
                        genres.append(genre)
                    final[show['title']] = {
                        "id": show['imdbId'],
                        "overview": show['overview'],
                        "rating": show['rating'],
                        "image_link": show['imageSet']['verticalPoster']['w600'],
                        "streaming_options": services,
                        "showType": show['showType'],
                        "genres": genres
                    }
            if not overwrite:
                i = 1
                while os.path.exists(os.path.join(os.getcwd(), 'data', f"formatted{i} at {datetime.date.today()}.json")):
                    i += 1
                with open(os.path.join(os.getcwd(), 'data', f"formatted{i} at {datetime.date.today()}.json"), 'w') as file_save:
                    json.dump(final, file_save, indent=4)
            else:
                with open(os.path.join(os.getcwd(), 'data', f"formatted.json"), 'w') as file_save:
                    json.dump(final, file_save, indent=4

            return final
        except (IOError, json.JSONDecodeError) as e:
            raise type(e)(f"Error in \033[94m {self.__class__.__name__}\033[0m, read function: \033[91m{str(e)}\033[0m")
