import json

def get_json_of_stores_data():
	with open("data/data_config.json", "r", encoding="utf-8") as json_file:
		data_stores = json.load(json_file)
		print("Data Loaded", data_stores)
		return data_stores
