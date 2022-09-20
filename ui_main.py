# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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

from widgets import CheckableComboBox
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1167, 849)
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
        self.btn_page_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_page_home)

        self.btn_page_estepa = QPushButton(self.topMenu)
        self.btn_page_estepa.setObjectName(u"btn_page_estepa")
        sizePolicy1.setHeightForWidth(self.btn_page_estepa.sizePolicy().hasHeightForWidth())
        self.btn_page_estepa.setSizePolicy(sizePolicy1)
        self.btn_page_estepa.setMinimumSize(QSize(0, 45))
        self.btn_page_estepa.setFont(font)
        self.btn_page_estepa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_estepa.setLayoutDirection(Qt.LeftToRight)
        self.btn_page_estepa.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

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

        self.btn_page_reports = QPushButton(self.topMenu)
        self.btn_page_reports.setObjectName(u"btn_page_reports")
        sizePolicy1.setHeightForWidth(self.btn_page_reports.sizePolicy().hasHeightForWidth())
        self.btn_page_reports.setSizePolicy(sizePolicy1)
        self.btn_page_reports.setMinimumSize(QSize(0, 45))
        self.btn_page_reports.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_reports.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-description.png);")

        self.verticalLayout_8.addWidget(self.btn_page_reports)


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
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy2)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setAutoFillBackground(False)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);")
        icon = QIcon()
        icon.addFile(u"images/icons/White Icons/option_bar_settings [#1399].png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleLeftBox.setIcon(icon)

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
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon1)
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
        self.verticalLayout_19 = QVBoxLayout(self.configuration_estepa)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.txtGraphTheme = QLabel(self.configuration_estepa)
        self.txtGraphTheme.setObjectName(u"txtGraphTheme")
        self.txtGraphTheme.setMaximumSize(QSize(400, 20))
        self.txtGraphTheme.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.txtGraphTheme)

        self.chk_theme = QCheckBox(self.configuration_estepa)
        self.chk_theme.setObjectName(u"chk_theme")
        self.chk_theme.setChecked(True)

        self.verticalLayout_19.addWidget(self.chk_theme)

        self.Outliner_2 = QLabel(self.configuration_estepa)
        self.Outliner_2.setObjectName(u"Outliner_2")
        self.Outliner_2.setMaximumSize(QSize(400, 20))
        self.Outliner_2.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.Outliner_2)

        self.cmbOutlinerMethod = QComboBox(self.configuration_estepa)
        self.cmbOutlinerMethod.addItem("")
        self.cmbOutlinerMethod.addItem("")
        self.cmbOutlinerMethod.addItem("")
        self.cmbOutlinerMethod.setObjectName(u"cmbOutlinerMethod")
        self.cmbOutlinerMethod.setEditable(False)
        self.cmbOutlinerMethod.setMinimumContentsLength(0)

        self.verticalLayout_19.addWidget(self.cmbOutlinerMethod)

        self.chkNonAutomaticLimits = QCheckBox(self.configuration_estepa)
        self.chkNonAutomaticLimits.setObjectName(u"chkNonAutomaticLimits")

        self.verticalLayout_19.addWidget(self.chkNonAutomaticLimits)

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

        self.verticalLayout_19.addWidget(self.optionsNonAutomatic)

        self.Font_2 = QLabel(self.configuration_estepa)
        self.Font_2.setObjectName(u"Font_2")
        self.Font_2.setMaximumSize(QSize(400, 16777215))
        self.Font_2.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.Font_2)

        self.cmbFontSize = QComboBox(self.configuration_estepa)
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.setObjectName(u"cmbFontSize")
        self.cmbFontSize.setEditable(False)
        self.cmbFontSize.setMinimumContentsLength(0)

        self.verticalLayout_19.addWidget(self.cmbFontSize)

        self.Performance_2 = QLabel(self.configuration_estepa)
        self.Performance_2.setObjectName(u"Performance_2")
        self.Performance_2.setMaximumSize(QSize(400, 16777215))
        self.Performance_2.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.Performance_2)

        self.cmbPerformancePresentation = QComboBox(self.configuration_estepa)
        self.cmbPerformancePresentation.addItem("")
        self.cmbPerformancePresentation.addItem("")
        self.cmbPerformancePresentation.setObjectName(u"cmbPerformancePresentation")
        self.cmbPerformancePresentation.setEditable(False)
        self.cmbPerformancePresentation.setMinimumContentsLength(0)

        self.verticalLayout_19.addWidget(self.cmbPerformancePresentation)

        self.Wafer_2 = QLabel(self.configuration_estepa)
        self.Wafer_2.setObjectName(u"Wafer_2")
        self.Wafer_2.setMaximumSize(QSize(400, 16777215))
        self.Wafer_2.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.Wafer_2)

        self.cmbWaferRepresentation = QComboBox(self.configuration_estepa)
        self.cmbWaferRepresentation.addItem("")
        self.cmbWaferRepresentation.addItem("")
        self.cmbWaferRepresentation.addItem("")
        self.cmbWaferRepresentation.setObjectName(u"cmbWaferRepresentation")
        self.cmbWaferRepresentation.setEditable(False)
        self.cmbWaferRepresentation.setMinimumContentsLength(0)

        self.verticalLayout_19.addWidget(self.cmbWaferRepresentation)

        self.HistogramTextLabel = QLabel(self.configuration_estepa)
        self.HistogramTextLabel.setObjectName(u"HistogramTextLabel")

        self.verticalLayout_19.addWidget(self.HistogramTextLabel)

        self.scrollHistogramChunks = QScrollBar(self.configuration_estepa)
        self.scrollHistogramChunks.setObjectName(u"scrollHistogramChunks")
        self.scrollHistogramChunks.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\\n QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.scrollHistogramChunks.setMinimum(2)
        self.scrollHistogramChunks.setMaximum(21)
        self.scrollHistogramChunks.setSingleStep(1)
        self.scrollHistogramChunks.setValue(2)
        self.scrollHistogramChunks.setOrientation(Qt.Horizontal)

        self.verticalLayout_19.addWidget(self.scrollHistogramChunks)

        self.txtHistogramChunks = QLineEdit(self.configuration_estepa)
        self.txtHistogramChunks.setObjectName(u"txtHistogramChunks")
        self.txtHistogramChunks.setEnabled(False)
        self.txtHistogramChunks.setMinimumSize(QSize(100, 30))
        self.txtHistogramChunks.setMaximumSize(QSize(100, 30))
        self.txtHistogramChunks.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_19.addWidget(self.txtHistogramChunks)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy3)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy4)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon1)
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
        self.verticalLayout_21 = QVBoxLayout(self.Home_Window)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_24)

        self.Home_Layout = QFormLayout()
        self.Home_Layout.setObjectName(u"Home_Layout")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Home_Layout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.lbl_home = QLabel(self.Home_Window)
        self.lbl_home.setObjectName(u"lbl_home")
        self.lbl_home.setMaximumSize(QSize(300, 85))
        self.lbl_home.setStyleSheet(u"font: 30pt \"Microsoft JhengHei\";\n"
"")

        self.Home_Layout.setWidget(1, QFormLayout.LabelRole, self.lbl_home)

        self.horizontalSpacer_2 = QSpacerItem(250, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.Home_Layout.setItem(1, QFormLayout.FieldRole, self.horizontalSpacer_2)

        self.home_analysis = QPushButton(self.Home_Window)
        self.home_analysis.setObjectName(u"home_analysis")
        self.home_analysis.setMinimumSize(QSize(102, 30))
        self.home_analysis.setMaximumSize(QSize(20, 10))
        self.home_analysis.setFont(font)
        self.home_analysis.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_analysis.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        self.home_analysis.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_analysis.setIcon(icon5)

        self.Home_Layout.setWidget(2, QFormLayout.LabelRole, self.home_analysis)

        self.home_consult = QPushButton(self.Home_Window)
        self.home_consult.setObjectName(u"home_consult")
        self.home_consult.setMinimumSize(QSize(68, 30))
        self.home_consult.setMaximumSize(QSize(16, 10))
        self.home_consult.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_consult.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon6 = QIcon()
        icon6.addFile(u"../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_consult.setIcon(icon6)

        self.Home_Layout.setWidget(3, QFormLayout.LabelRole, self.home_consult)

        self.home_upload = QPushButton(self.Home_Window)
        self.home_upload.setObjectName(u"home_upload")
        self.home_upload.setMinimumSize(QSize(150, 30))
        self.home_upload.setMaximumSize(QSize(20, 10))
        self.home_upload.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_upload.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon7 = QIcon()
        icon7.addFile(u"../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/images/icons/cil-cloud-upload.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_upload.setIcon(icon7)

        self.Home_Layout.setWidget(4, QFormLayout.LabelRole, self.home_upload)

        self.home_upload_2 = QPushButton(self.Home_Window)
        self.home_upload_2.setObjectName(u"home_upload_2")
        self.home_upload_2.setMinimumSize(QSize(73, 30))
        self.home_upload_2.setMaximumSize(QSize(20, 10))
        self.home_upload_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_upload_2.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-description.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_upload_2.setIcon(icon8)

        self.Home_Layout.setWidget(5, QFormLayout.LabelRole, self.home_upload_2)


        self.horizontalLayout_12.addLayout(self.Home_Layout)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_4 = QSpacerItem(5, 68, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_4)

        self.lbl_logo = QLabel(self.Home_Window)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setMinimumSize(QSize(280, 280))
        self.lbl_logo.setMaximumSize(QSize(300, 264))
        self.lbl_logo.setAutoFillBackground(False)
        self.lbl_logo.setStyleSheet(u"image: url(:/images/images/images/PyDracula_vertical.png);")
        self.lbl_logo.setLineWidth(0)
        self.lbl_logo.setPixmap(QPixmap(u"images/images/Estepa.png"))
        self.lbl_logo.setScaledContents(False)
        self.lbl_logo.setWordWrap(False)

        self.verticalLayout_18.addWidget(self.lbl_logo)

        self.verticalSpacer_11 = QSpacerItem(5, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)

        self.lbl_welcome = QLabel(self.Home_Window)
        self.lbl_welcome.setObjectName(u"lbl_welcome")
        self.lbl_welcome.setMinimumSize(QSize(274, 10))
        self.lbl_welcome.setMaximumSize(QSize(345, 60))
        self.lbl_welcome.setStyleSheet(u"font: 25 30pt \"Microsoft JhengHei Light\";")

        self.verticalLayout_16.addWidget(self.lbl_welcome)

        self.verticalSpacer_13 = QSpacerItem(23, 17, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_16.addItem(self.verticalSpacer_13)

        self.lbl_estepa = QLabel(self.Home_Window)
        self.lbl_estepa.setObjectName(u"lbl_estepa")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lbl_estepa.sizePolicy().hasHeightForWidth())
        self.lbl_estepa.setSizePolicy(sizePolicy5)
        self.lbl_estepa.setMinimumSize(QSize(351, 20))
        self.lbl_estepa.setMaximumSize(QSize(351, 100))
        self.lbl_estepa.setStyleSheet(u"font: 75 65pt \"Microsoft JhengHei\";")

        self.verticalLayout_16.addWidget(self.lbl_estepa)

        self.horizontalSpacer_28 = QSpacerItem(400, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_28)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_10)


        self.horizontalLayout_12.addLayout(self.verticalLayout_16)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)


        self.verticalLayout_22.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacer_6)


        self.verticalLayout_21.addLayout(self.verticalLayout_22)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_25)

        self.Options_Layout = QFormLayout()
        self.Options_Layout.setObjectName(u"Options_Layout")
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Options_Layout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_14)

        self.lbl_options = QLabel(self.Home_Window)
        self.lbl_options.setObjectName(u"lbl_options")
        self.lbl_options.setMinimumSize(QSize(0, 12))
        self.lbl_options.setMaximumSize(QSize(300, 85))
        self.lbl_options.setStyleSheet(u"font: 30pt \"Microsoft JhengHei\";\n"
"")

        self.Options_Layout.setWidget(1, QFormLayout.LabelRole, self.lbl_options)

        self.horizontalSpacer_9 = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Options_Layout.setItem(1, QFormLayout.FieldRole, self.horizontalSpacer_9)

        self.btn_ppg_8 = QPushButton(self.Home_Window)
        self.btn_ppg_8.setObjectName(u"btn_ppg_8")
        self.btn_ppg_8.setMinimumSize(QSize(63, 30))
        self.btn_ppg_8.setMaximumSize(QSize(20, 10))
        self.btn_ppg_8.setContextMenuPolicy(Qt.NoContextMenu)
        self.btn_ppg_8.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon9 = QIcon()
        icon9.addFile(u"../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_ppg_8.setIcon(icon9)

        self.Options_Layout.setWidget(3, QFormLayout.LabelRole, self.btn_ppg_8)

        self.btn_ppg_6 = QPushButton(self.Home_Window)
        self.btn_ppg_6.setObjectName(u"btn_ppg_6")
        self.btn_ppg_6.setMinimumSize(QSize(115, 30))
        self.btn_ppg_6.setMaximumSize(QSize(20, 10))
        self.btn_ppg_6.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon10 = QIcon()
        icon10.addFile(u"../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_ppg_6.setIcon(icon10)

        self.Options_Layout.setWidget(5, QFormLayout.LabelRole, self.btn_ppg_6)

        self.btn_ppg_7 = QPushButton(self.Home_Window)
        self.btn_ppg_7.setObjectName(u"btn_ppg_7")
        self.btn_ppg_7.setMinimumSize(QSize(81, 30))
        self.btn_ppg_7.setMaximumSize(QSize(20, 10))
        self.btn_ppg_7.setStyleSheet(u"border-color: rgb(40, 44, 52);\n"
"color:rgb(52, 141, 232)")
        icon11 = QIcon()
        icon11.addFile(u"../Users/Jorge/.designer/backup/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icons/images/icons/cil-notes.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_ppg_7.setIcon(icon11)

        self.Options_Layout.setWidget(6, QFormLayout.LabelRole, self.btn_ppg_7)

        self.verticalSpacer_15 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Options_Layout.setItem(7, QFormLayout.LabelRole, self.verticalSpacer_15)


        self.horizontalLayout_27.addLayout(self.Options_Layout)

        self.horizontalSpacer_27 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_27)


        self.verticalLayout_21.addLayout(self.horizontalLayout_27)

        self.stackedWidget.addWidget(self.Home_Window)
        self.Reports_Window = QWidget()
        self.Reports_Window.setObjectName(u"Reports_Window")
        self.Reports_Window.setStyleSheet(u"b")
        self.stackedWidget.addWidget(self.Reports_Window)
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
        self.gridLayout_3 = QGridLayout(self.files)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stk_loadfiles = QStackedWidget(self.files)
        self.stk_loadfiles.setObjectName(u"stk_loadfiles")
        self.stk_loadfiles.setMinimumSize(QSize(30, 30))
        self.loaded = QWidget()
        self.loaded.setObjectName(u"loaded")
        self.gridLayoutWidget = QWidget(self.loaded)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 402, 94))
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
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCorrelationFiles.setIcon(icon12)

        self.gridLayout_2.addWidget(self.btnCorrelationFiles, 2, 4, 1, 1)

        self.btnAnalyzeFiles = QPushButton(self.gridLayoutWidget)
        self.btnAnalyzeFiles.setObjectName(u"btnAnalyzeFiles")
        self.btnAnalyzeFiles.setMinimumSize(QSize(120, 30))
        self.btnAnalyzeFiles.setMaximumSize(QSize(120, 16777215))
        self.btnAnalyzeFiles.setFont(font)
        self.btnAnalyzeFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnalyzeFiles.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnAnalyzeFiles.setIcon(icon12)

        self.gridLayout_2.addWidget(self.btnAnalyzeFiles, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 2, 3, 1, 1)

        self.lbl_select = QLabel(self.gridLayoutWidget)
        self.lbl_select.setObjectName(u"lbl_select")
        self.lbl_select.setMaximumSize(QSize(200, 20))
        self.lbl_select.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_select.setLineWidth(1)
        self.lbl_select.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_select, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)

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

        self.gridLayout_2.addWidget(self.cmbParametersFile, 1, 1, 1, 6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 6, 1, 1)

        self.opt_clear = QStackedWidget(self.gridLayoutWidget)
        self.opt_clear.setObjectName(u"opt_clear")
        self.no = QWidget()
        self.no.setObjectName(u"no")
        self.opt_clear.addWidget(self.no)
        self.yes = QWidget()
        self.yes.setObjectName(u"yes")
        self.btn_clear_all = QPushButton(self.yes)
        self.btn_clear_all.setObjectName(u"btn_clear_all")
        self.btn_clear_all.setGeometry(QRect(0, 0, 30, 30))
        self.btn_clear_all.setMinimumSize(QSize(30, 30))
        self.btn_clear_all.setMaximumSize(QSize(30, 16777215))
        self.btn_clear_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear_all.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        icon13.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_all.setIcon(icon13)
        self.opt_clear.addWidget(self.yes)

        self.gridLayout_2.addWidget(self.opt_clear, 2, 5, 1, 1)

        self.stk_loadfiles.addWidget(self.loaded)
        self.not_loaded = QWidget()
        self.not_loaded.setObjectName(u"not_loaded")
        self.stk_loadfiles.addWidget(self.not_loaded)

        self.gridLayout_3.addWidget(self.stk_loadfiles, 2, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.btnOpenWafermapFile = QPushButton(self.files)
        self.btnOpenWafermapFile.setObjectName(u"btnOpenWafermapFile")
        self.btnOpenWafermapFile.setMinimumSize(QSize(40, 30))
        self.btnOpenWafermapFile.setMaximumSize(QSize(16777215, 30))
        self.btnOpenWafermapFile.setFont(font)
        self.btnOpenWafermapFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOpenWafermapFile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnOpenWafermapFile.setIcon(icon14)

        self.gridLayout_13.addWidget(self.btnOpenWafermapFile, 3, 1, 1, 1)

        self.txtWafermapFile = QLineEdit(self.files)
        self.txtWafermapFile.setObjectName(u"txtWafermapFile")
        self.txtWafermapFile.setEnabled(False)
        self.txtWafermapFile.setMinimumSize(QSize(100, 30))
        self.txtWafermapFile.setMaximumSize(QSize(300, 30))
        self.txtWafermapFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_13.addWidget(self.txtWafermapFile, 3, 0, 1, 1)

        self.lbl_data = QLabel(self.files)
        self.lbl_data.setObjectName(u"lbl_data")
        self.lbl_data.setMaximumSize(QSize(200, 20))
        self.lbl_data.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_data.setLineWidth(1)
        self.lbl_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.lbl_data, 0, 0, 1, 1)

        self.txtDataFile = QLineEdit(self.files)
        self.txtDataFile.setObjectName(u"txtDataFile")
        self.txtDataFile.setEnabled(False)
        self.txtDataFile.setMinimumSize(QSize(100, 30))
        self.txtDataFile.setMaximumSize(QSize(300, 30))
        self.txtDataFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_13.addWidget(self.txtDataFile, 1, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_13.addItem(self.verticalSpacer_16, 5, 0, 1, 1)

        self.lbl_wafer = QLabel(self.files)
        self.lbl_wafer.setObjectName(u"lbl_wafer")
        self.lbl_wafer.setMaximumSize(QSize(200, 20))
        self.lbl_wafer.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_wafer.setLineWidth(1)
        self.lbl_wafer.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.lbl_wafer, 2, 0, 1, 1)

        self.btnLoadFiles = QPushButton(self.files)
        self.btnLoadFiles.setObjectName(u"btnLoadFiles")
        self.btnLoadFiles.setMinimumSize(QSize(100, 30))
        self.btnLoadFiles.setMaximumSize(QSize(300, 16777215))
        self.btnLoadFiles.setFont(font)
        self.btnLoadFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLoadFiles.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnLoadFiles.setIcon(icon12)

        self.gridLayout_13.addWidget(self.btnLoadFiles, 4, 0, 1, 1)

        self.btnOpenDataFile = QPushButton(self.files)
        self.btnOpenDataFile.setObjectName(u"btnOpenDataFile")
        self.btnOpenDataFile.setMinimumSize(QSize(50, 30))
        self.btnOpenDataFile.setMaximumSize(QSize(50, 30))
        self.btnOpenDataFile.setFont(font)
        self.btnOpenDataFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOpenDataFile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnOpenDataFile.setIcon(icon14)

        self.gridLayout_13.addWidget(self.btnOpenDataFile, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_13, 0, 0, 1, 1)

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

        self.lbl_yech = QLabel(self.gridLayoutWidget_9)
        self.lbl_yech.setObjectName(u"lbl_yech")
        self.lbl_yech.setMaximumSize(QSize(200, 20))
        self.lbl_yech.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_yech.setLineWidth(1)
        self.lbl_yech.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.lbl_yech, 0, 0, 1, 1)

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

        self.lbl_run = QLabel(self.gridLayoutWidget_9)
        self.lbl_run.setObjectName(u"lbl_run")
        self.lbl_run.setMaximumSize(QSize(200, 20))
        self.lbl_run.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_run.setLineWidth(1)
        self.lbl_run.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.lbl_run, 2, 0, 1, 1)

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

        self.lbl_wfer = QLabel(self.gridLayoutWidget_9)
        self.lbl_wfer.setObjectName(u"lbl_wfer")
        self.lbl_wfer.setMaximumSize(QSize(200, 20))
        self.lbl_wfer.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_wfer.setLineWidth(1)
        self.lbl_wfer.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.lbl_wfer, 4, 0, 1, 1)

        self.btnAnalyzeBBDD = QPushButton(self.gridLayoutWidget_9)
        self.btnAnalyzeBBDD.setObjectName(u"btnAnalyzeBBDD")
        self.btnAnalyzeBBDD.setMinimumSize(QSize(120, 0))
        self.btnAnalyzeBBDD.setMaximumSize(QSize(120, 30))
        self.btnAnalyzeBBDD.setFont(font)
        self.btnAnalyzeBBDD.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnalyzeBBDD.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnAnalyzeBBDD.setIcon(icon12)

        self.gridLayout_16.addWidget(self.btnAnalyzeBBDD, 11, 0, 1, 1)

        self.lbl_params = QLabel(self.gridLayoutWidget_9)
        self.lbl_params.setObjectName(u"lbl_params")
        self.lbl_params.setMaximumSize(QSize(200, 20))
        self.lbl_params.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_params.setLineWidth(1)
        self.lbl_params.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.lbl_params, 6, 0, 1, 1)

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

        self.stk_results = QStackedWidget(self.estepa)
        self.stk_results.setObjectName(u"stk_results")
        self.data = QWidget()
        self.data.setObjectName(u"data")
        self.horizontalLayout_6 = QHBoxLayout(self.data)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_datavalues = QLabel(self.data)
        self.lbl_datavalues.setObjectName(u"lbl_datavalues")
        self.lbl_datavalues.setMinimumSize(QSize(100, 0))
        self.lbl_datavalues.setMaximumSize(QSize(100, 20))
        self.lbl_datavalues.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_datavalues.setLineWidth(1)
        self.lbl_datavalues.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.lbl_datavalues)

        self.horizontalSpacer_19 = QSpacerItem(24, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_19)

        self.btnSaveDescription_2 = QPushButton(self.data)
        self.btnSaveDescription_2.setObjectName(u"btnSaveDescription_2")
        self.btnSaveDescription_2.setEnabled(True)
        self.btnSaveDescription_2.setMinimumSize(QSize(30, 30))
        self.btnSaveDescription_2.setMaximumSize(QSize(30, 16777215))
        self.btnSaveDescription_2.setFont(font)
        self.btnSaveDescription_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSaveDescription_2.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	/*border: 2px solid rgb(52, 59, 72);*/\n"
"	border-radius: 5px;	\n"
"	/*background-color: rgb(52, 59, 72);*/\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        icon15.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSaveDescription_2.setIcon(icon15)
        self.btnSaveDescription_2.setFlat(False)

        self.horizontalLayout_10.addWidget(self.btnSaveDescription_2)

        self.btnCopyDescription_2 = QPushButton(self.data)
        self.btnCopyDescription_2.setObjectName(u"btnCopyDescription_2")
        self.btnCopyDescription_2.setMinimumSize(QSize(30, 30))
        self.btnCopyDescription_2.setMaximumSize(QSize(30, 16777215))
        self.btnCopyDescription_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCopyDescription_2.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        icon16.addFile(u":/icons/images/icons/cil-clone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCopyDescription_2.setIcon(icon16)

        self.horizontalLayout_10.addWidget(self.btnCopyDescription_2)


        self.verticalLayout_29.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.cmbCurrentParameter = QComboBox(self.data)
        self.cmbCurrentParameter.addItem("")
        self.cmbCurrentParameter.setObjectName(u"cmbCurrentParameter")
        self.cmbCurrentParameter.setMinimumSize(QSize(120, 30))
        self.cmbCurrentParameter.setMaximumSize(QSize(120, 30))
        self.cmbCurrentParameter.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbCurrentParameter.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_15.addWidget(self.cmbCurrentParameter)

        self.btnNextParam = QPushButton(self.data)
        self.btnNextParam.setObjectName(u"btnNextParam")
        self.btnNextParam.setMinimumSize(QSize(30, 30))
        self.btnNextParam.setMaximumSize(QSize(30, 30))
        self.btnNextParam.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNextParam.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	\n"
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/cil-chevron-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNextParam.setIcon(icon17)

        self.horizontalLayout_15.addWidget(self.btnNextParam)

        self.horizontalSpacer_5 = QSpacerItem(21, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.verticalLayout_29.addLayout(self.horizontalLayout_15)

        self.txtLoadedValues = QPlainTextEdit(self.data)
        self.txtLoadedValues.setObjectName(u"txtLoadedValues")
        self.txtLoadedValues.setMinimumSize(QSize(260, 350))
        self.txtLoadedValues.setMaximumSize(QSize(800, 350))
        self.txtLoadedValues.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_29.addWidget(self.txtLoadedValues)


        self.horizontalLayout_6.addLayout(self.verticalLayout_29)

        self.horizontalSpacer_14 = QSpacerItem(10, 80, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_parameters_results = QLabel(self.data)
        self.lbl_parameters_results.setObjectName(u"lbl_parameters_results")
        self.lbl_parameters_results.setMaximumSize(QSize(200, 20))
        self.lbl_parameters_results.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_parameters_results.setLineWidth(1)
        self.lbl_parameters_results.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lbl_parameters_results)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_17)

        self.btnSaveDescription_3 = QPushButton(self.data)
        self.btnSaveDescription_3.setObjectName(u"btnSaveDescription_3")
        self.btnSaveDescription_3.setEnabled(True)
        self.btnSaveDescription_3.setMinimumSize(QSize(30, 30))
        self.btnSaveDescription_3.setMaximumSize(QSize(30, 16777215))
        self.btnSaveDescription_3.setFont(font)
        self.btnSaveDescription_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSaveDescription_3.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	\n"
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        self.btnSaveDescription_3.setIcon(icon15)
        self.btnSaveDescription_3.setFlat(False)

        self.horizontalLayout_7.addWidget(self.btnSaveDescription_3)

        self.btnCopyDescription_3 = QPushButton(self.data)
        self.btnCopyDescription_3.setObjectName(u"btnCopyDescription_3")
        self.btnCopyDescription_3.setMinimumSize(QSize(30, 30))
        self.btnCopyDescription_3.setMaximumSize(QSize(30, 16777215))
        self.btnCopyDescription_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCopyDescription_3.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	\n"
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        icon18 = QIcon()
        icon18.addFile(u"images/icons/cil-clone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCopyDescription_3.setIcon(icon18)

        self.horizontalLayout_7.addWidget(self.btnCopyDescription_3)


        self.verticalLayout_30.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_7 = QSpacerItem(15, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_30.addItem(self.verticalSpacer_7)

        self.txtParametersResult = QPlainTextEdit(self.data)
        self.txtParametersResult.setObjectName(u"txtParametersResult")
        self.txtParametersResult.setMinimumSize(QSize(0, 350))
        self.txtParametersResult.setMaximumSize(QSize(16777215, 350))
        self.txtParametersResult.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_30.addWidget(self.txtParametersResult)


        self.horizontalLayout_6.addLayout(self.verticalLayout_30)

        self.stk_results.addWidget(self.data)
        self.no_data = QWidget()
        self.no_data.setObjectName(u"no_data")
        self.stk_results.addWidget(self.no_data)

        self.horizontalLayout_13.addWidget(self.stk_results)

        self.horizontalSpacer_15 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.stk_graph = QStackedWidget(self.estepa)
        self.stk_graph.setObjectName(u"stk_graph")
        self.graph = QWidget()
        self.graph.setObjectName(u"graph")
        self.horizontalLayout_23 = QHBoxLayout(self.graph)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.lbl_graph = QLabel(self.graph)
        self.lbl_graph.setObjectName(u"lbl_graph")
        self.lbl_graph.setMinimumSize(QSize(90, 0))
        self.lbl_graph.setMaximumSize(QSize(90, 20))
        self.lbl_graph.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_graph.setLineWidth(1)
        self.lbl_graph.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.lbl_graph)

        self.horizontalSpacer_20 = QSpacerItem(31, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")

        self.horizontalLayout_20.addLayout(self.horizontalLayout_buttons)


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


        self.horizontalLayout_23.addLayout(self.verticalLayout_32)

        self.stk_graph.addWidget(self.graph)
        self.no_graph = QWidget()
        self.no_graph.setObjectName(u"no_graph")
        self.stk_graph.addWidget(self.no_graph)

        self.horizontalLayout_8.addWidget(self.stk_graph)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)

        self.stk_wafermap = QStackedWidget(self.estepa)
        self.stk_wafermap.setObjectName(u"stk_wafermap")
        self.no_wafermap = QWidget()
        self.no_wafermap.setObjectName(u"no_wafermap")
        self.stk_wafermap.addWidget(self.no_wafermap)
        self.wafermap = QWidget()
        self.wafermap.setObjectName(u"wafermap")
        self.horizontalLayout_17 = QHBoxLayout(self.wafermap)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_wafermap_2 = QLabel(self.wafermap)
        self.lbl_wafermap_2.setObjectName(u"lbl_wafermap_2")
        self.lbl_wafermap_2.setMaximumSize(QSize(200, 20))
        self.lbl_wafermap_2.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_wafermap_2.setLineWidth(1)
        self.lbl_wafermap_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.lbl_wafermap_2)

        self.horizontalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_21)

        self.btnSaveDescription_5 = QPushButton(self.wafermap)
        self.btnSaveDescription_5.setObjectName(u"btnSaveDescription_5")
        self.btnSaveDescription_5.setEnabled(True)
        self.btnSaveDescription_5.setMinimumSize(QSize(30, 30))
        self.btnSaveDescription_5.setMaximumSize(QSize(30, 16777215))
        self.btnSaveDescription_5.setFont(font)
        self.btnSaveDescription_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSaveDescription_5.setStyleSheet(u"/*background-color: rgb(52, 59, 72);*/\n"
"\n"
"#pagesContainer .QPushButton {\n"
"	\n"
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        self.btnSaveDescription_5.setIcon(icon15)
        self.btnSaveDescription_5.setFlat(False)

        self.horizontalLayout_11.addWidget(self.btnSaveDescription_5)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_11)


        self.verticalLayout_33.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_wafermap = QHBoxLayout()
        self.horizontalLayout_wafermap.setObjectName(u"horizontalLayout_wafermap")
        self.horizontalSpacer_wafermap = QSpacerItem(40, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_wafermap.addItem(self.horizontalSpacer_wafermap)

        self.verticalLayout_wafermap = QVBoxLayout()
        self.verticalLayout_wafermap.setObjectName(u"verticalLayout_wafermap")

        self.horizontalLayout_wafermap.addLayout(self.verticalLayout_wafermap)


        self.verticalLayout_33.addLayout(self.horizontalLayout_wafermap)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_2)


        self.horizontalLayout_17.addLayout(self.verticalLayout_33)

        self.stk_wafermap.addWidget(self.wafermap)

        self.horizontalLayout_8.addWidget(self.stk_wafermap)


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
        self.cmbParametersBBDD_2 = CheckableComboBox(self.layoutWidget)
        self.cmbParametersBBDD_2.setObjectName(u"cmbParametersBBDD_2")
        self.cmbParametersBBDD_2.setEnabled(True)
        self.cmbParametersBBDD_2.setMinimumSize(QSize(100, 0))
        self.cmbParametersBBDD_2.setMaximumSize(QSize(300, 16777215))
        self.cmbParametersBBDD_2.setFont(font)
        self.cmbParametersBBDD_2.setAutoFillBackground(False)
        self.cmbParametersBBDD_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbParametersBBDD_2.setEditable(True)
        self.cmbParametersBBDD_2.setCurrentText(u"Select instrument")
        self.cmbParametersBBDD_2.setIconSize(QSize(16, 16))
        self.cmbParametersBBDD_2.setFrame(True)

        self.gridLayout_5.addWidget(self.cmbParametersBBDD_2, 7, 1, 1, 2)

        self.cmbRunsConsult = CheckableComboBox(self.layoutWidget)
        self.cmbRunsConsult.setObjectName(u"cmbRunsConsult")
        self.cmbRunsConsult.setEnabled(True)
        self.cmbRunsConsult.setMinimumSize(QSize(100, 0))
        self.cmbRunsConsult.setMaximumSize(QSize(300, 16777215))
        self.cmbRunsConsult.setFont(font)
        self.cmbRunsConsult.setAutoFillBackground(False)
        self.cmbRunsConsult.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbRunsConsult.setEditable(True)
        self.cmbRunsConsult.setCurrentText(u"Select instrument")
        self.cmbRunsConsult.setIconSize(QSize(16, 16))
        self.cmbRunsConsult.setFrame(True)

        self.gridLayout_5.addWidget(self.cmbRunsConsult, 3, 1, 1, 2)

        self.cmbTechnologyConsult = CheckableComboBox(self.layoutWidget)
        self.cmbTechnologyConsult.setObjectName(u"cmbTechnologyConsult")
        self.cmbTechnologyConsult.setEnabled(True)
        self.cmbTechnologyConsult.setMinimumSize(QSize(100, 0))
        self.cmbTechnologyConsult.setMaximumSize(QSize(300, 16777215))
        self.cmbTechnologyConsult.setFont(font)
        self.cmbTechnologyConsult.setAutoFillBackground(False)
        self.cmbTechnologyConsult.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbTechnologyConsult.setEditable(True)
        self.cmbTechnologyConsult.setCurrentText(u"Select instrument")
        self.cmbTechnologyConsult.setIconSize(QSize(16, 16))
        self.cmbTechnologyConsult.setFrame(True)

        self.gridLayout_5.addWidget(self.cmbTechnologyConsult, 1, 1, 1, 2)

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

        self.cmbWafersConsult = CheckableComboBox(self.layoutWidget)
        self.cmbWafersConsult.addItem("")
        self.cmbWafersConsult.setObjectName(u"cmbWafersConsult")
        self.cmbWafersConsult.setEnabled(True)
        self.cmbWafersConsult.setMinimumSize(QSize(100, 0))
        self.cmbWafersConsult.setMaximumSize(QSize(300, 16777215))
        self.cmbWafersConsult.setFont(font)
        self.cmbWafersConsult.setAutoFillBackground(False)
        self.cmbWafersConsult.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cmbWafersConsult.setEditable(True)
        self.cmbWafersConsult.setCurrentText(u"All wafers")
        self.cmbWafersConsult.setIconSize(QSize(16, 16))
        self.cmbWafersConsult.setFrame(True)

        self.gridLayout_5.addWidget(self.cmbWafersConsult, 5, 1, 1, 2)

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
        self.next_histogram_3.setIcon(icon17)

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
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        self.ListWafers.setFont(font3)
        self.ListWafers.setAutoFillBackground(False)
        self.ListWafers.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.ListWafers, 1, 4, 7, 1)

        self.btnConsult = QPushButton(self.layoutWidget)
        self.btnConsult.setObjectName(u"btnConsult")
        self.btnConsult.setMinimumSize(QSize(120, 30))
        self.btnConsult.setMaximumSize(QSize(120, 16777215))
        self.btnConsult.setFont(font)
        self.btnConsult.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnConsult.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btnConsult.setIcon(icon12)

        self.gridLayout_5.addWidget(self.btnConsult, 9, 1, 1, 1)


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
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        self.btnSaveDescription_4.setIcon(icon15)
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
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        self.btnCopyDescription_4.setIcon(icon18)

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
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        self.btnClearDescription_6.setIcon(icon13)
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
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        self.next_histogram_2.setIcon(icon17)

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
"	border-radius: 5px;	\n"
"	background-color:rgb(40, 44, 52);\n"
"	border: 2px solid rgb(40, 44, 52);\n"
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
        self.btnClearDescription_8.setIcon(icon13)
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
        icon19 = QIcon()
        icon19.addFile(u":/icons/images/icons/cil-cloud-upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnUploadFiles.setIcon(icon19)

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
        self.btnOpenWafermapFileInbase.setIcon(icon14)

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
        self.btnOpenDataFileInbase.setIcon(icon14)

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
        self.btnSaveImportReport.setIcon(icon15)
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
        self.btnClearImportReport.setIcon(icon13)
        self.btnClearImportReport.setFlat(False)

        self.horizontalLayout_31.addWidget(self.btnClearImportReport)


        self.verticalLayout_42.addLayout(self.horizontalLayout_31)

        self.txtImportReport = QPlainTextEdit(self.inbase)
        self.txtImportReport.setObjectName(u"txtImportReport")
        self.txtImportReport.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_42.addWidget(self.txtImportReport)


        self.verticalLayout_23.addLayout(self.verticalLayout_42)

        self.stackedWidget.addWidget(self.inbase)
        self.directories_window = QWidget()
        self.directories_window.setObjectName(u"directories_window")
        self.gridLayoutWidget_2 = QWidget(self.directories_window)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 521, 411))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_values_directory = QPushButton(self.gridLayoutWidget_2)
        self.btn_values_directory.setObjectName(u"btn_values_directory")
        self.btn_values_directory.setMinimumSize(QSize(120, 30))
        self.btn_values_directory.setMaximumSize(QSize(120, 30))
        self.btn_values_directory.setFont(font)
        self.btn_values_directory.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_values_directory.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_values_directory.setIcon(icon14)

        self.gridLayout_6.addWidget(self.btn_values_directory, 2, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)

        self.txt_values_directory = QLineEdit(self.gridLayoutWidget_2)
        self.txt_values_directory.setObjectName(u"txt_values_directory")
        self.txt_values_directory.setEnabled(False)
        self.txt_values_directory.setMinimumSize(QSize(300, 30))
        self.txt_values_directory.setMaximumSize(QSize(300, 30))
        self.txt_values_directory.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_6.addWidget(self.txt_values_directory, 2, 0, 1, 1)

        self.labelVersion_25 = QLabel(self.gridLayoutWidget_2)
        self.labelVersion_25.setObjectName(u"labelVersion_25")
        self.labelVersion_25.setMaximumSize(QSize(200, 20))
        self.labelVersion_25.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_25.setLineWidth(1)
        self.labelVersion_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelVersion_25, 1, 0, 1, 1)

        self.labelVersion_34 = QLabel(self.gridLayoutWidget_2)
        self.labelVersion_34.setObjectName(u"labelVersion_34")
        self.labelVersion_34.setMaximumSize(QSize(200, 20))
        self.labelVersion_34.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_34.setLineWidth(1)
        self.labelVersion_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelVersion_34, 3, 0, 1, 1)

        self.btn_wafermap_directory = QPushButton(self.gridLayoutWidget_2)
        self.btn_wafermap_directory.setObjectName(u"btn_wafermap_directory")
        self.btn_wafermap_directory.setMinimumSize(QSize(120, 30))
        self.btn_wafermap_directory.setMaximumSize(QSize(120, 30))
        self.btn_wafermap_directory.setFont(font)
        self.btn_wafermap_directory.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_wafermap_directory.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_wafermap_directory.setIcon(icon14)

        self.gridLayout_6.addWidget(self.btn_wafermap_directory, 4, 1, 1, 1)

        self.btn_results_directory = QPushButton(self.gridLayoutWidget_2)
        self.btn_results_directory.setObjectName(u"btn_results_directory")
        self.btn_results_directory.setMinimumSize(QSize(120, 30))
        self.btn_results_directory.setMaximumSize(QSize(120, 30))
        self.btn_results_directory.setFont(font)
        self.btn_results_directory.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_results_directory.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_results_directory.setIcon(icon14)

        self.gridLayout_6.addWidget(self.btn_results_directory, 6, 1, 1, 1)

        self.btn_graph_directory = QPushButton(self.gridLayoutWidget_2)
        self.btn_graph_directory.setObjectName(u"btn_graph_directory")
        self.btn_graph_directory.setMinimumSize(QSize(120, 30))
        self.btn_graph_directory.setMaximumSize(QSize(120, 30))
        self.btn_graph_directory.setFont(font)
        self.btn_graph_directory.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_graph_directory.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_graph_directory.setIcon(icon14)

        self.gridLayout_6.addWidget(self.btn_graph_directory, 8, 1, 1, 1)

        self.labelVersion_32 = QLabel(self.gridLayoutWidget_2)
        self.labelVersion_32.setObjectName(u"labelVersion_32")
        self.labelVersion_32.setMaximumSize(QSize(200, 20))
        self.labelVersion_32.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_32.setLineWidth(1)
        self.labelVersion_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelVersion_32, 7, 0, 1, 1)

        self.labelVersion_30 = QLabel(self.gridLayoutWidget_2)
        self.labelVersion_30.setObjectName(u"labelVersion_30")
        self.labelVersion_30.setMaximumSize(QSize(200, 20))
        self.labelVersion_30.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_30.setLineWidth(1)
        self.labelVersion_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelVersion_30, 5, 0, 1, 1)

        self.txt_results_directory = QLineEdit(self.gridLayoutWidget_2)
        self.txt_results_directory.setObjectName(u"txt_results_directory")
        self.txt_results_directory.setEnabled(False)
        self.txt_results_directory.setMinimumSize(QSize(300, 30))
        self.txt_results_directory.setMaximumSize(QSize(300, 30))
        self.txt_results_directory.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_6.addWidget(self.txt_results_directory, 6, 0, 1, 1)

        self.txt_wafermap_directory = QLineEdit(self.gridLayoutWidget_2)
        self.txt_wafermap_directory.setObjectName(u"txt_wafermap_directory")
        self.txt_wafermap_directory.setEnabled(False)
        self.txt_wafermap_directory.setMinimumSize(QSize(300, 30))
        self.txt_wafermap_directory.setMaximumSize(QSize(300, 30))
        self.txt_wafermap_directory.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_6.addWidget(self.txt_wafermap_directory, 4, 0, 1, 1)

        self.txt_graph_directory = QLineEdit(self.gridLayoutWidget_2)
        self.txt_graph_directory.setObjectName(u"txt_graph_directory")
        self.txt_graph_directory.setEnabled(False)
        self.txt_graph_directory.setMinimumSize(QSize(300, 30))
        self.txt_graph_directory.setMaximumSize(QSize(300, 30))
        self.txt_graph_directory.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_6.addWidget(self.txt_graph_directory, 8, 0, 1, 1)

        self.stackedWidget.addWidget(self.directories_window)

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
        self.btnDirectory = QPushButton(self.topMenus)
        self.btnDirectory.setObjectName(u"btnDirectory")
        sizePolicy1.setHeightForWidth(self.btnDirectory.sizePolicy().hasHeightForWidth())
        self.btnDirectory.setSizePolicy(sizePolicy1)
        self.btnDirectory.setMinimumSize(QSize(0, 45))
        self.btnDirectory.setFont(font)
        self.btnDirectory.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDirectory.setLayoutDirection(Qt.LeftToRight)
        self.btnDirectory.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btnDirectory)

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
        self.optionsESTEPA.setCurrentIndex(0)
        self.stk_loadfiles.setCurrentIndex(0)
        self.opt_clear.setCurrentIndex(1)
        self.stk_results.setCurrentIndex(0)
        self.stk_graph.setCurrentIndex(0)
        self.stk_wafermap.setCurrentIndex(1)
        self.optionsHistorical.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.topLogo.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
#if QT_CONFIG(tooltip)
        self.btn_page_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.btn_page_estepa.setToolTip(QCoreApplication.translate("MainWindow", u"Analyze", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_estepa.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
#if QT_CONFIG(tooltip)
        self.btn_page_consult.setToolTip(QCoreApplication.translate("MainWindow", u"Consult", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_consult.setText(QCoreApplication.translate("MainWindow", u"Consult Database", None))
#if QT_CONFIG(tooltip)
        self.btn_page_inbase.setToolTip(QCoreApplication.translate("MainWindow", u"Upload to BBDD", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_inbase.setText(QCoreApplication.translate("MainWindow", u"Upload files to BBDD", None))
#if QT_CONFIG(tooltip)
        self.btn_page_reports.setToolTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_reports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Options", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.txtGraphTheme.setText(QCoreApplication.translate("MainWindow", u"Graph theme:", None))
        self.chk_theme.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
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
        self.lbl_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.home_analysis.setText(QCoreApplication.translate("MainWindow", u"Start Analysis", None))
        self.home_consult.setText(QCoreApplication.translate("MainWindow", u"Consult", None))
        self.home_upload.setText(QCoreApplication.translate("MainWindow", u"Upload Files to BBDD", None))
        self.home_upload_2.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.lbl_logo.setText("")
        self.lbl_welcome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">	Welcome to</span></p></body></html>", None))
        self.lbl_estepa.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:590;\">ESTEPA<br/></span></p></body></html>", None))
        self.lbl_options.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.btn_ppg_8.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.btn_ppg_6.setText(QCoreApplication.translate("MainWindow", u"Open Directory", None))
        self.btn_ppg_7.setText(QCoreApplication.translate("MainWindow", u"Examples", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"STATISTICS for the PARAMETRIC TEST", None))
        self.optLoadFiles.setText(QCoreApplication.translate("MainWindow", u"Load from files", None))
        self.optLoadBBDD.setText(QCoreApplication.translate("MainWindow", u"Load from BBDD", None))
        self.btnCorrelationFiles.setText(QCoreApplication.translate("MainWindow", u"Correlation", None))
        self.btnAnalyzeFiles.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.lbl_select.setText(QCoreApplication.translate("MainWindow", u"Select parameters", None))
        self.cmbParametersFile.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

#if QT_CONFIG(tooltip)
        self.btn_clear_all.setToolTip(QCoreApplication.translate("MainWindow", u"Clear All", None))
#endif // QT_CONFIG(tooltip)
        self.btn_clear_all.setText("")
        self.btnOpenWafermapFile.setText("")
        self.txtWafermapFile.setText("")
        self.txtWafermapFile.setPlaceholderText("")
        self.lbl_data.setText(QCoreApplication.translate("MainWindow", u"Load DATA file", None))
        self.txtDataFile.setText("")
        self.txtDataFile.setPlaceholderText("")
        self.lbl_wafer.setText(QCoreApplication.translate("MainWindow", u"Load WAFERMAP file", None))
        self.btnLoadFiles.setText(QCoreApplication.translate("MainWindow", u"Load from files", None))
        self.btnOpenDataFile.setText("")
        self.cmbWafers.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbWafers.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.lbl_yech.setText(QCoreApplication.translate("MainWindow", u"Select technology", None))
        self.btnCorrelationBBDD.setText(QCoreApplication.translate("MainWindow", u"Correlation", None))
        self.cmbTechnology.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbTechnology.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.lbl_run.setText(QCoreApplication.translate("MainWindow", u"Select run", None))
        self.cmbRuns.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbRuns.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.lbl_wfer.setText(QCoreApplication.translate("MainWindow", u"Select wafer", None))
        self.btnAnalyzeBBDD.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.lbl_params.setText(QCoreApplication.translate("MainWindow", u"Select parameters", None))
        self.cmbParametersBBDD.setItemText(0, QCoreApplication.translate("MainWindow", u"Select instrument", None))

        self.cmbParametersBBDD.setCurrentText(QCoreApplication.translate("MainWindow", u"Select instrument", None))
        self.lbl_datavalues.setText(QCoreApplication.translate("MainWindow", u"DATA VALUES", None))
#if QT_CONFIG(tooltip)
        self.btnSaveDescription_2.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.btnSaveDescription_2.setText("")
#if QT_CONFIG(tooltip)
        self.btnCopyDescription_2.setToolTip(QCoreApplication.translate("MainWindow", u"Copy", None))
#endif // QT_CONFIG(tooltip)
        self.btnCopyDescription_2.setText("")
        self.cmbCurrentParameter.setItemText(0, QCoreApplication.translate("MainWindow", u"Parameter", None))

        self.cmbCurrentParameter.setCurrentText(QCoreApplication.translate("MainWindow", u"Parameter", None))
        self.btnNextParam.setText("")
#if QT_CONFIG(tooltip)
        self.txtLoadedValues.setToolTip(QCoreApplication.translate("MainWindow", u"Data values", None))
#endif // QT_CONFIG(tooltip)
        self.txtLoadedValues.setPlainText("")
        self.lbl_parameters_results.setText(QCoreApplication.translate("MainWindow", u"PARAMETERS RESULT", None))
#if QT_CONFIG(tooltip)
        self.btnSaveDescription_3.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.btnSaveDescription_3.setText("")
#if QT_CONFIG(tooltip)
        self.btnCopyDescription_3.setToolTip(QCoreApplication.translate("MainWindow", u"Copy", None))
#endif // QT_CONFIG(tooltip)
        self.btnCopyDescription_3.setText("")
#if QT_CONFIG(tooltip)
        self.txtParametersResult.setToolTip(QCoreApplication.translate("MainWindow", u"Results parameters", None))
#endif // QT_CONFIG(tooltip)
        self.txtParametersResult.setPlainText("")
        self.lbl_graph.setText(QCoreApplication.translate("MainWindow", u"GRAPH", None))
        self.lbl_wafermap_2.setText(QCoreApplication.translate("MainWindow", u"WAFERMAP", None))
#if QT_CONFIG(tooltip)
        self.btnSaveDescription_5.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.btnSaveDescription_5.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CONSULT DATA BASE", None))
        self.optWafers.setText(QCoreApplication.translate("MainWindow", u"Wafers", None))
        self.historicalcheck.setText(QCoreApplication.translate("MainWindow", u"Historical", None))
        self.optRuns.setText(QCoreApplication.translate("MainWindow", u"Runs", None))
        self.btnValues.setText(QCoreApplication.translate("MainWindow", u"Values", None))
        self.btnYield.setText(QCoreApplication.translate("MainWindow", u"Yield", None))
        self.labelVersion_26.setText(QCoreApplication.translate("MainWindow", u"Select technology", None))
        self.labelVersion_29.setText(QCoreApplication.translate("MainWindow", u"Select parameters", None))
        self.labelVersion_27.setText(QCoreApplication.translate("MainWindow", u"Select run", None))
        self.cmbWafersConsult.setItemText(0, QCoreApplication.translate("MainWindow", u"All wafers", None))

        self.labelVersion_28.setText(QCoreApplication.translate("MainWindow", u"Select wafer", None))
#if QT_CONFIG(tooltip)
        self.next_histogram_3.setToolTip(QCoreApplication.translate("MainWindow", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.next_histogram_3.setText("")
        self.labelVersion_31.setText(QCoreApplication.translate("MainWindow", u"WAFERS", None))
        self.btnConsult.setText(QCoreApplication.translate("MainWindow", u"Consult", None))
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
        self.btn_values_directory.setText(QCoreApplication.translate("MainWindow", u"Set Directory", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"USER DIRECTORIES", None))
        self.txt_values_directory.setText("")
        self.txt_values_directory.setPlaceholderText("")
        self.labelVersion_25.setText(QCoreApplication.translate("MainWindow", u"VALUES Directory", None))
        self.labelVersion_34.setText(QCoreApplication.translate("MainWindow", u"WAFERMAP Directory", None))
        self.btn_wafermap_directory.setText(QCoreApplication.translate("MainWindow", u"Set Directory", None))
        self.btn_results_directory.setText(QCoreApplication.translate("MainWindow", u"Set Directory", None))
        self.btn_graph_directory.setText(QCoreApplication.translate("MainWindow", u"Set Directory", None))
        self.labelVersion_32.setText(QCoreApplication.translate("MainWindow", u"GRAPH Directory", None))
        self.labelVersion_30.setText(QCoreApplication.translate("MainWindow", u"RESULTS Directory", None))
        self.txt_results_directory.setText("")
        self.txt_results_directory.setPlaceholderText("")
        self.txt_wafermap_directory.setText("")
        self.txt_wafermap_directory.setPlaceholderText("")
        self.txt_graph_directory.setText("")
        self.txt_graph_directory.setPlaceholderText("")
        self.btnDirectory.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v7.1", None))
    # retranslateUi

