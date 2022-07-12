#GENERAL FUNCTION
import os
import json

def get_json_file(filename, var_name):
	# if configuration json file exists load configuratión from file
	filename_config = os.getcwd() + '/modules/' + filename + '.json'
	file_exists = os.path.exists(filename_config)
	try :
		if file_exists:
			with open(filename_config) as json_file:
				return json.load(json_file)
		else:
			# generate json file default
			return ""
	except:
		return ""

	return var_name
