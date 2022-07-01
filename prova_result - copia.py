from modules.result_file import *
from modules.statistics_estepa import *

import statistics

file_dat = ResultFile("test.dat","metrics")
if file_dat.error:
	print("Error in file: " + file_dat.error_message)
else:
	print(file_dat.print_info())
	print("Configuration: " + str(config_estepa_file))
	for param in file_dat.params_list:
		sEstepa = StatisticsEstepa(param, file_dat.param_to_list(param), config_estepa_file)
		
		print(param + " : " + str(sEstepa.data_list))
		print(" - Mean:   \t" + str(sEstepa.mean))
		print(" - Median: \t" + str(sEstepa.median))
		print(" - Stdev:  \t" + str(sEstepa.stdev))
		print("")
	
file_dat2 = ResultFile("12914-1CV100KHz.dat", "old")

if file_dat2.error:
	print("Error in file 2: " + file_dat2.error_message)
else:
	print(file_dat2.print_info())
	for param in file_dat2.params_list:
		if param=="cmax(pF)":
			config_estepa_file2 = {
				"method" : "k-sigma", # none, f-spread or k-sigma
				"lna" : False,
				"limmin" : 580.0,
				"limmax" : 600.0
			}
			sEstepa2 = StatisticsEstepa(param,file_dat2.param_to_list(param), config_estepa_file2)
		else:
			sEstepa2 = StatisticsEstepa(param,file_dat2.param_to_list(param), config_estepa_file)
		#print(param + " : " + str(sEstepa2.data_list))
		print(param)
		print(" - Mean:   \t" + str(sEstepa2.mean))
		print(" - Median: \t" + str(sEstepa2.median))
		print(" - Stdev:  \t" + str(sEstepa2.stdev))
		print(" - Points:  \t" + str(sEstepa2.points_end) + "/" + str(sEstepa2.points_ini))
		print("")


