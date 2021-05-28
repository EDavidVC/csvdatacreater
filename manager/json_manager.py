import json

def get_json_of_stores_data():
	with open("data/data_config.json", "r", encoding="utf-8") as jsonFile:
		data_stores = json.load(jsonFile)
		#print("Data Loaded")
		#print(data_stores)
		print("Data Loaded\n", data_stores)
		return data_stores
