from manager.data_manager import DataManager, Forms
#from manager.data_manager import forms
from manager.json_manager import get_json_of_stores_data
from manager.data_creater import create_file
from time import sleep

class Control(DataManager):
	def error_option(self):
		print("Error to Insert Option")
		sleep(2)

	def config_data_options(self):
		print("Insert Your Uption: \n a : Update City \n b : Update Date Range \n c : Update Directions Shop Stores \n d : Update Workser Names \n e : Update Temperature (Min/Max) \n o : back")
		option = input("Insert Here: ")
		#if(option in ["a","b","d","e","o"]):
			#return option
		#else:
			#self.error_option()
		#return "error"
		if option in ("a","b","d","e","o"):
			return option
		else:
			self.error_option()
			return "error"

	def default_control(self):
		print("Welcome to my Tool\n** Control Panel **")
		print("Insert Your Option \n a : Config Data Parameters \n b : Start Create the File .CSV \n o : Exit Program")
		option = input("Insert Here: ")
		#if(option in ["a","b","o"]):
			#return option
		#else:
			#self.error_option()
		#return option

		if not option in ("a", "b", "o"):
			self.error_option()
		return option

	def start_create_file(self):
		print("Your Data is Saving Are you Ok?")
		option = input("Insert Option (y/n): ")
		#if(option in ["y","n"]):
			#return option
		#else:
			#self.error_option()
		#return option
		if not option in ("y","n"):
			self.error_option()

		return option

forms_manager = Forms()

def getForm(id_option):
	if id_option == "cdo_a":
		forms_manager.update_city_form()
	elif id_option == "cdo_b":
		forms_manager.update_date_range_form()
	elif id_option == "cdo_c":
		forms_manager.update_directions_shop_form()
	elif id_option == "cdo_d":
		forms_manager.update_workers_names_form()
	elif id_option == "cdo_c":
		forms_manager.update_temperatures_form()
	elif id_option == "dc_a":
		return "cdo"
	elif id_option == "dc_b":
		return "scf"
	elif id_option == "scf_y":
		create_file(forms_manager.generate_json_data())
		print("Data is Created")
		sleep(5)
		return True
	elif id_option == "scf_n":
		return False
	elif id_option == "load_json":
		forms_manager.charge_json_data(get_json_of_stores_data())
	else:
		print("Internal Error, Close Program Please")
