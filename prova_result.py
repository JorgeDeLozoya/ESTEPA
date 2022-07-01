from modules.result_file import *
import statistics

file_dat = ResultFile("test.dat")

if file_dat.error:
	print("Error in file: " + file_dat.error_message)
else:
	print(file_dat.print_info())
	print(file_dat.params_list)

	for param in file_dat.params_list:
		print(param + " : " + str(file_dat.param_to_list(param)))
		print(" - Mean:   \t" + str(statistics.mean(file_dat.param_to_list(param))))
		print(" - Median: \t" + str(statistics.median(file_dat.param_to_list(param))))
		print(" - Stdev:  \t" + str(statistics.stdev(file_dat.param_to_list(param))))
		print("")
	
