from functions import *
from . result_file import *
from . wafermap_file import *

import psycopg2 


class Estepa():
	def __init__(self, config_estepa):
		try:
			self.error = False
			self.error_message = ""
			parameters = ["host","port","user","database","password"]
			parameters_found = True
			for param in parameters:
				if not param in config_estepa:
					parameters_found = False
					break

			if parameters_found:
				self.host = config_estepa["host"]
				self.port = config_estepa["port"]
				self.user = config_estepa["user"]
				self.database = config_estepa["database"]
				self.password = config_estepa["password"]
				# set timeout = 1 seconds
				if "timeout" in config_estepa:
					self.timeout = config_estepa["timeout"]
				else:
					self.timeout = 5 # 1 sec

				self.conn = psycopg2.connect(self.get_connect_string())
				

				# set autocommit
				if "autocommit" in config_estepa:
					self.conn.autocommit = config_estepa["autocommit"]
				else:
					self.conn.autocommit = False
				
				# create a cursor
				self.cur = self.conn.cursor()
				# execute a statement
				self.cur.execute('SELECT version()')

				# display the PostgreSQL database server version
				self.db_version = self.cur.fetchone()
				

			else:
				self.error = True
				self.error_message = "Parameters not found"


			
		except (Exception, psycopg2.DatabaseError) as error:
			self.error = True
			self.error_message = str(error)

		# finally:
		# 	if self.conn is not None:
		# 		self.conn.close()
		# 		print('Database connection closed.')

	def close_connection(self):
		# close the communication with the PostgreSQL
		if not self.error:
			self.cur.close()
			if self.conn is not None:
				self.conn.close()


	def get_connect_string(self):
		if self.password != "":
			return "host=" + self.host + " dbname=" + str(self.database) + " port=" + str(self.port) + " user=" + str(self.user) + " password=" + str(self.password) + " connect_timeout = " + str(self.timeout)
		else:
			return "host=" + self.host + " dbname=" + str(self.database) + " port=" + str(self.port) + " user=" + str(self.user) + " connect_timeout = " + str(self.timeout)
	
	def get_technologies(self,run=""):
		get_technologies = list()
		sql = "select distinct tecnologia from runs"
		if run!="":
			sql += " WHERE run='" + run + "'"
		self.cur.execute(sql)
		if self.cur.rowcount>0:
			row = self.cur.fetchone()
			while row is not None:
				get_technologies.append(row[0])
				row = self.cur.fetchone()

		return get_technologies

	def create_technology(self,run,fecha,tecnologia):
		create_technology = True
		try:
			sql = "INSERT INTO runs (run,fecha,tecnologia) VALUES (%s,%s,%s)"
			self.cur.execute(sql,(str(run),str(fecha),str(tecnologia)))
		except:
			create_technology = False

		return create_technology





	def get_runs(self,tecnologia):
		get_runs = list()
		sql = "select DISTINCT run from runs where tecnologia='" + tecnologia + "' order by run"
		self.cur.execute(sql)
		if self.cur.rowcount>0:
			row = self.cur.fetchone()
			while row is not None:
				get_runs.append(row[0])
				row = self.cur.fetchone()

		return get_runs

	def get_wafers(self,run):
		get_wafers = list()
		sql = "select DISTINCT oblea_virtual from obleas where run='" + run + "' order by oblea_virtual"
		self.cur.execute(sql)
		if self.cur.rowcount>0:
			row = self.cur.fetchone()
			while row is not None:
				get_wafers.append(row[0])
				row = self.cur.fetchone()

		return get_wafers

	def get_parameters(self,oblea_virtual):
		get_parameters = list()
		sql = "select distinct parametro from medidas where oblea_virtual='" + oblea_virtual + "' order by parametro;"
		self.cur.execute(sql)
		if self.cur.rowcount>0:
			get_parameters.append("All parameters")
			row = self.cur.fetchone()
			while row is not None:
				get_parameters.append(row[0])
				row = self.cur.fetchone()

		return get_parameters

	def get_medidas(self,oblea_virtual,parameters_list):

		get_medidas = dict()
		sql = "select * from medidas where oblea_virtual LIKE '" + oblea_virtual + "%' and parametro IN('" + "','".join(parameters_list) + "') order by parametro;"
		self.cur.execute(sql)
		if self.cur.rowcount>0:
			row = self.cur.fetchone()

			while row is not None:
				parametro = row[1]
				chip = row[2]
				medida = row[3]
				if parametro not in get_medidas:
					get_medidas[parametro] = dict()
					get_medidas[parametro]["chip"] = list()
					get_medidas[parametro]["medida"] = list()
				get_medidas[parametro]["chip"].append(chip)
				get_medidas[parametro]["medida"].append(medida)
				row = self.cur.fetchone()
		
		return get_medidas


	def get_rangos(self,tecnologia,parametro):
		get_rangos = list()
		sql = "select minimo, maximo FROM rangos WHERE tecnologia='" + tecnologia + "' and parametro='" + parametro + "'"
		self.cur.execute(sql)
		if self.cur.rowcount>0:
			row = self.cur.fetchone()
			minimo = row[0]
			maximo = row[1]
			get_rangos.append(minimo)
			get_rangos.append(maximo)

		return get_rangos

	def get_masks(self,wafer=""):
		get_masks = list()
		sql = "select distinct mascara from mascaras"
		if wafer!="":
			sql += " WHERE oblea='" + wafer + "'"
		self.cur.execute(sql)
		if self.cur.rowcount>0:
			row = self.cur.fetchone()
			while row is not None:
				get_masks.append(row[0])
				row = self.cur.fetchone()

		return get_masks


	def create_mask(self,mascara,oblea):
		create_mask = True
		try:
			sql = "INSERT INTO mascaras (mascara,oblea) VALUES (%s,%s)"
			self.cur.execute(sql, (str(mascara),str(oblea)))
		except:
			create_mask = False

		return create_mask

	def create_fechas(self,oblea_virtual,fecha_medida):
		create_fechas = True
		try:
			sql = "SELECT * FROM fechas WHERE oblea_virtual='" + oblea_virtual + "'"
			self.cur.execute(sql)
			if self.cur.rowcount==1:
				# update
				sql_update = """UPDATE fechas SET fecha_medida=%s WHERE oblea_virtual=%s"""
				self.cur.execute(sql_update,(fecha_medida, oblea_virtual))
				# self.conn.commit()
			else:
				# insert
				sql_insert = "INSERT INTO fechas (oblea_virtual,fecha_medida) VALUES (%s,%s)"
				self.cur.execute(sql_insert,(oblea_virtual,fecha_medida))
				# self.conn.commit()
		except:
			create_fechas = False

		return create_fechas

	def create_geometrias(self,geometria,wafer_size,xsize,ysize,xmaxim,ymaxim,nchips):
		create_geometrias = True
		try:
			sql = "SELECT * FROM geometrias WHERE geometria='" + geometria + "'"
			self.cur.execute(sql)
			if self.cur.rowcount==0:
				# insert
				# sql_insert = "INSERT INTO geometrias (geometria,wafer_size,xsize,ysize,xmaxim,ymaxim,nchips) VALUES	('" + geometria +"'," + float(wafer_size) + "," + float(xsize) + "," + float(ysize) + "," + int(xmaxim) + "," + int(ymaxim) + "," + int(nchips) + ")"
				sql_insert = "INSERT INTO geometrias (geometria,wafer_size,xsize,ysize,xmaxim,ymaxim,nchips) VALUES	(%s, %s, %s, %s, %s, %s, %s)"
				self.cur.execute(sql_insert, (geometria, wafer_size, xsize, ysize,xmaxim,ymaxim,nchips))
				# self.conn.commit()
			else:
				sql_update = "UPDATE geometrias set wafer_size = %s, xsize = %s, ysize = %s, ymaxim = %s, xmaxim, ymaxim = %s, nchips = %s WHERE geometria = %s"
				self.cur.execute(sql_update, (wafer_size, xsize, ysize,xmaxim,ymaxim,nchips,geometria))
		except:
			create_geometrias = False

		return create_geometrias

	def create_obleageom(self,oblea_virtual,geometria):
		create_obleageom = True
		try:
			sql = "SELECT * FROM obleageom WHERE oblea_virtual='" + oblea_virtual + "'"
			self.cur.execute(sql)
			if self.cur.rowcount==1:
				# update
				sql_update = "UPDATE obleageom SET geometria=%s WHERE oblea_virtual=%s"
				self.cur.execute(sql_update,(geometria,oblea_virtual))
				# self.conn.commit()
			else:
				# insert
				sql_insert = "INSERT INTO obleageom (oblea_virtual,geometria) VALUES (%s,%s)"
				self.cur.execute(sql_insert,(oblea_virtual,geometria))
				# self.conn.commit()
		except:
			create_obleageom = False

		return create_obleageom

	def create_obleas(self,run,oblea,oblea_virtual,comentario):
		create_obleas = True
		try:
			sql = "SELECT * FROM obleas WHERE run = '" + run + "' and oblea='" + oblea + "' and oblea_virtual='" + oblea_virtual + "'"
			self.cur.execute(sql)
			if self.cur.rowcount==1:
				# update
				sql_update = "UPDATE obleas SET comentario=%s WHERE run = %s and oblea=%s and oblea_virtual=%s"
				self.cur.execute(sql_update,(comentario,run,oblea,oblea_virtual))
				# self.conn.commit()
			else:
				# insert
				sql_insert = "INSERT INTO obleas (run,oblea,oblea_virtual,comentario) VALUES (%s,%s,%s,%s)"
				self.cur.execute(sql_insert,(run,oblea,oblea_virtual,comentario))
				# self.conn.commit()
		except:
			create_obleas = False

		return create_obleas

	def create_runs(self,run,fecha,tecnologia):
		create_runs = True
		try:
			sql = "SELECT * FROM runs WHERE run ='" + run + "'"
			self.cur.execute(sql)
			if self.cur.rowcount==1:
				# update
				sql_update = "UPDATE runs SET fecha=%s, tecnologia = %s WHERE run = %s"
				self.cur.execute(sql_update,(fecha,tecnologia,run))
				# self.conn.commit()
			else:
				# insert
				sql_insert = "INSERT INTO runs (run,fecha,tecnologia) VALUES (%s,%s,%s)"
				self.cur.execute(sql_insert,(run,fecha,tecnologia))
				# self.conn.commit()
				
		except:
			create_runs = False

		return create_runs


	def create_localizaciones(self,oblea,localizacion,standard=False):
		create_localizaciones = True
		try:
			sql = "SELECT * FROM localizaciones WHERE oblea='" + oblea + "'"
			self.cur.execute(sql)
			if self.cur.rowcount==1:
				# update
				sql_update = "UPDATE localizaciones SET localizacion=%s, standard=%s WHERE oblea=%s"
				self.cur.execute(sql_update,(localizacion,standard,oblea))
				# self.conn.commit()
			else:
				# insert
				sql_insert = "INSERT INTO localizaciones (oblea,localizacion,standard) VALUES (%s,%s,%s)"
				self.cur.execute(sql_insert,(oblea,localizacion,standard))
				# self.conn.commit()
		except:
			create_localizaciones = False

		return create_localizaciones

	def create_medidas(self,mainWindow, inbase_parameters):
		create_medidas = True
		insert_medidas = list()
		try:
			# create result file
			result_file = ResultFile(inbase_parameters["dataFile"])
			num_modules = len(result_file.modules)
			for die in result_file.params:
				die_txt = "(" + die.replace(" ",",") + ")"
				for module in range(1,num_modules+1):
					for param in result_file.params[die][str(module)]:
						medida = result_file.params[die][str(module)][param]
						insert_medidas.append((inbase_parameters["virtual_wafer"],param,die_txt,float(medida)))
						
			mainWindow.updateTextImportReport(" => Loop finish...")
			if create_medidas:
				mainWindow.updateTextImportReport(" => Inserting medidas...")
				sql_insert = "INSERT INTO medidas (oblea_virtual,parametro,chip,medida) VALUES (%s,%s,%s,%s)"
				self.cur.executemany(sql_insert,insert_medidas)
				# if len(update_medidas)>0:
				# 	mainWindow.updateTextImportReport(" => Updating medidas...")
				# 	sql_update = "UPDATE medidas SET medida=%s WHERE oblea_virtual=%s and parametro=%s and chip=%s"
				# 	self.cur.executemany(sql_update,update_medidas)
		except:
			create_medidas = False

		return create_medidas

	def create_medida(self,oblea_virtual,parametro,chip,medida):
		create_medida = [True,"insert"]
		try:
			sql = "SELECT medida FROM medidas WHERE oblea_virtual='" + oblea_virtual + "' and parametro='" + parametro + "' and chip='" + chip + "'" 
			self.cur.execute(sql)
			if self.cur.rowcount==1:
				# update
				create_medida = [True,"update"]
				#sql_update = "UPDATE medidas SET medida=%s WHERE oblea_virtual=%s and parametro=%s and chip=%s"
				#self.cur.execute(sql_update,(float(medida),oblea_virtual,parametro,chip))

				# insert
				# sql_insert = "INSERT INTO medidas (oblea_virtual,parametro,chip,medida) VALUES (%s,%s,%s,%s)"
				# self.cur.execute(sql_insert, (oblea_virtual,parametro,chip,float(medida)))
				# self.conn.commit()
		except:
			create_medida = [False,""]

		return create_medida


	def exists_measurements(self,oblea_virtual):
		exists_measurements = False
		sql = "SELECT * FROM medidas WHERE oblea_virtual LIKE '" + oblea_virtual + "%'"
		self.cur.execute(sql)
		if self.cur.rowcount>0:
			exists_measurements = True

		return exists_measurements

	def get_virtual_wafer(self,oblea):
		letras = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
		sql = "SELECT * FROM obleas WHERE oblea_virtual LIKE '" + oblea + "%'"
		self.cur.execute(sql)
		numrows = self.cur.rowcount
		if numrows>0:
			if numrows==1:
				virtual_wafer = oblea + "a"
				# update oblea_virtual in all tables without letter to "a"
				sql = "UPDATE fechas SET oblea_virtual = %s WHERE oblea_virtual = %s"
				self.cur.execute(sql,(virtual_wafer,oblea))
				sql = "UPDATE obleageom SET oblea_virtual = %s WHERE oblea_virtual = %s"
				self.cur.execute(sql,(virtual_wafer,oblea))
				sql = "UPDATE obleas SET oblea_virtual = %s WHERE oblea_virtual = %s"
				self.cur.execute(sql,(virtual_wafer,oblea))
				sql = "UPDATE medidas SET oblea_virtual = %s WHERE oblea_virtual = %s"
				self.cur.execute(sql,(virtual_wafer,oblea))


			return oblea + letras[numrows+1]

		return oblea


	def inbase(self, mainWindow, inbase_parameters):
		# inbase_parameters = {
		#           "dataFile" : txtDataFileInbase,
		#           "wafermapFile" : txtWafermapFileInbase,
		#           "run" : txtRunUpload,
		#           "wafer" : txtRunUpload + "-" + txtWaferUpload,
		# 			"virtual_wafer" : txtRunUpload + "-" + txtWaferUpload + letra,
		#           "date" : txtDateUpload,
		#           "technology" : txtTechnologyUpload,
		#           "mask" : txtMaskUpload,
		#           "localization" : txtLocalizationUpload,
		#           "comment" : txtCommentUpload
		#       }

		try:
			error = False
			error_message = ""

			technologies = self.get_technologies(inbase_parameters["run"])
			masks = self.get_masks(inbase_parameters["wafer"])

			if not inbase_parameters["technology"] in technologies:
				# create technology
				mainWindow.updateTextImportReport("- Creating tecnologia...")
				if not self.create_technology(inbase_parameters["run"],inbase_parameters["date"],inbase_parameters["technology"]):
					error = True
					error_message = "Error uploading new technology: " + inbase_parameters["technology"]

			if not inbase_parameters["mask"] in masks:
				# create mask
				mainWindow.updateTextImportReport("- Creating mask...")
				if not self.create_mask(inbase_parameters["mask"],inbase_parameters["wafer"]):
					error = True
					error_message = "Error uploading new mask: " + inbase_parameters["mask"]

			
			if not error:
				mainWindow.updateTextImportReport("- Uploading fechas information...")
				# put all info in tables
				if self.create_fechas(inbase_parameters["virtual_wafer"],inbase_parameters["date"]):
					# create object wafermap file
					wafermap_file = WafermapFile(inbase_parameters["wafermapFile"])

					geometria = wafermap_file.wafer_parameters["wafer_name"]
					wafer_size = wafermap_file.wafer_parameters["wafer_size"]
					xsize = wafermap_file.wafer_parameters["xsize"]
					ysize = wafermap_file.wafer_parameters["ysize"]
					xmaxim = wafermap_file.wafer_parameters["xmax"]
					ymaxim = wafermap_file.wafer_parameters["ymax"]
					nchips = wafermap_file.wafer_parameters["nchips"]
					mainWindow.updateTextImportReport("- Uploading geometrias information...")
					if self.create_geometrias(geometria,wafer_size,xsize,ysize,xmaxim,ymaxim,nchips):
						mainWindow.updateTextImportReport("- Uploading localizaciones information...")
						if self.create_localizaciones(inbase_parameters["wafer"],inbase_parameters["localization"]):
							mainWindow.updateTextImportReport("- Uploading obleageom information...")
							if self.create_obleageom(inbase_parameters["virtual_wafer"],geometria):
								mainWindow.updateTextImportReport("- Uploading obleas information...")
								if self.create_obleas(inbase_parameters["run"],inbase_parameters["wafer"],inbase_parameters["virtual_wafer"],inbase_parameters["comment"]):
									mainWindow.updateTextImportReport("- Uploading runs information...")
									if self.create_runs(inbase_parameters["run"],inbase_parameters["date"],inbase_parameters["technology"]):
										# create measurements
										mainWindow.updateTextImportReport("- Uploading medidas information...")
										if self.create_medidas(mainWindow, inbase_parameters):
											if not self.conn.autocommit:
												mainWindow.updateTextImportReport("COMMIT process...")
												self.conn.commit()
										else:
											error = True
											error_message = "Error uploading medidas information!"
									else:
										error = True
										error_message = "Error uploading runs information!"
								else:
									error = True
									error_message = "Error uploading obleas information!"
							else:
								error = True
								error_message = "Error uploading obleageom information!"
						else:
							error = True
							error_message = "Error uploading localizaciones information!"	
					else:
						error = True
						error_message = "Error uploading geometrias information!"
				else:
					error = True
					error_message = "Error uploading fechas information!"

			if error and not self.conn.autocommit:
				mainWindow.updateTextImportReport("ROLLBACK process...")
				self.conn.rollback()
				error_message = "Error in transaction Reverting all other operations of a transaction: " + error_message

			return [error, error_message]

		except (Exception, psycopg2.DatabaseError) as errorDatabase:
			mainWindow.updateTextImportReport("Error in transaction: " + errorDatabase)
			if not self.conn.autocommit:
				mainWindow.updateTextImportReport("ROLLBACK process...")
				self.conn.rollback()
				return [False, "Error in transaction Reverting all other operations of a transaction: " + errorDatabase]
			return [False, "Error in transaction: " + errorDatabase]


	