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
        # widgets.CleanResultsButton.clicked.connect(self.clean_results)
        # widgets.CleanValuesButton.clicked.connect(self.clean_values)
        widgets.CopyResultsButton.clicked.connect(self.copy_results)
        widgets.CopyValuesButton.clicked.connect(self.copy_values)

        widgets.btnAnalyzeFiles.clicked.connect(self.print_analyze)
        # widgets.btnCorrelationFiles.clicked.connect(self.print_results)

        widgets.btnOpenDataFile.clicked.connect(self.open_file_dat)
        widgets.btnOpenWafermapFile.clicked.connect(self.open_file_ppg)
        widgets.DirectoryButton.clicked.connect(self.directory)

        widgets.optLoadBBDD.clicked.connect(self.buttonClick)
        widgets.optLoadFiles.clicked.connect(self.buttonClick)
        widgets.btnLoadFiles.clicked.connect(self.buttonClick)                              #Carregar les dades
        
        widgets.CopyValuesButton.clicked.connect(self.buttonClick)                                                          #11/7
        widgets.CleanResultsButton.clicked.connect(self.buttonClick)
        

        #PAGE ESTEPA
        widgets.optLoadFiles.clicked.connect(self.viewOptionsEstepa)
        widgets.optLoadBBDD.clicked.connect(self.viewOptionsEstepa)
        widgets.cmbParametersFile.addItems(["cmax(pF)","cmin(pF)","dox(A)","Na(cm-3)","Vfb(V)","Nss(cm-2)","Rs(ohms)"])
  

        #LEFT MENUS
        widgets.HomeWindow.clicked.connect(self.buttonClick)
        widgets.AnalyzeButton.clicked.connect(self.buttonClick)
        widgets.ConsultWindow.clicked.connect(self.buttonClick)

        #TOOGLE OPTIONS
        widgets.OutlierBox.addItems(["None","F-Spread","K-Sigmas"])       

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

        # CLEAN VALUES
        if btnName == "CleanValuesButton":                                                          #Només em funciona una opció, els dos alhora no
            widgets.txtLoadedValues.setPlainText("")

        #CLEAN RESULTS
        if btnName == "CleanResultsButton":
            widgets.txtParametersResult.setPlainText("")

    # COPIAR ELS VALORS
    def copy_values(self):
        widgets.txtLoadedValues.selectAll()
        widgets.txtLoadedValues.copy()

    # COPIAR ELS RESULTATS
    def copy_results(self):
        widgets.txtParametersResult.selectAll()
        widgets.txtParametersResult.copy()

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

    # DIRECTORY
    def directory(self):
        response = QFileDialog.getExistingDirectory(self, caption = 'Select a folder')                        #10/7
        print(response)     #print del actual directory
        return response
        # current_working_directory = os.getcwd()
        # print(current_working_directory)    

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
  
    def directory(self):
        btn = self.sender()                 #obte info del botó al fer click
        btnName = btn.objectName()          #obté el nom de la var
        if btnName == "DirectoryButton":
            dialog = QFileDialog()
            folder_path = dialog.getExistingDirectory(None, "Select Folder")
            print(folder_path)
            return folder_path

    def print_analyze(self):  
        config_estepa_file = {
            "method" : "k-sigma",
            "lna" : False,
            "limmin" : 600,
            "limmax" : 1000
            }
        parameters_file = widgets.cmbParametersFile.currentText()   #Captura el text dins dels parametres
        parameters_file_list = parameters_file.split(", ")  #per separar els parametres    
        number_of_params = len(parameters_file_list)    #per saber el nombre de parametres que hi han   
                                                                                           #####EDITAR

        print(str(parameters_file))
           

        if parameters_file == "":
            print("You can't analyze, select one variable!")    #Missatge si no s'agafa cap variable 

        else:
            FileName = widgets.txtDataFile.text() 
            result_file = ResultFile(FileName)
            measurements = result_file.get_params(parameters_file_list)

            for parameter in parameters_file_list:
                estadistica = StatisticsEstepa(parameter, measurements[parameter]["medida"], (config_estepa_file))
                widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+estadistica.print_statistics())

            if number_of_params == 1:
                data_values = result_file.get_values(parameters_file)
                widgets.txtLoadedValues.setPlainText("")
                for chip in data_values:
                    widgets.txtLoadedValues.setPlainText(widgets.txtLoadedValues.toPlainText()+"\n"+str(chip)+" "+str(data_values[chip]))        #Introduim el chip i el valor de la mesuara
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
