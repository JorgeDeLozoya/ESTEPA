# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)

from mplwidget import MplWidget
from pyqtgraph import PlotWidget
from widgets import CheckableComboBox
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1389, 891)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topLogo.sizePolicy().hasHeightForWidth())
        self.topLogo.setSizePolicy(sizePolicy)
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Montserrat ExtraBold"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setStyleSheet(u"font: 10pt \"absender\";\n"
"font: 81 11pt \"Montserrat ExtraBold\";")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.HomeWindow = QPushButton(self.topMenu)
        self.HomeWindow.setObjectName(u"HomeWindow")
        sizePolicy1.setHeightForWidth(self.HomeWindow.sizePolicy().hasHeightForWidth())
        self.HomeWindow.setSizePolicy(sizePolicy1)
        self.HomeWindow.setMinimumSize(QSize(0, 45))
        self.HomeWindow.setFont(font)
        self.HomeWindow.setCursor(QCursor(Qt.PointingHandCursor))
        self.HomeWindow.setLayoutDirection(Qt.LeftToRight)
        self.HomeWindow.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-description.png);")

        self.verticalLayout_8.addWidget(self.HomeWindow)

        self.AnalyzeButton = QPushButton(self.topMenu)
        self.AnalyzeButton.setObjectName(u"AnalyzeButton")
        sizePolicy1.setHeightForWidth(self.AnalyzeButton.sizePolicy().hasHeightForWidth())
        self.AnalyzeButton.setSizePolicy(sizePolicy1)
        self.AnalyzeButton.setMinimumSize(QSize(0, 45))
        self.AnalyzeButton.setFont(font)
        self.AnalyzeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.AnalyzeButton.setLayoutDirection(Qt.LeftToRight)
        self.AnalyzeButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-find-in-page.png);")

        self.verticalLayout_8.addWidget(self.AnalyzeButton)

        self.ConsultWindow = QPushButton(self.topMenu)
        self.ConsultWindow.setObjectName(u"ConsultWindow")
        sizePolicy1.setHeightForWidth(self.ConsultWindow.sizePolicy().hasHeightForWidth())
        self.ConsultWindow.setSizePolicy(sizePolicy1)
        self.ConsultWindow.setMinimumSize(QSize(0, 45))
        self.ConsultWindow.setFont(font)
        self.ConsultWindow.setCursor(QCursor(Qt.PointingHandCursor))
        self.ConsultWindow.setLayoutDirection(Qt.LeftToRight)
        self.ConsultWindow.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png)")

        self.verticalLayout_8.addWidget(self.ConsultWindow)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy1.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy1)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-notes.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)

        self.pushButton = QPushButton(self.topMenu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 45))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cloud-upload.png);")

        self.verticalLayout_8.addWidget(self.pushButton)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Outliner = QLabel(self.extraTopMenu)
        self.Outliner.setObjectName(u"Outliner")
        self.Outliner.setMaximumSize(QSize(400, 16777215))
        self.Outliner.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.Outliner)

        self.OutlinerBox = QComboBox(self.extraTopMenu)
        self.OutlinerBox.addItem("")
        self.OutlinerBox.addItem("")
        self.OutlinerBox.addItem("")
        self.OutlinerBox.setObjectName(u"OutlinerBox")
        self.OutlinerBox.setEditable(False)
        self.OutlinerBox.setMinimumContentsLength(0)

        self.verticalLayout_11.addWidget(self.OutlinerBox)

        self.Font = QLabel(self.extraTopMenu)
        self.Font.setObjectName(u"Font")
        self.Font.setMaximumSize(QSize(400, 16777215))
        self.Font.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.Font)

        self.FontBox = QComboBox(self.extraTopMenu)
        self.FontBox.addItem("")
        self.FontBox.addItem("")
        self.FontBox.setObjectName(u"FontBox")
        self.FontBox.setEditable(False)
        self.FontBox.setMinimumContentsLength(0)

        self.verticalLayout_11.addWidget(self.FontBox)

        self.Performance = QLabel(self.extraTopMenu)
        self.Performance.setObjectName(u"Performance")
        self.Performance.setMaximumSize(QSize(400, 16777215))
        self.Performance.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.Performance)

        self.PerformanceBox = QComboBox(self.extraTopMenu)
        self.PerformanceBox.addItem("")
        self.PerformanceBox.addItem("")
        self.PerformanceBox.setObjectName(u"PerformanceBox")
        self.PerformanceBox.setEditable(False)
        self.PerformanceBox.setMinimumContentsLength(0)

        self.verticalLayout_11.addWidget(self.PerformanceBox)

        self.Wafer = QLabel(self.extraTopMenu)
        self.Wafer.setObjectName(u"Wafer")
        self.Wafer.setMaximumSize(QSize(400, 16777215))
        self.Wafer.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.Wafer)

        self.WaferBox = QComboBox(self.extraTopMenu)
        self.WaferBox.addItem("")
        self.WaferBox.addItem("")
        self.WaferBox.addItem("")
        self.WaferBox.setObjectName(u"WaferBox")
        self.WaferBox.setEditable(False)
        self.WaferBox.setMinimumContentsLength(0)

        self.verticalLayout_11.addWidget(self.WaferBox)

        self.HistogramTextLabel = QLabel(self.extraTopMenu)
        self.HistogramTextLabel.setObjectName(u"HistogramTextLabel")

        self.verticalLayout_11.addWidget(self.HistogramTextLabel)

        self.NumbersBox = QSpinBox(self.extraTopMenu)
        self.NumbersBox.setObjectName(u"NumbersBox")
        self.NumbersBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.NumbersBox.setMinimum(2)
        self.NumbersBox.setMaximum(21)

        self.verticalLayout_11.addWidget(self.NumbersBox)

        self.checkBox = QCheckBox(self.extraTopMenu)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_11.addWidget(self.checkBox)

        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")
        self.btn_share.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.DirectoryButton = QPushButton(self.extraTopMenu)
        self.DirectoryButton.setObjectName(u"DirectoryButton")
        sizePolicy1.setHeightForWidth(self.DirectoryButton.sizePolicy().hasHeightForWidth())
        self.DirectoryButton.setSizePolicy(sizePolicy1)
        self.DirectoryButton.setMinimumSize(QSize(0, 45))
        self.DirectoryButton.setFont(font)
        self.DirectoryButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.DirectoryButton.setLayoutDirection(Qt.LeftToRight)
        self.DirectoryButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.DirectoryButton)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font2)
        self.titleRightInfo.setStyleSheet(u"font: 10pt \"absender\";\n"
"font: 81 11pt \"Montserrat ExtraBold\";")
        self.titleRightInfo.setScaledContents(False)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(self.home)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(2, 0, 1281, 771))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.gridLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setSizeIncrement(QSize(0, 0))
        self.graphicsView.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.graphicsView.setFrameShape(QFrame.NoFrame)

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.btn_ppg_3 = QPushButton(self.gridLayoutWidget)
        self.btn_ppg_3.setObjectName(u"btn_ppg_3")
        self.btn_ppg_3.setMinimumSize(QSize(150, 30))
        self.btn_ppg_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u"../../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ppg_3.setIcon(icon4)

        self.gridLayout_5.addWidget(self.btn_ppg_3, 3, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 1, 1, 1)

        self.btn_ppg_4 = QPushButton(self.gridLayoutWidget)
        self.btn_ppg_4.setObjectName(u"btn_ppg_4")
        self.btn_ppg_4.setMinimumSize(QSize(150, 30))
        self.btn_ppg_4.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_ppg_4.setIcon(icon4)

        self.gridLayout_5.addWidget(self.btn_ppg_4, 5, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_5.addWidget(self.lineEdit, 1, 0, 1, 2)

        self.btn_ppg_2 = QPushButton(self.gridLayoutWidget)
        self.btn_ppg_2.setObjectName(u"btn_ppg_2")
        self.btn_ppg_2.setMinimumSize(QSize(150, 30))
        self.btn_ppg_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_ppg_2.setIcon(icon4)

        self.gridLayout_5.addWidget(self.btn_ppg_2, 2, 0, 1, 1)

        self.btn_ppg_5 = QPushButton(self.gridLayoutWidget)
        self.btn_ppg_5.setObjectName(u"btn_ppg_5")
        self.btn_ppg_5.setMinimumSize(QSize(150, 30))
        self.btn_ppg_5.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_ppg_5.setIcon(icon4)

        self.gridLayout_5.addWidget(self.btn_ppg_5, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.stackedWidget.addWidget(self.widgets)
        self.analyze = QWidget()
        self.analyze.setObjectName(u"analyze")
        self.verticalLayout_22 = QVBoxLayout(self.analyze)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_10 = QLabel(self.analyze)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 20))
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_22.addWidget(self.label_10)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.optLoadFiles = QRadioButton(self.analyze)
        self.optLoadFiles.setObjectName(u"optLoadFiles")
        self.optLoadFiles.setMinimumSize(QSize(150, 0))
        self.optLoadFiles.setMaximumSize(QSize(150, 16777215))
        self.optLoadFiles.setChecked(True)

        self.gridLayout_24.addWidget(self.optLoadFiles, 0, 0, 1, 1)

        self.optLoadBBDD = QRadioButton(self.analyze)
        self.optLoadBBDD.setObjectName(u"optLoadBBDD")
        self.optLoadBBDD.setMinimumSize(QSize(150, 0))
        self.optLoadBBDD.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_24.addWidget(self.optLoadBBDD, 0, 1, 1, 1)


        self.horizontalLayout_22.addLayout(self.gridLayout_24)


        self.verticalLayout_39.addLayout(self.horizontalLayout_22)

        self.optionsESTEPA = QStackedWidget(self.analyze)
        self.optionsESTEPA.setObjectName(u"optionsESTEPA")
        self.optionsESTEPA.setMinimumSize(QSize(520, 310))
        self.optionsESTEPA.setMaximumSize(QSize(520, 310))
        self.files = QWidget()
        self.files.setObjectName(u"files")
        self.gridLayoutWidget_8 = QWidget(self.files)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(9, 20, 481, 231))
        self.gridLayout_25 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.btnLoadFiles = QPushButton(self.gridLayoutWidget_8)
        self.btnLoadFiles.setObjectName(u"btnLoadFiles")
        self.btnLoadFiles.setMinimumSize(QSize(150, 30))
        self.btnLoadFiles.setFont(font)
        self.btnLoadFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLoadFiles.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLoadFiles.setIcon(icon5)

        self.gridLayout_25.addWidget(self.btnLoadFiles, 4, 0, 1, 1)

        self.labelVersion_34 = QLabel(self.gridLayoutWidget_8)
        self.labelVersion_34.setObjectName(u"labelVersion_34")
        self.labelVersion_34.setMaximumSize(QSize(200, 20))
        self.labelVersion_34.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_34.setLineWidth(1)
        self.labelVersion_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_34, 0, 0, 1, 1)

        self.btnOpenWafermapFile = QPushButton(self.gridLayoutWidget_8)
        self.btnOpenWafermapFile.setObjectName(u"btnOpenWafermapFile")
        self.btnOpenWafermapFile.setMinimumSize(QSize(40, 30))
        self.btnOpenWafermapFile.setMaximumSize(QSize(16777215, 30))
        self.btnOpenWafermapFile.setFont(font)
        self.btnOpenWafermapFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOpenWafermapFile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnOpenWafermapFile.setIcon(icon6)

        self.gridLayout_25.addWidget(self.btnOpenWafermapFile, 3, 1, 1, 1)

        self.txtDataFile = QLineEdit(self.gridLayoutWidget_8)
        self.txtDataFile.setObjectName(u"txtDataFile")
        self.txtDataFile.setEnabled(False)
        self.txtDataFile.setMinimumSize(QSize(400, 30))
        self.txtDataFile.setMaximumSize(QSize(400, 30))
        self.txtDataFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtDataFile, 1, 0, 1, 1)

        self.txtWafermapFile = QLineEdit(self.gridLayoutWidget_8)
        self.txtWafermapFile.setObjectName(u"txtWafermapFile")
        self.txtWafermapFile.setEnabled(False)
        self.txtWafermapFile.setMinimumSize(QSize(400, 30))
        self.txtWafermapFile.setMaximumSize(QSize(400, 30))
        self.txtWafermapFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtWafermapFile, 3, 0, 1, 1)

        self.btnOpenDataFile = QPushButton(self.gridLayoutWidget_8)
        self.btnOpenDataFile.setObjectName(u"btnOpenDataFile")
        self.btnOpenDataFile.setMinimumSize(QSize(50, 30))
        self.btnOpenDataFile.setMaximumSize(QSize(50, 30))
        self.btnOpenDataFile.setFont(font)
        self.btnOpenDataFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOpenDataFile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnOpenDataFile.setIcon(icon6)

        self.gridLayout_25.addWidget(self.btnOpenDataFile, 1, 1, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_25.addItem(self.verticalSpacer_18, 5, 0, 1, 1)

        self.labelVersion_35 = QLabel(self.gridLayoutWidget_8)
        self.labelVersion_35.setObjectName(u"labelVersion_35")
        self.labelVersion_35.setMaximumSize(QSize(200, 20))
        self.labelVersion_35.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_35.setLineWidth(1)
        self.labelVersion_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_35, 2, 0, 1, 1)

        self.cmbParametersFile = CheckableComboBox(self.gridLayoutWidget_8)
        self.cmbParametersFile.addItem("")
        self.cmbParametersFile.addItem("")
        self.cmbParametersFile.addItem("")
        self.cmbParametersFile.addItem("")
        self.cmbParametersFile.addItem("")
        self.cmbParametersFile.addItem("")
        self.cmbParametersFile.addItem("")
        self.cmbParametersFile.addItem("")
        self.cmbParametersFile.setObjectName(u"cmbParametersFile")
        self.cmbParametersFile.setMinimumSize(QSize(400, 0))
        self.cmbParametersFile.setMaximumSize(QSize(400, 16777215))
        self.cmbParametersFile.setFont(font)
        self.cmbParametersFile.setAutoFillBackground(False)
        self.cmbParametersFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbParametersFile.setEditable(True)
        self.cmbParametersFile.setCurrentText(u"Select instrument")
        self.cmbParametersFile.setIconSize(QSize(16, 16))
        self.cmbParametersFile.setFrame(True)

        self.gridLayout_25.addWidget(self.cmbParametersFile, 7, 0, 1, 1)

        self.labelVersion_36 = QLabel(self.gridLayoutWidget_8)
        self.labelVersion_36.setObjectName(u"labelVersion_36")
        self.labelVersion_36.setMaximumSize(QSize(200, 20))
        self.labelVersion_36.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_36.setLineWidth(1)
        self.labelVersion_36.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_36, 6, 0, 1, 1)

        self.gridLayoutWidget_11 = QWidget(self.files)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(10, 260, 481, 41))
        self.gridLayout_26 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.btnAnalyzeFiles = QPushButton(self.gridLayoutWidget_11)
        self.btnAnalyzeFiles.setObjectName(u"btnAnalyzeFiles")
        self.btnAnalyzeFiles.setEnabled(True)
        self.btnAnalyzeFiles.setMinimumSize(QSize(150, 30))
        self.btnAnalyzeFiles.setMaximumSize(QSize(150, 16777215))
        self.btnAnalyzeFiles.setFont(font)
        self.btnAnalyzeFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnalyzeFiles.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"\n"
"")
        self.btnAnalyzeFiles.setIcon(icon5)

        self.gridLayout_26.addWidget(self.btnAnalyzeFiles, 0, 0, 1, 1)

        self.btnCorrelationFiles = QPushButton(self.gridLayoutWidget_11)
        self.btnCorrelationFiles.setObjectName(u"btnCorrelationFiles")
        self.btnCorrelationFiles.setMinimumSize(QSize(150, 30))
        self.btnCorrelationFiles.setMaximumSize(QSize(150, 16777215))
        self.btnCorrelationFiles.setFont(font)
        self.btnCorrelationFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCorrelationFiles.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"\n"
"")
        self.btnCorrelationFiles.setIcon(icon5)

        self.gridLayout_26.addWidget(self.btnCorrelationFiles, 0, 1, 1, 1)

        self.optionsESTEPA.addWidget(self.files)
        self.bbdd = QWidget()
        self.bbdd.setObjectName(u"bbdd")
        self.gridLayoutWidget_12 = QWidget(self.bbdd)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(10, 10, 471, 298))
        self.gridLayout_27 = QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.cmbWafers = QComboBox(self.gridLayoutWidget_12)
        self.cmbWafers.addItem("")
        self.cmbWafers.setObjectName(u"cmbWafers")
        self.cmbWafers.setMinimumSize(QSize(160, 30))
        self.cmbWafers.setMaximumSize(QSize(16777215, 30))
        self.cmbWafers.setFont(font)
        self.cmbWafers.setAutoFillBackground(False)
        self.cmbWafers.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbWafers.setEditable(True)
        self.cmbWafers.setIconSize(QSize(16, 16))
        self.cmbWafers.setFrame(True)

        self.gridLayout_27.addWidget(self.cmbWafers, 5, 0, 1, 1)

        self.labelVersion_37 = QLabel(self.gridLayoutWidget_12)
        self.labelVersion_37.setObjectName(u"labelVersion_37")
        self.labelVersion_37.setMaximumSize(QSize(200, 20))
        self.labelVersion_37.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_37.setLineWidth(1)
        self.labelVersion_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelVersion_37, 0, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_27.addItem(self.verticalSpacer_14, 9, 0, 1, 1)

        self.btnCorrelationBBDD = QPushButton(self.gridLayoutWidget_12)
        self.btnCorrelationBBDD.setObjectName(u"btnCorrelationBBDD")
        self.btnCorrelationBBDD.setMinimumSize(QSize(150, 30))
        self.btnCorrelationBBDD.setMaximumSize(QSize(150, 30))
        self.btnCorrelationBBDD.setFont(font)
        self.btnCorrelationBBDD.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCorrelationBBDD.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnCorrelationBBDD.setIcon(icon5)

        self.gridLayout_27.addWidget(self.btnCorrelationBBDD, 11, 1, 1, 1)

        self.cmbTechnology = QComboBox(self.gridLayoutWidget_12)
        self.cmbTechnology.addItem("")
        self.cmbTechnology.setObjectName(u"cmbTechnology")
        self.cmbTechnology.setMinimumSize(QSize(160, 30))
        self.cmbTechnology.setMaximumSize(QSize(16777215, 30))
        self.cmbTechnology.setFont(font)
        self.cmbTechnology.setAutoFillBackground(False)
        self.cmbTechnology.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbTechnology.setEditable(True)
        self.cmbTechnology.setIconSize(QSize(16, 16))
        self.cmbTechnology.setFrame(True)

        self.gridLayout_27.addWidget(self.cmbTechnology, 1, 0, 1, 1)

        self.labelVersion_38 = QLabel(self.gridLayoutWidget_12)
        self.labelVersion_38.setObjectName(u"labelVersion_38")
        self.labelVersion_38.setMaximumSize(QSize(200, 20))
        self.labelVersion_38.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_38.setLineWidth(1)
        self.labelVersion_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelVersion_38, 2, 0, 1, 1)

        self.cmbRuns = QComboBox(self.gridLayoutWidget_12)
        self.cmbRuns.addItem("")
        self.cmbRuns.setObjectName(u"cmbRuns")
        self.cmbRuns.setMinimumSize(QSize(160, 30))
        self.cmbRuns.setMaximumSize(QSize(16777215, 30))
        self.cmbRuns.setFont(font)
        self.cmbRuns.setAutoFillBackground(False)
        self.cmbRuns.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbRuns.setEditable(True)
        self.cmbRuns.setIconSize(QSize(16, 16))
        self.cmbRuns.setFrame(True)

        self.gridLayout_27.addWidget(self.cmbRuns, 3, 0, 1, 1)

        self.labelVersion_39 = QLabel(self.gridLayoutWidget_12)
        self.labelVersion_39.setObjectName(u"labelVersion_39")
        self.labelVersion_39.setMaximumSize(QSize(200, 20))
        self.labelVersion_39.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_39.setLineWidth(1)
        self.labelVersion_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelVersion_39, 4, 0, 1, 1)

        self.btnAnalyzeBBDD = QPushButton(self.gridLayoutWidget_12)
        self.btnAnalyzeBBDD.setObjectName(u"btnAnalyzeBBDD")
        self.btnAnalyzeBBDD.setMinimumSize(QSize(150, 0))
        self.btnAnalyzeBBDD.setMaximumSize(QSize(150, 30))
        self.btnAnalyzeBBDD.setFont(font)
        self.btnAnalyzeBBDD.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnalyzeBBDD.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnAnalyzeBBDD.setIcon(icon5)

        self.gridLayout_27.addWidget(self.btnAnalyzeBBDD, 11, 0, 1, 1)

        self.labelVersion_40 = QLabel(self.gridLayoutWidget_12)
        self.labelVersion_40.setObjectName(u"labelVersion_40")
        self.labelVersion_40.setMaximumSize(QSize(200, 20))
        self.labelVersion_40.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_40.setLineWidth(1)
        self.labelVersion_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelVersion_40, 6, 0, 1, 1)

        self.cmbParametersBBDD = QComboBox(self.gridLayoutWidget_12)
        self.cmbParametersBBDD.addItem("")
        self.cmbParametersBBDD.setObjectName(u"cmbParametersBBDD")
        self.cmbParametersBBDD.setMinimumSize(QSize(160, 30))
        self.cmbParametersBBDD.setMaximumSize(QSize(16777215, 30))
        self.cmbParametersBBDD.setFont(font)
        self.cmbParametersBBDD.setAutoFillBackground(False)
        self.cmbParametersBBDD.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbParametersBBDD.setEditable(True)
        self.cmbParametersBBDD.setIconSize(QSize(16, 16))
        self.cmbParametersBBDD.setFrame(True)

        self.gridLayout_27.addWidget(self.cmbParametersBBDD, 8, 0, 1, 1)

        self.optionsESTEPA.addWidget(self.bbdd)

        self.verticalLayout_39.addWidget(self.optionsESTEPA)


        self.horizontalLayout_21.addLayout(self.verticalLayout_39)

        self.horizontalSpacer_20 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_20)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.labelVersion_41 = QLabel(self.analyze)
        self.labelVersion_41.setObjectName(u"labelVersion_41")
        self.labelVersion_41.setMaximumSize(QSize(200, 20))
        self.labelVersion_41.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_41.setLineWidth(1)
        self.labelVersion_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_40.addWidget(self.labelVersion_41)

        self.txtLoadedValues = QPlainTextEdit(self.analyze)
        self.txtLoadedValues.setObjectName(u"txtLoadedValues")
        self.txtLoadedValues.setMinimumSize(QSize(150, 350))
        self.txtLoadedValues.setMaximumSize(QSize(250, 350))
        self.txtLoadedValues.setStyleSheet(u"border: 1px solid #FAFAFA;")

        self.verticalLayout_40.addWidget(self.txtLoadedValues)


        self.horizontalLayout_21.addLayout(self.verticalLayout_40)

        self.horizontalSpacer_21 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.labelVersion_42 = QLabel(self.analyze)
        self.labelVersion_42.setObjectName(u"labelVersion_42")
        self.labelVersion_42.setMaximumSize(QSize(200, 20))
        self.labelVersion_42.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_42.setLineWidth(1)
        self.labelVersion_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_41.addWidget(self.labelVersion_42)

        self.txtParametersResult = QPlainTextEdit(self.analyze)
        self.txtParametersResult.setObjectName(u"txtParametersResult")
        self.txtParametersResult.setMinimumSize(QSize(0, 350))
        self.txtParametersResult.setMaximumSize(QSize(16777215, 350))
        self.txtParametersResult.setStyleSheet(u"border: 1px solid #FAFAFA;")

        self.verticalLayout_41.addWidget(self.txtParametersResult)

        self.CleanResultsButton = QPushButton(self.analyze)
        self.CleanResultsButton.setObjectName(u"CleanResultsButton")
        self.CleanResultsButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u"images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CleanResultsButton.setIcon(icon7)

        self.verticalLayout_41.addWidget(self.CleanResultsButton)


        self.horizontalLayout_21.addLayout(self.verticalLayout_41)


        self.verticalLayout_22.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.labelVersion_43 = QLabel(self.analyze)
        self.labelVersion_43.setObjectName(u"labelVersion_43")
        self.labelVersion_43.setMaximumSize(QSize(200, 20))
        self.labelVersion_43.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_43.setLineWidth(1)
        self.labelVersion_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_42.addWidget(self.labelVersion_43)

        self.txtLoadedValues_7 = QPlainTextEdit(self.analyze)
        self.txtLoadedValues_7.setObjectName(u"txtLoadedValues_7")
        self.txtLoadedValues_7.setMinimumSize(QSize(520, 0))
        self.txtLoadedValues_7.setMaximumSize(QSize(520, 16777215))
        self.txtLoadedValues_7.setStyleSheet(u"border: 1px solid #FAFAFA;")

        self.verticalLayout_42.addWidget(self.txtLoadedValues_7)


        self.horizontalLayout_10.addLayout(self.verticalLayout_42)

        self.horizontalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_22)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.labelVersion_44 = QLabel(self.analyze)
        self.labelVersion_44.setObjectName(u"labelVersion_44")
        self.labelVersion_44.setMaximumSize(QSize(200, 20))
        self.labelVersion_44.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_44.setLineWidth(1)
        self.labelVersion_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_43.addWidget(self.labelVersion_44)

        self.txtLoadedValues_8 = QPlainTextEdit(self.analyze)
        self.txtLoadedValues_8.setObjectName(u"txtLoadedValues_8")
        self.txtLoadedValues_8.setMinimumSize(QSize(0, 0))
        self.txtLoadedValues_8.setMaximumSize(QSize(16777215, 16777215))
        self.txtLoadedValues_8.setStyleSheet(u"border: 1px solid #FAFAFA;")

        self.verticalLayout_43.addWidget(self.txtLoadedValues_8)


        self.horizontalLayout_10.addLayout(self.verticalLayout_43)


        self.verticalLayout_22.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.analyze)
        self.page_results = QWidget()
        self.page_results.setObjectName(u"page_results")
        self.plot_widget = PlotWidget(self.page_results)
        self.plot_widget.setObjectName(u"plot_widget")
        self.plot_widget.setGeometry(QRect(0, 0, 1291, 771))
        self.gridLayout_4 = QGridLayout(self.plot_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.graph_Waveform = QGraphicsView(self.plot_widget)
        self.graph_Waveform.setObjectName(u"graph_Waveform")
        self.graph_Waveform.setMaximumSize(QSize(16777, 16777))

        self.gridLayout_3.addWidget(self.graph_Waveform, 1, 0, 1, 1)

        self.WaveformLabel = QLabel(self.plot_widget)
        self.WaveformLabel.setObjectName(u"WaveformLabel")
        self.WaveformLabel.setStyleSheet(u"font: 10pt \"absender\";\n"
"font: 81 11pt \"Montserrat ExtraBold\";")

        self.gridLayout_3.addWidget(self.WaveformLabel, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 1, 1, 1)

        self.histogram = MplWidget(self.page_results)
        self.histogram.setObjectName(u"histogram")
        self.histogram.setGeometry(QRect(1170, 30, 151, 91))
        self.stackedWidget.addWidget(self.page_results)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.optionsESTEPA.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText("")
        self.titleLeftDescription.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.HomeWindow.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.AnalyzeButton.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.ConsultWindow.setText(QCoreApplication.translate("MainWindow", u"Consult", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Simulation Settings", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.Outliner.setText(QCoreApplication.translate("MainWindow", u"Outliner Removal Method:", None))
        self.OutlinerBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.OutlinerBox.setItemText(1, QCoreApplication.translate("MainWindow", u"F-spread", None))
        self.OutlinerBox.setItemText(2, QCoreApplication.translate("MainWindow", u"K-sigmas", None))

        self.Font.setText(QCoreApplication.translate("MainWindow", u"Font Size:", None))
        self.FontBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Small", None))
        self.FontBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Big", None))

        self.Performance.setText(QCoreApplication.translate("MainWindow", u"Performance Presentation:", None))
        self.PerformanceBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Number of Points", None))
        self.PerformanceBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Percentage", None))

        self.Wafer.setText(QCoreApplication.translate("MainWindow", u"Wafer Representation:", None))
        self.WaferBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Colors", None))
        self.WaferBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Gravity centers", None))
        self.WaferBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Letters", None))

        self.HistogramTextLabel.setText(QCoreApplication.translate("MainWindow", u"Histogram chunks", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Non-automatic limits", None))
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.DirectoryButton.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"ESTEPA", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.btn_ppg_3.setText(QCoreApplication.translate("MainWindow", u"Examples", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt; font-weight:700;\">WELCOME TO ESTEPA</span></p></body></html>", None))
        self.btn_ppg_4.setText(QCoreApplication.translate("MainWindow", u"Tutorials", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Search recent files...", None))
        self.btn_ppg_2.setText(QCoreApplication.translate("MainWindow", u"Start Analysis", None))
        self.btn_ppg_5.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"STATISTICS for the PARAMETRIC TEST", None))
        self.optLoadFiles.setText(QCoreApplication.translate("MainWindow", u"Load from files", None))
        self.optLoadBBDD.setText(QCoreApplication.translate("MainWindow", u"Load from BBDD", None))
        self.btnLoadFiles.setText(QCoreApplication.translate("MainWindow", u"Load from files", None))
        self.labelVersion_34.setText(QCoreApplication.translate("MainWindow", u"Load DATA file", None))
        self.btnOpenWafermapFile.setText("")
        self.txtDataFile.setText("")
        self.txtDataFile.setPlaceholderText("")
        self.txtWafermapFile.setText("")
        self.txtWafermapFile.setPlaceholderText("")
        self.btnOpenDataFile.setText("")
        self.labelVersion_35.setText(QCoreApplication.translate("MainWindow", u"Load WAFERMAP file", None))
        self.cmbParametersFile.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.cmbParametersFile.setItemText(1, QCoreApplication.translate("MainWindow", u"cmax(pF)", None))
        self.cmbParametersFile.setItemText(2, QCoreApplication.translate("MainWindow", u"cmin(pF)", None))
        self.cmbParametersFile.setItemText(3, QCoreApplication.translate("MainWindow", u"dox(A)", None))
        self.cmbParametersFile.setItemText(4, QCoreApplication.translate("MainWindow", u"Na(cm-3)", None))
        self.cmbParametersFile.setItemText(5, QCoreApplication.translate("MainWindow", u"Vfb(V)", None))
        self.cmbParametersFile.setItemText(6, QCoreApplication.translate("MainWindow", u"Nss(cm-2)", None))
        self.cmbParametersFile.setItemText(7, QCoreApplication.translate("MainWindow", u"Rs(ohms)", None))

        self.labelVersion_36.setText(QCoreApplication.translate("MainWindow", u"Select parameters", None))
        self.btnAnalyzeFiles.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.btnCorrelationFiles.setText(QCoreApplication.translate("MainWindow", u"Correlation", None))
        self.cmbWafers.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbWafers.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.labelVersion_37.setText(QCoreApplication.translate("MainWindow", u"Select technology", None))
        self.btnCorrelationBBDD.setText(QCoreApplication.translate("MainWindow", u"Correlation", None))
        self.cmbTechnology.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbTechnology.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.labelVersion_38.setText(QCoreApplication.translate("MainWindow", u"Select runs", None))
        self.cmbRuns.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbRuns.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.labelVersion_39.setText(QCoreApplication.translate("MainWindow", u"Select wafers", None))
        self.btnAnalyzeBBDD.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.labelVersion_40.setText(QCoreApplication.translate("MainWindow", u"Select parameters", None))
        self.cmbParametersBBDD.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbParametersBBDD.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.labelVersion_41.setText(QCoreApplication.translate("MainWindow", u"Data Values", None))
#if QT_CONFIG(tooltip)
        self.txtLoadedValues.setToolTip(QCoreApplication.translate("MainWindow", u"Data values", None))
#endif // QT_CONFIG(tooltip)
        self.txtLoadedValues.setPlainText(QCoreApplication.translate("MainWindow", u"0 0 325.00E-12\n"
"0 -1 320.45E-12", None))
        self.labelVersion_42.setText(QCoreApplication.translate("MainWindow", u"Parameters result", None))
#if QT_CONFIG(tooltip)
        self.txtParametersResult.setToolTip(QCoreApplication.translate("MainWindow", u"Results parameters", None))
#endif // QT_CONFIG(tooltip)
        self.txtParametersResult.setPlainText(QCoreApplication.translate("MainWindow", u"cmax(pF)\n"
"Mean\n"
"Median \n"
"Stdev\n"
"Points\n"
"\n"
"", None))
        self.CleanResultsButton.setText("")
        self.labelVersion_43.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
#if QT_CONFIG(tooltip)
        self.txtLoadedValues_7.setToolTip(QCoreApplication.translate("MainWindow", u"Histogram", None))
#endif // QT_CONFIG(tooltip)
        self.txtLoadedValues_7.setPlainText("")
        self.labelVersion_44.setText(QCoreApplication.translate("MainWindow", u"Wafermap", None))
#if QT_CONFIG(tooltip)
        self.txtLoadedValues_8.setToolTip(QCoreApplication.translate("MainWindow", u"Wafermap", None))
#endif // QT_CONFIG(tooltip)
        self.txtLoadedValues_8.setPlainText("")
        self.WaveformLabel.setText(QCoreApplication.translate("MainWindow", u"Waveform", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v7.1", None))
    # retranslateUi

