#from manager import control_panel
from manager.control_panel import getForm, Control
from os import system

#running = False

self_control = Control()

#def start():
def start(running=True):
	#global running
	state_panel = "dc"
	while(running):
		system("cls")
		if(state_panel == "dc"):
			option = self_control.default_control()
			if(option != "o"):
				state_panel = getForm("dc_" + option)
			else:
				running = False

		elif(state_panel == "cdo"):
			getForm("cdo_" + self_control.config_data_options())
		elif(state_panel == "scf"):
			if()
			getForm("scf_" + self_control.start_create_file())
			state_panel = "dc"

		else:
			print("Internal Error Sorry, restart Program Please")
			running = False



if(__name__ == "__main__"):
	#running = True
	getForm("load_json")
	start()	





