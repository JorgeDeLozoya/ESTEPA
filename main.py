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

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        #widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        #PRINT CONSOLA
        # widgets.HomeWindow.clicked.connect(self.print_home)
        # widgets.AnalyzeWindow.clicked.connect(self.print_analysis)
        # widgets.ConsultWindow.clicked.connect(self.print_consult)
        # widgets.btn_exit.clicked.connect(self.print_about)
        # widgets.VisualizeGraphsButton.clicked.connect(self.print_results)
        widgets.btnAnalyzeFiles.clicked.connect(self.print_analyze)
        # widgets.btnCorrelationFiles.clicked.connect(self.print_results)

        widgets.btnOpenDataFile.clicked.connect(self.open_file_dat)
        widgets.btnOpenWafermapFile.clicked.connect(self.open_file_ppg)
        widgets.DirectoryButton.clicked.connect(self.directory)

        widgets.optLoadBBDD.clicked.connect(self.buttonClick)
        widgets.optLoadFiles.clicked.connect(self.buttonClick)
        #widgets.OutlinerBox.currentIndexChanged.connect(self.print_outlinerbox)
        widgets.btnLoadFiles.clicked.connect(self.buttonClick)                           #Carregar les dades
        widgets.btnAnalyzeFiles.clicked.connect(self.buttonClick)                             #Botó analitzar
        #widgets.VisualizeGraphsButton.clicked.connect(self.buttonClick)                    #Resultats grafiques
        widgets.CleanResultsButton.clicked.connect(self.buttonClick)                        #Netejar els resultats

        #PAGE ESTEPA
        widgets.optLoadFiles.clicked.connect(self.viewOptionsEstepa)
        widgets.optLoadBBDD.clicked.connect(self.viewOptionsEstepa)
        widgets.cmbParametersFile.addItems(["cmax(pF)","cmin(pF)","dox(A)","Na(cm-3)","Vfb(V)","Nss(cm-2)","Rs(ohms)"])
        widgets.btnAnalyzeFiles.clicked.connect(self.analyzeFiles)

        # cmbVariables = VariablesComboBox()     
        # cmbVariables.setObjectName(u"cmbVariables")
        # cmbVariables.setGeometry(QRect(0, 200, 191, 22))

        # txtOutlinerMethod = QLabel("Outliner Removal Method")
        # DisplayText = QLabel("")

        #widgets.horizontalLayoutVariables.addWidget(cmbVariables)
        #widgets.horizontalLayoutVariables.addWidget(txtOutlinerMethod)

        #LEFT MENUS
        widgets.HomeWindow.clicked.connect(self.buttonClick)
        #widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.AnalyzeButton.clicked.connect(self.buttonClick)
        widgets.ConsultWindow.clicked.connect(self.buttonClick)

        
        

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
        widgets.HomeWindow.setStyleSheet(UIFunctions.selectMenu(widgets.HomeWindow.styleSheet()))
        



    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()     #obte info del botó al fer click
        btnName = btn.objectName()  #obté el nom de la var

        # PAGINA PRINCIPAL
        if btnName == "HomeWindow":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # FINESTRA ANÁLISI
        if btnName == "AnalyzeButton":
            widgets.stackedWidget.setCurrentWidget(widgets.analyze) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # SUBFINESTRA FILES
        if btnName == "optLoadFiles":
            widgets.stackedWidget.setCurrentWidget(widgets.files)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SUBFINESTRA BBDD
        if btnName == "optLoadBBDD":
            widgets.stackedWidget.setCurrentWidget(widgets.bbdd)
            UIFunctions.resetStyle(self, btnName) 
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # # NETEJAR ELS RESULTATS
        if btnName == "CleanResultsButton":                                   ##5/7            
            def delete(self):                                                           #COMPLETAR                                           
                self.txtParametersResult.clear()

        # BOTÓ PER CARREGAR LES DADES .DAT I .PPG           
        #if btnName == "LoadFilesButton":
            #DirectoryDat = 
            #DirectoryPpg = 
            #label.setText("Directory '% s' created" % DirectoryDat)
            #label.setText("Directory '% s' created" % DirectoryPpg)

       


        #BOTÓ CORRELATION
        if btnName == "btnCorrelationFiles":
            #self.btnAnalyzeFiles.connect(self.getItems)
            #if per comprovar que s'han agafat dos opcions
            #if si no s'han agafat dos variables
            #else si no s'ha agat cap variable

        # BOTÓ ANALITZAR
            if btnName == "btnAnalyzeFiles":
                
                file_dat = ResultFile("test.dat", "metrics")
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
                        if param == "cmax(pF)":
                            config_estepa_file2 = {
                                "method": "k-sigma",  # none, f-spread or k-sigma
                                "lna": False,
                                "limmin": 580.0,
                                "limmax": 600.0
                            }
                            sEstepa2 = StatisticsEstepa(param, file_dat2.param_to_list(param), config_estepa_file2)
                        else:
                            sEstepa2 = StatisticsEstepa(param, file_dat2.param_to_list(param), config_estepa_file)
                        # print(param + " : " + str(sEstepa2.data_list))
                        print(param)
                        print(" - Mean:   \t" + str(sEstepa2.mean))
                        print(" - Median: \t" + str(sEstepa2.median))
                        print(" - Stdev:  \t" + str(sEstepa2.stdev))
                        print(" - Points:  \t" + str(sEstepa2.points_end) + "/" + str(sEstepa2.points_ini))
                        print("")

    config_estepa_file = {
        "method" : "k-sigma",
        "lna" : False,
        "limmin" : 600,
        "limmax" : 1000
     }

    #BOTÓN PARA ANALIZAR
    def analyzeFiles(self):
        paramFiles = widgets.cmbParametersFile.currentText()
        paramFilesList = paramFiles.split(', ')
        counter = widgets.cmbParametersFile.count()
        if paramFiles != "" and paramFiles != "Select Parameters":
            run = widgets.cmbRuns.currentText()
            wafer = widgets.cmbWafers.currentText()
            if paramFiles == "All parameters":
                paramFilesList == [widgets.cmbParametersFile.itemText(i) for i in range.widgets.cmbParametersFile.count()]                  ##revisar
            measurements = self.estepa.get_medidas(wafer, paramFilesList)

            for parameter in paramFilesList:
                estadistica = StatisticsEstepa(parameter, measurements[parameter]["medida"], (self.cofig_estepa_file))
                widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\nª+estadistica.print_sta")

    #ORIGEN DE LES DADES
    def viewOptionsEstepa(self):                                                                                                

            if widgets.optLoadFiles.isChecked():
                widgets.optionsESTEPA.setCurrentIndex(0)
            if widgets.optLoadBBDD.isChecked():
                widgets.optionsESTEPA.setCurrentIndex(1)  
    
    #BOTÓ PER .DAT pushButton
    def open_file_dat(self):
        print("Open File")

        fileName, _ = QFileDialog.getOpenFileName(self,
            "Open .dat file", "C:", "Dat Files (*.dat);; All Files (*.*)")

        if fileName:
            widgets.txtDataFile.setText(fileName)
            result_file = ResultFile(fileName)
            if not result_file.error:
                print(result_file.info())
                widgets.cmbParametersFile.clear()     #Esborra els elements de la combobox
                parameters_list = result_file.params_list
                parameters_list.insert(0,"All parameters")
                print(str(result_file.params_list))
                print(str(parameters_list))
                widgets.cmbParametersFile.addItems(parameters_list)  #Afegeix tots els parametres del result_file
            else:
                print(result_file.error_message)            #Tornar un missatge d'error si no detecta parametres




    #BOTÓ PER .PPG 
    def open_file_ppg(self):
        print("Open File")
        fileName, _ = QFileDialog.getOpenFileName(self,         #,_ per retornar objecte amb molts atributs
            "Open .ppg file", "C:", "Ppg Files (*.ppg);; All Files (*.*)")
                
        if fileName:   
            widgets.txt_ppg.setText(fileName)   

 
        # method or slot for the toggled signal
            def on_selected(self):
                radio_button = self.sender()
        
                if radio_button.isChecked():
                    self.label.setText("You have selected : " + radio_button.text())



    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        #if event.buttons() == Qt.LeftButton:
        #    print('Mouse click: LEFT CLICK')
        #if event.buttons() == Qt.RightButton:
        #    print('Mouse click: RIGHT CLICK')

    #NUMBER VARIABLES
    # def NumberVariables (self):
    #     ParamList = ["cmax(pF)","cmin(pF)","dox(A)","Na(cm-3)","Vfb(V)","Nss(cm-2)","Rs(ohms)"]    
    #     number_of_params = len(ParamList)
             
        # if number_of_params == '1':                                                                               ####EDITAR
        #     btnAnalyzeFiles = True
        #     btnCorrelationFiles = False
        # if number_of_params == '2':
        #     btnCorrelationFiles = True
        #     btnAnalyzeFiles = False
        # else:
        #     btnCorrelationFiles = False
        #     btnAnalyzeFiles = False


  
    def directory(self):
        btn = self.sender()                 #obte info del botó al fer click
        btnName = btn.objectName()          #obté el nom de la var
        if btnName == "DirectoryButton":
            dialog = QFileDialog()
            folder_path = dialog.getExistingDirectory(None, "Select Folder")
            return folder_path


    #PRINT BUTTONS

    # def print_home(self):
    #     print("Home")

    # def print_analysis(self):
    #     print("Analyze")


    # def print_consult(self):
    #     print("Consult")


    # def print_about(self):
    #     print("About")

    # def print_results(self):
    #     print("Results")

    def print_analyze(self):      
        ParamList = ["cmax(pF)","cmin(pF)","dox(A)","Na(cm-3)","Vfb(V)","Nss(cm-2)","Rs(ohms)"]    
        number_of_params = len(ParamList)                                                                                              #####EDITAR

        if number_of_params == 1:
            print("You can analyze!")   

            if ParamList == ["cmax(pF)"]:
                widgets.txtLoadedValues.setText("cmax(pF)")
            if ParamList == ["cmin(pF)"]:
                widgets.txtLoadedValues.setText("cmin(pF)")
            if ParamList == ["dox(A)"]:
                widgets.txtLoadedValues.setText("dox(A)")
            if ParamList == ["Na(cm-3)"]:
                widgets.txtLoadedValues.setText("Na(cm-3)")
            if ParamList == ["Vfb(V)"]:
                widgets.txtLoadedValues.setText("Vfb(V)")
            if ParamList == ["Nss(cm-2)"]:
                widgets.txtLoadedValues.setText("Nss(cm-2)")
            if ParamList == ["Rs(ohms)"]:
                widgets.txtLoadedValues.setText("Rs(ohms)")

        if number_of_params != 1:
            print("You can't analyze, select one variable!")    #Missatge si no s'agafa cap variable 





#     #Correlació (2 var.)
#     #//////////////////////////////////////////////////////////////////  
#         #correlation()   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
