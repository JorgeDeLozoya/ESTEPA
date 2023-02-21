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

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from widgets import *
from functions import *
from modules import *

# GENERAL FUNCTIONS
# ///////////////////////////////////////////////////////////////
import sys, platform, os, toml, mplcursors, logging, json, matplotlib.pyplot as plt, numpy as np, pandas as pd, seaborn as sns, matplotlib as mpl
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)        #Si no és qt5agg no agafa el NavigationToolbar
from scipy.stats import norm, kendalltau, spearmanr, pearsonr, chi2_contingency
from matplotlib.backends.qt_compat import QtWidgets         #No reconeix
from matplotlib.figure import Figure
from matplotlib.colors import LinearSegmentedColormap
from io import StringIO, open
from datetime import datetime
from qbstyles import mpl_style
from statistics import stdev, mean, median


os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
#app = QtWidget.QApplication(sys.argv) Per solucionar el error de QApplication

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
import_report_file = "report_import.txt"

class NavigationToolbarMod(NavigationToolbar):
    # only display the buttons we need

    def __init__(self, figure_canvas, MainWindow, where):
        NavigationToolbar.__init__(self, figure_canvas, parent=None)
        self.where = where
        self.MainWindowClass = MainWindow

        self.setStyleSheet("color: white; background-color: #343B48;")

    NavigationToolbar.toolitems = (
        ('Home', 'Reset original view', 'home', 'home'),
        ('Back', 'Back to previous view', 'back', 'back'),
        ('Forward', 'Forward to next view', 'forward', 'forward'),
        (None, None, None, None),
        ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
        ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
        ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
        (None, None, None, None),
        (None, None, None, None),
        # ('Save', 'Save the figure', 'filesave', 'save_graph'), # save_figure modification
    )

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        # CONFIG
        self.left_box_open = False
        self.histogram_mode=True
        self.wafermap_mode=True
        self.measurements=None
        self.graph_mode=True    #True = Analisis 
                                #False = Correlación
        self.path_config_file = os.getcwd() + '/config/config.toml'

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)   
        global widgets  
        widgets = self.ui
        
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "ESTEPA"
        description = "ESTEPA"
        
        # SET MINIMUN WINDOW SIZE
        self.setMinimumSize(800, 600)
        
        # ///////////////////////////////////////////////////////////////
                
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # LOGGING
        logging.basicConfig(filename='register.log', encoding='utf-8', level=logging.INFO)
        
        # LOAD configuration TOML
        self.path_config_file = os.getcwd() + '/config/config.toml'
        self.load_config() 
        
        # -----------
        # PAGE ESTEPA
        # -----------
        
        # ANALYZE WINDOW
        widgets.btnOpenDataFile.clicked.connect(self.open_file_dat)
        widgets.btnOpenWafermapFile.clicked.connect(self.open_file_ppg)
        widgets.btnLoadFiles.clicked.connect(self.load_from_files)
        
        widgets.btnAnalyzeFiles.clicked.connect(self.analyze_files)
        widgets.btnCorrelationFiles.clicked.connect(self.correlation_files)
        widgets.btn_clear.clicked.connect(self.buttonClick)
        
        widgets.optLoadFiles.clicked.connect(self.viewOptionsEstepa)
        widgets.optLoadBBDD.clicked.connect(self.viewOptionsEstepa)
        
        widgets.cmbParametersFile.editTextChanged.connect(self.update_cmbParametersFile)
        widgets.cmbTechnology.currentIndexChanged.connect(self.load_cmbRuns)
        widgets.cmbRuns.currentIndexChanged.connect(self.load_cmbWafers)
        widgets.cmbWafers.currentIndexChanged.connect(self.load_cmbParametersBBDD)
        widgets.cmbParametersBBDD.editTextChanged.connect(self.update_cmbParametersBBDD)
        
        widgets.btnAnalyzeBBDD.clicked.connect(self.analyze_BBDD)
        widgets.btnCorrelationBBDD.clicked.connect(self.correlation_BBDD)
        
        widgets.cmbCurrentParameter.currentIndexChanged.connect(self.search_parameter)
        widgets.btnCopyDescription.clicked.connect(self.copy_results)
        widgets.btnCopyDescriptionConsult.clicked.connect(self.copy_consult)
        widgets.btnSaveDescription.clicked.connect(self.save_results)
        widgets.btnNextParamFiles.clicked.connect(self.next_parameter)
        widgets.btnPreviousParamFiles.clicked.connect(self.previous_parameter)
        widgets.btn_clear_all.clicked.connect(self.buttonClick)                             
        

        # PAGE CONSULT
        widgets.optionsHistorical.setCurrentWidget(widgets.NoHistorical)
        widgets.optValues.setChecked(True)
        widgets.historicalcheck.stateChanged.connect(self.optionsHistorical)
        widgets.cmbTechnologyConsult.currentIndexChanged.connect(self.load_cmbRunsConsult)
        widgets.cmbRunsConsult.currentIndexChanged.connect(self.load_cmbWafersConsult)
        widgets.cmbWafersConsult.editTextChanged.connect(self.load_cmbParametersConsult)
        widgets.cmbParametersConsult.editTextChanged.connect(self.load_controlsConsult)     #caixa parameters
        widgets.btn_add_wafers.clicked.connect(self.add_wafers_to_ListBox)
        widgets.lbWafers.itemDoubleClicked.connect(self.remove_item_ListBox)
        widgets.lbWafers.clear()
        widgets.btnConsult.clicked.connect(self.consult)
        widgets.btnClearlConsult.clicked.connect(self.clearDiagram)      #botó x
        widgets.btnClearlConsult.clicked.connect(self.buttonClick)
        # widgets.lblLoadingConsult.setVisible(False)     #animació carrega
        widgets.btnPreviousParamConsult.clicked.connect(self.nextParamConsult)      #prev
        widgets.btnNextParamConsult.clicked.connect(self.nextParamConsult)          #next
        self.load_controlsConsult()

        # CONFIG ESTEPA
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
        widgets.chk_theme.stateChanged.connect(self.change_theme)
        widgets.historicalcheck.stateChanged.connect(self.historical_check)
        
        #HOME WINDOW
        widgets.home_analysis.clicked.connect(self.buttonClick)
        widgets.home_consult.clicked.connect(self.buttonClick)
        widgets.home_upload.clicked.connect(self.buttonClick)
        widgets.home_reports.clicked.connect(self.buttonClick)  
        
        widgets.txt_results_directory_2.setText(str(self.config["directory"]["res_directory"]))
        widgets.txt_results_directory_2.textChanged.connect(self.save_config_estepa_file)
        widgets.txt_working_directory_2.setText(str(self.config["directory"]["work_directory"]))
        widgets.txt_working_directory_2.textChanged.connect(self.save_config_estepa_file)
        widgets.btn_results_directory_2.clicked.connect(self.set_results_directory)
        widgets.btn_working_directory_2.clicked.connect(self.set_working_directory)

        # PAGE INBASE
        widgets.cmbTechnologyUpload.currentIndexChanged.connect(self.updateTextTechnologyUpload)
        widgets.cmbMaskUpload.currentIndexChanged.connect(self.updateTextMaskUpload)
        widgets.txtDateUpload.setText(datetime.today().strftime('%Y-%m-%d'))
        widgets.btnUploadFiles.clicked.connect(self.UploadFiles)
        widgets.btnClearImportReport.clicked.connect(lambda: widgets.txtImportReport.setPlainText(""))
        widgets.btnSaveImportReport.clicked.connect(self.save_import_report)
        widgets.btnOpenDataFileInbase.clicked.connect(self.open_file_dat)
        widgets.btnOpenWafermapFileInbase.clicked.connect(self.open_file_ppg)

        # CONFIG PAGES
        widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_measurements)
        widgets.optionsESTEPA.setCurrentIndex(0)

        # WIDGETS CONFIG
        widgets.stk_graph.setCurrentWidget(widgets.no_graph)
        widgets.stk_loadfiles.setCurrentWidget(widgets.not_loaded) 
        widgets.wgt_estepa.setCurrentWidget(widgets.pg_load)
        widgets.load_clear.setCurrentWidget(widgets.clear)
        widgets.optionsHistorical.setCurrentWidget(widgets.NoHistorical) 
        widgets.consultWidget.setCurrentWidget(widgets.ConsultData)

        #LEFT MENUS
        widgets.btn_page_home.clicked.connect(self.buttonClick)
        widgets.btn_page_estepa.clicked.connect(self.buttonClick)
        widgets.btn_page_consult.clicked.connect(self.buttonClick)
        widgets.btn_page_inbase.clicked.connect(self.buttonClick)
        widgets.btn_page_reports.clicked.connect(self.buttonClick)
              
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            if self.left_box_open:
                self.left_box_open = False
                UIFunctions.toggleLeftBox(self, False)
            else:
                self.left_box_open = True
                UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        
        # RIGHT MENU
        widgets.txt_results_directory.setText(str(self.config["directory"]["res_directory"]))                       
        widgets.txt_working_directory.setText(str(self.config["directory"]["work_directory"]))
        widgets.txt_results_directory.textChanged.connect(self.save_config_estepa_file)
        widgets.txt_working_directory.textChanged.connect(self.save_config_estepa_file)
        widgets.btn_results_directory.clicked.connect(self.set_results_directory)
        widgets.btn_working_directory.clicked.connect(self.set_working_directory)

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
        widgets.settings.setCurrentWidget(widgets.no)
        widgets.options.setCurrentWidget(widgets.not_able)
        widgets.btn_page_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_page_home.styleSheet()))
        
        # LOAD ESTEPA 
        config_estepa = {
            "host" : "opter6.cnm.es",
            "port" : "5432",
            "user" : "joaquin",
            "database" : "mecao",
            "password" : "",
            "autocommit" : False,
            # "res_directory"
            # "work_directory"
        }

        # config_estepa = {
        #     "host" : "localhost",
        #     "port" : "5432",
        #     "user" : "postgres",
        #     "database" : "mecao",
        #     "password" : "",
        #     "autocommit" : False,
        # }


        # if configuration json file exists load configurationñ from file
        get_json = get_json_file('estepa',config_estepa)
        if get_json!="":
            config_estepa = get_json
        self.estepa = Estepa(self.config["connection"])     
        # self.estepa = Estepa(self.config["estepa"])
        # self.estepa = Estepa(self.config["directory"])
        if not self.estepa.error:
            self.load_cmbTechnology()
            self.load_cmbMask()
        else:
            retval = messageBox(self,"Error loading ESTEPA class",self.estepa.error_message,"error")
        widgets.cmbParametersFile.clear()
        widgets.cmbParametersBBDD.clear()

    # ----------------
    # USER CONFIG FUNCTIONS
    # ----------------

    # ----------------
    # ESTEPA FUNCTIONS
    # ----------------
        
    #LOAD FROM FILES
    def load_from_files(self):
        '''
        Used to load both files from qlineedits (.dat and wafermap.py or .ppg)
        '''
        logging.info('Loading Started')
        if not widgets.txtDataFile.text() and widgets.txtWafermapFile.text():
            error = True
            retval = messageBox(self,"Error loading files","Select data and wafermap files before loading files","warning")   
            
        if widgets.txtDataFile.text() and widgets.txtWafermapFile.text():
            widgets.stk_loadfiles.setCurrentWidget(widgets.loaded)
            widgets.stk_graph.setCurrentWidget(widgets.no_graph)
            
            file_dat = widgets.txtDataFile.text()
            file_ppg = widgets.txtWafermapFile.text()
            file_result = ResultFile(file_dat)
            file_wafermap = WafermapFile(file_ppg)
            self.parameters_list = file_result.params_list
            self.parameters_list.insert(0,"All parameters")
            widgets.cmbParametersFile.addItems(self.parameters_list)
            
        else:
            error = True
            retval = messageBox(self,"Error loading files","Select data and wafermap files before loading files","warning")   
        logging.info('Loading Finished')

    #ANALYZE
    def analyze_files(self, parametroMostrando=0):
        logging.warning('Analyze debug')
        try: 
            self.graph_mode = True
            self.textoParametros={} 
            
            widgets.wgt_estepa.setCurrentWidget(widgets.pg_analyze)                          
            parameters_file = widgets.cmbParametersFile.currentText()   # get text of combo Parameters
            parameters_file_list = parameters_file.split(", ")          # split to create list
            
            FileName = widgets.txtDataFile.text() 
            result_file = ResultFile(FileName)

            if not result_file.error:
                if parameters_file!="":
                    #LOAD STACKED WIDGETS
                    widgets.stk_graph.setCurrentWidget(widgets.graph)                
                    widgets.txtLoadedValues.setPlainText("")
                    widgets.txtParametersResult.setPlainText("")
                    
                    # GET parameters result
                    measurements = result_file.get_params(parameters_file_list)
                    parameter = parameters_file_list[parametroMostrando]
                    widgets.cmbCurrentParameter.setCurrentText(parameter)
                    # Get data values from result_file
                    # for parameter in parameters_file_list:
                    estadistica = StatisticsEstepa(parameter, measurements[parameter]["medida"], (self.config["estepa"]))
                    widgets.txtParametersResult.setPlainText(estadistica.print_statistics())               
                    data_values = result_file.get_data_values(parameter)                 
                    
                    # widgets.txtLoadedValues.setPlainText("X"+"\t"+ "Y"+"\t"+ "Measurement"+ "\n" + "\n")

                    for chip in data_values:
                        widgets.txtLoadedValues.setPlainText(widgets.txtLoadedValues.toPlainText()+"\n"+"\t".join(str(chip).split(" "))+"\t"+str(data_values[chip]))
                    
                    # Get histogram
                    self.generate_histogram(measurements[parameter]["medida"], parameters_file_list, parametroMostrando)
                    # Get wafermap
                    self.generate_wafermap(data_values, parameter)   
                    
                else:
                    retval = messageBox(self,"Error getting parameters list","Please, select at least one parameter!","warning")
            else:
                retval = messageBox(self,"Error getting Result File",self.result_file.error_message,"warning")
                
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)    
            
    # CORRELATION
    def correlation_files(self, parametroMostrando=0):
        self.graph_mode=False
        textoParametros={}
        error = False
        widgets.wgt_estepa.setCurrentWidget(widgets.pg_analyze)
        widgets.stk_graph.setCurrentWidget(widgets.no_graph)
        widgets.txtLoadedValues.setPlainText("")
        widgets.txtParametersResult.setPlainText("")
     
        if widgets.optLoadFiles.isChecked():
            txt_param_selected = widgets.cmbParametersFile.currentText().split(', ')[0]
            parameters = widgets.cmbParametersFile.currentText()
            parameters_list = parameters.split(", ")
            parameters_file = widgets.cmbParametersFile.currentText()
            parameters_file_list = parameters_file.split(", ")

            
            FileName = widgets.txtDataFile.text()
            result_file = ResultFile(FileName)
            if not result_file.error:
                if len(parameters_list)==2:
                    widgets.stk_graph.setCurrentWidget(widgets.correlation)
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
            
            txt_param_selected = widgets.cmbParametersFile.currentText().split(', ')[0]
            parameters = widgets.cmbParametersFile.currentText()
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
            
            statistics_correlation = StatisticsEstepa(parameters_list[0],data1,self.config["estepa"],data2)
            data1 = statistics_correlation.data_list
            data2 = statistics_correlation.data_list2
            statistics_correlation = StatisticsEstepa(parameters_list[1],data2,self.config["estepa"],data1)
            data2 = statistics_correlation.data_list
            data1 = statistics_correlation.data_list2

            corr, pvalue = pearsonr(data1, data2) # Pearson's r, valor p
            obs = np.array([data1, data2])
            chi2, p_value, dof, expected = chi2_contingency(obs)

            
            result = linregress(data1, data2)

            widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+ 
                " - Pearson correlation:   \n" +
                " - r-value: %.3f, p-value: %.3f \t" % (corr,pvalue) + "\n" +
                " - Chisquare: : %.3f \t" % (chi2) + "\n" +
                " - a: %.3f \t" %  (result.slope) + "\n" +
                " - b: %.3f \t" %  (result.intercept) + "\n" +
                " - siga: %.3f \t" %  (result.stderr) + "\n" +
                " - sigb: %.3f \t" %  (result.intercept_stderr) + "\n")
            
            self.print_correlation(data1, data2, parameters_list[0], parameters_list[1])

        
        # Get data values from result_file
        for parameter in parameters_file_list:   
            textoParametros[parameter]=""
            data_values = result_file.get_data_values(parameter)
            for chip in data_values:
                textoParametros[parameter]+=str(chip)+"\t"+str(data_values[chip])+"\n"
        par=list(textoParametros.keys())[parametroMostrando]
        widgets.cmbCurrentParameter.setCurrentText(par)
                    
        data_value = textoParametros[par].replace(" ", "\t")
        widgets.txtLoadedValues.setPlainText("X"+"\t"+ "Y"+"\t"+ "Measurement"+ "\n" + "\n" + data_value)
           
    # PREVIOUS PARAMETER
    def previous_parameter(self):
    
        currentWidget = widgets.stk_graph.currentWidget()
        widgets.txtLoadedValues.setPlainText("")
        widgets.txtParametersResult.setPlainText("")
        btn = self.sender()
        btnName = btn.objectName()
        
        txt_param_selected = widgets.cmbCurrentParameter.currentText()
        
        parameters_file = widgets.cmbParametersFile.currentText()   # get text of combo Parameters
        parameters_file_list = parameters_file.split(", ")
        position = parameters_file_list.index(txt_param_selected)
        elements = widgets.cmbParametersFile.itemsChecked()
        
        if btnName == "btnPreviousParamFiles":
            if position - 1 < elements:
                next_position = position-1
            else:
                next_position = 0
        else:
            if position > 0:
                next_position = position+1
            else:
                next_position = elements+1
                
        if currentWidget == widgets.graph:
            print("Graph")
            
            self.analyze_files(next_position) 

          
        if currentWidget == widgets.correlation:
            print("Correlation")
            self.correlation_files(next_position)
                                                         
    # NEXT PARAMETER
    def next_parameter(self):
        
        currentWidget = widgets.stk_graph.currentWidget()
        widgets.txtLoadedValues.setPlainText("")
        
        btn = self.sender()
        btnName = btn.objectName()
        
        txt_param_selected = widgets.cmbCurrentParameter.currentText()
        parameters_file = widgets.cmbParametersFile.currentText()   # get text of combo Parameters
        parameters_file_list = parameters_file.split(", ")
        position = parameters_file_list.index(txt_param_selected)
        elements = widgets.cmbParametersFile.itemsChecked()
        
        if btnName == "btnNextParamFiles":
            if position + 1 < elements:
                next_position = position+1      #Parameter
            else:
                next_position = 0
            
        else:
            if position > 0:
                next_position = position-1
            else:
                next_position = elements-1
        
        if currentWidget == widgets.graph:
            widgets.txtParametersResult.setPlainText("")
            self.analyze_files(next_position)  
              
        if currentWidget == widgets.correlation:
            widgets.txtParametersResult.setPlainText("")
            self.correlation_files(next_position)         #Només cal carregar els data values un altre cop
      
    def update_cmbParametersFile(self):
        parameters_file = widgets.cmbParametersFile.currentText()   # get text of combo Parameters
        parameters_file_list = parameters_file.split(", ")
        
        widgets.cmbCurrentParameter.clear()
        widgets.cmbCurrentParameter.addItems(parameters_file_list)   
                           
    def search_parameter(self):
        
        currentWidget = widgets.stk_graph.currentWidget()
        
        txt_param_selected = widgets.cmbCurrentParameter.currentText()
        parameters_file = widgets.cmbParametersFile.currentText()
        parameters_file_list = parameters_file.split(", ") 
        
        if txt_param_selected != "":
            parametroMostrando = parameters_file_list.index(txt_param_selected)
            
            if currentWidget == widgets.graph:
                self.analyze_files(parametroMostrando)  
                
            if currentWidget == widgets.correlation:
                self.correlation_files(parametroMostrando)  
    
    def print_correlation(self,data1,data2,param1_name,param2_name):

        mpl_style(dark=self.histogram_mode)
        # Delete all widgets in layout
        layout = widgets.verticalLayout_correlation
        layout_buttons = widgets.horizontalLayout_btnCorrelation
        for i in reversed(range(widgets.verticalLayout_correlation.count())):
            widgets.verticalLayout_correlation.itemAt(i).widget().deleteLater()
        for i in reversed(range(widgets.horizontalLayout_btnCorrelation.count())):
            widgets.horizontalLayout_btnCorrelation.itemAt(i).widget().deleteLater()


        # create a FigureCanvas & add to layout
        static_canvas = FigureCanvas(Figure())

        static_canvas_buttons = FigureCanvas(Figure())
        static_canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        static_canvas.updateGeometry()

        toolbar = NavigationToolbar(static_canvas, self)
        toolbar.setStyleSheet("color: white;"
                            "background-color:#343B48")

        
        layout_buttons.addWidget(toolbar)
        layout.addWidget(static_canvas)
        _static_ax = static_canvas.figure.subplots()
        _static_ax.grid(True, color='gray', linewidth=1.0)
        # _static_ax.set_xlabel(param1_name)
        # _static_ax.set_ylabel(param2_name)
        _static_ax.scatter(data1, data2, color='white', linewidth=0.01)        #Punts

        # linear regression
        m, b = np.polyfit(data1, data2, 1)
        print (m, b)

        data22 = [float(x)* m +b  for x in data1]
        _static_ax.plot(data1, data22, color='#077f82', linewidth=1.0)  #Color de fons

        _static_ax.set_title(param1_name + " vs " + param2_name)
        
    #DATA FILE
    def open_file_dat(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        working_directory = str(self.config["directory"]["work_directory"])
        print(working_directory)
        fileName, _ = QFileDialog.getOpenFileName(self,         
            "Open .dat file", working_directory, "Dat Files (*.dat);; All files (*.*)")

        if fileName:
            working_directory=os.path.dirname(fileName)
            file_result = ResultFile(fileName)
            if not file_result.error:
                if btnName == "btnOpenDataFileInbase":
                    widgets.txtDataFileInbase.setText(fileName)
                    widgets.txtRunUpload.setText(file_result.lot)
                    widgets.txtWaferUpload.setText(file_result.wafer)
                if btnName == "btnOpenDataFile":
                    widgets.txtDataFile.setText(fileName)
                
                # print(file_result.info())
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
        working_directory = str(self.config["directory"]["work_directory"])
        fileName, _ = QFileDialog.getOpenFileName(self,'Open wafermap file', working_directory, 'PPG and PY Files (*_wafermap.py; *.ppg);; All files (*.*)')


        if fileName:
            working_directory=os.path.dirname(fileName)
            file_wafermap = WafermapFile(fileName)
            if not file_wafermap.error:
                if btnName == "btnOpenWafermapFileInbase":
                    widgets.txtWafermapFileInbase.setText(fileName)
                if btnName == "btnOpenWafermapFile":
                    widgets.txtWafermapFile.setText(fileName)

            else:
                # show error
                retval = messageBox(self,"Error loading PPG File",file_wafermap.error_message,"error")
                if btnName == "btnOpenDataFileInbase":
                    widgets.txtDataFileInbase.setText("")
                if btnName == "btnOpenDataFile":
                    widgets.txtDataFile.setText("")

    def generate_graph_correlation(self, parametroMostrando=0):               ###
        par=list(self.textoParametros.keys())[parametroMostrando]
        data=self.measurements[par]["medida"]
        mpl_style(dark=self.histogram_mode)
        layout = widgets.verticalLayout_correlation
        for i in reversed(range(widgets.verticalLayout_correlation.count())):
            widgets.verticalLayout_correlation.itemAt(i).widget().deleteLater()
        layout_buttons = widgets.horizontalLayout_btnCorrelation    
        for i in reversed(range(widgets.horizontalLayout_btnCorrelation.count())):
            widgets.horizontalLayout_btnCorrelation.itemAt(i).widget().deleteLater()
        

        # create a FigureCanvas & add to layout
        static_canvas = FigureCanvas(Figure())
        toolbar = NavigationToolbar(static_canvas, self)
        toolbar.setStyleSheet("background-color:#343B48")
        layout.addWidget(toolbar)
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

    def generate_histogram(self, data, parameters_file_list, parametroMostrando):
        
        mpl_style(dark=self.histogram_mode)
        
        # get data
        mu, std = norm.fit(data)
        print(mu)
        print(std)
        # Delete all widgets in layout
        layout = widgets.verticalLayout_histogram
        layout_buttons = widgets.horizontalLayout_btnHistogram
        for i in reversed(range(widgets.verticalLayout_histogram.count())):
            widgets.verticalLayout_histogram.itemAt(i).widget().deleteLater()
        for i in reversed(range(widgets.horizontalLayout_btnHistogram.count())):
            widgets.horizontalLayout_btnHistogram.itemAt(i).widget().deleteLater()
            
        # create a FigureCanvas & add to layout
        static_canvas = FigureCanvas(Figure())
    
        toolbar = NavigationToolbar(static_canvas, self)
        toolbar.setStyleSheet("color: white;"
                            "background-color:#343B48")
            
        layout_buttons.addWidget(toolbar)
        layout.addWidget(static_canvas)
        _static_ax = static_canvas.figure.subplots()
        
        # Plot the histogram.
        num_chunks = int(widgets.txtHistogramChunks.text())
        _static_ax.hist(data, bins=num_chunks, density=True, alpha=0.6, color='c')
        # Plot the PDF.
        xmin, xmax = min(data),max(data)
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        if self.histogram_mode :
            color_linea="w"
        else:
            color_linea="k"

        _static_ax.plot(x, p, color_linea, linewidth=1)
        _static_ax.set_title(parameters_file_list[parametroMostrando])
    
    def generate_wafermap(self, data_values, parameter):
        
        parameters = widgets.cmbParametersFile.currentText()
        parameters_list = parameters.split(", ")
        
        layout = widgets.horizontalLayout_wafermap
        layout_buttons = widgets.horizontalLayout_btnWafermap
        for i in reversed(range(widgets.horizontalLayout_wafermap.count())): 
            widgets.horizontalLayout_wafermap.itemAt(i).widget().deleteLater()
        for i in reversed(range(widgets.horizontalLayout_btnWafermap.count())): 
            widgets.horizontalLayout_btnWafermap.itemAt(i).widget().deleteLater()

        btn = self.sender()
        btnName = btn.objectName()

        fileName = widgets.txtWafermapFile.text()
        file_wafermap = WafermapFile(fileName)
        wafer = Wafer(file_wafermap.wafer_parameters)

        # get real xmax & ymax
        xmax_real = wafer.wafer_size_mm*1000/(wafer.xsize)
        ymax_real = wafer.wafer_size_mm*1000/(wafer.ysize)
        # Prepare 3 lists: X, Y, Values real
        data_values_real = dict()
        data_values_min = 1E99 
        data_values_max = -1E99
        error_value = 1E30
        errors_found = False
        outliers_found = False
        X = [*range(0, int(xmax_real)*-1, -1)]
        Y = [*range(0, int(ymax_real)*-1, -1)]
        # get min & max values in data values
        for k, v in data_values.items():
            new_coord = wafer.calculate_real_coordinate(k)
            data_values_real[new_coord] = v
            if (v>data_values_max and v<error_value): data_values_max = v
            if (v<data_values_min): data_values_min = v
            if (v==error_value): errors_found = True
        # fill values, assign value_in & value_out & value_errors & value_outliers
        values = list()
        num_colors = 15
        
        statistics_estepa = StatisticsEstepa(parameter, list(data_values.values()), self.config["estepa"])
        data_list_without_outliers = statistics_estepa.data_list
        
        if len( list(data_values.values()) ) != len(data_list_without_outliers):
            outliers_found = True
            # redifinir valors
            data_values_max = max(data_list_without_outliers)
            data_values_min = min(data_list_without_outliers)

        dif = data_values_max - data_values_min
        value_in = data_values_min - (dif*10/100) # in 
        value_out = data_values_min - (dif*20/100) # out
        
        value_outliers = data_values_max + (dif*10/100)
        value_errors = data_values_max + (dif*20/100)


        for y_axis in Y:
            y_axis_list = list()
            for x_axis in X:
                coord = str(x_axis) + " " + str(y_axis)
                if coord not in data_values_real:
                    if wafer.is_in(x_axis, y_axis):
                        value_add = value_in
                    else:
                        value_add = value_out
                else:
                    if data_values_real[coord]==error_value:
                        value_add = value_errors
                    elif data_values_real[coord] not in data_list_without_outliers:
                        value_add = value_outliers
                    else:
                        value_add = data_values_real[coord]

                y_axis_list.append(value_add)
            values.append(y_axis_list)

        # set colors
        background_options = ["white", "black", "mpl_style"]               #definim el background per cada tema
        background = "black"
        if background == "white":
            color_out = background
        if background == "black":
            color_out = "#0C1C23"  #Color fosc
            plt.style.use('dark_background')
            mpl.rcParams["figure.facecolor"] = "#0C1C23"
            mpl.rcParams["axes.facecolor"] = "#0C1C23"
            mpl.rcParams["savefig.facecolor"] = "#0C1C23"
        if background == "mpl_style":
            color_out = "#0C1C23"
            

        color_in = '#5E6A82'#gris
        color_outliers = 'Blue'
        color_error = 'Red'
        cmap_reds = plt.get_cmap('PuBuGn')
    
        colors = [color_out, color_in] + [cmap_reds(i / num_colors) for i in range(2, num_colors)]
        if outliers_found: colors = colors + [color_outliers]
        if errors_found: colors = colors + [color_error]

        cmap = LinearSegmentedColormap.from_list('', colors, num_colors)


        # create a FigureCanvas & add to layout
        static_canvas = FigureCanvas(Figure())

        static_canvas_buttons = FigureCanvas(Figure())
        static_canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        static_canvas.updateGeometry()

        toolbar = NavigationToolbar(static_canvas, self, "wafermap")
        toolbar.setStyleSheet("background-color:#343B48")
        
        layout_buttons.addWidget(toolbar)
        fig = static_canvas.figure
        ax = static_canvas.figure.subplots()
        # construct figure, axis
        im = ax.imshow(np.array(values), interpolation='nearest', aspect='auto',cmap=cmap)

        # add space for colour bar
        fig.subplots_adjust(right=0.85)
        cbar_ax = fig.add_axes([0.88, 0.15, 0.04, 0.7])
        cbar_ax.grid(False) # warning  message in console

        # get ticks: value_0 + value_ 1 + 12 colors from data_values_min to data_values_max + ERROR
        dif_value = data_values_min + (dif/2)
        ticks = [value_out, value_in, data_values_min, dif_value , data_values_max]
        yticks_list = ["OUT", "IN", str('%.2f' % data_values_min), str('%.2f' %dif_value), str('%.2f' %data_values_max)]
        if outliers_found:
            ticks.append(value_outliers)
            yticks_list.append("OUTLIER")
        if errors_found: 
            ticks.append(value_errors)
            yticks_list.append("ERROR")
        cbar = fig.colorbar(im, cax=cbar_ax, ticks=ticks)
        cbar.ax.set_yticklabels(yticks_list)

        # Show all ticks and label them with the respective list entries
        ax.set_xticks(np.arange(len(X)), labels=X)
        ax.set_yticks(np.arange(len(Y)), labels=Y)

        ax.locator_params(axis='y', nbins=6)
        ax.locator_params(axis='x', nbins=10)

        # Loop over data dimensions and create text annotations.
        for i in range(len(Y)):
            for j in range(len(X)):
                if wafer.is_home(j,i):
                    text = ax.text(j, i, "H",ha="center", va="center", color="w", fontsize=10)
                    #text = ax.text(j, i, "%.2f" % df.iloc[i, j],ha="center", va="center", color="w", fontsize=8)
                if wafer.is_origin(j,i):
                    text = ax.text(j, i, "O",ha="center", va="center", color="w", fontsize=10)
        title = parameter
        ax.set_title(title)                 

        def selection(sel):
            x = round(sel.target[0])*-1
            y = round(sel.target[1])*-1
            coord = str(x) + " " + str(y)
            if coord in data_values_real:
                if data_values_real[coord]==error_value:
                    text_insert = '{} [{} {}] = {}'.format(title, x, y, " ERROR value")
                else:
                    text_insert = '{} [{} {}] = {}'.format(title, x, y, '%.2f' % data_values_real[coord])
                sel.annotation.set_text(text_insert)
                sel.annotation.get_bbox_patch().set(fc=color_out, alpha=0.8)
                
                # ax.annotate(text_insert, xy=(x,y),bbox=dict(boxstyle="square", fc="w"))
            else:
                sel.annotation.set_text('')
        # set cursors
        crs = mplcursors.cursor(ax,hover=False)
        crs.connect("add", selection)
        # insert in layout
        layout.addWidget(static_canvas)
        static_canvas.draw()    
    
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

    def historical_check(self):                                                                                                   
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
        txt_results_directory = widgets.txt_results_directory.text()
        txt_working_directory = widgets.txt_working_directory.text()
        try:
            if str(txtLimitMin)!="" and str(txtLimitMax)!="" and isinstance(int(txtLimitMin),int) and isinstance(int(txtLimitMax),int):
                self.config["estepa"]["method"] = cmbOutlinerMethod
                self.config["estepa"]["lna"] = chkNonAutomaticLimits
                self.config["estepa"]["autolimits"] = chkGetAutoLimits
                self.config["estepa"]["limmin"] = txtLimitMin
                self.config["estepa"]["limmax"] = txtLimitMax
                self.config["estepa"]["chunks"] = txtHistogramChunks
                self.config["directory"]["res_directory"] = txt_results_directory             
                self.config["directory"]["work_directory"] = txt_working_directory
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
        # load estepa combo technology in pages estepa, upload and consult
        widgets.cmbTechnology.clear()
        widgets.cmbTechnologyUpload.clear()
        widgets.cmbTechnologyConsult.clear()
        widgets.cmbTechnology.addItem("Select technology")
        widgets.cmbTechnologyUpload.addItem("Select technology")
        widgets.cmbTechnologyConsult.addItem("Select technology")
        lista_technologies = self.estepa.get_technologies()
        widgets.cmbTechnology.addItems(lista_technologies)
        widgets.cmbTechnologyUpload.addItems(lista_technologies)
        widgets.cmbTechnologyConsult.addItems(lista_technologies)
        widgets.cmbParametersBBDD.clear()
        widgets.txtTechnologyUpload.setText("")
        widgets.cmbParametersConsult.clear()
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

    # CONSULT functions
    # -----------------

    def optionsHistorical(self):
        if widgets.historicalcheck.isChecked():
            widgets.optionsHistorical.setCurrentWidget(widgets.YesHistorical)
        else:
            widgets.optionsHistorical.setCurrentWidget(widgets.NoHistorical)

    def load_cmbRunsConsult(self):
        widgets.cmbRunsConsult.clear()
        widgets.cmbRunsConsult.addItem("Select run")
        technology = widgets.cmbTechnologyConsult.currentText()
        if technology != "Select technology" and technology != "":
            widgets.cmbRunsConsult.addItems([str(x) for x in self.estepa.get_runs(technology)])
        widgets.cmbParametersConsult.clear()

    def load_cmbWafersConsult(self):
        widgets.cmbWafersConsult.clear()
        widgets.cmbWafersConsult.addItem("Select wafer")
        run = widgets.cmbRunsConsult.currentText()
        if run != "Select run" and run != "":
            wafers_list = [str(x) for x in self.estepa.get_wafers(run)]
            wafers_list.insert(0, "All wafers")
            widgets.cmbWafersConsult.addItems(wafers_list)
        widgets.cmbParametersConsult.clear()

    def load_cmbParametersConsult(self):
        widgets.cmbParametersConsult.clear()
        widgets.cmbParametersConsult.addItem("Select parameters")
        wafers = widgets.cmbWafersConsult.currentText()
        if wafers!="Select wafer" and wafers!="":
            wafers_list = wafers.split(", ")
            # agafem només primera wafer seleccionada
            parameters_list = [str(x) for x in self.estepa.get_parameters(wafers_list[0])]
            widgets.cmbParametersConsult.addItems(parameters_list)
        else:
            widgets.cmbParametersConsult.clear()

    def load_controlsConsult(self):
        activate = widgets.cmbParametersConsult.currentText() != ""
        widgets.btnPreviousParamConsult.setVisible(activate)
        widgets.btnNextParamConsult.setVisible(activate)
        widgets.txtParamSelectedConsult.setVisible(activate)
        if activate:
            # view parameters in txtParamSelectedConsult
            parameters_list = widgets.cmbParametersConsult.currentText().split(", ")
            # widgets.txtParamSelectedConsult.setText(parameters_list[0])

            widgets.txtParamSelectedConsult.setCurrentText(parameters_list[0])

    def add_wafers_to_ListBox(self):
        wafers = widgets.cmbWafersConsult.currentText()
        if wafers != "Select wafers":
            wafers_list = wafers.split(", ")
            for wafer in wafers_list:           #PER EVITAR QUE ES REPETEIXIN
                if wafer not in [widgets.lbWafers.item(i).text() for i in range(widgets.lbWafers.count())]:
                # if wafer not in items_lbWafers:    
                    widgets.lbWafers.addItem(wafer)

    def get_items_ListBox(self):
        items = []
        for index in range(widgets.lbWafers.count()):
            items.append(widgets.lbWafers.item(index).text())
        return items


    def remove_item_ListBox(self, item):
        row = widgets.lbWafers.row(item)
        widgets.lbWafers.takeItem(row)

    def get_options_Consult(self):
        option_checked = "Wafers"
        option_historical = "No"
        option_values = "Values"
        if widgets.optRunsConsult.isChecked():
            option_checked = "Runs"
        if widgets.historicalcheck.isChecked():
            option_historical = "Yes"
            if widgets.optYield.isChecked():
                option_values = "Yield"
        # option_checked = Wafers or Runs
        # option_historical = Yes or No
        # option_values = Values or Yield
        options = [option_checked, option_historical, option_values]
        return options

    def consult(self, param_selected=0):
        mpl_style(dark=self.histogram_mode)
        widgets.txtDataValuesConsult.setPlainText("")
        widgets.consultWidget.setCurrentWidget(widgets.ConsultResults)
        parameters_consult = widgets.cmbParametersConsult.currentText()  # get text of combo Parameters
        parameters_consult_list = parameters_consult.split(", ")  # split to create list
        parameter_selected = parameters_consult_list[param_selected]
        widgets.txtParamSelectedConsult.setCurrentText(parameter_selected)

        tecnologia_consult = widgets.cmbTechnologyConsult.currentText()

        list_values_yields_param = []
        list_runs_wafers_param = []
        list_wafers = [widgets.lbWafers.item(i).text() for i in range(widgets.lbWafers.count())]
        list_rangos = self.estepa.get_rangos(tecnologia_consult, parameter_selected)

        # movie = QMovie("images\images\loading.gif")
        # widgets.lblLoadingConsult.setMovie(movie)
        if len(list_wafers) > 0  and len(parameters_consult_list) > 0:
            options = self.get_options_Consult()
            for parameter in parameters_consult_list:
                print(parameter)
                # widgets.lblLoadingConsult.setVisible(True)
                # movie.start()
                QApplication.processEvents()
                list_values_yields, list_runs_wafers = self.consult_get_parameter(list_wafers, options, parameter)

                if parameter == parameter_selected:
                    list_values_yields_param = list_values_yields
                    list_runs_wafers_param = list_runs_wafers

                new_text = parameter + "\n"
                actual_text = widgets.txtDataValuesConsult.toPlainText()
                if len(list_runs_wafers) == len(list_values_yields):
                    for i, _ in enumerate(list_runs_wafers):
                        print(i)
                        # print pantalla
                        QApplication.processEvents()
                        new_text += self.get_text_consult(list_values_yields[i], list_runs_wafers[i], parameter, options)
                    new_text += "\n"
                    widgets.txtDataValuesConsult.setPlainText(actual_text + new_text)
                    QApplication.processEvents()
                else:
                    messageBox(self, "Error in length lists", "Not the same length for list values/yields and runs/wafers",
                            "warning")
            # print graphs only for parameter selected
            self.print_consult(list_values_yields_param, list_runs_wafers_param, parameter_selected, options, list_rangos)
            # movie.stop()
            # widgets.lblLoadingConsult.setVisible(False)

        else:
            messageBox(self, "Wafers or parameters not selected", "Please, select at least one wafer and parameter to consult", "warning")

    def get_text_consult(self, values_yields, runs_wafers, parameter, options):
        text_print = ""

        text_print = " - " + runs_wafers + ": "
        if options[2] == "Values":
            text_print += f"Mean: {values_yields[0]:.2f}, "\
                        f"Median: {values_yields[1]:.2f}, "\
                        f"Stdev: {values_yields[2]:.2f}"
        else:
            text_print += f"{values_yields[0]} of {values_yields[1]}"
        text_print += "\n"
        return text_print

    def print_consult(self, values_yields, runs_wafers, parameter, options, list_rangos):

        layout, layout_buttons = self.clearDiagram()
        _static_ax = self.create_static_ax(layout, layout_buttons, "diagram")
        list_rangos_min = []
        list_rangos_max = []

        if options[2] == "Values":
            means = []
            val_X = []

            for i, _ in enumerate(runs_wafers):
                mean = float(values_yields[i][0])
                median = float(values_yields[i][2])
                stdev = float(values_yields[i][1])
                means.append(mean)
                val_X.append(i+1)
                if len(list_rangos)==2:
                    list_rangos_min.append(list_rangos[0])
                    list_rangos_max.append(list_rangos[1])

                value_max = mean + stdev
                value_min = mean - stdev
                label_stdev = ""
                label_median = ""
                label_mean = ""
                if i == 0:
                    # add label
                    label_stdev = "stdev"
                    label_median = "median"
                    label_mean = "mean"

                _static_ax.scatter(val_X[i], value_max, marker="+", color="blue", label=label_stdev)
                _static_ax.scatter(val_X[i], value_min, marker="+", color="blue")
                _static_ax.scatter(val_X[i], mean, marker="o", color="green", label=label_mean)
                _static_ax.scatter(val_X[i], median, marker="^", color="red", label=label_median)

            if len(means)>1:
                _static_ax.plot(val_X, means, color="green")
        else:
            yield_values = []
            val_X = []

            for i, _ in enumerate(runs_wafers):
                label_yield = ""
                if i == 0:
                    label_yield = "yield"
                val_X.append(i + 1)
                points_ini = values_yields[i][3]
                points_end = values_yields[i][4]
                yield_value = round((points_ini*100 / points_end), 2)
                yield_values.append(yield_value)
                _static_ax.scatter(val_X[i], yield_value, marker="+", color="gray", label=label_yield)

            if len(yield_values)>1:
                _static_ax.plot(val_X, yield_values, color="gray")

        # Add rangos
        if len(list_rangos)==2:
            _static_ax.plot(val_X, list_rangos_min, color="gray", linestyle="--")
            _static_ax.plot(val_X, list_rangos_max, color="gray", linestyle="--")
        # Add a title and axis labels
        if options[1] == "Yes":
            title = "Historical graph "
        else:
            title = "Graph "
        title += "of " + options[2].lower() + " for " + parameter
        # Set the x-axis to display variable names
        _static_ax.set_xticks(val_X)
        _static_ax.set_xticklabels(runs_wafers)
        # Add a legend
        _static_ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        # etiquetas
        _static_ax.set_xlabel(options[0])
        _static_ax.set_ylabel(parameter)
        _static_ax.set_title(title)

        # widgets.btnSaveDiagram.setVisible(True)
        # widgets.btnClearDiagram.setVisible(True)

    def clear_layouts(self, layout, layout_buttons):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()
        for i in reversed(range(layout_buttons.count())):
            layout_buttons.itemAt(i).widget().deleteLater()


    def create_static_ax(self, layout, layout_buttons, name):
        # create a FigureCanvas & add to layout
        static_canvas = FigureCanvas(Figure())

        static_canvas_buttons = FigureCanvas(Figure())
        static_canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        static_canvas.updateGeometry()

        toolbar = NavigationToolbarMod(static_canvas, self, name)
        layout_buttons.addWidget(toolbar)
        layout.addWidget(static_canvas)
        _static_ax = static_canvas.figure.subplots()

        return _static_ax

    def clearDiagram(self):
        # Delete all widgtets in layout
        layout = widgets.verticalLayout_diagram
        layout_buttons = widgets.horizontalLayout_btnDiagram
        self.clear_layouts(layout, layout_buttons)

        # widgets.btnSaveDiagram.setVisible(False)
        # widgets.btnClearDiagram.setVisible(False)

        return layout, layout_buttons

    def nextParamConsult(self):

        btn = self.sender()
        btnName = btn.objectName()

        txt_param_selected = widgets.txtParamSelectedConsult.currentText()
        parameters_file = widgets.cmbParametersConsult.currentText()
        parameters_file_list = parameters_file.split(", ")
        position = parameters_file_list.index(txt_param_selected)
        elements = widgets.cmbParametersConsult.itemsChecked()

        if btnName == "btnNextParamConsult":
            if position + 1 < elements:
                next_position = position + 1
            else:
                next_position = 0
        else:
            if position > 0:
                next_position = position - 1
            else:
                next_position = elements - 1
        self.consult(next_position)

    def consult_get_parameter(self, list_wafers, options, parameter):
        # check parameters in wafers
        list_values_yields = []
        list_runs_wafers = []
        check_parameter = True
        for wafer in list_wafers:
            QApplication.processEvents()
            if not self.estepa.exists_parameter_in_wafer(wafer, parameter):
                check_parameter = False
                break;

        if check_parameter:
            if options[0] == "Runs":
                # format lists wafers in list of list
                # order list and get list_wafers (runs) list of lists
                list_wafers_sort = sorted(list_wafers)
                list_wafers_runs = []
                run_prev = ""
                run_list = []
                for wafer in list_wafers_sort:
                    QApplication.processEvents()
                    run = wafer.split("-")[0]
                    if run == run_prev:
                        run_list.append(wafer)
                    else:
                        if run_prev!= "": list_wafers_runs.append(run_list)
                        run_list = []
                        run_list.append(wafer)
                        run_prev = run
                list_wafers_runs.append(run_list)
                list_wafers = list_wafers_runs

            for wafer in list_wafers:
                # if historical try to get values saved
                QApplication.processEvents()
                list_values = []
                stat_list = []
                if options[1] == "Yes":
                    list_values, run = self.estepa.get_medida_historical_consult(wafer, parameter, options)
                if len(list_values) == 0:
                    list_values, run = self.estepa.get_medida_consult(wafer, parameter)
                    stat = StatisticsEstepa(parameter, list_values, self.config["estepa"])
                    # get list of [mean, median, stdev, points_end, points_ini]
                    if stat.error:
                        messageBox(self, "Error in statistics", stat.error_message, "warning")
                    else:
                        stat_list = stat.get_parameters()
                else:
                    # Historical get values (create statistics with values returned)
                    if len(list_values) == 1:
                        stat_list = list_values
                    else:
                        means = []
                        medians = []
                        stdevs = []
                        points_end = 0
                        points_total = 0
                        for lv in list_values:
                            means.append(lv[0])
                            stdevs.append(lv[1])
                            medians.append(lv[2])
                            points_end += lv[3]
                            points_total += lv[4]

                        stat_list = [statistics.mean(means), statistics.mean(stdevs), statistics.mean(medians), points_end, points_total]

                if len(stat_list) > 0:
                    # if options[2] == "Values":
                    #     # get values
                    #     stat_list = stat_list[:3]
                    # else:
                    #     stat_list = stat_list[3:5]
                    list_values_yields.append(stat_list)
                    list_runs_wafers.append(run)
                else:
                    messageBox(self, "Values not found", f"Value not found for parameter '{parameter}'", "warning")

        else:
            messageBox(self, "Parameter not found in wafer", f"Parameter '{parameter}' not found in wafer: {wafer}!", "warning")

        return list_values_yields, list_runs_wafers


    # end CONSULT functions
    # ---------------------

    #UPDATE PARAMETERS IN BBDD
    def update_cmbParametersBBDD(self):
        cmbParametersBBDD = widgets.cmbParametersBBDD.currentText()
        cmbParametersBBDD_list = cmbParametersBBDD.split(",")

    def viewOptionsEstepa(self):
        
        if widgets.optLoadFiles.isChecked():
            widgets.optionsESTEPA.setCurrentIndex(0)
        if widgets.optLoadBBDD.isChecked():
            widgets.stk_loadfiles.setCurrentWidget(widgets.not_loaded)
            widgets.optionsESTEPA.setCurrentIndex(1)

    def analyze_BBDD(self):
        widgets.txtParametersResult.setPlainText("")
        widgets.txtLoadedValues.setPlainText("")
        self.graph_mode = True
        self.textoParametros={}
        widgets.wgt_estepa.setCurrentWidget(widgets.pg_analyze)
        widgets.stk_graph.setCurrentWidget(widgets.graph)
        
        parametersBBDD = widgets.cmbParametersBBDD.currentText()
        parametersBBDD_list = parametersBBDD.split(', ')
        counter = widgets.cmbParametersBBDD.count()
        if parametersBBDD!="" and parametersBBDD!="Select parameters":
            run = widgets.cmbRuns.currentText()
            wafer = widgets.cmbWafers.currentText()
            if parametersBBDD=="All parameters":
                parametersBBDD_list = [widgets.cmbParametersBBDD.itemText(i) for i in range(1,widgets.cmbParametersBBDD.count())]
            measurements = self.estepa.get_medidas(wafer,parametersBBDD_list)
            # print(measurements)
            
            for par in parametersBBDD_list:
                estadistica = StatisticsEstepa(par,measurements[par]["medida"],self.config["estepa"])
                widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+estadistica.print_statistics())
        else:
            widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+"No parameters selected!")

    def correlation_BBDD(self):
        widgets.txtParametersResult.setPlainText("")
        self.graph_mode=False
        textoParametros={}
        
        widgets.wgt_estepa.setCurrentWidget(widgets.pg_analyze)
        widgets.stk_graph.setCurrentWidget(widgets.no_graph)
        
        parametersBBDD = widgets.cmbParametersBBDD.currentText()
        parametersBBDD_list = parametersBBDD.split(', ')
        counter = widgets.cmbParametersBBDD.count()
        if parametersBBDD!="" and parametersBBDD!="Select parameters":
            run = widgets.cmbRuns.currentText()
            wafer = widgets.cmbWafers.currentText()
            if len(parametersBBDD)==2:
                    widgets.stk_graph.setCurrentWidget(widgets.correlation)
                    parametersBBDD_list = [widgets.cmbParametersBBDD.itemText(i) for i in range(1,widgets.cmbParametersBBDD.count())]
                    measurements = self.estepa.get_medidas(wafer,parametersBBDD_list)
                    print(measurements)
                    data1 = measurements[parametersBBDD[0]]["medida"]
                    data2 = measurements[parametersBBDD[1]]["medida"]
            else:
                error = True
                retval = messageBox(self,"Error selecting variables","Select 2 parameters for correlation","warning")    
            
            statistics_correlation = StatisticsEstepa(parametersBBDD[0],data1,self.config["estepa"],data2)
            data1 = statistics_correlation.data_list
            data2 = statistics_correlation.data_list2
            statistics_correlation = StatisticsEstepa(parametersBBDD[1],data2,self.config["estepa"],data1)
            data2 = statistics_correlation.data_list
            data1 = statistics_correlation.data_list2
            widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+statistics_correlation.print_correlation())
            
            
        else:
            widgets.txtParametersResult.setPlainText(widgets.txtParametersResult.toPlainText()+"\n"+"No parameters selected!")

    #CAMBIAR DE TEMA A CLARO                                                                                                               
    def change_theme(self):
        self.histogram_mode= not self.histogram_mode
        widgets.chk_theme.isChecked()
        if self.graph_mode:
            self.analyze_files()
        else:
            self.correlation_files()

    # end ESTEPA functions
    # --------------------

    # ----------------
    # USER SETTINGS
    # ----------------
    
    #DIRECTORIES
    def set_results_directory(self):
        
        btn = self.sender()
        btnName = btn.objectName()
        result_directory = QFileDialog.getExistingDirectory(self, "Set Results Directory")
        print(result_directory)
        
        if widgets.txt_results_directory_2 != "":
            widgets.txt_results_directory.setText(result_directory)
            widgets.txt_results_directory_2.setText(result_directory)
        
    def set_working_directory(self):
        btn = self.sender()
        btnName = btn.objectName()
        working_directory = QFileDialog.getExistingDirectory(self, "Set Working Directory")
        print(working_directory)
        widgets.txt_working_directory.setText(working_directory)
        widgets.txt_working_directory_2.setText(working_directory)


    #CLOSE OPTIONS MENU WHEN PRESSING OTHER WINDOWS
    def closeLeftBox(self):
        self.left_box_open = False
        print("Closing Options")
        UIFunctions.toggleLeftBox(self, False)
        

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()     #obte info del botó al fer click
        btnName = btn.objectName()  #obté el nom de la var
    

        # PAGINA PRINCIPAL
        if btnName == "btn_page_home":
            
            if self.left_box_open == True:
                self.closeLeftBox()
            
            self.left_box_open = False
            widgets.stackedWidget.setCurrentWidget(widgets.Home_Window)
            widgets.settings.setCurrentWidget(widgets.no)
            widgets.options.setCurrentWidget(widgets.not_able)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            
            
        # PAGINA REPORTS
        if btnName == "btn_page_reports":
            if self.left_box_open == True:
                self.closeLeftBox()
            
            self.left_box_open = False
            widgets.stackedWidget.setCurrentWidget(widgets.Reports_Window)
            widgets.settings.setCurrentWidget(widgets.no)
            widgets.options.setCurrentWidget(widgets.not_able)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            
        if btnName == "home_reports":
            if self.left_box_open == True:
                self.closeLeftBox()
            
            self.left_box_open = False
            widgets.stackedWidget.setCurrentWidget(widgets.Reports_Window)
            widgets.settings.setCurrentWidget(widgets.no)
            widgets.options.setCurrentWidget(widgets.not_able)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW HOME ESTEPA
        if btnName == "btn_page_estepa":
            
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.estepa)
            widgets.settings.setCurrentWidget(widgets.no)                   #CANVIAR QUAN TINGUI FUNCIONALITAT
            widgets.options.setCurrentWidget(widgets.able)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "home_analysis":
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.estepa)
            widgets.settings.setCurrentWidget(widgets.no)                   #CANVIAR QUAN TINGUI FUNCIONALITAT
            widgets.options.setCurrentWidget(widgets.able)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_page_consult":
            if self.left_box_open == True:
                self.closeLeftBox()
            
            self.left_box_open = False
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            # show estepa page
            
            widgets.stackedWidget.setCurrentWidget(widgets.consult_estepa)
            widgets.settings.setCurrentWidget(widgets.no)
            widgets.options.setCurrentWidget(widgets.not_able)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "home_consult":
            if self.left_box_open == True:
                self.closeLeftBox()
            
            self.left_box_open = False
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.consult_estepa)
            widgets.settings.setCurrentWidget(widgets.no)
            widgets.options.setCurrentWidget(widgets.not_able)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_page_inbase":
            if self.left_box_open == True:
                self.closeLeftBox()
            
            self.left_box_open = False
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.inbase)
            widgets.settings.setCurrentWidget(widgets.no)
            widgets.options.setCurrentWidget(widgets.not_able)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "home_upload":
            if self.left_box_open == True:
                print("Closing Options")
                self.closeLeftBox()
            
            self.left_box_open = False
            # show estepa configuration
            widgets.stackedWidget_configuration.setCurrentWidget(widgets.configuration_estepa)
            
            # show estepa page
            widgets.stackedWidget.setCurrentWidget(widgets.inbase)
            widgets.settings.setCurrentWidget(widgets.no)
            widgets.options.setCurrentWidget(widgets.not_able)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
            
        if btnName == "btn_clear_all":
            widgets.wgt_estepa.setCurrentWidget(widgets.pg_load)
            widgets.stk_graph.setCurrentWidget(widgets.no_graph)
            # widgets.stk_loadfiles.setCurrentWidget(widgets.not_loaded) 

        if btnName == "btn_clear":
            widgets.stk_loadfiles.setCurrentWidget(widgets.not_loaded)
            widgets.txtDataFile.setText("")
            widgets.txtWafermapFile.setText("")

        if btnName == "btnClearlConsult":
            widgets.consultWidget.setCurrentWidget(widgets.ConsultData)
            widgets.txtDataValuesConsult.setText("")

    # COPIAR RESULTADOS
    def copy_results(self):
        
        currentWidget = widgets.ResultsWidget.currentWidget()
        
        if currentWidget == widgets.tab_results:
            widgets.txtParametersResult.selectAll()
            widgets.txtParametersResult.copy()

        if currentWidget == widgets.tab_values:
            widgets.txtLoadedValues.selectAll()
            widgets.txtLoadedValues.copy()


    def copy_consult(self):
        
        currentWidget = widgets.ResultsWidgetConsult.currentWidget()
        
        if currentWidget == widgets.tab_results_consult:
            widgets.txtParametersResult.selectAll()
            widgets.txtParametersResult.copy()

    # GUARDAR RESULTADOS
    def save_results(self, parametroMostrando):
        
        FileName = widgets.txtDataFile.text()    
        result_file = ResultFile(FileName)
        results_directory = str(self.config["directory"]["res_directory"])   
        currentWidget = widgets.ResultsWidget.currentWidget()  
        
        self.lot = result_file.process.split("-")[0] # run
        self.wafer = result_file.process.split("-")[1] # wafer
        # parameter=list(self.textoParametros.keys())[parametroMostrando]
        
        parameters_file = widgets.cmbParametersFile.currentText()   # get text of combo Parameters
        parameters_file_list = parameters_file.split(", ")
        parameter = parameters_file_list[parametroMostrando]
        
        print(parametroMostrando)
   
        if currentWidget == widgets.tab_results:
            fileName, _ = QFileDialog.getSaveFileName(self,
                "Save result file", results_directory + "/" + self.lot + "-" + self.wafer + "_" + parameter + "_results", "TXT Files (*.txt);; DOC Files (*.doc);; All files (*.*)")
        
        if currentWidget == widgets.tab_values:
            fileName, _ = QFileDialog.getSaveFileName(self,
                "Save result file", results_directory + "/" + self.lot + "-" + self.wafer + "_" + parameter + "_values", "TXT Files (*.txt);; DOC Files (*.doc);; All files (*.*)")
                                                                    
        #Format RUN-WAFER_PARAMETER_histogram      Modificar botó guardar imatge
        #Format RUN-WAFER_PARAMETER_wafermap


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()                            
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos

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
        
        [directory]
        res_directory = "D:/USUARIS/AKAIYFS/Documents/ESTEPA/Results/"
        work_directory = "D:/USUARIS/AKAIYFS/Desktop/ESTEPA ACTUAL/Files/"
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








#Posar cometaris de les funcions i les clases 
'''
Class Wafermap File:...
...
'''

#per fer help(main.py)

