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

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
# general functions
from functions import *
# datetime
from datetime import datetime




os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
#app = QtWidget.QApplication(sys.argv) Per solucionar el error de QApplication

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
import_report_file = "report_import.txt"


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__(self)
        
                # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow(object)
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

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # LOAD configuration TOML
        # self.path_config_file = os.getcwd() + '/config/config.toml'
        # self.load_config() 
        # -----------
        # PAGE ESTEPA
        # -----------

    
# def get_json_file(filename, var_name):
#     # if configuration json file exists load configuratión from file
#     filename_config = os.getcwd() + '/modules/' + filename + '.json'
#     file_exists = os.path.exists(filename_config)
#     try :
#         if file_exists:
#             with open(filename_config) as json_file:
#                 return json.load(json_file)
#         else:
#             # generate json file default
#             return ""
#     except:
#         return ""
#     return var_name
              
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = LoginWindow()
    sys.exit(app.exec())