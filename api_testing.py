import json

from typing import Dict

import requests


class API_Tester:

    def __init__(self, API_Name: str, API_URL: str, API_Headers: Dict[str, str]):
        if not isinstance(API_Name, str):
            raise TypeError("\033[91mAPI_Name must be a String\033[0m")
        if not isinstance(API_URL, str):
            raise TypeError("\033[91mAPI_URL must be a String\033[0m")
        if not isinstance(API_Headers, dict) or not all(
                isinstance(k, str) and isinstance(v, str) for k, v in API_Headers.items()):
            raise TypeError("\033[91mAPI_Headers must be a dictionary of string keys and values\033[0m")
        self.API_Name = API_Name
        self.API_URL = API_URL
        self.API_Headers = API_Headers

    def writeToFile(self, json_file) -> bool:
        try:
            with open(self.API_Name + '.json', 'w') as outfile:
                json.dump(json_file, outfile, indent=4)
            return True
        except (IOError, TypeError) as e:
            error_message = f"Error in \033[94m{self.API_Name}\033[0m, writeToFile function: \033[91m{str(e)}\033[0m"
            raise type(e)(error_message)

    def query(self, params: Dict[str,str]):
        self.writeToFile(requests.get(params=params, headers=self.API_Headers, url=self.API_URL).json())


def createNewAPI(json_file) -> API_Tester:
    try:
        with open(json_file, 'r') as params_file:
            params = json.load(params_file)
            return API_Tester(API_Name=params['API_Name'], API_URL=params['API_URL'], API_Headers=params['API_Headers'])
    except (IOError, json.JSONDecodeError) as e:
        raise type(e)(f"Error in createNewAPI function: \033[91m{str(e)}\033[0m")

# class OTT_Details(API_Tester):
#     def __init__(self, API_Name, API_URL, API_Headers):
#         super().__init__(API_Name, API_URL, API_Headers)
