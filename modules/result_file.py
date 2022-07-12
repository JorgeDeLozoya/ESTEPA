# ----------------------------------------------
# CLASS ResultFile to read a measure file (could be from old format or metrics format)
# ----------------------------------------------
import os
import datetime
import re

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

#from modules.functions import *

class ResultFile():
	def __init__(self, path_to_file):
		self.error = False
		self.error_message = ""
		self.path_to_file = path_to_file
		self.filename = os.path.basename(self.path_to_file)
		self.mode_types = ["metrics","old"]
		self.mode_type = ""
		self.number_lines = 0
		self.process = ""
		self.lot = ""
		self.wafer = ""
		self.mask = ""
		self.operator = ""
		self.date = ""
		self.time = ""
		self.params = {}
		self.data = {}
		self.dies = []
		self.modules = []
		self.params_list = []
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
					self.error_message = "Problem getting params or data!"
		else:
			#retval = messageBox(self,"Error loading file","File: " + path_to_file + " doesn't exists!","error")
			self.error_message = "File: " + path_to_file + " doesn't exists!"
			self.error = True

	def info(self):
		return "------------------------------------------\n" \
		"  INFO FILE: " + "\t" + self.filename + "\n" \
		"------------------------------------------\n" \
		"  - Process:   " + "\t" + self.process + "\n" \
		"  - Lot:       " + "\t" + self.lot + "\n" \
		"  - Wafer:     " + "\t" + self.wafer + "\n" \
		"  - Mask:      " + "\t" + self.mask + "\n" \
		"  - Operator:  " + "\t" + self.operator + "\n" \
		"  - Date:      " + "\t" + self.date + "\n" \
		"  - Time:      " + "\t" + self.time + "\n" \
		"  - Chips:     " + "\t" + str(len(self.dies)) + "\n" \
		"------------------------------------------\n" 

	def check_file(self):
		if self.lines[0]=="<BEG GLOBAL>":
			self.mode_type = "metrics"
		elif "No=" in self.lines[2] and "Nv=" in self.lines[3]:
			self.mode_type = "old"

		# Verifications for result file
		if self.mode_type in self.mode_types:
			if self.mode_type=="metrics":
				# 1) check begin and end
				if not "<BEG GLOBAL>" in self.lines[0] or not"<END> WAFER" in self.lines[self.number_lines-1]:
					return [False, "Problem in BEGIN or END tags"]
				# 2) check globals
				header_file = self.check_header_file()
				if not header_file[0]:
					return [False, header_file[1]]
			if self.mode_type=="old":
				if self.lines[0]!='""':
					self.process = self.line[0].replace('"','') # run-wafer
					self.lot = self.process.split("-")[0] # run
					self.wafer = self.process.split("-")[1] # wafer
				else:
					# get process, lot & wafer from name if empty information
					s = [str(s) for s in re.findall(r'-?\d+\.?\d*', self.filename)]
					if len(s)>=2: # first 2 contains run & wafer!!
						s = s[0:2]
						self.process = ''.join(s)
						self.lot = s[0]
						self.wafer = s[1].replace("-","")

				# file modification timestamp of a file
				m_time = os.path.getmtime(self.path_to_file)
				# file creation timestamp of a file
				c_time = os.path.getctime(self.path_to_file)
				# convert timestamp into DateTime object
				dt_m = datetime.datetime.fromtimestamp(c_time)
				dt_ms = dt_m.strftime("%d/%m/%Y %H:%M:%S")
				self.date = dt_ms.split(" ")[0]
				self.time = dt_ms.split(" ")[1]
		else:
			return [False, "Mode type '" + str(self.mode_type) + "' not available!"]

		return [True,""]

	def check_header_file(self):
		# Check header file metrics (process, lot, wafer, operator, date, time)
		line_number = 0
		header_variables = ["Process","Lot","Wafer","Mask","Operator","Date","Time"]
		line = self.lines[line_number].strip("\t")
		if not "<BEG GLOBAL>" in line:
			return [False, "Not BEG GLOBAL tag founded!"]
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
		if not "<END GLOBAL>" in line:
			return [False, "Not END GLOBAL tag founded!"]

		return [True,""]

	def get_variables(self):
		# get all variables (params & data) in file and save to self.params & self.data
		try:
			self.params = {}
			self.data = {}
			die = ""
			module = ""
			line_number = 0
			if self.mode_type=="metrics":
				# get variables from metrics format file
				for line_number in range(0,self.number_lines-1):
					line = self.lines[line_number]
					if "<BEG> DIE " in line:
						die = line.replace("<BEG> DIE ","").replace("\t","")
						self.params[die] = {}
						self.data[die] = {}
						self.dies.append(die)
					if "<BEG> MODULE " in line:
						module = line.replace("<BEG> MODULE ","").replace("\t","")
						self.params[die][module] = {}
						self.data[die][module] = {}
						if not module in self.modules:
							self.modules.append(module)
					if "<END> DIE " in line:
						die = ""
					if "<END> MODULE " in line:
						module = ""
					if "<BEG PARMS>" in line:
						line_number += 1
						self.params[die][module] = {}
						while (not "<END PARMS>" in self.lines[line_number]):
							line = self.lines[line_number].strip("\t") # out tab at beggining & end
							param = line.split("\t")[0]
							value = line.split("\t")[1]
							self.params[die][module][param] = float(value)
							line_number += 1
							if param not in self.params_list:
								self.params_list.append(param)
					if "<BEG DATA>" in line:
						line_number += 1
						self.data[die][module] = {}
						firstline = True
						while (not "<END DATA>" in self.lines[line_number]):
							# first line with variable names
							line = self.lines[line_number].strip("\t") # out tab at beggining & end
							if firstline:
								variables_list = line.split("\t")
								# create vars into data
								for var in variables_list:
									self.data[die][module][var] = []
								firstline = False
							else: 
								# get data for each line
								data_list = line.split("\t")
								num = 0
								# assign into var list
								for var in variables_list:
									self.data[die][module][var].append(data_list[num])
									num +=1
							line_number += 1
				return True
			if self.mode_type=="old":
				# get variables from metrics format file (no data)
				number_dies = 0
				number_parameters = 0
				numero_linea = 0
				for line_number in range(0,self.number_lines):
					line = self.lines[line_number]
					if "No=" in line:
						number_dies = int(line.replace('"','').replace('No=',''))
						if number_dies<=0:
							return False
					if "Nv=" in line:
						number_parameters = int(line.replace('"','').replace('Nv=','')) - 2
						if number_parameters<=0:
							return False
					if '"" "COLUMN" "ROW"' in line:
						# get parameters
						self.params_list = line.replace('"" "COLUMN" "ROW" ','').replace('"','').split()
						if len(self.params_list)!=number_parameters:
							return False
						else:
							numero_linea = line_number
				for line_number in range (numero_linea+1,self.number_lines):
					line = self.lines[line_number]
					if line!="": 
						# while not empty
						datos = line.replace('" " ','').split(" ")
						column = datos[0]
						row = datos[1]
						die = column + " " + row
						module = "1" # only one module
						if not die in self.dies:
							self.dies.append(die)
						if not module in self.modules:
							self.modules.append(module)
						# init dicts
						self.params[die] = {}
						self.data[die] = {}
						self.params[die][module] = {}
						self.data[die][module] = {}
						# add all params
						i = 2
						for param in self.params_list:
							self.params[die][module][param] = float(datos[i])
							i += 1

					else:
						break
				return True
		except:
			print("Exception")
			return False

	def param_to_list(self,name_param):
		list_return = []
		if name_param in self.params_list:
			for die in self.dies:
				for module in self.modules:
					if name_param in self.params[die][module]:
						list_return.append(self.params[die][module][name_param])
		return list_return
	
	
	
	def get_params(self, name_params):
		# get param + medida for get the statistics to print in QPlainText
		get_params = dict()			
		for die in self.dies:
			for module in self.modules:
				for param in self.params_list:
					if param in name_params:
						medida = self.params[die][module][param]		# get medida value	
						if not param in get_params:
							get_params[param] = dict()					# create dict to store medida value
							get_params[param]["medida"] = list()
						get_params[param]["medida"].append(medida)		# append value medida to list

		return get_params							

	def get_data_values(self, name_param):
		# get data values chip + medida for printing in QPlainText
		get_values = dict()			
		for die in self.dies:
			for module in self.modules:
				for param in self.params_list:
					if param == name_param:
						medida = self.params[die][module][param]		# get medida value		
						if not die in get_values:
							get_values[die] = dict()					
							get_values[die] = medida	

		return get_values							


