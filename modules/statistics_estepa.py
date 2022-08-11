# Class to get all statistics needed
# Get parameters (list with all data) and config (dict with configurations)
# Config could be get from json file or default config
import os
import statistics
import json
import toml

#import scipy.integrate as integrate
import math
import numpy as np

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

import main
#from modules.functions import *

config_estepa_file = {
	"method" : "k-sigma",
	"lna" : False,
	"limmin" : 600,
	"limmax" : 1000
	}

class StatisticsEstepa():
	def __init__(self, param, data_list,config_estepa_file):
		self.param = param
		self.data_list = data_list # original data list
		self.data_list_ori = data_list
		self.ERROR_VALUE = -9e99
		self.ERROR_VALUE2 = 1e30
		self.mean = self.ERROR_VALUE
		self.median = self.ERROR_VALUE
		self.stdev = self.ERROR_VALUE
		self.corr = self.ERROR_VALUE							###
		self.points_ini = 0
		self.points_end = 0
		self.error = False
		self.error_message = ""

		self.methods = ["none","f-spread","k-sigma"]
		self.corr_methods = ["Pearson", "Spearman"]

		if "method" in config_estepa_file and "lna" in config_estepa_file and "limmin" in config_estepa_file and "limmax" in config_estepa_file:
			self.config = config_estepa_file # {"method": "None", lna" : False, "limmin" : 0, "limmax" : 100}

		else:
			self.error = True
			self.error_message = "Configuration estepa file not valid!"
		if isinstance(data_list,list):
			if len(self.data_list)>0:
				self.points_ini = len(data_list)
				# delete outliers
				self.outliers()
				# load statistics
				self.load_statistics()
				self.load_correlation()																				###
				self.points_end = len(data_list)
			else:
				self.error = True
				self.error_message = "List empty!"
		else:
			self.error = True
			self.error_message = "Is not a list!"

	def print_statistics(self):

		print_statistics = self.param + " : " + "\n"
		print_statistics +=" - Mean:   \t" + str(self.mean) + "\n"
		print_statistics +=" - Median:   \t" + str(self.median) + "\n"
		print_statistics +=" - Stdev:   \t" + str(self.stdev) + "\n"
		print_statistics +=" - Points:   \t" + str(self.points_end) + "/" + str(self.points_ini) + "\n"
		print_statistics +=" - Method:   \t" + str(self.config["method"]) + "\n"

		return print_statistics

	def print_correlation(self):																					###
		print_correlation = self.param + " : " + "\n"
		print_correlation +=" - Correlation:   \t" + str(self.corr) + "\n"
		print_correlation +=" - Points:   \t" + str(self.points_end) + "/" + str(self.points_ini) + "\n"
		print_correlation +=" - Method:   \t" + str(self.config["method"]) + "\n"
		print_correlation +=" - Corr. Method:   \t" + str(self.config["Corr. method"]) + "\n"

		return print_correlation

	def load_statistics(self):
		self.mean_estepa()
		self.median_estepa()
		self.stdev_estepa()

	def load_correlation(self):
		self.correlation_estepa()															####

	def mean_estepa(self):
		if len(self.data_list)>0:
			self.mean = statistics.mean(self.data_list)
		else:
			self.mean = self.ERROR_VALUE

	def median_estepa(self):
		if len(self.data_list)>0:
			self.median = statistics.median(self.data_list)
		else:
			self.median = self.ERROR_VALUE

	def stdev_estepa(self):
		if len(self.data_list)>1:
			self.stdev = statistics.stdev(self.data_list)
		else:
			self.stdev = self.ERROR_VALUE

	def correlation_estepa(self,data_list2):																	###
		if len(self.data_list)==2:
			self.corr = np.corrcoef(self.data_list, data_list2)
		else:
			self.corr = self.ERROR_VALUE

	def correlation_methods(self):
		if self.config["Corr. method"] in self.corr_methods:
			if self.config["Corr. method"]=="Pearson" and len(self.data_list_ori)>2:
				# method Pearson
				pass

			elif self.config["Corr. method"]=="Spearman" and len(self.data_list_ori)>2:
				# method Spearman
				pass

			elif self.config["Corr. method"]=="Kendall" and len(self.data_list_ori)>2:
				# method Spearman
				pass
		else:
			self.error = True
			self.error_message = "Mode not accepted!"

	def outliers(self):
		if self.config["method"] in self.methods:
			# 1) delete errors from list
			self.elim_err()
			# 2) delete limits not automatic
			if self.config["lna"]:
				self.data_list = self.elim_lna()

			# get limits  min (xmin) & max (xmax) of the list sended
			if self.config["method"]!="none":
				if self.config["method"]=="f-spread" and len(self.data_list)>2:
					# method f-spread (get quantiles with statistics library)
					while True:
						eliminados = 0
						n = len(self.data_list)
						if n==0: break
						arr = self.data_list
						r1 = (n+1) % 2
						d1 = int((n+1)/2)
						r2 = (n+1) % 4
						d2 = int((n+1)/4)
						x50 = ((2-r1)*self.kthSmallest(d1,n,arr) + r1*self.kthSmallest(d1+1,n,arr))/2
						x25 = ((3-r2)*self.kthSmallest(d2,n,arr) + (r2+1)*self.kthSmallest(d2+1,n,arr))/4
						x75 = ((r2+1)*self.kthSmallest(n-d2,n,arr) + (3-r2)*self.kthSmallest(n-d2+1,n,arr))/4
						# x25, x50, x75 = statistics.quantiles(self.data_list)
						r50 = x75 - x25
						xmin = x25 - 1.5*r50
						xmax = x75 + 1.5*r50


						for data in self.data_list:
							if data<=xmin or data>=xmax:
								self.data_list.remove(data)
								eliminados +=1
						if eliminados == 0: break

				elif self.config["method"]=="k-sigma" and len(self.data_list)>2:
					# metode K-SIGMA
					prvb=0.2
					while True:
						eliminados = 0
						n = len(self.data_list)
						if n==0: break
						self.load_statistics() # calc mean, median & stdev
						self.load_correlation() # calc correlation															#20/7
						klim = self.extract_k(n,prvb)
						xmin = self.mean - float(klim) * self.stdev
						xmax = self.mean + float(klim) * self.stdev

						for data in self.data_list:
							if data<=xmin or data>=xmax:
								self.data_list.remove(data)
								eliminados +=1
						if eliminados == 0: break

		else:
			self.error = True
			self.error_message = "Mode not accepted!"


	def elim_err(self):
		# delete errors in data_list
		if self.ERROR_VALUE2 in self.data_list:
			self.data_list.remove(self.ERROR_VALUE2)

	def elim_lna(self):
		# delete lna in data_list
		data_lista = self.data_list
		long = len(data_lista)-1
		# inverse loop for delete elements
		for i in range(long,-1,-1):
			if self.config["limmax"] < data_lista[i] or data_lista[i] < self.config["limmin"]:
				data_lista.remove(data_lista[i])
		return data_lista

	# method to extract the k'th smallest (sort & get element -1)
	def kthSmallest(self,k, n, arr):
		# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
		# Sort the given array
		arr.sort()
		# Return k'th element in the
		# sorted array
		return arr[k-1]

	# FUNCTIONS TO RESOLVE K-SIGMA METHOD
	# K is the value to resolve the ecuation (see integral_k-sigma.png)
	# (1/sqrt(2*PI)) * INTEGRAL{[-inf k](pow(e,x^2 / 2)) dx}  = (1/2) + (pow((1-p),(1/N))/2)

	# FUNCTION : erf (error function) is the solved integral (series function: see series_k-sigma.png)
	# ERROR FUNCTION FOR INTEGRAL K-SIGMA
	def erf(self,x):
		mult = math.sqrt(2)/2
		cte = 2/math.sqrt(math.pi)
		valor = float(x) * mult
		sign = -1
		serie = valor
		number_terms = 30 # number of terms in series
		# calculate factor numbers in series & save in list
		factor_numbers = []
		for i in range(0,number_terms):
			factor_numbers.append(i*2+1)
		# calc value serie of erf(valor)
		for terms in range(1,number_terms):
			# get fact_number
			fact_number = factor_numbers[terms]
			# get serie value
			serie = serie + sign * (pow(valor,fact_number))/(fact_number*math.factorial(terms))
			sign = sign * -1

		# return value : 0.5 is the value from integral from -inf to 0
		return 0.5 + (serie*cte)/2


	# FUNCTION : prvb_number
	# (1/2) + (pow((1-p),(1/N))/2) is a number function of N (number of samples)

	def prvb_number(self,N,prvb):
		return 0.5 + ((pow((1-prvb),1/N))/2)


	# EXTRACT KLIM FOR N SAMPLES & PROBABILITY NUMBER (assumed between 2-4)
	def extract_k(self,N,prvb,low_limit=2.0,high_limit=4.0):
		prvb_num = self.prvb_number(N,prvb)
		for i in np.arange(low_limit,high_limit,0.01):
			format_float = "{:.3f}".format(i)
			if self.erf(format_float)>=prvb_num:
				break

		return format_float

