import json
import os

from api_handler import API_Handler, createNewAPI
import sys

from dataManager import dataManager

if __name__ == '__main__':
    if len(sys.argv) > 2:
        try:
            file_path = sys.argv[1]
            if '.json' not in sys.argv[1]:
                file_path += '.json'
            if os.path.exists(os.path.join(os.getcwd(), file_path)):
                with open(os.path.join(os.getcwd(), file_path)) as file_load:
                    data = json.load(file_load)
                    key = sys.argv[2]
                    api = createNewAPI(data, key)
                    api.query()
                    manager = dataManager(api)
                    manager.createReport()
                    manager.downloadImages()
        except (IOError, json.JSONDecodeError) as e:
            raise type(e)(f"Error in reading or loading params file, please make sure it is a JSON and exists in the "
                          f"current working directory or the relative path is given.")
    else:
        raise IOError("Please provide a parameters file in the correct format. Please check the documentation to see "
                      "the format.")
