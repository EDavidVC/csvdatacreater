import csv
import json

class CSVFile:
    def __init__(self, path="data/alldata.csv", num_rows=1000):
        self._path = path
        self._data_stores = None

    def create_file(self, data):
        with open("data/alldata.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(data)

class JSONFile:
    def __init__(self, path="data/data_config.json"):
        self._path = path

    def load_file(self):
        with open(self.path, "r", encoding="utf-8") as file:
            self._data_stores = json.load(file)
            print("Data Loaded!", self._data_stores, sep="\n")