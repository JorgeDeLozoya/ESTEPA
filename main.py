# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

#from distutils.log import error
import sys
import os
import platform
import toml

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
# general functions
from functions import *
# datetime
from datetime import datetime

from scipy.stats import norm, kendalltau, spearmanr, pearsonr, chi2_contingency
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from qbstyles import mpl_style

from scipy.stats import norm
from io import open             #mòdul per obrir fitxers externs      

#import matplotlib.pyplot as plt
import pyqtgraph as pg     
import seaborn as sb                      
import statistics               #Biblioteca que inclou les funcions estadistiques
#import matplotlib
import scipy
import numpy as np                     
import json                     #Opció 2

import matplotlib.pyplot as plt
import pandas as p


os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
#app = QtWidget.QApplication(sys.argv) Per solucionar el error de QApplication

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
import_report_file = "report_import.txt"


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        # CONFIG
        self.modo_histograma=True
        self.measurements=None
        self.directorio_trabajo=""  #POR ACABAR

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets  #var global per tots els widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "ESTEPA"
        description = "ESTEPA"
        # ///////////////////////////////////////////////////////////////
        # SET MINIMUN WINDOW SIZE

        self.setMinimumSize(1360, 1000)

        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # LOAD configuration TOML
        self.path_config_file = os.getcwd() + '/config/config.toml'
        self.load_config() 
        # -----------
        # PAGE ESTEPA
        # -----------
  
        # LOAD FROM FILES
        widgets.btnLoadFiles.clicked.connect(self.load_from_files)
        widgets.btnAnalyzeFiles.clicked.connect(self.analyze_files)
        widgets.btnCorrelationFiles.clicked.connect(self.correlation_files)

        # LOAD FROM BBDD
        widgets.optLoadFiles.clicked.connect(self.viewOptionsEstepa)
        widgets.optLoadBBDD.clicked.connect(self.viewOptionsEstepa)
        widgets.cmbTechnology.currentIndexChanged.connect(self.load_cmbRuns)
        widgets.cmbTechnologyConsult.currentIndexChanged.connect(self.load_cmbRuns_consult)
        widgets.cmbRuns.currentIndexChanged.connect(self.load_cmbWafers)
        widgets.cmbRunsConsult.currentIndexChanged.connect(self.load_cmbWafers_consult)
        widgets.cmbWafers.currentIndexChanged.connect(self.load_cmbParametersBBDD)
        widgets.cmbWafersConsult.currentIndexChanged.connect(self.load_cmbParametersBBDD_consult)
        widgets.cmbParametersBBDD.editTextChanged.connect(self.update_cmbParametersBBDD)
        widgets.btnAnalyzeBBDD.clicked.connect(self.analyze_BBDD)
        widgets.btnConsult.clicked.connect(self.consult_BBDD)

        # configuration estepa
        widgets.scrollHistogramChunks.valueChanged.connect(lambda: widgets.txtHistogramChunks.setText(str(widgets.scrollHistogramChunks.value())))
        widgets.txtHistogramChunks.textChanged.connect(self.save_config_estepa_file)
        # get values from toml config & set widgets
        self.methods = ["none","f-spread","k-sigma"]
        widgets.cmbOutlinerMethod.setCurrentIndex(self.methods.index(self.config["estepa"]["method"]))
        widgets.chkNonAutomaticLimits.setChecked(self.config["estepa"]["lna"])
        if self.config["estepa"]["lna"]:
            widgets.optionsNonAutomatic.setCurrentWidget(widgets.config_nonAutomatic)
        else:
            widgets.optionsNonAutomatic.setCurrentWidget(widgets.config_Automatic)

        widgets.chkGetAutoLimits.setChecked(self.config["estepa"]["autolimits"])

        widgets.txtLimitMin.setText(str(self.config["estepa"]["limmin"]))
        widgets.txtLimitMax.setText(str(self.config["estepa"]["limmax"]))

        widgets.cmbOutlinerMethod.currentIndexChanged.connect(self.save_config_estepa_file)
        widgets.chkNonAutomaticLimits.stateChanged.connect(self.save_config_estepa_file)
        widgets.txtLimitMin.textChanged.connect(self.save_config_estepa_file)
        widgets.txtLimitMax.textChanged.connect(self.save_config_estepa_file)
        widgets.chkGetAutoLimits.stateChanged.connect(self.save_config_estepa_file)

        widgets.historicalcheck.stateChanged.connect(self.historical_check)

        
        ##btnDirectory

        widgets.cmbTechnologyUpload.currentIndexChanged.connect(self.updateTextTechnologyUpload)
        widgets.cmbMaskUpload.currentIndexChanged.connect(self.updateTextMaskUpload)
        widgets.txtDateUpload.setText(datetime.today().strftime('%Y-%m-%d'))
        widgets.btnUploadFiles.clicked.connect(self.UploadFiles)
        widgets.btnClearImportReport.clicked.connect(lambda: widgets.txtImportReport.setPlainText(""))
        widgets.btnSaveImportReport.clicked.connect(self.save_import_report)

        widgets.btnOpenDataFile.clicked.connect(self.open_file_dat)
        widgets.btnOpenWafermapFile.clicked.connect(self.open_file_ppg)

        # PAGE INBASE
        widgets.btnOpenDataFileInbase.clicked.connect(self.open_file_dat)
        widgets.btnOpenWafermapFileInbase.clicked.connect(self.open_file_ppg)

        # configuration pages
        widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_measurements)
        
        widgets.btnClear_DataValues.clicked.connect(self.buttonClick)
        widgets.btnClear_ParametersResult.clicked.connect(self.buttonClick)
        widgets.btnCopyDescription_2.clicked.connect(self.copy_values)
        widgets.btnCopyDescription_3.clicked.connect(self.copy_results)
        widgets.btnSaveDescription_2.clicked.connect(self.save_values)
        widgets.btnSaveDescription_3.clicked.connect(self.save_results)
        widgets.btnNextParam.clicked.connect(self.next_parameter)
        widgets.btnTheme.clicked.connect(self.change_theme)
        
        widgets.txtCurrentParameter.text()

        # HOME MENUS
        widgets.home_analysis.clicked.connect(self.buttonClick)
        widgets.home_consult.clicked.connect(self.buttonClick)
        widgets.home_upload.clicked.connect(self.buttonClick)



        #LEFT MENUS
        widgets.btn_page_home.clicked.connect(self.buttonClick)
        widgets.btn_page_estepa.clicked.connect(self.buttonClick)
        widgets.btn_page_consult.clicked.connect(self.buttonClick)
        widgets.btn_page_inbase.clicked.connect(self.buttonClick)


        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.Home_Window)
        widgets.btn_page_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_page_home.styleSheet()))
        # widgets.btn_page_estepa.setStyleSheet(UIFunctions.selectMenu(widgets.btn_page_estepa.styleSheet()))
        # widgets.btn_page_consult.setStyleSheet(UIFunctions.selectMenu(widgets.btn_page_consult.styleSheet()))
        # widgets.btn_page_inbase.setStyleSheet(UIFunctions.selectMenu(widgets.btn_page_inbase.styleSheet()))

        # widgets.home_analysis.setStyleSheet(UIFunctions.selectMenu(widgets.home_analysis.styleSheet()))                   #4/8
        # widgets.home_consult.setStyleSheet(UIFunctions.selectMenu(widgets.home_consult.styleSheet()))
        # widgets.home_upload.setStyleSheet(UIFunctions.selectMenu(widgets.home_upload.styleSheet()))
        
        # LOAD ESTEPA 
        # config_estepa = {
        #     "host" : "opter6.cnm.es",
        #     "port" : "5432",
        #     "user" : "joaquin",
        #     "database" : "mecao",
        #     "password" : "",
        #     "autocommit" : False
        # }
        # # if configuration json file exists load configurationñ from file
        # get_json = get_json_file('estepa',config_estepa)
        # if get_json!="":
        #     config_estepa = get_json
        # # self.estepa = Estepa(self.config["connection"])         #Descomentar error inicial
        # # if not self.estepa.error:
        # #     self.load_cmbTechnology()
        # #     self.load_cmbMask()
        # # else:
        # #         retval = messageBox(self,"Error loading ESTEPA class",self.estepa.error_message,"error")
        # # widgets.cmbParametersFile.clear()
        # # widgets.cmbParametersBBDD.clear()

    # ----------------
    # ESTEPA FUNCTIONS
    # ----------------

    #LOAD FROM FILES
    def load_from_files(self):
        file_dat = widgets.txtDataFile.text()
        file_ppg = widgets.txtWafermapFile.text()
        file_result = ResultFile(file_dat)
        file_wafermap = WafermapFile(file_ppg)
        parameters_list = file_result.params_list
        parameters_list.insert(0,"All parameters")
        widgets.cmbParametersFile.addItems(parameters_list)

    #ANALYZE
    def analyze_files(self):

        self.textoParametros={}             #16/8       diccionario
        
        parameters_file = widgets.cmbParametersFile.currentText()   # get text of combo Parameters
        parameters_file_list = parameters_file.split(", ")          # split to create list
        FileName = widgets.txtDataFile.text() 
        result_file = ResultFile(FileName)

        self.parametroMostrando=0           #16/8

        print(parameters_file)

        # wafermap_file = WafermapFile(FileName)
        if not result_file.error:
            if parameters_file!="":
                # GET parameters result
                measurements = result_file.get_params(parameters_file_list)
                # wafer = wafermap_file.get_xmax_ymax()

                widgets.txtParametersResult.setPlainText("")
                for par in parameters_file_list:
                    estadistica = StatisticsEstepa(par, measurements[par]["medida"], (self.config["estepa"]))
                    widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+estadistica.print_statistics())
                # GET DATA VALUES, HISTOGRAM & WAFERMAP IF PARAM==1
                
                # Get data values from result_file
                for fileName in parameters_file_list:
                    self.textoParametros[fileName]=""
                    data_values = result_file.get_data_values(fileName)
                    widgets.txtParametersResult.setPlainText("X "+"Y "+"Measurement")
                    for chip in data_values:
                        self.textoParametros[fileName]+=str(chip)+" "+str(data_values[chip])+"\n"
                
                par=list(self.textoParametros.keys())[self.parametroMostrando]
                widgets.txtCurrentParameter.setText(par)
                widgets.txtLoadedValues.setPlainText(self.textoParametros[par])
                self.generate_histogram(measurements[par]["medida"])
                # Get wafermap
                self.generate_wafermap()   
            else:
                retval = messageBox(self,"Error getting parameters list","Please, select at least one parameter!","warning")
        else:
            retval = messageBox(self,"Error getting Result File",self.result_file.error_message,"warning")

    # NEXT PARAMETER
    def next_parameter(self):
        FileName = widgets.txtDataFile.text() 
        result_file = ResultFile(FileName)
        measurements = result_file.get_params(list(self.textoParametros.keys()))
        self.parametroMostrando=(self.parametroMostrando+1)%len(self.textoParametros)
        par=list(self.textoParametros.keys())[self.parametroMostrando]
        widgets.txtCurrentParameter.setText(par)
        widgets.txtLoadedValues.setPlainText(self.textoParametros[par])
        self.generate_histogram(measurements[par]["medida"])                        #ERROR

    # CORRELATION
    def correlation_files(self):
        error = False
        if widgets.optLoadFiles.isChecked():
            txt_param_selected = widgets.cmbParametersFile.currentText().split(', ')[0]
            parameters = widgets.cmbParametersFile.currentText()
            parameters_list = parameters.split(", ")
            FileName = widgets.txtDataFile.text()
            result_file = ResultFile(FileName)
            if not result_file.error:
                if len(parameters_list)==2:
                    measurements = result_file.get_params(parameters_list)
                    data1 = measurements[parameters_list[0]]["medida"]
                    data2 = measurements[parameters_list[1]]["medida"]
                else:
                    error = True
                    retval = messageBox(self,"Error selecting variables","Select 2 parameters for correlation","warning")    
            else:
                error = True
                retval = messageBox(self,"Error getting Result File",self.result_file.error_message,"warning")
        else:
            txt_param_selected = widgets.cmbParametersBBDD.currentText().split(', ')[0]
            parameters = widgets.cmbParametersBBDD.currentText()
            parameters_list = parameters.split(", ")
            wafer = widgets.cmbWafers.currentText()
            measurements = self.estepa.get_medidas(wafer,parameters_list)
            if not self.estepa.error:
                # get data1 & data2
                data1 = measurements[parameters_list[0]]["medida"]
                data2 = measurements[parameters_list[1]]["medida"]
            else:
                error = True
                retval = messageBox(self,"Error getting measurements Estepa",self.estepa.error_message,"warning")
            

        if not error:
            statistics1 = StatisticsEstepa(parameters_list[0],data1,self.config["estepa"])
            data1, data2 = statistics1.get_data_correlation(data1,data2)
            # widgets.lblHistogramCorrelation.setText("CORRELATION")
            # calculate Pearson's correlation
            corr, pvalue = pearsonr(data1, data2) # Pearson's r, valor p
            corr2, pvalue2 = spearmanr(data1, data2) # Spearman's rho, valor p
            corr3, pvalue3 = kendalltau(data1, data2) # Kendall's tau, valor p
            print('Pearsons correlation: %.3f , %.3f' % (corr,pvalue))
            print('spearmanr correlation: %.3f , %.3f' % (corr2, pvalue2))
            print('kendalltau correlation: %.3f , %.3f' % (corr3, pvalue3))
            #kf_data = np.array([data1, data2])
            #kf_data = np.array([[data1[0], data2[0]],[data1[1], data2[1]],[data1[2], data2[2]],[data1[3], data2[3]]])
            #kf = chi2_contingency(kf_data)
            #print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s'%kf)
            # ACTIVATE DARK MODE
            mpl_style(dark=True)
            self.print_correlation(data1, data2,parameters_list[0],parameters_list[1])

    def print_correlation(self,data1,data2,param1_name,param2_name):
        # Delete all widgets in layout
        layout = widgets.verticalLayout_histogram
        layout_buttons = widgets.horizontalLayout_buttons
        for i in reversed(range(widgets.verticalLayout_histogram.count())):
            widgets.verticalLayout_histogram.itemAt(i).widget().deleteLater()
        for i in reversed(range(widgets.horizontalLayout_buttons.count())):
            widgets.horizontalLayout_buttons.itemAt(i).widget().deleteLater()
        # delete dataValues
        widgets.btnClear_DataValues.clicked.emit()
        # delete Parameters Result
        widgets.btnClear_ParametersResult.clicked.emit()
        # delete wafermap
        for i in reversed(range(widgets.horizontalLayout_wafermap.count())):
            widgets.horizontalLayout_wafermap.itemAt(i).widget().deleteLater()

        # create a FigureCanvas & add to layout
        static_canvas = FigureCanvas(Figure())

        static_canvas_buttons = FigureCanvas(Figure())
        static_canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        static_canvas.updateGeometry()

        toolbar = NavigationToolbar(static_canvas, self)
        
        layout_buttons.addWidget(toolbar)
        layout.addWidget(static_canvas)
        _static_ax = static_canvas.figure.subplots()
        _static_ax.grid(True, color='gray')
        #_static_ax.set_xlabel(param1_name)
        #_static_ax.set_ylabel(param2_name)
        _static_ax.scatter(data1, data2)

        # linear regression
        m, b = np.polyfit(data1, data2, 1)
        data22 = [float(x)*m +b  for x in data1]
        _static_ax.plot(data1, data22, 'k', color='green')

        _static_ax.set_title(param1_name + " vs " + param2_name)

    #DATA FILE
    def open_file_dat(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        fileName, _ = QFileDialog.getOpenFileName(self,
            "Open .dat file", "C:", "Dat Files (*.dat);; All files (*.*)")

        if fileName:
            file_result = ResultFile(fileName)
            if not file_result.error:
                if btnName == "btnOpenDataFileInbase":
                    widgets.txtDataFileInbase.setText(fileName)
                    widgets.txtRunUpload.setText(file_result.lot)
                    widgets.txtWaferUpload.setText(file_result.wafer)
                if btnName == "btnOpenDataFile":
                    widgets.txtDataFile.setText(fileName)
                
                print(file_result.info())
            else:
                # show error
                retval = messageBox(self,"Error loading DAT File",file_result.error_message,"error")
                if btnName == "btnOpenDataFileInbase":
                    widgets.txtDataFileInbase.setText("")
                if btnName == "btnOpenDataFile":
                    widgets.txtDataFile.setText("")
                
    #WAFERMAP FILE    
    def open_file_ppg(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        fileName, _ = QFileDialog.getOpenFileName(self,
            "Open wafermap file", "C:", "PPG Files (*.ppg);; PPG py Files (*_wafermap.py);; All files (*.*)")

        if fileName:
            file_wafermap = WafermapFile(fileName)
            if not file_wafermap.error:
                if btnName == "btnOpenWafermapFileInbase":
                    widgets.txtWafermapFileInbase.setText(fileName)
                if btnName == "btnOpenWafermapFile":
                    widgets.txtWafermapFile.setText(fileName)
                
                print(file_wafermap.info())
            else:
                # show error
                retval = messageBox(self,"Error loading PPG File",file_wafermap.error_message,"error")
                if btnName == "btnOpenDataFileInbase":
                    widgets.txtDataFileInbase.setText("")
                if btnName == "btnOpenDataFile":
                    widgets.txtDataFile.setText("")

    def generate_graph_correlation(self,data):
        mpl_style(dark=True)
        layout = widgets.verticalLayout_histogram
        for i in reversed(range(widgets.verticalLayout_histogram.count())):
            widgets.verticalLayout_histogram.itemAt(i).widget().deleteLater()

        # create a FigureCanvas & add to layout
        static_canvas = FigureCanvas(Figure())
        layout.addWidget(NavigationToolbar(static_canvas, self))
        layout.addWidget(static_canvas)
        _static_ax = static_canvas.figure.subplots()

        parameters_file = widgets.cmbParametersFile.currentText()   # get text of combo Parameters
        parameters_file_list = parameters_file.split(", ")          # split to create list
        parameters = result_file.get_params(parameters_file_list)
        parameter1 = parameters[parameters_file_list[0]]
        parameter2 = parameters[parameters_file_list[1]]
        cai = p.Series(parameter1["medida"])
        pa = parameter2["medida"]

        mu, std = norm.fit(data)
        # Plot the histogram.
        num_chunks = int(widgets.txtHistogramChunks.text())
        _static_ax.corr(pa, np.poly1d(np.polyfit(pa, cai, 1))(pa), color='c', density=True, alpha=0.6)
        # Plot the PDF.
        xmin, xmax = min(data),max(data)
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)

        _static_ax.plot(x, mu, std, 'w', linewidth=1)
        # Put title in histogram
        title = widgets.cmbParametersFile.currentText()
        _static_ax.set_title(title)
        
        _static_ax.plot(x, p, 'w', linewidth=1)
        # Put title in histogram
        title = widgets.cmbParametersFile.currentText()
        _static_ax.set_title(title)
        # 
        # # temp data
        # mpl_style(dark=True)
        # # temp data

        # parameters_file = widgets.cmbParametersFile.currentText()   # get text of combo Parameters
        # parameters_file_list = parameters_file.split(", ")          # split to create list
        # parameters = result_file.get_params(parameters_file_list)
        # parameter1 = parameters[parameters_file_list[0]]
        # parameter2 = parameters[parameters_file_list[1]]

        # cai = parameter1["medida"]
        # pa = parameter2["medida"]
        # plt.scatter(pa, cai, s=2)
        # plt.plot(pa, np.poly1d(np.polyfit(pa, cai, 1))(pa), color='red')
        # plt.text(9, 0.25, f'Spearman R = {round(p.Series(pa).corr(cai, method="spearman"), 3)}')
        # plt.show()
        pass
        # # mpl_style(dark=True)
        # # # get data
        # # mu, std = norm.fit(data)
        # # # Delete all widgets in layout
        # # layout = widgets.verticalLayout_histogram
        # # for i in reversed(range(widgets.verticalLayout_histogram.count())):
        # #     widgets.verticalLayout_histogram.itemAt(i).widget().deleteLater()
        # # # create a FigureCanvas & add to layout
        
    def generate_histogram(self,data):
        par=list(self.textoParametros.keys())[self.parametroMostrando]
        data=self.measurements[par]["medida"]
        mpl_style(dark=True)
        # get data
        mu, std = norm.fit(data)
        # Delete all widgets in layout
        layout = widgets.verticalLayout_histogram
        for i in reversed(range(widgets.verticalLayout_histogram.count())):
            widgets.verticalLayout_histogram.itemAt(i).widget().deleteLater()
        # create a FigureCanvas & add to layout
        static_canvas = FigureCanvas(Figure())
        layout.addWidget(NavigationToolbar(static_canvas, self))
        layout.addWidget(static_canvas)
        _static_ax = static_canvas.figure.subplots()
        
        # Plot the histogram.
        num_chunks = int(widgets.txtHistogramChunks.text())
        _static_ax.hist(data, bins=num_chunks, density=True, alpha=0.6, color='c')
        # Plot the PDF.
        xmin, xmax = min(data),max(data)
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
          
        _static_ax.plot(x, p, 'w', linewidth=1)
        # Put title in histogram
        title = widgets.txtCurrentParameter.currentText()
        _static_ax.set_title(title)
        # layout = widgets.verticalLayout_histogram
        # for i in reversed(range(widgets.verticalLayout_histogram.count())):
        #     widgets.verticalLayout_histogram.itemAt(i).widget().deleteLater()

        # # create a FigureCanvas & add to layout
        # static_canvas = FigureCanvas(Figure())
        # layout.addWidget(NavigationToolbar(static_canvas, self))
        # layout.addWidget(static_canvas)
        # _static_ax = static_canvas.figure.subplots()

        # parameters_file = widgets.cmbParametersFile.currentText()   # get text of combo Parameters
        # parameters_file_list = parameters_file.split(", ")          # split to create list
        # parameters = result_file.get_params(parameters_file_list)
        # parameter1 = parameters[parameters_file_list[0]]
        # parameter2 = parameters[parameters_file_list[1]]
        # cai = p.Series(parameter1["medida"])
        # pa = parameter2["medida"]

        # mu, std = norm.fit(data)
        # # Plot the histogram.
        # num_chunks = int(widgets.txtHistogramChunks.text())
        # _static_ax.corr(pa, np.poly1d(np.polyfit(pa, cai, 1))(pa), color='c', density=True, alpha=0.6)
        # # Plot the PDF.
        # xmin, xmax = min(data),max(data)
        # x = np.linspace(xmin, xmax, 100)
        # p = norm.pdf(x, mu, std)

        # _static_ax.plot(x, mu, std, 'w', linewidth=1)
        # # Put title in histogram
        # title = widgets.cmbParametersFile.currentText()
        # _static_ax.set_title(title)
        
        # _static_ax.plot(x, p, 'w', linewidth=1)
        # # Put title in histogram
        # title = widgets.cmbParametersFile.currentText()         #ERROR
        # _static_ax.set_title(title)
    
    def generate_wafermap(self):
        pass

    # ----------------
    # BBDD FUNCTIONS
    # ----------------

    #SAVE IMPORT REPORT
    def save_import_report(self):
        global widgets
        texto = widgets.txtImportReport.toPlainText()
        destFile = os.getcwd() + "/" + import_report_file
        with open(destFile, 'w') as f:
            f.write(texto)

    #UPDATE IMPORT REPORT
    def updateTextImportReport(self,texto,color="NORMAL"):
        global widgets
        date_today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        colors = {"NORMAL": "#FFFFFF", "ERROR": "#FF3300","WARNING" : "orange"}
        if not color in colors:
            color = "NORMAL"
        texto_final =  '<span style="color: #ff79c6">' + "[" + date_today + "]</span>" + "<br />" + '<span style="color: ' + colors[color] + '">' + texto + "</span>"

        widgets.txtImportReport.appendHtml(texto_final)
        QApplication.processEvents()
    
    #UPDATE IMPORT REPORT
    def UploadFiles(self):
        try:
            CheckParameteres = True
            txtDataFileInbase = widgets.txtDataFileInbase.text()        #captura de fitxers
            txtWafermapFileInbase = widgets.txtWafermapFileInbase.text()
            # first check all parameters
            if txtDataFileInbase=="" or not os.path.exists(txtDataFileInbase):  #check si els fitxers estan buits i si existeixen
                CheckParameteres = False
                self.updateTextImportReport("- File DATA doesn't selected or path not exists!", "WARNING")

            if txtWafermapFileInbase=="" or not os.path.exists(txtWafermapFileInbase):
                CheckParameteres = False
                self.updateTextImportReport("- File WAFERMAP doesn't selected or path not exists!", "WARNING")


            if CheckParameteres:
                # first load files (data file & wafermap)
                

                while True: 
                    # check other parameters
                    txtRunUpload = widgets.txtRunUpload.text().strip()      #captura dels valors al formulari
                    txtWaferUpload = widgets.txtWaferUpload.text().strip()
                    txtDateUpload = widgets.txtDateUpload.text().strip()
                    txtTechnologyUpload = widgets.txtTechnologyUpload.text().strip()
                    txtMaskUpload = widgets.txtMaskUpload.text().strip()
                    txtLocalizationUpload = widgets.txtLocalizationUpload.text().strip()
                    txtCommentUpload = widgets.txtCommentUpload.text().strip()
                    if txtTechnologyUpload=="":
                        self.updateTextImportReport("- Technology not selected!", "WARNING")
                        CheckParameteres = False
                        break
                    if txtMaskUpload=="":
                        self.updateTextImportReport("- Mask not selected!", "WARNING")
                        CheckParameteres = False
                        break
                    
                    if txtRunUpload=="":
                        self.updateTextImportReport("- Run not selected!", "WARNING")
                        CheckParameteres = False
                        break  

                    if txtWaferUpload=="":
                        self.updateTextImportReport("- Wafer not selected!", "WARNING")
                        CheckParameteres = False
                        break    

                    if txtDateUpload=="":
                        self.updateTextImportReport("- Date not selected!", "WARNING")
                        CheckParameteres = False
                        break                    
                    else:
                        # check date format
                        formato = "%Y-%m-%d"
                        if not datetime.strptime(txtDateUpload,formato):
                            self.updateTextImportReport("- Date format not correct!", "WARNING")
                            CheckParameteres = False
                            break  
                    break

            if CheckParameteres:
                # import data
                dataFile = ResultFile(txtDataFileInbase)        #crea dos objectes data i wafer
                wafermapFile = WafermapFile(txtWafermapFileInbase)
                if len(dataFile.dies) == int(wafermapFile.wafer_parameters["nchips"]):
                    if dataFile.error:
                        retval = messageBox(self,"Error loading DAT File",dataFile.error_message,"error")
                    elif wafermapFile.error:
                        retval = messageBox(self,"Error loading PPG File",wafermapFile.error_message,"error")
                    else:
                        
                        self.updateTextImportReport("START import process")
                        # get parameters
                        inbase_parameters = {               #diccionari amb totes les dades
                            "dataFile" : txtDataFileInbase,
                            "wafermapFile" : txtWafermapFileInbase,
                            "run" : txtRunUpload,
                            "wafer" : txtRunUpload + "-" + txtWaferUpload,  #run i num. d'oblea
                            "date" : txtDateUpload,
                            "technology" : txtTechnologyUpload,
                            "mask" : txtMaskUpload,
                            "localization" : txtLocalizationUpload,
                            "comment" : txtCommentUpload
                        }
                        # put all info in estepa database
                        putAllInfo = False
                        virtual_wafer = inbase_parameters["wafer"]      #oblea diferent a la normal
                        # first search for measurement of this wafer in database
                        if self.estepa.exists_measurements(inbase_parameters["wafer"]):
                            retval = messageBox(self,"Measurements for this wafer exists","Do you want to CREATE new virtual wafer for run " + txtRunUpload + " and wafer " + txtWaferUpload + " ?","question")
                            if retval == QMessageBox.Yes:
                                virtual_wafer = self.estepa.get_virtual_wafer(inbase_parameters["wafer"])
                                print("Virtual wafer: "+ virtual_wafer)
                                putAllInfo = True
                        else:
                            retval = messageBox(self,"Measurements for this wafer not exists","The process INSERTS the results for run " + txtRunUpload + " and wafer " + txtWaferUpload + " automatically!","question")
                            if retval == QMessageBox.Yes:
                                putAllInfo = True
                        
                        # put the virtual wafer into inbase parameters
                        inbase_parameters["virtual_wafer"] = virtual_wafer

                        if putAllInfo:

                            # then put measurements in database
                            self.updateTextImportReport("UPLOADING results, please wait...")
                            retVal = self.estepa.inbase(self,inbase_parameters)
                            self.updateTextImportReport("FINISH import process")
                            #upadte combos technology
                            self.load_cmbTechnology()
                            self.load_cmbMask()
                            if retVal[0]:
                                retval = messageBox(self,"Error uploading info to database",retVal[1],"error")  #retorna l'error que és
                            else:
                                retval = messageBox(self,"Success upload","Uploaded all information to database successfully!","info")
                                
                        else:
                            self.updateTextImportReport("Process aborted!")
                else:
                    self.updateTextImportReport("Error in selected files: Different number of chips!", "ERROR")
                    retval = messageBox(self,"Error in selected files","Different number of chips!","error")


            else:
                self.updateTextImportReport("Parameters error: Problems checking parameters", "WARNING")
                retval = messageBox(self,"Parameters error","Problems checking parameters","warning")

        except Exception as error:
            print(error)
            self.updateTextImportReport("Some error occurs!", "ERROR")

    # COPIAR ELS VALORS
    def copy_values(self):
        widgets.txtLoadedValues.selectAll()
        widgets.txtLoadedValues.copy()

    # COPIAR ELS RESULTATS
    def copy_results(self):
        widgets.txtParametersResult.selectAll()
        widgets.txtParametersResult.copy()

    #UPDATE TEXT TECHNOLOGY UPLOAD
    #Change text by selecting technology from combobox
    def updateTextTechnologyUpload(self):
        if widgets.cmbTechnologyUpload.currentIndex()>0:
            widgets.txtTechnologyUpload.setText(str(widgets.cmbTechnologyUpload.currentText()))

    #UPDATE TEXT MASK UPLOAD
    #Change text by selecting mask from combobox
    def updateTextMaskUpload(self):
        if widgets.cmbMaskUpload.currentIndex()>0:
            widgets.txtMaskUpload.setText(str(widgets.cmbMaskUpload.currentText()))

    #GET RANGOS
    #Change text by selecting mask from combobox
    def get_rangos(self):
        parametersBBDD_list = widgets.cmbParametersBBDD.currentText().split(",")
        if len(parametersBBDD_list)==1:
            if widgets.cmbParametersBBDD.currentText()!="All parameters" and widgets.cmbParametersBBDD.currentText()!="":
                # only one parameter selected, search rangos
                rangos = self.estepa.get_rangos(widgets.cmbTechnology.currentText(),widgets.cmbParametersBBDD.currentText())
                # if rangos is not empty assign to texts
                if len(rangos)==2:
                    widgets.txtLimitMin.setText(str(rangos[0]))
                    widgets.txtLimitMax.setText(str(rangos[1]))

    def historical_check(self):                                                                                                     #3/8
        historicalcheck = "false"   
        if widgets.historicalcheck.isChecked():
            historicalcheck = "true"
            widgets.optionsHistorical.setCurrentWidget(widgets.YesHistorical)
        else:
            widgets.optionsHistorical.setCurrentWidget(widgets.NoHistorical) 
        
    def save_config_estepa_file(self):
        # change in chk non automatic limits or cmb otuliers method => save estepa file
        chkNonAutomaticLimits = widgets.chkNonAutomaticLimits.isChecked()
        chkGetAutoLimits = widgets.chkGetAutoLimits.isChecked()
        if chkNonAutomaticLimits:
            widgets.optionsNonAutomatic.setCurrentWidget(widgets.config_nonAutomatic)
            # get rangos
            if chkGetAutoLimits:
                self.get_rangos()
        else:
            widgets.optionsNonAutomatic.setCurrentWidget(widgets.config_Automatic)

        cmbOutlinerMethod = widgets.cmbOutlinerMethod.currentText()
        txtLimitMax = int(widgets.txtLimitMax.text())
        txtLimitMin = int(widgets.txtLimitMin.text())
        txtHistogramChunks = int(widgets.txtHistogramChunks.text())
        try:
            if str(txtLimitMin)!="" and str(txtLimitMax)!="" and isinstance(int(txtLimitMin),int) and isinstance(int(txtLimitMax),int):
                self.config["estepa"]["method"] = cmbOutlinerMethod
                self.config["estepa"]["lna"] = chkNonAutomaticLimits
                self.config["estepa"]["autolimits"] = chkGetAutoLimits
                self.config["estepa"]["limmin"] = txtLimitMin
                self.config["estepa"]["limmax"] = txtLimitMax
                self.config["estepa"]["chunks"] = txtHistogramChunks
                toml_file = open(self.path_config_file,"w")
                toml.dump(self.config, toml_file)
                toml_file.close()
            else:
                # get from file
                widgets.txtLimitMin.setText(str(self.config["estepa"]["limmin"]))
                widgets.txtLimitMax.setText(str(self.config["estepa"]["limmax"]))
        except:
            pass

    def load_cmbMask(self):
        # load estepa combo technology
        widgets.cmbMaskUpload.clear()
        widgets.cmbMaskUpload.addItem("Select mask")
        widgets.cmbMaskUpload.addItems(self.estepa.get_masks())
        widgets.txtMaskUpload.setText("")

    def load_cmbTechnology(self):
        # load estepa combo technology
        widgets.cmbTechnology.clear()
        widgets.cmbTechnologyUpload.clear()
        widgets.cmbTechnology.addItem("Select technology")
        widgets.cmbTechnologyUpload.addItem("Select technology")
        lista_technologies = self.estepa.get_technologies()
        widgets.cmbTechnology.addItems(lista_technologies)
        widgets.cmbTechnologyUpload.addItems(lista_technologies)
        widgets.cmbParametersBBDD.clear()
        widgets.txtTechnologyUpload.setText("")

    #LOAD COMBOS
    def load_cmbRuns(self):
        widgets.cmbRuns.clear()
        widgets.cmbRuns.addItem("Select run")
        technology = widgets.cmbTechnology.currentText()
        if technology!="Select technology" and technology!="":
            widgets.cmbRuns.addItems([str(x) for x in self.estepa.get_runs(technology)])
        widgets.cmbParametersBBDD.clear()

    def load_cmbWafers(self):
        widgets.cmbWafers.clear()
        widgets.cmbWafers.addItem("Select wafer")
        run = widgets.cmbRuns.currentText()
        if run!="Select run" and run!="":
            widgets.cmbWafers.addItems([str(x) for x in self.estepa.get_wafers(run)])
        widgets.cmbParametersBBDD.clear()

    def load_cmbParametersBBDD(self):
        widgets.cmbParametersBBDD.clear()
        widgets.cmbParametersBBDD.addItem("Select parameters")
        wafer = widgets.cmbWafers.currentText()
        if wafer!="Select wafer" and wafer!="":
            widgets.cmbParametersBBDD.addItems([str(x) for x in self.estepa.get_parameters(wafer)])
        else:
            widgets.cmbParametersBBDD.clear()
    
    #LOAD COMBOS CONSULT
    def load_cmbRuns_consult(self):
        widgets.cmbRunsConsult.clear()
        widgets.cmbRunsConsult.addItem("Select run")
        technology = widgets.cmbTechnologyConsult.currentText()
        if technology!="Select technology" and technology!="":
            widgets.cmbRunsConsult.addItems([str(x) for x in self.estepa.get_runs(technology)])
        widgets.cmbParametersBBDDConsult.clear()

    def load_cmbWafers_consult(self):
        widgets.cmbWafersConsult.clear()
        widgets.cmbWafersConsult.addItem("Select wafer")
        run = widgets.cmbRunsConsult.currentText()
        if run!="Select run" and run!="":
            widgets.cmbWafersConsult.addItems([str(x) for x in self.estepa.get_wafers(run)])
        widgets.cmbParametersBBDDConsult.clear()

    def load_cmbParametersBBDD_consult(self):
        widgets.cmbParametersBBDDConsult.clear()
        widgets.cmbParametersBBDDConsult.addItem("Select parameters")
        wafer = widgets.cmbWafersConsult.currentText()
        if wafer!="Select wafer" and wafer!="":
            widgets.cmbParametersBBDDConsult.addItems([str(x) for x in self.estepa.get_parameters(wafer)])
        else:
            widgets.cmbParametersBBDDConsult.clear()    

    def consult_BBDD(self):
        parametersBBDD = widgets.cmbParametersBBDDConsult.currentText()
        parametersBBDD_list = parametersBBDD.split(', ')
        counter = widgets.cmbParametersBBDDConsult.count()
        if parametersBBDD!="" and parametersBBDD!="Select parameters":
            run = widgets.cmbRunsConsult.currentText()
            wafer = widgets.cmbWafersConsult.currentText()
            if parametersBBDD=="All parameters":
                parametersBBDD_list = [widgets.cmbParametersBBDDConsult.itemText(i) for i in range(1,widgets.cmbParametersBBDDConsult.count())]
            measurements = self.estepa.get_medidas(wafer,parametersBBDD_list)
            print(measurements)

    #UPDATE PARAMETERS IN BBDD
    def update_cmbParametersBBDD(self):
        cmbParametersBBDD = widgets.cmbParametersBBDD.currentText()
        cmbParametersBBDD_list = cmbParametersBBDD.split(",")

    def viewOptionsEstepa(self):
        
        if widgets.optLoadFiles.isChecked():
            widgets.optionsESTEPA.setCurrentIndex(0)
        if widgets.optLoadBBDD.isChecked():
            widgets.optionsESTEPA.setCurrentIndex(1)

    def analyze_BBDD(self):
        parametersBBDD = widgets.cmbParametersBBDD.currentText()
        parametersBBDD_list = parametersBBDD.split(', ')
        counter = widgets.cmbParametersBBDD.count()
        if parametersBBDD!="" and parametersBBDD!="Select parameters":
            run = widgets.cmbRuns.currentText()
            wafer = widgets.cmbWafers.currentText()
            if parametersBBDD=="All parameters":
                parametersBBDD_list = [widgets.cmbParametersBBDD.itemText(i) for i in range(1,widgets.cmbParametersBBDD.count())]
            measurements = self.estepa.get_medidas(wafer,parametersBBDD_list)
            print(measurements)
            
            for par in parametersBBDD_list:
                estadistica = StatisticsEstepa(par,measurements[par]["medida"],self.config["estepa"])
                widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+estadistica.print_statistics())
        else:
            widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+"No parameters selected!")

    #CAMBIAR DE TEMA A CLARO                                                                                                                    #NUEVO 18/8
    def change_theme(self):
        self.modo_histograma= not self.modo_histograma
        self.analyze_files()

    # end ESTEPA functions
    # --------------------

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()     #obte info del botó al fer click
        btnName = btn.objectName()  #obté el nom de la var
    

        # PAGINA PRINCIPAL
        if btnName == "btn_page_home":
            widgets.stackedWidget.setCurrentWidget(widgets.Home_Window)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))


        # SHOW HOME ESTEPA
        if btnName == "btn_page_estepa":
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.estepa)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "home_analysis":
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.estepa)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_page_consult":
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.consult_estepa)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "home_consult":
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.consult_estepa)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_page_inbase":
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.inbase)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "home_upload":
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.inbase)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btnClear_DataValues":
            widgets.txtLoadedValues.setPlainText("")

        if btnName == "btnClear_ParametersResult":
            widgets.txtParametersResult.setPlainText("")

    # COPIAR VALORES
    def copy_values(self):
        widgets.txtLoadedValues.selectAll()
        widgets.txtLoadedValues.copy()

    # COPIAR RESULTADOS
    def copy_results(self):
        widgets.txtParametersResult.selectAll()
        widgets.txtParametersResult.copy()
    
    # GUARDAR VALORES
    def save_values(self):
        with open ("values.txt", "w") as file:                      #Formato RUN-WAFER_PARAMETER_values
            content = str(widgets.txtLoadedValues.toPlainText())
            file.write(content)
            file.close()

    # GUARDAR RESULTADOS
    def save_results(self):
        with open ("results.txt", "w") as file:                      #Formato RUN-WAFER_PARAMETER_results
            content = str(widgets.txtParametersResult.toPlainText())
            file.write(content)
            file.close()
                                                                    
        #Formato RUN-WAFER_PARAMETER_histogram      Modificar botón guardar imagen
        #Formato RUN-WAFER_PARAMETER_wafermap

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()                                         ###
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos

        # PRINT MOUSE EVENTS
        # if event.buttons() == Qt.LeftButton:
        #     print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.RightButton:
        #     print('Mouse click: RIGHT CLICK')

    # LOAD TOML FILES FUNCTIONS
    # CONFIG FILE FUNCTIONS
    def load_config(self):
        config_string = """
        title = "PROGRAM config file"
        [connection]
        host = "opter6.cnm.es"
        port = "5432"
        user = "joaquin"
        database = "mecao"
        password = ""
        autocommit = false

        [estepa]
        method = "k-sigma"
        lna = false
        autolimits = false
        limmin = 600
        limmax = 1000
        chunks = 16
        """

        
        
        if os.path.exists(self.path_config_file):
            self.load_config_file()
            
        else:
            # create file toml
            print("Toml doesn't exists: " + self.path_config_file + "!")
            toml_file = open(self.path_config_file,"w")
            toml_file.write(config_string)
            toml_file.close()
            self.load_config_file()

    def load_config_file(self):
        with open(self.path_config_file, mode="r") as fp:
            config = toml.load(fp)
            self.config = config

def messageBox(self,title,message,type):
    if type=="information" or type=="info":
        retval = QMessageBox.information(
            self,
            title,
            message,
            buttons=QMessageBox.Ok ,
            defaultButton=QMessageBox.Ok,
        )
    if type=="warning":
        retval = QMessageBox.warning(
            self,
            title,
            message,
            buttons=QMessageBox.Ok ,
            defaultButton=QMessageBox.Ok,
        )
    if type=="error" or type=="critical":
        retval = QMessageBox.critical(
            self,
            title,
            message,
            buttons=QMessageBox.Ok ,
            defaultButton=QMessageBox.Ok,
        )
    if type=="question":
        retval = QMessageBox.question(
            self,
            title,
            message,
            buttons=QMessageBox.Yes | QMessageBox.No ,
            defaultButton=QMessageBox.Yes,
        )
    return retval
    
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
              
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
