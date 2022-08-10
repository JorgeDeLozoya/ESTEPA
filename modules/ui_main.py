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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListView, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollBar,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget
from widgets import CheckableComboBox
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1436, 786)
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
        self.verticalLayout_17 = QVBoxLayout(self.topLogoInfo)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topLogo.sizePolicy().hasHeightForWidth())
        self.topLogo.setSizePolicy(sizePolicy)
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"image: url(:/images/images/images/PyDracula.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.topLogo)


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
        self.btn_page_home = QPushButton(self.topMenu)
        self.btn_page_home.setObjectName(u"btn_page_home")
        sizePolicy1.setHeightForWidth(self.btn_page_home.sizePolicy().hasHeightForWidth())
        self.btn_page_home.setSizePolicy(sizePolicy1)
        self.btn_page_home.setMinimumSize(QSize(0, 45))
        self.btn_page_home.setFont(font)
        self.btn_page_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_page_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-description.png);")

        self.verticalLayout_8.addWidget(self.btn_page_home)

        self.btn_page_estepa = QPushButton(self.topMenu)
        self.btn_page_estepa.setObjectName(u"btn_page_estepa")
        sizePolicy1.setHeightForWidth(self.btn_page_estepa.sizePolicy().hasHeightForWidth())
        self.btn_page_estepa.setSizePolicy(sizePolicy1)
        self.btn_page_estepa.setMinimumSize(QSize(0, 45))
        self.btn_page_estepa.setFont(font)
        self.btn_page_estepa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_estepa.setLayoutDirection(Qt.LeftToRight)
        self.btn_page_estepa.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-find-in-page.png);")

        self.verticalLayout_8.addWidget(self.btn_page_estepa)

        self.btn_page_consult = QPushButton(self.topMenu)
        self.btn_page_consult.setObjectName(u"btn_page_consult")
        sizePolicy1.setHeightForWidth(self.btn_page_consult.sizePolicy().hasHeightForWidth())
        self.btn_page_consult.setSizePolicy(sizePolicy1)
        self.btn_page_consult.setMinimumSize(QSize(0, 45))
        self.btn_page_consult.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_consult.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png)")

        self.verticalLayout_8.addWidget(self.btn_page_consult)

        self.btn_page_inbase = QPushButton(self.topMenu)
        self.btn_page_inbase.setObjectName(u"btn_page_inbase")
        self.btn_page_inbase.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_page_inbase.sizePolicy().hasHeightForWidth())
        self.btn_page_inbase.setSizePolicy(sizePolicy1)
        self.btn_page_inbase.setMinimumSize(QSize(0, 45))
        self.btn_page_inbase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_inbase.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cloud-upload.png);")

        self.verticalLayout_8.addWidget(self.btn_page_inbase)


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
        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 1, 1, 1)

        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)


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
        self.stackedWidget_configuration = QStackedWidget(self.extraTopMenu)
        self.stackedWidget_configuration.setObjectName(u"stackedWidget_configuration")
        self.stackedWidget_configuration.setStyleSheet(u"\n"
"background: transparent;\n"
"\n"
"")
        self.stackedWidget_configuration.setFrameShape(QFrame.NoFrame)
        self.configuration_measurements = QWidget()
        self.configuration_measurements.setObjectName(u"configuration_measurements")
        self.verticalLayout_config_meas = QVBoxLayout(self.configuration_measurements)
        self.verticalLayout_config_meas.setObjectName(u"verticalLayout_config_meas")
        self.stackedWidget_configuration.addWidget(self.configuration_measurements)
        self.configuration_estepa = QWidget()
        self.configuration_estepa.setObjectName(u"configuration_estepa")
        self.verticalLayout_config_estepa = QVBoxLayout(self.configuration_estepa)
        self.verticalLayout_config_estepa.setObjectName(u"verticalLayout_config_estepa")
        self.Outliner_2 = QLabel(self.configuration_estepa)
        self.Outliner_2.setObjectName(u"Outliner_2")
        self.Outliner_2.setMaximumSize(QSize(400, 20))
        self.Outliner_2.setStyleSheet(u"")

        self.verticalLayout_config_estepa.addWidget(self.Outliner_2)

        self.cmbOutlinerMethod = QComboBox(self.configuration_estepa)
        self.cmbOutlinerMethod.addItem("")
        self.cmbOutlinerMethod.addItem("")
        self.cmbOutlinerMethod.addItem("")
        self.cmbOutlinerMethod.setObjectName(u"cmbOutlinerMethod")
        self.cmbOutlinerMethod.setEditable(False)
        self.cmbOutlinerMethod.setMinimumContentsLength(0)

        self.verticalLayout_config_estepa.addWidget(self.cmbOutlinerMethod)

        self.chkNonAutomaticLimits = QCheckBox(self.configuration_estepa)
        self.chkNonAutomaticLimits.setObjectName(u"chkNonAutomaticLimits")

        self.verticalLayout_config_estepa.addWidget(self.chkNonAutomaticLimits)

        self.optionsNonAutomatic = QStackedWidget(self.configuration_estepa)
        self.optionsNonAutomatic.setObjectName(u"optionsNonAutomatic")
        self.optionsNonAutomatic.setMinimumSize(QSize(200, 20))
        self.optionsNonAutomatic.setMaximumSize(QSize(200, 100))
        self.config_Automatic = QWidget()
        self.config_Automatic.setObjectName(u"config_Automatic")
        self.optionsNonAutomatic.addWidget(self.config_Automatic)
        self.config_nonAutomatic = QWidget()
        self.config_nonAutomatic.setObjectName(u"config_nonAutomatic")
        self.verticalLayout_44 = QVBoxLayout(self.config_nonAutomatic)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.chkGetAutoLimits = QCheckBox(self.config_nonAutomatic)
        self.chkGetAutoLimits.setObjectName(u"chkGetAutoLimits")

        self.verticalLayout_44.addWidget(self.chkGetAutoLimits)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.labelVersion_55 = QLabel(self.config_nonAutomatic)
        self.labelVersion_55.setObjectName(u"labelVersion_55")
        self.labelVersion_55.setMaximumSize(QSize(200, 20))
        self.labelVersion_55.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_55.setLineWidth(1)
        self.labelVersion_55.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.labelVersion_55, 0, 1, 1, 1)

        self.labelVersion_56 = QLabel(self.config_nonAutomatic)
        self.labelVersion_56.setObjectName(u"labelVersion_56")
        self.labelVersion_56.setMaximumSize(QSize(200, 20))
        self.labelVersion_56.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_56.setLineWidth(1)
        self.labelVersion_56.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.labelVersion_56, 0, 0, 1, 1)

        self.txtLimitMin = QLineEdit(self.config_nonAutomatic)
        self.txtLimitMin.setObjectName(u"txtLimitMin")
        self.txtLimitMin.setEnabled(True)
        self.txtLimitMin.setMinimumSize(QSize(50, 30))
        self.txtLimitMin.setMaximumSize(QSize(50, 30))
        self.txtLimitMin.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_8.addWidget(self.txtLimitMin, 1, 0, 1, 1)

        self.txtLimitMax = QLineEdit(self.config_nonAutomatic)
        self.txtLimitMax.setObjectName(u"txtLimitMax")
        self.txtLimitMax.setEnabled(True)
        self.txtLimitMax.setMinimumSize(QSize(50, 30))
        self.txtLimitMax.setMaximumSize(QSize(50, 30))
        self.txtLimitMax.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_8.addWidget(self.txtLimitMax, 1, 1, 1, 1)


        self.verticalLayout_44.addLayout(self.gridLayout_8)

        self.optionsNonAutomatic.addWidget(self.config_nonAutomatic)

        self.verticalLayout_config_estepa.addWidget(self.optionsNonAutomatic)

        self.verticalSpacer_estepa = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_config_estepa.addItem(self.verticalSpacer_estepa)

        self.Font_2 = QLabel(self.configuration_estepa)
        self.Font_2.setObjectName(u"Font_2")
        self.Font_2.setMaximumSize(QSize(400, 16777215))
        self.Font_2.setStyleSheet(u"")

        self.verticalLayout_config_estepa.addWidget(self.Font_2)

        self.cmbFontSize = QComboBox(self.configuration_estepa)
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.setObjectName(u"cmbFontSize")
        self.cmbFontSize.setEditable(False)
        self.cmbFontSize.setMinimumContentsLength(0)

        self.verticalLayout_config_estepa.addWidget(self.cmbFontSize)

        self.Performance_2 = QLabel(self.configuration_estepa)
        self.Performance_2.setObjectName(u"Performance_2")
        self.Performance_2.setMaximumSize(QSize(400, 16777215))
        self.Performance_2.setStyleSheet(u"")

        self.verticalLayout_config_estepa.addWidget(self.Performance_2)

        self.cmbPerformancePresentation = QComboBox(self.configuration_estepa)
        self.cmbPerformancePresentation.addItem("")
        self.cmbPerformancePresentation.addItem("")
        self.cmbPerformancePresentation.setObjectName(u"cmbPerformancePresentation")
        self.cmbPerformancePresentation.setEditable(False)
        self.cmbPerformancePresentation.setMinimumContentsLength(0)

        self.verticalLayout_config_estepa.addWidget(self.cmbPerformancePresentation)

        self.Wafer_2 = QLabel(self.configuration_estepa)
        self.Wafer_2.setObjectName(u"Wafer_2")
        self.Wafer_2.setMaximumSize(QSize(400, 16777215))
        self.Wafer_2.setStyleSheet(u"")

        self.verticalLayout_config_estepa.addWidget(self.Wafer_2)

        self.cmbWaferRepresentation = QComboBox(self.configuration_estepa)
        self.cmbWaferRepresentation.addItem("")
        self.cmbWaferRepresentation.addItem("")
        self.cmbWaferRepresentation.addItem("")
        self.cmbWaferRepresentation.setObjectName(u"cmbWaferRepresentation")
        self.cmbWaferRepresentation.setEditable(False)
        self.cmbWaferRepresentation.setMinimumContentsLength(0)

        self.verticalLayout_config_estepa.addWidget(self.cmbWaferRepresentation)

        self.HistogramTextLabel = QLabel(self.configuration_estepa)
        self.HistogramTextLabel.setObjectName(u"HistogramTextLabel")

        self.verticalLayout_config_estepa.addWidget(self.HistogramTextLabel)

        self.scrollHistogramChunks = QScrollBar(self.configuration_estepa)
        self.scrollHistogramChunks.setObjectName(u"scrollHistogramChunks")
        self.scrollHistogramChunks.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\\n QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.scrollHistogramChunks.setMinimum(2)
        self.scrollHistogramChunks.setMaximum(21)
        self.scrollHistogramChunks.setSingleStep(1)
        self.scrollHistogramChunks.setValue(2)
        self.scrollHistogramChunks.setOrientation(Qt.Horizontal)

        self.verticalLayout_config_estepa.addWidget(self.scrollHistogramChunks)

        self.txtHistogramChunks = QLineEdit(self.configuration_estepa)
        self.txtHistogramChunks.setObjectName(u"txtHistogramChunks")
        self.txtHistogramChunks.setEnabled(False)
        self.txtHistogramChunks.setMinimumSize(QSize(100, 30))
        self.txtHistogramChunks.setMaximumSize(QSize(100, 30))
        self.txtHistogramChunks.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_config_estepa.addWidget(self.txtHistogramChunks)

        self.stackedWidget_configuration.addWidget(self.configuration_estepa)

        self.verticalLayout_11.addWidget(self.stackedWidget_configuration)


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
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setStyleSheet(u"font: 75 14pt \"Microsoft JhengHei\";")
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
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font2)
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
        self.Home_Window = QWidget()
        self.Home_Window.setObjectName(u"Home_Window")
        self.Home_Window.setStyleSheet(u"")
        self.formLayoutWidget_3 = QWidget(self.Home_Window)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(120, 40, 1111, 669))
        self.formLayout = QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.Home_Layout = QFormLayout()
        self.Home_Layout.setObjectName(u"Home_Layout")
        self.label_2 = QLabel(self.formLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(300, 85))
        self.label_2.setStyleSheet(u"font: 30pt \"Microsoft JhengHei\";\n"
"")

        self.Home_Layout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.home_analysis = QPushButton(self.formLayoutWidget_3)
        self.home_analysis.setObjectName(u"home_analysis")
        self.home_analysis.setMinimumSize(QSize(102, 30))
        self.home_analysis.setMaximumSize(QSize(20, 10))
        self.home_analysis.setFont(font)
        self.home_analysis.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_analysis.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        self.home_analysis.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))
        icon4 = QIcon()
        icon4.addFile(u"../../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/images/icons/cil-find-in-page.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_analysis.setIcon(icon4)

        self.Home_Layout.setWidget(2, QFormLayout.LabelRole, self.home_analysis)

        self.home_consult = QPushButton(self.formLayoutWidget_3)
        self.home_consult.setObjectName(u"home_consult")
        self.home_consult.setMinimumSize(QSize(68, 30))
        self.home_consult.setMaximumSize(QSize(16, 10))
        self.home_consult.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_consult.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon5 = QIcon()
        icon5.addFile(u"../../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_consult.setIcon(icon5)

        self.Home_Layout.setWidget(3, QFormLayout.LabelRole, self.home_consult)

        self.home_upload = QPushButton(self.formLayoutWidget_3)
        self.home_upload.setObjectName(u"home_upload")
        self.home_upload.setMinimumSize(QSize(150, 30))
        self.home_upload.setMaximumSize(QSize(20, 10))
        self.home_upload.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_upload.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon6 = QIcon()
        icon6.addFile(u"../../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/images/icons/cil-cloud-upload.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_upload.setIcon(icon6)

        self.Home_Layout.setWidget(4, QFormLayout.LabelRole, self.home_upload)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Home_Layout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.horizontalSpacer_2 = QSpacerItem(264, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Home_Layout.setItem(1, QFormLayout.FieldRole, self.horizontalSpacer_2)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.Home_Layout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_4 = QSpacerItem(30, 68, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_4)

        self.label_6 = QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(280, 280))
        self.label_6.setMaximumSize(QSize(300, 264))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"image: url(:/images/images/images/PyDracula_vertical.png);")
        self.label_6.setLineWidth(0)
        self.label_6.setPixmap(QPixmap(u"images/images/Estepa.png"))
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(False)

        self.verticalLayout_18.addWidget(self.label_6)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_11)


        self.horizontalLayout_6.addLayout(self.verticalLayout_18)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.formLayoutWidget_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(274, 0))
        self.label.setMaximumSize(QSize(345, 94))
        self.label.setStyleSheet(u"font: 25 36pt \"Microsoft JhengHei Light\";")

        self.verticalLayout_16.addWidget(self.label)

        self.label_5 = QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMinimumSize(QSize(351, 14))
        self.label_5.setMaximumSize(QSize(330, 100))
        self.label_5.setStyleSheet(u"font: 75 72pt \"Microsoft JhengHei\";")

        self.verticalLayout_16.addWidget(self.label_5)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_10)


        self.horizontalLayout_6.addLayout(self.verticalLayout_16)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(1, QFormLayout.LabelRole, self.verticalSpacer_6)

        self.Options_Layout = QFormLayout()
        self.Options_Layout.setObjectName(u"Options_Layout")
        self.label_3 = QLabel(self.formLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 12))
        self.label_3.setMaximumSize(QSize(300, 85))
        self.label_3.setStyleSheet(u"font: 30pt \"Microsoft JhengHei\";\n"
"")

        self.Options_Layout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.btn_ppg_9 = QPushButton(self.formLayoutWidget_3)
        self.btn_ppg_9.setObjectName(u"btn_ppg_9")
        self.btn_ppg_9.setMinimumSize(QSize(82, 30))
        self.btn_ppg_9.setMaximumSize(QSize(20, 10))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.btn_ppg_9.setFont(font3)
        self.btn_ppg_9.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon7 = QIcon()
        icon7.addFile(u"../../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/images/icons/cil-wallet.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_ppg_9.setIcon(icon7)

        self.Options_Layout.setWidget(3, QFormLayout.LabelRole, self.btn_ppg_9)

        self.btn_ppg_6 = QPushButton(self.formLayoutWidget_3)
        self.btn_ppg_6.setObjectName(u"btn_ppg_6")
        self.btn_ppg_6.setMinimumSize(QSize(114, 30))
        self.btn_ppg_6.setMaximumSize(QSize(20, 10))
        self.btn_ppg_6.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon8 = QIcon()
        icon8.addFile(u"../../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_ppg_6.setIcon(icon8)

        self.Options_Layout.setWidget(5, QFormLayout.LabelRole, self.btn_ppg_6)

        self.btn_ppg_7 = QPushButton(self.formLayoutWidget_3)
        self.btn_ppg_7.setObjectName(u"btn_ppg_7")
        self.btn_ppg_7.setMinimumSize(QSize(81, 30))
        self.btn_ppg_7.setMaximumSize(QSize(20, 10))
        self.btn_ppg_7.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon9 = QIcon()
        icon9.addFile(u"../../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icons/images/icons/cil-notes.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_ppg_7.setIcon(icon9)

        self.Options_Layout.setWidget(6, QFormLayout.LabelRole, self.btn_ppg_7)

        self.btn_ppg_8 = QPushButton(self.formLayoutWidget_3)
        self.btn_ppg_8.setObjectName(u"btn_ppg_8")
        self.btn_ppg_8.setMinimumSize(QSize(57, 30))
        self.btn_ppg_8.setMaximumSize(QSize(20, 10))
        self.btn_ppg_8.setContextMenuPolicy(Qt.NoContextMenu)
        self.btn_ppg_8.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon10 = QIcon()
        icon10.addFile(u"../../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_ppg_8.setIcon(icon10)

        self.Options_Layout.setWidget(2, QFormLayout.LabelRole, self.btn_ppg_8)

        self.horizontalSpacer_9 = QSpacerItem(300, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Options_Layout.setItem(0, QFormLayout.FieldRole, self.horizontalSpacer_9)


        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.Options_Layout)

        self.horizontalSpacer_8 = QSpacerItem(800, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.horizontalSpacer_8)

        self.stackedWidget.addWidget(self.Home_Window)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.stackedWidget.addWidget(self.widgets)
        self.estepa = QWidget()
        self.estepa.setObjectName(u"estepa")
        self.verticalLayout = QVBoxLayout(self.estepa)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(self.estepa)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 20))
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.optLoadFiles = QRadioButton(self.estepa)
        self.optLoadFiles.setObjectName(u"optLoadFiles")
        self.optLoadFiles.setMinimumSize(QSize(130, 0))
        self.optLoadFiles.setMaximumSize(QSize(150, 16777215))
        self.optLoadFiles.setChecked(True)

        self.gridLayout_15.addWidget(self.optLoadFiles, 0, 0, 1, 1)

        self.optLoadBBDD = QRadioButton(self.estepa)
        self.optLoadBBDD.setObjectName(u"optLoadBBDD")
        self.optLoadBBDD.setMinimumSize(QSize(130, 0))
        self.optLoadBBDD.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_15.addWidget(self.optLoadBBDD, 0, 1, 1, 1)


        self.horizontalLayout_18.addLayout(self.gridLayout_15)


        self.verticalLayout_31.addLayout(self.horizontalLayout_18)

        self.horizontalSpacer = QSpacerItem(427, 4, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_31.addItem(self.horizontalSpacer)

        self.optionsESTEPA = QStackedWidget(self.estepa)
        self.optionsESTEPA.setObjectName(u"optionsESTEPA")
        self.optionsESTEPA.setMinimumSize(QSize(420, 310))
        self.optionsESTEPA.setMaximumSize(QSize(420, 310))
        self.files = QWidget()
        self.files.setObjectName(u"files")
        self.gridLayoutWidget_4 = QWidget(self.files)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 371, 191))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btnOpenDataFile = QPushButton(self.gridLayoutWidget_4)
        self.btnOpenDataFile.setObjectName(u"btnOpenDataFile")
        self.btnOpenDataFile.setMinimumSize(QSize(50, 30))
        self.btnOpenDataFile.setMaximumSize(QSize(50, 30))
        self.btnOpenDataFile.setFont(font)
        self.btnOpenDataFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOpenDataFile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnOpenDataFile.setIcon(icon11)

        self.gridLayout_13.addWidget(self.btnOpenDataFile, 1, 1, 1, 1)

        self.btnOpenWafermapFile = QPushButton(self.gridLayoutWidget_4)
        self.btnOpenWafermapFile.setObjectName(u"btnOpenWafermapFile")
        self.btnOpenWafermapFile.setMinimumSize(QSize(40, 30))
        self.btnOpenWafermapFile.setMaximumSize(QSize(16777215, 30))
        self.btnOpenWafermapFile.setFont(font)
        self.btnOpenWafermapFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOpenWafermapFile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnOpenWafermapFile.setIcon(icon11)

        self.gridLayout_13.addWidget(self.btnOpenWafermapFile, 3, 1, 1, 1)

        self.labelVersion_13 = QLabel(self.gridLayoutWidget_4)
        self.labelVersion_13.setObjectName(u"labelVersion_13")
        self.labelVersion_13.setMaximumSize(QSize(200, 20))
        self.labelVersion_13.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_13.setLineWidth(1)
        self.labelVersion_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.labelVersion_13, 0, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_13.addItem(self.verticalSpacer_16, 5, 0, 1, 1)

        self.txtWafermapFile = QLineEdit(self.gridLayoutWidget_4)
        self.txtWafermapFile.setObjectName(u"txtWafermapFile")
        self.txtWafermapFile.setEnabled(False)
        self.txtWafermapFile.setMinimumSize(QSize(100, 30))
        self.txtWafermapFile.setMaximumSize(QSize(300, 30))
        self.txtWafermapFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_13.addWidget(self.txtWafermapFile, 3, 0, 1, 1)

        self.txtDataFile = QLineEdit(self.gridLayoutWidget_4)
        self.txtDataFile.setObjectName(u"txtDataFile")
        self.txtDataFile.setEnabled(False)
        self.txtDataFile.setMinimumSize(QSize(100, 30))
        self.txtDataFile.setMaximumSize(QSize(300, 30))
        self.txtDataFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_13.addWidget(self.txtDataFile, 1, 0, 1, 1)

        self.btnLoadFiles = QPushButton(self.gridLayoutWidget_4)
        self.btnLoadFiles.setObjectName(u"btnLoadFiles")
        self.btnLoadFiles.setMinimumSize(QSize(100, 30))
        self.btnLoadFiles.setMaximumSize(QSize(300, 16777215))
        self.btnLoadFiles.setFont(font)
        self.btnLoadFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLoadFiles.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLoadFiles.setIcon(icon12)

        self.gridLayout_13.addWidget(self.btnLoadFiles, 4, 0, 1, 1)

        self.labelVersion_14 = QLabel(self.gridLayoutWidget_4)
        self.labelVersion_14.setObjectName(u"labelVersion_14")
        self.labelVersion_14.setMaximumSize(QSize(200, 20))
        self.labelVersion_14.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_14.setLineWidth(1)
        self.labelVersion_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.labelVersion_14, 2, 0, 1, 1)

        self.gridLayoutWidget = QWidget(self.files)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(11, 200, 371, 101))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnCorrelationFiles = QPushButton(self.gridLayoutWidget)
        self.btnCorrelationFiles.setObjectName(u"btnCorrelationFiles")
        self.btnCorrelationFiles.setMinimumSize(QSize(120, 30))
        self.btnCorrelationFiles.setMaximumSize(QSize(120, 16777215))
        self.btnCorrelationFiles.setFont(font)
        self.btnCorrelationFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCorrelationFiles.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnCorrelationFiles.setIcon(icon12)

        self.gridLayout_2.addWidget(self.btnCorrelationFiles, 2, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 5, 1, 1)

        self.btnAnalyzeFiles = QPushButton(self.gridLayoutWidget)
        self.btnAnalyzeFiles.setObjectName(u"btnAnalyzeFiles")
        self.btnAnalyzeFiles.setMinimumSize(QSize(120, 30))
        self.btnAnalyzeFiles.setMaximumSize(QSize(120, 16777215))
        self.btnAnalyzeFiles.setFont(font)
        self.btnAnalyzeFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnalyzeFiles.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnAnalyzeFiles.setIcon(icon12)

        self.gridLayout_2.addWidget(self.btnAnalyzeFiles, 2, 1, 1, 1)

        self.cmbParametersFile = CheckableComboBox(self.gridLayoutWidget)
        self.cmbParametersFile.addItem("")
        self.cmbParametersFile.setObjectName(u"cmbParametersFile")
        self.cmbParametersFile.setEnabled(True)
        self.cmbParametersFile.setMinimumSize(QSize(100, 0))
        self.cmbParametersFile.setMaximumSize(QSize(300, 16777215))
        self.cmbParametersFile.setFont(font)
        self.cmbParametersFile.setAutoFillBackground(False)
        self.cmbParametersFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbParametersFile.setEditable(True)
        self.cmbParametersFile.setCurrentText(u"Select instrument")
        self.cmbParametersFile.setIconSize(QSize(16, 16))
        self.cmbParametersFile.setFrame(True)

        self.gridLayout_2.addWidget(self.cmbParametersFile, 1, 1, 1, 5)

        self.labelVersion_19 = QLabel(self.gridLayoutWidget)
        self.labelVersion_19.setObjectName(u"labelVersion_19")
        self.labelVersion_19.setMaximumSize(QSize(200, 20))
        self.labelVersion_19.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_19.setLineWidth(1)
        self.labelVersion_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelVersion_19, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 2, 3, 1, 1)

        self.optionsESTEPA.addWidget(self.files)
        self.bbdd = QWidget()
        self.bbdd.setObjectName(u"bbdd")
        self.gridLayoutWidget_9 = QWidget(self.bbdd)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(10, 10, 471, 298))
        self.gridLayout_16 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.cmbWafers = QComboBox(self.gridLayoutWidget_9)
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

        self.gridLayout_16.addWidget(self.cmbWafers, 5, 0, 1, 1)

        self.labelVersion_15 = QLabel(self.gridLayoutWidget_9)
        self.labelVersion_15.setObjectName(u"labelVersion_15")
        self.labelVersion_15.setMaximumSize(QSize(200, 20))
        self.labelVersion_15.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_15.setLineWidth(1)
        self.labelVersion_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.labelVersion_15, 0, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_16.addItem(self.verticalSpacer_12, 9, 0, 1, 1)

        self.btnCorrelationBBDD = QPushButton(self.gridLayoutWidget_9)
        self.btnCorrelationBBDD.setObjectName(u"btnCorrelationBBDD")
        self.btnCorrelationBBDD.setMinimumSize(QSize(120, 30))
        self.btnCorrelationBBDD.setMaximumSize(QSize(120, 30))
        self.btnCorrelationBBDD.setFont(font)
        self.btnCorrelationBBDD.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCorrelationBBDD.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnCorrelationBBDD.setIcon(icon12)

        self.gridLayout_16.addWidget(self.btnCorrelationBBDD, 11, 1, 1, 1)

        self.cmbTechnology = QComboBox(self.gridLayoutWidget_9)
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

        self.gridLayout_16.addWidget(self.cmbTechnology, 1, 0, 1, 1)

        self.labelVersion_17 = QLabel(self.gridLayoutWidget_9)
        self.labelVersion_17.setObjectName(u"labelVersion_17")
        self.labelVersion_17.setMaximumSize(QSize(200, 20))
        self.labelVersion_17.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_17.setLineWidth(1)
        self.labelVersion_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.labelVersion_17, 2, 0, 1, 1)

        self.cmbRuns = QComboBox(self.gridLayoutWidget_9)
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

        self.gridLayout_16.addWidget(self.cmbRuns, 3, 0, 1, 1)

        self.labelVersion_16 = QLabel(self.gridLayoutWidget_9)
        self.labelVersion_16.setObjectName(u"labelVersion_16")
        self.labelVersion_16.setMaximumSize(QSize(200, 20))
        self.labelVersion_16.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_16.setLineWidth(1)
        self.labelVersion_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.labelVersion_16, 4, 0, 1, 1)

        self.btnAnalyzeBBDD = QPushButton(self.gridLayoutWidget_9)
        self.btnAnalyzeBBDD.setObjectName(u"btnAnalyzeBBDD")
        self.btnAnalyzeBBDD.setMinimumSize(QSize(120, 0))
        self.btnAnalyzeBBDD.setMaximumSize(QSize(120, 30))
        self.btnAnalyzeBBDD.setFont(font)
        self.btnAnalyzeBBDD.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnalyzeBBDD.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnAnalyzeBBDD.setIcon(icon12)

        self.gridLayout_16.addWidget(self.btnAnalyzeBBDD, 11, 0, 1, 1)

        self.labelVersion_18 = QLabel(self.gridLayoutWidget_9)
        self.labelVersion_18.setObjectName(u"labelVersion_18")
        self.labelVersion_18.setMaximumSize(QSize(200, 20))
        self.labelVersion_18.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_18.setLineWidth(1)
        self.labelVersion_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.labelVersion_18, 6, 0, 1, 1)

        self.cmbParametersBBDD = CheckableComboBox(self.gridLayoutWidget_9)
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

        self.gridLayout_16.addWidget(self.cmbParametersBBDD, 8, 0, 1, 1)

        self.optionsESTEPA.addWidget(self.bbdd)

        self.verticalLayout_31.addWidget(self.optionsESTEPA)


        self.horizontalLayout_13.addLayout(self.verticalLayout_31)

        self.horizontalSpacer_18 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.labelVersion_20 = QLabel(self.estepa)
        self.labelVersion_20.setObjectName(u"labelVersion_20")
        self.labelVersion_20.setMinimumSize(QSize(100, 0))
        self.labelVersion_20.setMaximumSize(QSize(100, 20))
        self.labelVersion_20.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_20.setLineWidth(1)
        self.labelVersion_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.labelVersion_20)

        self.horizontalSpacer_19 = QSpacerItem(24, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_19)

        self.btnSaveDescription_2 = QPushButton(self.estepa)
        self.btnSaveDescription_2.setObjectName(u"btnSaveDescription_2")
        self.btnSaveDescription_2.setEnabled(True)
        self.btnSaveDescription_2.setMinimumSize(QSize(30, 30))
        self.btnSaveDescription_2.setMaximumSize(QSize(30, 16777215))
        self.btnSaveDescription_2.setFont(font)
        self.btnSaveDescription_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSaveDescription_2.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSaveDescription_2.setIcon(icon13)
        self.btnSaveDescription_2.setFlat(False)

        self.horizontalLayout_10.addWidget(self.btnSaveDescription_2)

        self.btnCopyDescription_2 = QPushButton(self.estepa)
        self.btnCopyDescription_2.setObjectName(u"btnCopyDescription_2")
        self.btnCopyDescription_2.setMinimumSize(QSize(30, 30))
        self.btnCopyDescription_2.setMaximumSize(QSize(30, 16777215))
        self.btnCopyDescription_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCopyDescription_2.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"images/icons/cil-clone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCopyDescription_2.setIcon(icon14)

        self.horizontalLayout_10.addWidget(self.btnCopyDescription_2)

        self.btnClearDescription_2 = QPushButton(self.estepa)
        self.btnClearDescription_2.setObjectName(u"btnClearDescription_2")
        self.btnClearDescription_2.setEnabled(True)
        self.btnClearDescription_2.setMinimumSize(QSize(30, 30))
        self.btnClearDescription_2.setMaximumSize(QSize(30, 16777215))
        self.btnClearDescription_2.setFont(font)
        self.btnClearDescription_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClearDescription_2.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClearDescription_2.setIcon(icon15)
        self.btnClearDescription_2.setFlat(False)

        self.horizontalLayout_10.addWidget(self.btnClearDescription_2)


        self.verticalLayout_29.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.txtCurrentParameter = QLineEdit(self.estepa)
        self.txtCurrentParameter.setObjectName(u"txtCurrentParameter")
        self.txtCurrentParameter.setEnabled(True)
        self.txtCurrentParameter.setMinimumSize(QSize(82, 30))
        self.txtCurrentParameter.setMaximumSize(QSize(120, 30))
        self.txtCurrentParameter.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_15.addWidget(self.txtCurrentParameter)

        self.pushButton = QPushButton(self.estepa)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        self.pushButton.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/cil-chevron-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon16)

        self.horizontalLayout_15.addWidget(self.pushButton)

        self.horizontalSpacer_5 = QSpacerItem(21, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.verticalLayout_29.addLayout(self.horizontalLayout_15)

        self.txtLoadedValues = QPlainTextEdit(self.estepa)
        self.txtLoadedValues.setObjectName(u"txtLoadedValues")
        self.txtLoadedValues.setMinimumSize(QSize(260, 350))
        self.txtLoadedValues.setMaximumSize(QSize(400, 350))
        self.txtLoadedValues.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_29.addWidget(self.txtLoadedValues)


        self.horizontalLayout_13.addLayout(self.verticalLayout_29)

        self.horizontalSpacer_15 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelVersion_21 = QLabel(self.estepa)
        self.labelVersion_21.setObjectName(u"labelVersion_21")
        self.labelVersion_21.setMaximumSize(QSize(200, 20))
        self.labelVersion_21.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_21.setLineWidth(1)
        self.labelVersion_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.labelVersion_21)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_17)

        self.btnSaveDescription_3 = QPushButton(self.estepa)
        self.btnSaveDescription_3.setObjectName(u"btnSaveDescription_3")
        self.btnSaveDescription_3.setEnabled(True)
        self.btnSaveDescription_3.setMinimumSize(QSize(30, 30))
        self.btnSaveDescription_3.setMaximumSize(QSize(30, 16777215))
        self.btnSaveDescription_3.setFont(font)
        self.btnSaveDescription_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSaveDescription_3.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnSaveDescription_3.setIcon(icon13)
        self.btnSaveDescription_3.setFlat(False)

        self.horizontalLayout_7.addWidget(self.btnSaveDescription_3)

        self.btnCopyDescription_3 = QPushButton(self.estepa)
        self.btnCopyDescription_3.setObjectName(u"btnCopyDescription_3")
        self.btnCopyDescription_3.setMinimumSize(QSize(30, 30))
        self.btnCopyDescription_3.setMaximumSize(QSize(30, 16777215))
        self.btnCopyDescription_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCopyDescription_3.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnCopyDescription_3.setIcon(icon14)

        self.horizontalLayout_7.addWidget(self.btnCopyDescription_3)

        self.btnClearDescription_3 = QPushButton(self.estepa)
        self.btnClearDescription_3.setObjectName(u"btnClearDescription_3")
        self.btnClearDescription_3.setEnabled(True)
        self.btnClearDescription_3.setMinimumSize(QSize(30, 30))
        self.btnClearDescription_3.setMaximumSize(QSize(30, 16777215))
        self.btnClearDescription_3.setFont(font)
        self.btnClearDescription_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClearDescription_3.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnClearDescription_3.setIcon(icon15)
        self.btnClearDescription_3.setFlat(False)

        self.horizontalLayout_7.addWidget(self.btnClearDescription_3)


        self.verticalLayout_30.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_7 = QSpacerItem(15, 24, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_30.addItem(self.verticalSpacer_7)

        self.txtParametersResult = QPlainTextEdit(self.estepa)
        self.txtParametersResult.setObjectName(u"txtParametersResult")
        self.txtParametersResult.setMinimumSize(QSize(0, 350))
        self.txtParametersResult.setMaximumSize(QSize(16777215, 350))
        self.txtParametersResult.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_30.addWidget(self.txtParametersResult)


        self.horizontalLayout_13.addLayout(self.verticalLayout_30)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.labelVersion_22 = QLabel(self.estepa)
        self.labelVersion_22.setObjectName(u"labelVersion_22")
        self.labelVersion_22.setMinimumSize(QSize(75, 0))
        self.labelVersion_22.setMaximumSize(QSize(75, 20))
        self.labelVersion_22.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_22.setLineWidth(1)
        self.labelVersion_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.labelVersion_22)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)

        self.btnClearDescription_4 = QPushButton(self.estepa)
        self.btnClearDescription_4.setObjectName(u"btnClearDescription_4")
        self.btnClearDescription_4.setEnabled(True)
        self.btnClearDescription_4.setMinimumSize(QSize(30, 30))
        self.btnClearDescription_4.setMaximumSize(QSize(30, 16777215))
        self.btnClearDescription_4.setFont(font)
        self.btnClearDescription_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClearDescription_4.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnClearDescription_4.setIcon(icon15)
        self.btnClearDescription_4.setFlat(False)

        self.horizontalLayout_20.addWidget(self.btnClearDescription_4)


        self.verticalLayout_32.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_histogram = QHBoxLayout()
        self.horizontalLayout_histogram.setObjectName(u"horizontalLayout_histogram")
        self.horizontalSpacer_histogram = QSpacerItem(40, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_histogram.addItem(self.horizontalSpacer_histogram)

        self.verticalLayout_histogram = QVBoxLayout()
        self.verticalLayout_histogram.setObjectName(u"verticalLayout_histogram")

        self.horizontalLayout_histogram.addLayout(self.verticalLayout_histogram)


        self.verticalLayout_32.addLayout(self.horizontalLayout_histogram)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer)


        self.horizontalLayout_8.addLayout(self.verticalLayout_32)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.labelVersion_23 = QLabel(self.estepa)
        self.labelVersion_23.setObjectName(u"labelVersion_23")
        self.labelVersion_23.setMaximumSize(QSize(200, 20))
        self.labelVersion_23.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_23.setLineWidth(1)
        self.labelVersion_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.labelVersion_23)

        self.horizontalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_21)

        self.btnSaveDescription_5 = QPushButton(self.estepa)
        self.btnSaveDescription_5.setObjectName(u"btnSaveDescription_5")
        self.btnSaveDescription_5.setEnabled(True)
        self.btnSaveDescription_5.setMinimumSize(QSize(30, 30))
        self.btnSaveDescription_5.setMaximumSize(QSize(30, 16777215))
        self.btnSaveDescription_5.setFont(font)
        self.btnSaveDescription_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSaveDescription_5.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnSaveDescription_5.setIcon(icon13)
        self.btnSaveDescription_5.setFlat(False)

        self.horizontalLayout_11.addWidget(self.btnSaveDescription_5)

        self.btnClearDescription_5 = QPushButton(self.estepa)
        self.btnClearDescription_5.setObjectName(u"btnClearDescription_5")
        self.btnClearDescription_5.setEnabled(True)
        self.btnClearDescription_5.setMinimumSize(QSize(30, 30))
        self.btnClearDescription_5.setMaximumSize(QSize(30, 16777215))
        self.btnClearDescription_5.setFont(font)
        self.btnClearDescription_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClearDescription_5.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnClearDescription_5.setIcon(icon15)
        self.btnClearDescription_5.setFlat(False)

        self.horizontalLayout_11.addWidget(self.btnClearDescription_5)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_11)


        self.verticalLayout_33.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_wafermap = QSpacerItem(40, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_wafermap)

        self.verticalLayout_wafermap = QVBoxLayout()
        self.verticalLayout_wafermap.setObjectName(u"verticalLayout_wafermap")

        self.horizontalLayout_12.addLayout(self.verticalLayout_wafermap)


        self.verticalLayout_33.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_33)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.estepa)
        self.consult_estepa = QWidget()
        self.consult_estepa.setObjectName(u"consult_estepa")
        self.label_13 = QLabel(self.consult_estepa)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 1390, 20))
        self.label_13.setMinimumSize(QSize(0, 20))
        self.label_13.setMaximumSize(QSize(16777215, 20))
        self.label_13.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.layoutWidget = QWidget(self.consult_estepa)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 1311, 441))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setVerticalSpacing(6)
        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_11, 0, 1, 1, 1)

        self.optWafers = QRadioButton(self.layoutWidget)
        self.optWafers.setObjectName(u"optWafers")
        self.optWafers.setMinimumSize(QSize(130, 0))
        self.optWafers.setMaximumSize(QSize(150, 16777215))
        self.optWafers.setChecked(True)

        self.gridLayout_17.addWidget(self.optWafers, 0, 0, 1, 1)

        self.historicalcheck = QCheckBox(self.layoutWidget)
        self.historicalcheck.setObjectName(u"historicalcheck")

        self.gridLayout_17.addWidget(self.historicalcheck, 0, 2, 1, 1)

        self.optRuns = QRadioButton(self.layoutWidget)
        self.optRuns.setObjectName(u"optRuns")
        self.optRuns.setMinimumSize(QSize(130, 0))
        self.optRuns.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_17.addWidget(self.optRuns, 1, 0, 1, 1)

        self.optionsHistorical = QStackedWidget(self.layoutWidget)
        self.optionsHistorical.setObjectName(u"optionsHistorical")
        self.optionsHistorical.setMinimumSize(QSize(300, 50))
        self.optionsHistorical.setMaximumSize(QSize(300, 50))
        self.YesHistorical = QWidget()
        self.YesHistorical.setObjectName(u"YesHistorical")
        self.gridLayoutWidget_3 = QWidget(self.YesHistorical)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(-1, 9, 271, 31))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.btnValues = QRadioButton(self.gridLayoutWidget_3)
        self.btnValues.setObjectName(u"btnValues")
        self.btnValues.setMinimumSize(QSize(70, 0))
        self.btnValues.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.btnValues, 0, 0, 1, 1)

        self.btnYield = QRadioButton(self.gridLayoutWidget_3)
        self.btnYield.setObjectName(u"btnYield")
        self.btnYield.setMaximumSize(QSize(143, 16777215))

        self.gridLayout.addWidget(self.btnYield, 0, 2, 1, 1)

        self.optionsHistorical.addWidget(self.YesHistorical)
        self.NoHistorical = QWidget()
        self.NoHistorical.setObjectName(u"NoHistorical")
        self.gridLayoutWidget_10 = QWidget(self.NoHistorical)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(0, 10, 421, 31))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.optionsHistorical.addWidget(self.NoHistorical)

        self.gridLayout_17.addWidget(self.optionsHistorical, 1, 2, 1, 1)


        self.horizontalLayout_19.addLayout(self.gridLayout_17)


        self.verticalLayout_34.addLayout(self.horizontalLayout_19)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cmbParameters = CheckableComboBox(self.layoutWidget)
        self.cmbParameters.setObjectName(u"cmbParameters")
        self.cmbParameters.setEnabled(True)
        self.cmbParameters.setMinimumSize(QSize(100, 0))
        self.cmbParameters.setMaximumSize(QSize(300, 16777215))
        self.cmbParameters.setFont(font)
        self.cmbParameters.setAutoFillBackground(False)
        self.cmbParameters.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbParameters.setEditable(True)
        self.cmbParameters.setCurrentText(u"")
        self.cmbParameters.setIconSize(QSize(16, 16))
        self.cmbParameters.setFrame(True)

        self.gridLayout_5.addWidget(self.cmbParameters, 7, 1, 1, 2)

        self.cmbRun = CheckableComboBox(self.layoutWidget)
        self.cmbRun.setObjectName(u"cmbRun")
        self.cmbRun.setEnabled(True)
        self.cmbRun.setMinimumSize(QSize(100, 0))
        self.cmbRun.setMaximumSize(QSize(300, 16777215))
        self.cmbRun.setFont(font)
        self.cmbRun.setAutoFillBackground(False)
        self.cmbRun.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbRun.setEditable(True)
        self.cmbRun.setCurrentText(u"")
        self.cmbRun.setIconSize(QSize(16, 16))
        self.cmbRun.setFrame(True)

        self.gridLayout_5.addWidget(self.cmbRun, 3, 1, 1, 2)

        self.cmbTechnologies = CheckableComboBox(self.layoutWidget)
        self.cmbTechnologies.setObjectName(u"cmbTechnologies")
        self.cmbTechnologies.setEnabled(True)
        self.cmbTechnologies.setMinimumSize(QSize(100, 0))
        self.cmbTechnologies.setMaximumSize(QSize(300, 16777215))
        self.cmbTechnologies.setFont(font)
        self.cmbTechnologies.setAutoFillBackground(False)
        self.cmbTechnologies.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbTechnologies.setEditable(True)
        self.cmbTechnologies.setCurrentText(u"")
        self.cmbTechnologies.setIconSize(QSize(16, 16))
        self.cmbTechnologies.setFrame(True)

        self.gridLayout_5.addWidget(self.cmbTechnologies, 1, 1, 1, 2)

        self.labelVersion_26 = QLabel(self.layoutWidget)
        self.labelVersion_26.setObjectName(u"labelVersion_26")
        self.labelVersion_26.setMaximumSize(QSize(200, 20))
        self.labelVersion_26.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_26.setLineWidth(1)
        self.labelVersion_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.labelVersion_26, 0, 1, 1, 1)

        self.labelVersion_29 = QLabel(self.layoutWidget)
        self.labelVersion_29.setObjectName(u"labelVersion_29")
        self.labelVersion_29.setMaximumSize(QSize(200, 20))
        self.labelVersion_29.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_29.setLineWidth(1)
        self.labelVersion_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.labelVersion_29, 6, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_10, 9, 0, 1, 1)

        self.labelVersion_27 = QLabel(self.layoutWidget)
        self.labelVersion_27.setObjectName(u"labelVersion_27")
        self.labelVersion_27.setMaximumSize(QSize(200, 20))
        self.labelVersion_27.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_27.setLineWidth(1)
        self.labelVersion_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.labelVersion_27, 2, 1, 1, 1)

        self.cmbWafer = CheckableComboBox(self.layoutWidget)
        self.cmbWafer.addItem("")
        self.cmbWafer.setObjectName(u"cmbWafer")
        self.cmbWafer.setEnabled(True)
        self.cmbWafer.setMinimumSize(QSize(100, 0))
        self.cmbWafer.setMaximumSize(QSize(300, 16777215))
        self.cmbWafer.setFont(font)
        self.cmbWafer.setAutoFillBackground(False)
        self.cmbWafer.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbWafer.setEditable(True)
        self.cmbWafer.setCurrentText(u"All wafers")
        self.cmbWafer.setIconSize(QSize(16, 16))
        self.cmbWafer.setFrame(True)

        self.gridLayout_5.addWidget(self.cmbWafer, 5, 1, 1, 2)

        self.labelVersion_28 = QLabel(self.layoutWidget)
        self.labelVersion_28.setObjectName(u"labelVersion_28")
        self.labelVersion_28.setMaximumSize(QSize(200, 20))
        self.labelVersion_28.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_28.setLineWidth(1)
        self.labelVersion_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.labelVersion_28, 4, 1, 1, 1)

        self.next_histogram_3 = QPushButton(self.layoutWidget)
        self.next_histogram_3.setObjectName(u"next_histogram_3")
        self.next_histogram_3.setMinimumSize(QSize(30, 30))
        self.next_histogram_3.setMaximumSize(QSize(30, 16777215))
        self.next_histogram_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_histogram_3.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.next_histogram_3.setIcon(icon16)

        self.gridLayout_5.addWidget(self.next_histogram_3, 5, 3, 1, 1)

        self.labelVersion_31 = QLabel(self.layoutWidget)
        self.labelVersion_31.setObjectName(u"labelVersion_31")
        self.labelVersion_31.setMinimumSize(QSize(100, 0))
        self.labelVersion_31.setMaximumSize(QSize(100, 20))
        self.labelVersion_31.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_31.setLineWidth(1)
        self.labelVersion_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.labelVersion_31, 0, 4, 1, 1)

        self.ListWafers = QListView(self.layoutWidget)
        self.ListWafers.setObjectName(u"ListWafers")
        self.ListWafers.setMaximumSize(QSize(300, 335))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(True)
        self.ListWafers.setFont(font4)
        self.ListWafers.setAutoFillBackground(False)
        self.ListWafers.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.ListWafers, 1, 4, 7, 1)


        self.verticalLayout_34.addLayout(self.gridLayout_5)


        self.horizontalLayout_14.addLayout(self.verticalLayout_34)

        self.horizontalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_22)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labelVersion_24 = QLabel(self.layoutWidget)
        self.labelVersion_24.setObjectName(u"labelVersion_24")
        self.labelVersion_24.setMaximumSize(QSize(200, 20))
        self.labelVersion_24.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_24.setLineWidth(1)
        self.labelVersion_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.labelVersion_24)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_23)

        self.btnSaveDescription_4 = QPushButton(self.layoutWidget)
        self.btnSaveDescription_4.setObjectName(u"btnSaveDescription_4")
        self.btnSaveDescription_4.setEnabled(True)
        self.btnSaveDescription_4.setMinimumSize(QSize(30, 30))
        self.btnSaveDescription_4.setMaximumSize(QSize(30, 16777215))
        self.btnSaveDescription_4.setFont(font)
        self.btnSaveDescription_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSaveDescription_4.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnSaveDescription_4.setIcon(icon13)
        self.btnSaveDescription_4.setFlat(False)

        self.horizontalLayout_9.addWidget(self.btnSaveDescription_4)

        self.btnCopyDescription_4 = QPushButton(self.layoutWidget)
        self.btnCopyDescription_4.setObjectName(u"btnCopyDescription_4")
        self.btnCopyDescription_4.setMinimumSize(QSize(30, 30))
        self.btnCopyDescription_4.setMaximumSize(QSize(30, 16777215))
        self.btnCopyDescription_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCopyDescription_4.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnCopyDescription_4.setIcon(icon14)

        self.horizontalLayout_9.addWidget(self.btnCopyDescription_4)

        self.btnClearDescription_6 = QPushButton(self.layoutWidget)
        self.btnClearDescription_6.setObjectName(u"btnClearDescription_6")
        self.btnClearDescription_6.setEnabled(True)
        self.btnClearDescription_6.setMinimumSize(QSize(30, 30))
        self.btnClearDescription_6.setMaximumSize(QSize(30, 16777215))
        self.btnClearDescription_6.setFont(font)
        self.btnClearDescription_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClearDescription_6.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnClearDescription_6.setIcon(icon15)
        self.btnClearDescription_6.setFlat(False)

        self.horizontalLayout_9.addWidget(self.btnClearDescription_6)


        self.verticalLayout_35.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_8 = QSpacerItem(15, 24, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_35.addItem(self.verticalSpacer_8)

        self.txtParametersResult_2 = QPlainTextEdit(self.layoutWidget)
        self.txtParametersResult_2.setObjectName(u"txtParametersResult_2")
        self.txtParametersResult_2.setMinimumSize(QSize(10, 350))
        self.txtParametersResult_2.setMaximumSize(QSize(16777215, 350))
        self.txtParametersResult_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_35.addWidget(self.txtParametersResult_2)


        self.horizontalLayout_14.addLayout(self.verticalLayout_35)

        self.layoutWidget_2 = QWidget(self.consult_estepa)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(12, 484, 1311, 261))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, -1)
        self.labelVersion_33 = QLabel(self.layoutWidget_2)
        self.labelVersion_33.setObjectName(u"labelVersion_33")
        self.labelVersion_33.setMinimumSize(QSize(135, 0))
        self.labelVersion_33.setMaximumSize(QSize(75, 20))
        self.labelVersion_33.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_33.setLineWidth(1)
        self.labelVersion_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.labelVersion_33)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_26)

        self.next_histogram_2 = QPushButton(self.layoutWidget_2)
        self.next_histogram_2.setObjectName(u"next_histogram_2")
        self.next_histogram_2.setMinimumSize(QSize(30, 30))
        self.next_histogram_2.setMaximumSize(QSize(30, 16777215))
        self.next_histogram_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_histogram_2.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.next_histogram_2.setIcon(icon16)

        self.horizontalLayout_22.addWidget(self.next_histogram_2)

        self.btnClearDescription_8 = QPushButton(self.layoutWidget_2)
        self.btnClearDescription_8.setObjectName(u"btnClearDescription_8")
        self.btnClearDescription_8.setEnabled(True)
        self.btnClearDescription_8.setMinimumSize(QSize(30, 30))
        self.btnClearDescription_8.setMaximumSize(QSize(30, 16777215))
        self.btnClearDescription_8.setFont(font)
        self.btnClearDescription_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClearDescription_8.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnClearDescription_8.setIcon(icon15)
        self.btnClearDescription_8.setFlat(False)

        self.horizontalLayout_22.addWidget(self.btnClearDescription_8)


        self.verticalLayout_37.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_histogram_2 = QHBoxLayout()
        self.horizontalLayout_histogram_2.setObjectName(u"horizontalLayout_histogram_2")
        self.horizontalSpacer_histogram_2 = QSpacerItem(40, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_histogram_2.addItem(self.horizontalSpacer_histogram_2)

        self.verticalLayout_histogram_2 = QVBoxLayout()
        self.verticalLayout_histogram_2.setObjectName(u"verticalLayout_histogram_2")

        self.horizontalLayout_histogram_2.addLayout(self.verticalLayout_histogram_2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_histogram_2)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_9)


        self.horizontalLayout_16.addLayout(self.verticalLayout_37)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_wafermap_2 = QVBoxLayout()
        self.verticalLayout_wafermap_2.setObjectName(u"verticalLayout_wafermap_2")

        self.horizontalLayout_24.addLayout(self.verticalLayout_wafermap_2)


        self.verticalLayout_38.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_16.addLayout(self.verticalLayout_38)

        self.stackedWidget.addWidget(self.consult_estepa)
        self.inbase = QWidget()
        self.inbase.setObjectName(u"inbase")
        self.verticalLayout_23 = QVBoxLayout(self.inbase)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_12 = QLabel(self.inbase)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 20))
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_23.addWidget(self.label_12)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.labelVersion_45 = QLabel(self.inbase)
        self.labelVersion_45.setObjectName(u"labelVersion_45")
        self.labelVersion_45.setMaximumSize(QSize(200, 20))
        self.labelVersion_45.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_45.setLineWidth(1)
        self.labelVersion_45.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_45, 2, 0, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_25.addItem(self.verticalSpacer_23, 4, 0, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_25.addItem(self.verticalSpacer_24, 17, 0, 1, 1)

        self.btnUploadFiles = QPushButton(self.inbase)
        self.btnUploadFiles.setObjectName(u"btnUploadFiles")
        self.btnUploadFiles.setMinimumSize(QSize(150, 30))
        self.btnUploadFiles.setMaximumSize(QSize(300, 16777215))
        self.btnUploadFiles.setFont(font)
        self.btnUploadFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnUploadFiles.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/cil-cloud-upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnUploadFiles.setIcon(icon17)

        self.gridLayout_25.addWidget(self.btnUploadFiles, 18, 0, 1, 1)

        self.txtRunUpload = QLineEdit(self.inbase)
        self.txtRunUpload.setObjectName(u"txtRunUpload")
        self.txtRunUpload.setEnabled(True)
        self.txtRunUpload.setMinimumSize(QSize(100, 30))
        self.txtRunUpload.setMaximumSize(QSize(100, 30))
        self.txtRunUpload.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtRunUpload, 6, 0, 1, 1)

        self.txtLocalizationUpload = QLineEdit(self.inbase)
        self.txtLocalizationUpload.setObjectName(u"txtLocalizationUpload")
        self.txtLocalizationUpload.setEnabled(True)
        self.txtLocalizationUpload.setMinimumSize(QSize(300, 30))
        self.txtLocalizationUpload.setMaximumSize(QSize(300, 30))
        self.txtLocalizationUpload.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtLocalizationUpload, 14, 0, 1, 1)

        self.txtCommentUpload = QLineEdit(self.inbase)
        self.txtCommentUpload.setObjectName(u"txtCommentUpload")
        self.txtCommentUpload.setEnabled(True)
        self.txtCommentUpload.setMinimumSize(QSize(300, 30))
        self.txtCommentUpload.setMaximumSize(QSize(300, 30))
        self.txtCommentUpload.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtCommentUpload, 14, 1, 1, 1)

        self.btnOpenWafermapFileInbase = QPushButton(self.inbase)
        self.btnOpenWafermapFileInbase.setObjectName(u"btnOpenWafermapFileInbase")
        self.btnOpenWafermapFileInbase.setMinimumSize(QSize(50, 30))
        self.btnOpenWafermapFileInbase.setMaximumSize(QSize(50, 30))
        self.btnOpenWafermapFileInbase.setFont(font)
        self.btnOpenWafermapFileInbase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOpenWafermapFileInbase.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnOpenWafermapFileInbase.setIcon(icon11)

        self.gridLayout_25.addWidget(self.btnOpenWafermapFileInbase, 3, 1, 1, 1)

        self.labelVersion_46 = QLabel(self.inbase)
        self.labelVersion_46.setObjectName(u"labelVersion_46")
        self.labelVersion_46.setMaximumSize(QSize(200, 20))
        self.labelVersion_46.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_46.setLineWidth(1)
        self.labelVersion_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_46, 10, 1, 1, 1)

        self.cmbMaskUpload = QComboBox(self.inbase)
        self.cmbMaskUpload.addItem("")
        self.cmbMaskUpload.setObjectName(u"cmbMaskUpload")
        self.cmbMaskUpload.setMinimumSize(QSize(160, 30))
        self.cmbMaskUpload.setMaximumSize(QSize(16777215, 30))
        self.cmbMaskUpload.setFont(font)
        self.cmbMaskUpload.setAutoFillBackground(False)
        self.cmbMaskUpload.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbMaskUpload.setEditable(True)
        self.cmbMaskUpload.setIconSize(QSize(16, 16))
        self.cmbMaskUpload.setFrame(True)

        self.gridLayout_25.addWidget(self.cmbMaskUpload, 11, 1, 1, 1)

        self.btnOpenDataFileInbase = QPushButton(self.inbase)
        self.btnOpenDataFileInbase.setObjectName(u"btnOpenDataFileInbase")
        self.btnOpenDataFileInbase.setMinimumSize(QSize(50, 30))
        self.btnOpenDataFileInbase.setMaximumSize(QSize(50, 30))
        self.btnOpenDataFileInbase.setFont(font)
        self.btnOpenDataFileInbase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOpenDataFileInbase.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnOpenDataFileInbase.setIcon(icon11)

        self.gridLayout_25.addWidget(self.btnOpenDataFileInbase, 1, 1, 1, 1)

        self.txtDataFileInbase = QLineEdit(self.inbase)
        self.txtDataFileInbase.setObjectName(u"txtDataFileInbase")
        self.txtDataFileInbase.setEnabled(True)
        self.txtDataFileInbase.setMinimumSize(QSize(300, 30))
        self.txtDataFileInbase.setMaximumSize(QSize(300, 30))
        self.txtDataFileInbase.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtDataFileInbase, 1, 0, 1, 1)

        self.labelVersion_47 = QLabel(self.inbase)
        self.labelVersion_47.setObjectName(u"labelVersion_47")
        self.labelVersion_47.setMaximumSize(QSize(200, 20))
        self.labelVersion_47.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_47.setLineWidth(1)
        self.labelVersion_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_47, 5, 0, 1, 1)

        self.labelVersion_48 = QLabel(self.inbase)
        self.labelVersion_48.setObjectName(u"labelVersion_48")
        self.labelVersion_48.setMaximumSize(QSize(200, 20))
        self.labelVersion_48.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_48.setLineWidth(1)
        self.labelVersion_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_48, 13, 0, 1, 1)

        self.txtWafermapFileInbase = QLineEdit(self.inbase)
        self.txtWafermapFileInbase.setObjectName(u"txtWafermapFileInbase")
        self.txtWafermapFileInbase.setEnabled(True)
        self.txtWafermapFileInbase.setMinimumSize(QSize(300, 30))
        self.txtWafermapFileInbase.setMaximumSize(QSize(300, 30))
        self.txtWafermapFileInbase.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtWafermapFileInbase, 3, 0, 1, 1)

        self.labelVersion_49 = QLabel(self.inbase)
        self.labelVersion_49.setObjectName(u"labelVersion_49")
        self.labelVersion_49.setMaximumSize(QSize(200, 20))
        self.labelVersion_49.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_49.setLineWidth(1)
        self.labelVersion_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_49, 13, 1, 1, 1)

        self.txtWaferUpload = QLineEdit(self.inbase)
        self.txtWaferUpload.setObjectName(u"txtWaferUpload")
        self.txtWaferUpload.setEnabled(True)
        self.txtWaferUpload.setMinimumSize(QSize(100, 30))
        self.txtWaferUpload.setMaximumSize(QSize(100, 30))
        self.txtWaferUpload.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtWaferUpload, 6, 1, 1, 1)

        self.txtTechnologyUpload = QLineEdit(self.inbase)
        self.txtTechnologyUpload.setObjectName(u"txtTechnologyUpload")
        self.txtTechnologyUpload.setEnabled(True)
        self.txtTechnologyUpload.setMinimumSize(QSize(300, 30))
        self.txtTechnologyUpload.setMaximumSize(QSize(300, 30))
        self.txtTechnologyUpload.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtTechnologyUpload, 12, 0, 1, 1)

        self.labelVersion_50 = QLabel(self.inbase)
        self.labelVersion_50.setObjectName(u"labelVersion_50")
        self.labelVersion_50.setMaximumSize(QSize(200, 20))
        self.labelVersion_50.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_50.setLineWidth(1)
        self.labelVersion_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_50, 0, 0, 1, 1)

        self.labelVersion_51 = QLabel(self.inbase)
        self.labelVersion_51.setObjectName(u"labelVersion_51")
        self.labelVersion_51.setMaximumSize(QSize(200, 20))
        self.labelVersion_51.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_51.setLineWidth(1)
        self.labelVersion_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_51, 10, 0, 1, 1)

        self.cmbTechnologyUpload = QComboBox(self.inbase)
        self.cmbTechnologyUpload.addItem("")
        self.cmbTechnologyUpload.setObjectName(u"cmbTechnologyUpload")
        self.cmbTechnologyUpload.setMinimumSize(QSize(160, 30))
        self.cmbTechnologyUpload.setMaximumSize(QSize(16777215, 30))
        self.cmbTechnologyUpload.setFont(font)
        self.cmbTechnologyUpload.setAutoFillBackground(False)
        self.cmbTechnologyUpload.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbTechnologyUpload.setEditable(True)
        self.cmbTechnologyUpload.setIconSize(QSize(16, 16))
        self.cmbTechnologyUpload.setFrame(True)

        self.gridLayout_25.addWidget(self.cmbTechnologyUpload, 11, 0, 1, 1)

        self.txtMaskUpload = QLineEdit(self.inbase)
        self.txtMaskUpload.setObjectName(u"txtMaskUpload")
        self.txtMaskUpload.setEnabled(True)
        self.txtMaskUpload.setMinimumSize(QSize(300, 30))
        self.txtMaskUpload.setMaximumSize(QSize(300, 30))
        self.txtMaskUpload.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtMaskUpload, 12, 1, 1, 1)

        self.labelVersion_52 = QLabel(self.inbase)
        self.labelVersion_52.setObjectName(u"labelVersion_52")
        self.labelVersion_52.setMaximumSize(QSize(200, 20))
        self.labelVersion_52.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_52.setLineWidth(1)
        self.labelVersion_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_52, 5, 1, 1, 1)

        self.labelVersion_53 = QLabel(self.inbase)
        self.labelVersion_53.setObjectName(u"labelVersion_53")
        self.labelVersion_53.setMaximumSize(QSize(220, 20))
        self.labelVersion_53.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_53.setLineWidth(1)
        self.labelVersion_53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_53, 8, 0, 1, 1)

        self.txtDateUpload = QLineEdit(self.inbase)
        self.txtDateUpload.setObjectName(u"txtDateUpload")
        self.txtDateUpload.setEnabled(True)
        self.txtDateUpload.setMinimumSize(QSize(100, 30))
        self.txtDateUpload.setMaximumSize(QSize(100, 30))
        self.txtDateUpload.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.txtDateUpload, 9, 0, 1, 1)


        self.horizontalLayout_30.addLayout(self.gridLayout_25)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_31)


        self.verticalLayout_42.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_25 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_42.addItem(self.verticalSpacer_25)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 20, -1, -1)
        self.labelVersion_54 = QLabel(self.inbase)
        self.labelVersion_54.setObjectName(u"labelVersion_54")
        self.labelVersion_54.setMaximumSize(QSize(200, 20))
        self.labelVersion_54.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_54.setLineWidth(1)
        self.labelVersion_54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.labelVersion_54)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_32)

        self.btnSaveImportReport = QPushButton(self.inbase)
        self.btnSaveImportReport.setObjectName(u"btnSaveImportReport")
        self.btnSaveImportReport.setEnabled(True)
        self.btnSaveImportReport.setMinimumSize(QSize(30, 30))
        self.btnSaveImportReport.setMaximumSize(QSize(30, 16777215))
        self.btnSaveImportReport.setFont(font)
        self.btnSaveImportReport.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSaveImportReport.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnSaveImportReport.setIcon(icon13)
        self.btnSaveImportReport.setFlat(False)

        self.horizontalLayout_31.addWidget(self.btnSaveImportReport)

        self.btnClearImportReport = QPushButton(self.inbase)
        self.btnClearImportReport.setObjectName(u"btnClearImportReport")
        self.btnClearImportReport.setEnabled(True)
        self.btnClearImportReport.setMinimumSize(QSize(30, 30))
        self.btnClearImportReport.setMaximumSize(QSize(30, 16777215))
        self.btnClearImportReport.setFont(font)
        self.btnClearImportReport.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClearImportReport.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton:disabled {\n"
"\n"
"	background-color: #333333; border: none;\n"
"}")
        self.btnClearImportReport.setIcon(icon15)
        self.btnClearImportReport.setFlat(False)

        self.horizontalLayout_31.addWidget(self.btnClearImportReport)


        self.verticalLayout_42.addLayout(self.horizontalLayout_31)

        self.txtImportReport = QPlainTextEdit(self.inbase)
        self.txtImportReport.setObjectName(u"txtImportReport")
        self.txtImportReport.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_42.addWidget(self.txtImportReport)


        self.verticalLayout_23.addLayout(self.verticalLayout_42)

        self.stackedWidget.addWidget(self.inbase)
        self.page_results = QWidget()
        self.page_results.setObjectName(u"page_results")
        self.plot_widget = PlotWidget(self.page_results)
        self.plot_widget.setObjectName(u"plot_widget")
        self.plot_widget.setGeometry(QRect(0, 0, 1291, 771))
        self.gridLayout_4 = QGridLayout(self.plot_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
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

        self.stackedWidget_configuration.setCurrentIndex(1)
        self.optionsNonAutomatic.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(2)
        self.optionsESTEPA.setCurrentIndex(1)
        self.optionsHistorical.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.topLogo.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_page_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_page_estepa.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.btn_page_consult.setText(QCoreApplication.translate("MainWindow", u"Consult", None))
        self.btn_page_inbase.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Options", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.Outliner_2.setText(QCoreApplication.translate("MainWindow", u"Outlier Removal Method:", None))
        self.cmbOutlinerMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"none", None))
        self.cmbOutlinerMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"f-spread", None))
        self.cmbOutlinerMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"k-sigma", None))

        self.chkNonAutomaticLimits.setText(QCoreApplication.translate("MainWindow", u"Non-automatic limits", None))
        self.chkGetAutoLimits.setText(QCoreApplication.translate("MainWindow", u"Auto limits", None))
        self.labelVersion_55.setText(QCoreApplication.translate("MainWindow", u"Limit max", None))
        self.labelVersion_56.setText(QCoreApplication.translate("MainWindow", u"Limit min", None))
        self.txtLimitMin.setText("")
        self.txtLimitMin.setPlaceholderText("")
        self.txtLimitMax.setText("")
        self.txtLimitMax.setPlaceholderText("")
        self.Font_2.setText(QCoreApplication.translate("MainWindow", u"Font Size:", None))
        self.cmbFontSize.setItemText(0, QCoreApplication.translate("MainWindow", u"Small", None))
        self.cmbFontSize.setItemText(1, QCoreApplication.translate("MainWindow", u"Big", None))

        self.Performance_2.setText(QCoreApplication.translate("MainWindow", u"Performance Presentation:", None))
        self.cmbPerformancePresentation.setItemText(0, QCoreApplication.translate("MainWindow", u"Number of Points", None))
        self.cmbPerformancePresentation.setItemText(1, QCoreApplication.translate("MainWindow", u"Percentage", None))

        self.Wafer_2.setText(QCoreApplication.translate("MainWindow", u"Wafer Representation:", None))
        self.cmbWaferRepresentation.setItemText(0, QCoreApplication.translate("MainWindow", u"Colors", None))
        self.cmbWaferRepresentation.setItemText(1, QCoreApplication.translate("MainWindow", u"Gravity centers", None))
        self.cmbWaferRepresentation.setItemText(2, QCoreApplication.translate("MainWindow", u"Letters", None))

        self.HistogramTextLabel.setText(QCoreApplication.translate("MainWindow", u"Histogram chunks", None))
        self.txtHistogramChunks.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.txtHistogramChunks.setPlaceholderText("")
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.home_analysis.setText(QCoreApplication.translate("MainWindow", u"Start Analysis", None))
        self.home_consult.setText(QCoreApplication.translate("MainWindow", u"Consult", None))
        self.home_upload.setText(QCoreApplication.translate("MainWindow", u"Upload Files to BBDD", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">	Welcome to</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">ESTEPA<br/></span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.btn_ppg_9.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.btn_ppg_6.setText(QCoreApplication.translate("MainWindow", u"Open Directory", None))
        self.btn_ppg_7.setText(QCoreApplication.translate("MainWindow", u"Examples", None))
        self.btn_ppg_8.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"STATISTICS for the PARAMETRIC TEST", None))
        self.optLoadFiles.setText(QCoreApplication.translate("MainWindow", u"Load from files", None))
        self.optLoadBBDD.setText(QCoreApplication.translate("MainWindow", u"Load from BBDD", None))
        self.btnOpenDataFile.setText("")
        self.btnOpenWafermapFile.setText("")
        self.labelVersion_13.setText(QCoreApplication.translate("MainWindow", u"Load DATA file", None))
        self.txtWafermapFile.setText("")
        self.txtWafermapFile.setPlaceholderText("")
        self.txtDataFile.setText("")
        self.txtDataFile.setPlaceholderText("")
        self.btnLoadFiles.setText(QCoreApplication.translate("MainWindow", u"Load from files", None))
        self.labelVersion_14.setText(QCoreApplication.translate("MainWindow", u"Load WAFERMAP file", None))
        self.btnCorrelationFiles.setText(QCoreApplication.translate("MainWindow", u"Correlation", None))
        self.btnAnalyzeFiles.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.cmbParametersFile.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.labelVersion_19.setText(QCoreApplication.translate("MainWindow", u"Select parameters", None))
        self.cmbWafers.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbWafers.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.labelVersion_15.setText(QCoreApplication.translate("MainWindow", u"Select technology", None))
        self.btnCorrelationBBDD.setText(QCoreApplication.translate("MainWindow", u"Correlation", None))
        self.cmbTechnology.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbTechnology.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.labelVersion_17.setText(QCoreApplication.translate("MainWindow", u"Select run", None))
        self.cmbRuns.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbRuns.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.labelVersion_16.setText(QCoreApplication.translate("MainWindow", u"Select wafer", None))
        self.btnAnalyzeBBDD.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.labelVersion_18.setText(QCoreApplication.translate("MainWindow", u"Select parameters", None))
        self.cmbParametersBBDD.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbParametersBBDD.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.labelVersion_20.setText(QCoreApplication.translate("MainWindow", u"DATA VALUES", None))
#if QT_CONFIG(tooltip)
        self.btnSaveDescription_2.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.btnSaveDescription_2.setText("")
#if QT_CONFIG(tooltip)
        self.btnCopyDescription_2.setToolTip(QCoreApplication.translate("MainWindow", u"Copy", None))
#endif // QT_CONFIG(tooltip)
        self.btnCopyDescription_2.setText("")
#if QT_CONFIG(tooltip)
        self.btnClearDescription_2.setToolTip(QCoreApplication.translate("MainWindow", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearDescription_2.setText("")
        self.txtCurrentParameter.setText(QCoreApplication.translate("MainWindow", u"Parameter", None))
        self.txtCurrentParameter.setPlaceholderText("")
        self.pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.txtLoadedValues.setToolTip(QCoreApplication.translate("MainWindow", u"Data values", None))
#endif // QT_CONFIG(tooltip)
        self.txtLoadedValues.setPlainText("")
        self.labelVersion_21.setText(QCoreApplication.translate("MainWindow", u"PARAMETERS RESULT", None))
#if QT_CONFIG(tooltip)
        self.btnSaveDescription_3.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.btnSaveDescription_3.setText("")
#if QT_CONFIG(tooltip)
        self.btnCopyDescription_3.setToolTip(QCoreApplication.translate("MainWindow", u"Copy", None))
#endif // QT_CONFIG(tooltip)
        self.btnCopyDescription_3.setText("")
#if QT_CONFIG(tooltip)
        self.btnClearDescription_3.setToolTip(QCoreApplication.translate("MainWindow", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearDescription_3.setText("")
#if QT_CONFIG(tooltip)
        self.txtParametersResult.setToolTip(QCoreApplication.translate("MainWindow", u"Results parameters", None))
#endif // QT_CONFIG(tooltip)
        self.txtParametersResult.setPlainText("")
        self.labelVersion_22.setText(QCoreApplication.translate("MainWindow", u"GRAPH", None))
#if QT_CONFIG(tooltip)
        self.btnClearDescription_4.setToolTip(QCoreApplication.translate("MainWindow", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearDescription_4.setText("")
        self.labelVersion_23.setText(QCoreApplication.translate("MainWindow", u"WAFERMAP", None))
#if QT_CONFIG(tooltip)
        self.btnSaveDescription_5.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.btnSaveDescription_5.setText("")
#if QT_CONFIG(tooltip)
        self.btnClearDescription_5.setToolTip(QCoreApplication.translate("MainWindow", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearDescription_5.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CONSULT DATA BASE", None))
        self.optWafers.setText(QCoreApplication.translate("MainWindow", u"Wafers", None))
        self.historicalcheck.setText(QCoreApplication.translate("MainWindow", u"Historical", None))
        self.optRuns.setText(QCoreApplication.translate("MainWindow", u"Runs", None))
        self.btnValues.setText(QCoreApplication.translate("MainWindow", u"Values", None))
        self.btnYield.setText(QCoreApplication.translate("MainWindow", u"Yield", None))
        self.labelVersion_26.setText(QCoreApplication.translate("MainWindow", u"Select technology", None))
        self.labelVersion_29.setText(QCoreApplication.translate("MainWindow", u"Select parameters", None))
        self.labelVersion_27.setText(QCoreApplication.translate("MainWindow", u"Select run", None))
        self.cmbWafer.setItemText(0, QCoreApplication.translate("MainWindow", u"All wafers", None))

        self.labelVersion_28.setText(QCoreApplication.translate("MainWindow", u"Select wafer", None))
#if QT_CONFIG(tooltip)
        self.next_histogram_3.setToolTip(QCoreApplication.translate("MainWindow", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.next_histogram_3.setText("")
        self.labelVersion_31.setText(QCoreApplication.translate("MainWindow", u"WAFERS", None))
        self.labelVersion_24.setText(QCoreApplication.translate("MainWindow", u"PARAMETERS RESULT", None))
#if QT_CONFIG(tooltip)
        self.btnSaveDescription_4.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.btnSaveDescription_4.setText("")
#if QT_CONFIG(tooltip)
        self.btnCopyDescription_4.setToolTip(QCoreApplication.translate("MainWindow", u"Copy", None))
#endif // QT_CONFIG(tooltip)
        self.btnCopyDescription_4.setText("")
#if QT_CONFIG(tooltip)
        self.btnClearDescription_6.setToolTip(QCoreApplication.translate("MainWindow", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearDescription_6.setText("")
#if QT_CONFIG(tooltip)
        self.txtParametersResult_2.setToolTip(QCoreApplication.translate("MainWindow", u"Results parameters", None))
#endif // QT_CONFIG(tooltip)
        self.txtParametersResult_2.setPlainText("")
        self.labelVersion_33.setText(QCoreApplication.translate("MainWindow", u"HISTORICAL DIAGRAM", None))
#if QT_CONFIG(tooltip)
        self.next_histogram_2.setToolTip(QCoreApplication.translate("MainWindow", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.next_histogram_2.setText("")
#if QT_CONFIG(tooltip)
        self.btnClearDescription_8.setToolTip(QCoreApplication.translate("MainWindow", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearDescription_8.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"UPLOAD RESULTS to ESTEPA", None))
        self.labelVersion_45.setText(QCoreApplication.translate("MainWindow", u"Load WAFERMAP file", None))
        self.btnUploadFiles.setText(QCoreApplication.translate("MainWindow", u"Upload results from files", None))
        self.txtRunUpload.setText("")
        self.txtRunUpload.setPlaceholderText("")
        self.txtLocalizationUpload.setText("")
        self.txtLocalizationUpload.setPlaceholderText("")
        self.txtCommentUpload.setText("")
        self.txtCommentUpload.setPlaceholderText("")
        self.btnOpenWafermapFileInbase.setText("")
        self.labelVersion_46.setText(QCoreApplication.translate("MainWindow", u"Select Mask", None))
        self.cmbMaskUpload.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbMaskUpload.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.btnOpenDataFileInbase.setText("")
        self.txtDataFileInbase.setText("")
        self.txtDataFileInbase.setPlaceholderText("")
        self.labelVersion_47.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.labelVersion_48.setText(QCoreApplication.translate("MainWindow", u"Localization", None))
        self.txtWafermapFileInbase.setText("")
        self.txtWafermapFileInbase.setPlaceholderText("")
        self.labelVersion_49.setText(QCoreApplication.translate("MainWindow", u"Comment for wafer", None))
        self.txtWaferUpload.setText("")
        self.txtWaferUpload.setPlaceholderText("")
        self.txtTechnologyUpload.setText("")
        self.txtTechnologyUpload.setPlaceholderText("")
        self.labelVersion_50.setText(QCoreApplication.translate("MainWindow", u"Load DATA file", None))
        self.labelVersion_51.setText(QCoreApplication.translate("MainWindow", u"Select technology", None))
        self.cmbTechnologyUpload.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbTechnologyUpload.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.txtMaskUpload.setText("")
        self.txtMaskUpload.setPlaceholderText("")
        self.labelVersion_52.setText(QCoreApplication.translate("MainWindow", u"Wafer", None))
        self.labelVersion_53.setText(QCoreApplication.translate("MainWindow", u"Run Date (yyyy-mm-dd)", None))
        self.txtDateUpload.setText("")
        self.txtDateUpload.setPlaceholderText("")
        self.labelVersion_54.setText(QCoreApplication.translate("MainWindow", u"Import report", None))
#if QT_CONFIG(tooltip)
        self.btnSaveImportReport.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.btnSaveImportReport.setText("")
#if QT_CONFIG(tooltip)
        self.btnClearImportReport.setToolTip(QCoreApplication.translate("MainWindow", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearImportReport.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v7.1", None))
    # retranslateUi

