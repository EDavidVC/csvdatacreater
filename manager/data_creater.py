import csv
def create_file(data):
	with open("data/alldata.csv", "w", newline="") as file:
		writer = csv.writer(file, delimiter=",")
		writer.writerows(data)