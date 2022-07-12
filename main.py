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

from distutils.log import error
import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
# general functions
from functions import *
# datetime
from datetime import datetime


from scipy.stats import norm
from io import open             #mòdul per obrir fitxers externs      

import matplotlib.pyplot as plt
import pyqtgraph as pg                           
import statistics               #Biblioteca que inclou les funcions estadistiques
import matplotlib
import numpy as np                     
import json                     #Opció 2

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
#app = QtWidget.QApplication(sys.argv) Per solucionar el error de QApplication

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
import_report_file = "report_import.txt"


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

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
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)


        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        
        # -----------
        # PAGE ESTEPA
        # -----------
        # config default if file doesn't exists
        config_estepa_file = {
            "method" : "k-sigma", # none, f-spread or k-sigma
            "lna" : False,
            "limmin" : 600,
            "limmax" : 1000
        }
        # if configuration json file exists load configurationñ from file
        get_json = get_json_file('statistics_estepa',config_estepa_file)
        self.config_estepa_file = config_estepa_file
        if get_json!="":
            self.config_estepa_file = get_json

        # LOAD FROM FILES
        widgets.btnLoadFiles.clicked.connect(self.load_from_files)
        widgets.btnAnalyzeFiles.clicked.connect(self.analyze_files)
        widgets.btnCorrelationFiles.clicked.connect(self.correlation_files)


        # LOAD FROM BBDD
        widgets.optLoadFiles.clicked.connect(self.viewOptionsEstepa)
        widgets.optLoadBBDD.clicked.connect(self.viewOptionsEstepa)
        widgets.cmbTechnology.currentIndexChanged.connect(self.load_cmbRuns)
        widgets.cmbRuns.currentIndexChanged.connect(self.load_cmbWafers)
        widgets.cmbWafers.currentIndexChanged.connect(self.load_cmbParametersBBDD)
        widgets.cmbParametersBBDD.editTextChanged.connect(self.update_cmbParametersBBDD)
        widgets.btnAnalyzeBBDD.clicked.connect(self.analyze_BBDD)

        # configuration estepa
        widgets.scrollHistogramChunks.valueChanged.connect(lambda: widgets.txtHistogramChunks.setText(str(widgets.scrollHistogramChunks.value())))
        # get values from file json & set widgets
        self.methods = ["none","f-spread","k-sigma"]
        widgets.cmbOutlinerMethod.setCurrentIndex(self.methods.index(self.config_estepa_file["method"]))
        #print(config_estepa_file)
        if self.config_estepa_file["lna"]:
            widgets.chkNonAutomaticLimits.setChecked(self.config_estepa_file["lna"])
            widgets.optionsNonAutomatic.setCurrentWidget(widgets.config_nonAutomatic)
        else:
            widgets.chkNonAutomaticLimits.setChecked(False)
            widgets.optionsNonAutomatic.setCurrentWidget(widgets.config_Automatic)

        widgets.txtLimitMin.setText(str(self.config_estepa_file["limmin"]))
        widgets.txtLimitMax.setText(str(self.config_estepa_file["limmax"]))

        widgets.cmbOutlinerMethod.currentIndexChanged.connect(self.save_config_estepa_file)
        widgets.chkNonAutomaticLimits.stateChanged.connect(self.save_config_estepa_file)
        widgets.txtLimitMin.textChanged.connect(self.save_config_estepa_file)
        widgets.txtLimitMax.textChanged.connect(self.save_config_estepa_file)

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
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_page_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_page_home.styleSheet()))
        

        # LOAD ESTEPA 
        config_estepa = {
            "host" : "opter6.cnm.es",
            "port" : "5432",
            "user" : "joaquin",
            "database" : "mecao",
            "password" : "",
            "autocommit" : False
        }
        # if configuration json file exists load configurationñ from file
        get_json = get_json_file('estepa',config_estepa)
        if get_json!="":
            config_estepa = get_json
        self.estepa = Estepa(config_estepa)
        if not self.estepa.error:
            self.load_cmbTechnology()
            self.load_cmbMask()
        else:
            retval = messageBox(self,"Error loading ESTEPA class",self.estepa.error_message,"error")
        widgets.cmbParametersFile.clear()
        widgets.cmbParametersBBDD.clear()

    # ----------------
    # ESTEPA FUNCTIONS
    # ----------------
    def load_from_files(self):
        file_dat = widgets.txtDataFile.text()
        file_ppg = widgets.txtWafermapFile.text()
        file_result = ResultFile(file_dat)
        file_wafermap = WafermapFile(file_ppg)
        parameters_list = file_result.params_list
        parameters_list.insert(0,"All parameters")
        widgets.cmbParametersFile.addItems(parameters_list)


    def analyze_files(self):
        parameters_file = widgets.cmbParametersFile.currentText()   # get text of combo Parameters
        parameters_file_list = parameters_file.split(", ")          # split to create list
        FileName = widgets.txtDataFile.text() 
        result_file = ResultFile(FileName)
        if not result_file.error:
            if parameters_file!="":
                # GET parameters result
                measurements = result_file.get_params(parameters_file_list)
                for parameter in parameters_file_list:
                    estadistica = StatisticsEstepa(parameter, measurements[parameter]["medida"], (self.config_estepa_file))
                    widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+estadistica.print_statistics())
                # GET DATA VALUES, HISTOGRAM & WAFERMAP IF PARAM==1
                if len(parameters_file_list) == 1:
                    # Get data values from result_file
                    data_values = result_file.get_data_values(parameters_file)
                    widgets.txtLoadedValues.setPlainText("")
                    # print data values in widget Plain text
                    for chip in data_values:
                        widgets.txtLoadedValues.setPlainText(widgets.txtLoadedValues.toPlainText()+"\n"+str(chip)+" "+str(data_values[chip]))
                    # Get histogram
                    

                    # Get wafermap



            else:
                retval = messageBox(self,"Error getting parameters list","Please, select at least one parameter!","warning")

        else:
            retval = messageBox(self,"Error getting Result File",self.result_file.error_message,"warning")

    def correlation_files(self):
        pass

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

    def save_import_report(self):
        global widgets
        texto = widgets.txtImportReport.toPlainText()
        destFile = os.getcwd() + "/" + import_report_file
        with open(destFile, 'w') as f:
            f.write(texto)

    def updateTextImportReport(self,texto,color="NORMAL"):
        global widgets
        date_today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        colors = {"NORMAL": "#FFFFFF", "ERROR": "#FF3300","WARNING" : "orange"}
        if not color in colors:
            color = "NORMAL"
        texto_final =  '<span style="color: #ff79c6">' + "[" + date_today + "]</span>" + "<br />" + '<span style="color: ' + colors[color] + '">' + texto + "</span>"

        widgets.txtImportReport.appendHtml(texto_final)
        QApplication.processEvents()

    def UploadFiles(self):
        try:
            CheckParameteres = True
            txtDataFileInbase = widgets.txtDataFileInbase.text()
            txtWafermapFileInbase = widgets.txtWafermapFileInbase.text()
            # first check all parameters
            if txtDataFileInbase=="" or not os.path.exists(txtDataFileInbase):
                CheckParameteres = False
                self.updateTextImportReport("- File DATA doesn't selected or path not exists!", "WARNING")

            if txtWafermapFileInbase=="" or not os.path.exists(txtWafermapFileInbase):
                CheckParameteres = False
                self.updateTextImportReport("- File WAFERMAP doesn't selected or path not exists!", "WARNING")


            if CheckParameteres:
                # first load files (data file & wafermap)
                

                while True:
                    # check other parameters
                    txtRunUpload = widgets.txtRunUpload.text().strip()
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
                dataFile = ResultFile(txtDataFileInbase)
                wafermapFile = WafermapFile(txtWafermapFileInbase)
                if len(dataFile.dies) == int(wafermapFile.wafer_parameters["nchips"]):
                    if dataFile.error:
                        retval = messageBox(self,"Error loading DAT File",dataFile.error_message,"error")
                    elif wafermapFile.error:
                        retval = messageBox(self,"Error loading PPG File",wafermapFile.error_message,"error")
                    else:
                        
                        self.updateTextImportReport("START import process")
                        # get parameters
                        inbase_parameters = {
                            "dataFile" : txtDataFileInbase,
                            "wafermapFile" : txtWafermapFileInbase,
                            "run" : txtRunUpload,
                            "wafer" : txtRunUpload + "-" + txtWaferUpload,
                            "date" : txtDateUpload,
                            "technology" : txtTechnologyUpload,
                            "mask" : txtMaskUpload,
                            "localization" : txtLocalizationUpload,
                            "comment" : txtCommentUpload
                        }
                        # put all info in estepa database
                        putAllInfo = False
                        virtual_wafer = inbase_parameters["wafer"]
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
                            if retVal[0]:
                                retval = messageBox(self,"Error uploading info to database",retVal[1],"error")
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

    def updateTextTechnologyUpload(self):
        if widgets.cmbTechnologyUpload.currentIndex()>0:
            widgets.txtTechnologyUpload.setText(str(widgets.cmbTechnologyUpload.currentText()))

    def updateTextMaskUpload(self):
        if widgets.cmbMaskUpload.currentIndex()>0:
            widgets.txtMaskUpload.setText(str(widgets.cmbMaskUpload.currentText()))

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

    def save_config_estepa_file(self):
        # change in chk non automatic limits or cmb otuliers method => save estepa file
        chkNonAutomaticLimits = "false"
        if widgets.chkNonAutomaticLimits.isChecked():
            chkNonAutomaticLimits = "true"
            widgets.optionsNonAutomatic.setCurrentWidget(widgets.config_nonAutomatic)
            # get rangos
            self.get_rangos()
        else:
            widgets.optionsNonAutomatic.setCurrentWidget(widgets.config_Automatic)
            
        cmbOutlinerMethod = widgets.cmbOutlinerMethod.currentText()
        txtLimitMax = widgets.txtLimitMax.text()
        txtLimitMin = widgets.txtLimitMin.text()
        try:
            if str(txtLimitMin)!="" and str(txtLimitMax)!="" and isinstance(int(txtLimitMin),int) and isinstance(int(txtLimitMax),int):
                path_file = os.getcwd() + "\\modules\\statistics_estepa.json"
                # save file
                texto = '{\n\
                    \t"method" : "'+ cmbOutlinerMethod +'", \n\
                    \t"lna" : ' + chkNonAutomaticLimits + ', \n\
                    \t"limmin" : ' + txtLimitMin + ', \n\
                    \t"limmax" : ' + txtLimitMax + ' \n\
                    }\n'
                with open(path_file, 'w') as f:
                    f.write(texto)

                self.config_estepa_file = json.loads(texto)
            else:
                # get from file
                widgets.txtLimitMin.setText(str(self.config_estepa_file["limmin"]))
                widgets.txtLimitMax.setText(str(self.config_estepa_file["limmax"]))
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

    def update_cmbParametersBBDD(self):
        cmbParametersBBDD = widgets.cmbParametersBBDD.currentText()
        cmbParametersBBDD_list = cmbParametersBBDD.split(",")
        # if "All parameters" in cmbParametersBBDD_list:
        #     if len(cmbParametersBBDD_list)>1:
        #         # clear combo & load again all the parameters
        #         widgets.cmbParametersBBDD.clear()
        #         self.load_cmbParametersBBDD()
        #         # then the user can select one-two parameter or all parameters

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
            
            for parameter in parametersBBDD_list:
                estadistica = StatisticsEstepa(parameter,measurements[parameter]["medida"],self.config_estepa_file)
                widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+estadistica.print_statistics())
        else:
            widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+"No parameters selected!")



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
            widgets.stackedWidget.setCurrentWidget(widgets.home)
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

        if btnName == "btn_page_consult":
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


    # COPIAR ELS VALORS
    def copy_values(self):
        widgets.txtLoadedValues.selectAll()
        widgets.txtLoadedValues.copy()

    # COPIAR ELS RESULTATS
    def copy_results(self):
        widgets.txtParametersResult.selectAll()
        widgets.txtParametersResult.copy()

     

 


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        #self.dragPos = event.globalPos()
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

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
