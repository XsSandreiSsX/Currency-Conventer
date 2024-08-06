# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QWidget)
import app_icons


class Ui_CurrencyConventer(object):
    def setupUi(self, CurrencyConventer):
        if not CurrencyConventer.objectName():
            CurrencyConventer.setObjectName(u"CurrencyConventer")
        CurrencyConventer.setEnabled(True)
        CurrencyConventer.setFixedSize(500, 600)
        font = QFont()
        font.setFamilies([u"quicksand"])
        font.setPointSize(25)
        icon = QIcon()
        icon.addFile(u":/icons/icons/main_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        CurrencyConventer.setFont(font)
        CurrencyConventer.setStyleSheet(u"font-family: \"quicksand\";\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:2, x2:1, y2:0, stop:0 rgba(57, 66, 83, 1), stop:1 rgba(24, 28, 39, 1))")
        CurrencyConventer.setWindowFilePath(u"")
        self.centralwidget = QWidget(CurrencyConventer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Currency_Line_Top = QLineEdit(self.centralwidget)
        self.Currency_Line_Top.setObjectName(u"Currency_Line_Top")
        self.Currency_Line_Top.setGeometry(QRect(145, 245, 150, 30))
        self.Currency_Line_Top.setStyleSheet(u"QLineEdit{\n"
                                             "	background: rgba(24, 28, 39, 0.5);\n"
                                             "	border: 1px solid rgba(24, 28, 39, 0.5);\n"
                                             "	border-top-left-radius: 6px;\n"
                                             "	border-bottom-left-radius: 6px;\n"
                                             "}\n"
                                             "QLineEdit:focus{\n"
                                             "	border: 1px solid rgb(48, 186, 143)\n"
                                             "}\n"
                                             "")
        self.Currency_Line_Bottom = QLineEdit(self.centralwidget)
        self.Currency_Line_Bottom.setObjectName(u"Currency_Line_Bottom")
        self.Currency_Line_Bottom.setGeometry(QRect(145, 325, 150, 30))
        self.Currency_Line_Bottom.setStyleSheet(u"background: rgba(24, 28, 39, 0.5);\n"
                                                "border: 1px solid rgba(24, 28, 39, 0.5);\n"
                                                "border-top-left-radius: 6px;\n"
                                                "border-bottom-left-radius: 6px;\n")
        self.Currency_Box_Top = QComboBox(self.centralwidget)
        self.Currency_Box_Top.setObjectName(u"Currency_Box_Top")
        self.Currency_Box_Top.setGeometry(QRect(295, 245, 60, 30))
        self.Currency_Box_Top.setStyleSheet(u"QComboBox{\n"
                                            "   background: rgba(24, 28, 39, 0.8);\n"
                                            "	border: 1px rgba(24, 28, 39, 0.8);\n"
                                            "	border-top-right-radius: 6px;\n"
                                            "	border-bottom-right-radius: 6px;\n"
                                            "}\n"
                                            "QComboBox:editable{\n"
                                            "	background: rgba(24, 28, 39, 0.8);\n"
                                            "}\n"
                                            "QComboBox::drop-down{\n"
                                            "	border: 1px rgba(24, 28, 39, 0.8);\n"
                                            "}\n"
                                            "QComboBox::down-arrow {\n"
                                            "	image: url(:/icons/icons/expand_more.svg);\n"
                                            "	image-size: 60px;\n"
                                            "	width: 80px;\n"
                                            "	height: 20px;\n"
                                            "	margin-right: 7px;\n"
                                            "}")
        self.Currency_Box_Bottom = QComboBox(self.centralwidget)
        self.Currency_Box_Bottom.setObjectName(u"Currency_Box_Bottom")
        self.Currency_Box_Bottom.setGeometry(QRect(295, 325, 60, 30))
        self.Currency_Box_Bottom.setStyleSheet(u"QComboBox{\n"
                                               "	background: rgba(24, 28, 39, 0.8);\n"
                                               "	border: 1px rgba(24, 28, 39, 0.8);\n"
                                               "	border-top-right-radius: 6px;\n"
                                               "	border-bottom-right-radius: 6px;\n"
                                               "}\n"
                                               "QComboBox:editable{\n"
                                               "	background: rgba(24, 28, 39, 0.8);\n"
                                               "}\n"
                                               "QComboBox::drop-down{\n"
                                               "	border: 1px rgba(24, 28, 39, 0.8);\n"
                                               "}\n"
                                               "QComboBox::down-arrow {\n"
                                               "	image: url(:/icons/icons/expand_more.svg);\n"
                                               "	image-size: 60px;\n"
                                               "	width: 80px;\n"
                                               "	height: 20px;\n"
                                               "	margin-right: 7px;\n"
                                               "}")
        self.Main_Text = QLabel(self.centralwidget)
        self.Main_Text.setObjectName(u"Main_Text")
        self.Main_Text.setGeometry(QRect(35, 40, 293, 38))
        font1 = QFont()
        font1.setFamilies([u"quicksand"])
        font1.setPointSize(20)
        self.Main_Text.setFont(font1)
        self.Main_Text.setStyleSheet(u"background: none;")
        self.Convert_Text = QLabel(self.centralwidget)
        self.Convert_Text.setObjectName(u"Convert_Text")
        self.Convert_Text.setGeometry(QRect(59, 118, 261, 25))
        font2 = QFont()
        font2.setFamilies([u"quicksand"])
        font2.setPointSize(15)
        self.Convert_Text.setFont(font2)
        self.Convert_Text.setStyleSheet(u"background: none;")
        self.Review_Image = QLabel(self.centralwidget)
        self.Review_Image.setObjectName(u"Review_Image")
        self.Review_Image.setGeometry(QRect(35, 546, 24, 24))
        self.Review_Image.setStyleSheet(u"background: none;")
        self.Review_Image.setPixmap(QPixmap(u":/icons/icons/mark_chat_unread.svg"))
        self.Review_Button = QPushButton(self.centralwidget)
        self.Review_Button.setObjectName(u"Review_Button")
        self.Review_Button.setGeometry(QRect(60, 550, 88, 15))
        self.Review_Button.setStyleSheet(u"QPushButton{\n"
                                         "   border: none;\n"
                                         "   background: none;\n"
                                         "}\n"
                                         "   QPushButton:hover{\n"
                                         "   background: rgb(48, 186, 143);\n"
                                         "}")
        self.Internet_Status_Image = QLabel(self.centralwidget)
        self.Internet_Status_Image.setObjectName(u"Internet_Status_Image")
        self.Internet_Status_Image.setGeometry(QRect(430, 546, 24, 24))
        self.Internet_Status_Image.setStyleSheet(u"background: none;")
        self.Internet_Status_Image.setPixmap(QPixmap(u":/icons/icons/wifi_on.svg"))
        self.Internet_Status = QLabel(self.centralwidget)
        self.Internet_Status.setObjectName(u"Internet_Status")
        self.Internet_Status.setGeometry(QRect(315, 550, 110, 15))
        font3 = QFont()
        font3.setFamilies([u"quicksand"])
        font3.setPointSize(9)
        font3.setHintingPreference(QFont.PreferDefaultHinting)
        self.Internet_Status.setFont(font3)
        self.Internet_Status.setStyleSheet(u"background: none;")
        self.Internet_Status.setFrameShape(QFrame.Shape.NoFrame)
        self.Internet_Status.setFrameShadow(QFrame.Shadow.Plain)
        self.Internet_Note = QLabel(self.centralwidget)
        self.Internet_Note.setObjectName(u"Internet_Note")
        self.Internet_Note.setEnabled(False)
        self.Internet_Note.setVisible(False)
        self.Internet_Note.setGeometry(QRect(300, 570, 141, 15))
        self.Internet_Note.setFont(font3)
        self.Internet_Note.setStyleSheet(u"background: none;\n"
                                         "color: rgba(255,0,51,1);\n"
                                         "")
        self.Internet_Note.setFrameShape(QFrame.Shape.NoFrame)
        self.Internet_Note.setFrameShadow(QFrame.Shadow.Plain)
        CurrencyConventer.setCentralWidget(self.centralwidget)

        self.retranslateUi(CurrencyConventer)

        QMetaObject.connectSlotsByName(CurrencyConventer)

    # setupUi

    def retranslateUi(self, CurrencyConventer):
        CurrencyConventer.setWindowTitle(
            QCoreApplication.translate("CurrencyConventer", u"Currency Conventer | Version 1.0", None))
        self.Currency_Line_Top.setText("")
        self.Currency_Line_Bottom.setText("")
        self.Main_Text.setText(QCoreApplication.translate("CurrencyConventer", u"Currency Conventer!", None))
        self.Review_Image.setText("")
        self.Review_Button.setText(QCoreApplication.translate("CurrencyConventer", u"Leave a review", None))
        self.Internet_Status_Image.setText("")
        self.Internet_Status.setText(QCoreApplication.translate("CurrencyConventer", u"connection active\n"
                                                                                     "", None))
        self.Internet_Note.setText(QCoreApplication.translate("CurrencyConventer", u"outdated course is used\n"
                                                                                   "", None))
    # retranslateUi
