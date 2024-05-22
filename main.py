from api_testing import API_Tester, createNewAPI

api = createNewAPI("apis/ott_details.json")

query = {"title": "Endgame", "page": "1"}
api.query(query)
