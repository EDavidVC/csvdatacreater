from random import randint
from datetime import datetime
import random

#class data_manager():
class DataManager:
	config_data = {}

	def __init__(self):
		print("Data Manager LocalDB is Initialized")

	def update_city(self, new_city_name):
		self.config_data["city"] = new_city_name

	def update_date_range(self, first_year, last_year):
		self.config_data["date_range"] = [first_year, last_year]

	def update_directions_shop(self, list_direction_shop):
		self.config_data["direction_shop"] = [list_direction_shop]

	def update_workers_names(self, list_workers_names):
		self.config_data["workers_names"] = [list_workers_names]

	def update_temperature(self, min_temperature, max_temperature):
		self.config_data["temperature"] = [min_temperature, max_temperature]

	def update_config(self, new_config_data):
		pass

	def charge_json_data(self, data_json):
		self.config_data = data_json

class Forms(DataManager):
	def update_city_form(self):
		new_city_name = input("Insert a new City: ")
		self.update_city(new_city_name)
		print("Update Successfully...")

	def update_date_range_form(self):
		first_year = int(input("Insert First YEAR(year: 1999): "))
		last_year = int(input("Insert Last YEAR  (year: 1999): "))
		self.update_date_range(first_year, last_year)
		print("Update Successfully...")

	def update_directions_shop_form(self):
		#isUpdating = True
		#direction_list = []
		#while (isUpdating):
			#direction = input("Insert a new Direction ('o' to save): ")
			#if(direction != o):
				#direction_list.append(direction)
			#else:
				#isUpdating = False
		#self.update_directions_shop(direction_list)
		direction_list = []
		while True :
			direction = input("Insert a new Direction ('o' to save): ")
			if direction != o:
				direction_list.append(direction)
			else:
				break
		self.update_directions_shop(direction_list)

	def update_workers_names_form(self):
		#isUpdating = True
		#workers_names = []
		#while (isUpdating):
			#worker_name = input("Insert a new Name Worker ('o' to save): ")
			#if(direction != o):
				#workers_names.append(worker_name)
			#else:
				#isUpdating = False
		#self.update_workers_names(list_workers_names)
		workers_names = []
		while True:
			worker_name = input("Insert a new Name Worker ('o' to save): ")
			if direction != o:
				workers_names.append(worker_name)
			else:
				break
		self.update_workers_names(list_workers_names)

	def update_temperatures_form(self):
		minTemperature = int(input("Insert to Min value to Temperature: "))
		maxTemperature = int(input("Insert to Max Value to Temperature: "))
		self.update_temperature(minTemperature, maxTemperature)

	def get_temperature(self, hour, mounth):
		t_min = 10
		t_max = 22
		temperature = 0
		if hour in self.config_data["max_sun_force"] and not mounth in self.config_data["summer_mounths"]:
			t_min = 18
			#temperature = randint(t_min, t_max)
		elif not hour in self.config_data["max_sun_force"] and not mounth in self.config_data["summer_mounths"]:
			#temperature = randint(t_min, t_max)
			pass
		elif not  hour in self.config_data["max_sun_force"] and mounth in self.config_data["summer_mounths"]:
			t_min = 18
			t_max = 25
			#temperature = randint(t_min, t_max)
		elif hour in self.config_data["max_sun_force"] and mounth in self.config_data["summer_mounths"]:
			t_min = 20
			t_max = 28
			#temperature = randint(t_min, t_max)
		temperature = randint(t_min, t_max)
		return temperature

	def get_ice_hour_sale(self, temperature):
		ices = 0
		ice_min = 0
		ice_max = 1
		if randint(-3,5) >= 1:
			#if temperature >=10 and temperature <=15:
			if temperature in range(10, 16):
				pass
				#ices = randint(ice_min, ice_max)
			elif temperature in range(16, 21):
				ice_max = 4
				#ices = randint(ice_min, ice_max)
			elif temperature in range(20, 25):
				ice_min = 2
				ice_max = 9
				#ices = randint(ice_min, ice_max)
			elif temperature >= 24:
				ice_min = 2
				ice_max = 12
				#ices = randint(ice_min, ice_max)
			ices = randint(ice_min, ice_max)
		minutes_sales = []
		while ices > len(minutes_sales):
			tem_minute = randint(0, 59)
			if not tem_minute in minutes_sales:
				minutes_sales.append(tem_minute)
		minutes_sales.sort()
		return minutes_sales

	def Day_its_okay(self, year, mounth, day):
		date = "%s/%s/%s"%(year,mounth,day)
		try:
			datetime.strptime(date, "%Y/%m/%d")
			return True
		except ValueError:
			return False

	def generate_json_data(self):
		#columnames = ["id", "Pais", "Ciudad", "Temperatura", "Encargado", "Tienda","Producto","Precio", "Fecha", "Hora"]
		columnames = ("id", "Pais", "Ciudad", "Temperatura", "Encargado", "Tienda","Producto","Precio", "Fecha", "Hora")
		temp_data = [columnames]
		mounth_cant = 12

		id_ = 0
		country_ = self.config_data["country"]
		year_init_ = self.config_data["date_range"][0]
		while year_init_ <= self.config_data["date_range"][1]:
			for mounth_ in range(1, mounth_cant+1):
				name_worker_ = ""
				city_ = ""
				name_store_ = ""
				temperature_ = 0
				hour_ = 0
				day_ = 0
				for day in range(1, 35):
					day_ = day
					temp_day_data =[]
					if self.Day_its_okay(year_init_, mounth_, day_):
						for name_worker in self.config_data["stores"]:
							name_worker_ = name_worker
							city_ = self.config_data["stores"][name_worker][0]
							name_store_ = self.config_data["stores"][name_worker][1]
							if self.Day_its_okay(year_init_, mounth_, day_):
								for hour in range(self.config_data["regular_time_work"][0], self.config_data["regular_time_work"][1]):
									hour_ = hour
									temperature_ = self.get_temperature(hour_,mounth_)
									
									for minute in self.get_ice_hour_sale(temperature_):
										product = random.choice(list(self.config_data["products"].items()))
										date_temp = datetime.strptime("%s/%s/%s %s:%s:%s"%(year_init_, mounth_, day_, hour_, minute, randint(0,59)), "%Y/%m/%d %H:%M:%S")
										temp_day_data.append([0, country_, city_, str(temperature_), name_worker_, name_store_,product[0], product[1], date_temp.date(),  date_temp.time()])
						temp_day_data.sort(key=lambda date: date[9])
						for hour_data in temp_day_data:
							hour_data[0] = id_
							temp_data.append(hour_data)
							id_ += 1


			year_init_ += 1

		return temp_data