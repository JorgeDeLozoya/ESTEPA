# Class to get Wafermap (could be from .py format or .ppg format)
import os
import datetime

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

#from modules.functions import *

class WafermapFile():
	def __init__(self, path_to_file,mode_type=".py"):
		self.error = False
		self.error_message = ""
		self.path_to_file = path_to_file
		self.filename = os.path.basename(self.path_to_file)
		self.mode_type = mode_type

		if os.path.exists(path_to_file):
			self.lines = []
			with open(path_to_file) as file_in:
				for line in file_in:
					if line!="":
						self.lines.append(line.replace("\n",""))
				self.number_lines = len(self.lines)
			if self.number_lines==0:
				#retval = messageBox(self,"Error loading file","File: " + path_to_file + " is empty!","error")	
				self.error_message = "File: " + path_to_file + " is empty!"
				self.error = True
			else:
				check_file = self.check_file()
				if not check_file[0]:
					#retval = messageBox(self,"Error checking file",check_file[1],"error")
					self.error = True
					self.error_message = check_file[1]
				# get params & data info
				if not self.get_variables():
					self.error = True
					self.error_message = "Problem getting wafermap!"
		else:
			#retval = messageBox(self,"Error loading file","File: " + path_to_file + " doesn't exists!","error")
			self.error_message = "File: " + path_to_file + " doesn't exists!"
			self.error = True

	#def print_info(self):


	def check_file(self):
	# set xmax & ymax
		if check_wafer_parameters:
			xmax_detected = 0
			ymax_detected = 0
			elementos_x_detected = []
			elementos_y_detected = []
			for elemento in self.wafer_positions:
				elemento_array = elemento.split()
				if len(elemento_array)!=2:
					check_wafer_parameters = False
					break
                # init variables
				elemento_x = elemento_array[0]
				elemento_y = elemento_array[1]
				buscar_x = False
				buscar_y = False
				num_elemento_x = 0
				num_elemento_y = 0
				if elemento_x not in elementos_x_detected:
#					elementos_x_detected = np.append(elementos_x_detected, elemento_x)
					buscar_x = True
				if elemento_y not in elementos_y_detected:
#					elementos_y_detected = np.append(elementos_y_detected, elemento_y)
					buscar_y = True
				if buscar_x and buscar_y:
					for elemento_buscar in self.wafer_positions:
						elemento_buscar_array = elemento_buscar.split()
						if elemento_buscar_array[0] == elemento_x:
							num_elemento_y += 1 # cambiamos el eje porque buscamos sumatorio en vertical
						if elemento_buscar_array[1] == elemento_y:
							num_elemento_x += 1 # cambiamos el eje porque buscamos sumatorio en horizontal

					if num_elemento_x>xmax_detected:
						xmax_detected = num_elemento_x
					if num_elemento_y>ymax_detected:
						ymax_detected = num_elemento_y

            # if xmax or ymax not initialized then equal to detected
			if self.xmax==0:
				self.xmax = xmax_detected
			if self.ymax==0:
				self.ymax = ymax_detected

			if xmax_detected!=self.xmax and ymax_detected!=self.ymax:
				check_wafer_parameters = False
				print("Error checking xmax (" + str(xmax_detected) + ") & ymax (" + str(ymax_detected) + ")...")


	def check_header_file(self):
		# Check header file metrics (wafer_name, wafer_size, xsize, ysize, nchips, nmodules)
		line_number = 0
		header_variables = ["wafer_name","wafer_size","xsize","ysize","nchips","nmodules"] 

		line = self.lines[line_number].strip("\t")
		if not "global wafer_parameters" in line:
			return [False, "Not global wafer_parameters tag founded!"]
		for header_var in header_variables:
			line_number += 1
			line = self.lines[line_number].strip("\t")
			if not header_var in line:
				return [False, "Not " + header_var + " info founded!"]
			else:
				line_split = line.split("\t")
				if (len(line_split)==2):
					cmd = "self." + header_var.lower() + "='" + line_split[1] + "'"
					exec(cmd)
		
		line_number += 1
		line = self.lines[line_number].strip("\t")
		if not ": navigation_options}" in line:
			return [False, "Not navigation_options tag founded!"]

		return [True,""]

	
	
	



