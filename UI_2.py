# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from preprocess import *
from feature import *
from model import *
from PandasModel import *

class Ui_Form(object):
        def __init__(self):
                self.Data_Pre = None
                self.Train_Feature = None
                self.Test_Feature = None
                self.Model = None
                self.list_feature = []
                self.text_input = None

        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.setEnabled(True)
                Form.resize(741, 599)
                font = QtGui.QFont()
                font.setFamily("Batang")
                font.setBold(False)
                font.setWeight(50)
                Form.setFont(font)
                Form.setWindowTitle("Poker Hand Prediction with Machine Learning")
                Form.setStyleSheet("QWidget{\n"
        "    \n"
        "    background-color: #ffffff;\n"
        "}")
                self.label = QtWidgets.QLabel(Form)
                self.label.setGeometry(QtCore.QRect(60, 40, 311, 21))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label.setFont(font)
                self.label.setStyleSheet("#label{\n"
        "    color: #263238;\n"
        "    font: 20pt;\n"
        "}\n"
        "QLabel{\n"
        "    font:\"Helvetica Neue\";\n"
        "}\n"
        "")
                self.label.setObjectName("label")
                self.tabWidget = QtWidgets.QTabWidget(Form)
                self.tabWidget.setEnabled(True)
                self.tabWidget.setGeometry(QtCore.QRect(50, 112, 651, 811))
                self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
        "    background: white;\n"
        "border-style: outset;\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar:top {\n"
        "    top: 1px;\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar:bottom {\n"
        "    bottom: 1px;\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar:left {\n"
        "    right: 1px;\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar:right {\n"
        "    left: 1px;\n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "    color: #263238;\n"
        "}\n"
        "\n"
        "QTabBar::tab:!selected {\n"
        "    color: #78909c;\n"
        "}\n"
        "\n"
        "QTabBar::tab:!selected:hover {\n"
        "    color: #03a9f4;\n"
        "}\n"
        "\n"
        "QTabBar::tab:top:!selected {\n"
        "    margin-top: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:bottom:!selected {\n"
        "    margin-bottom: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:top, QTabBar::tab:bottom {\n"
        "    min-width: 8ex;\n"
        "    margin-right: -1px;\n"
        "    padding: 5px 10px 5px 10px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:top:selected {\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QTabBar::tab:bottom:selected {\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
        "QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
        "    margin-right: 0;\n"
        "}\n"
        "\n"
        "QTabBar::tab:left:!selected {\n"
        "    margin-right: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:right:!selected {\n"
        "    margin-left: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:left, QTabBar::tab:right {\n"
        "    min-height: 8ex;\n"
        "    margin-bottom: -1px;\n"
        "    padding: 10px 5px 10px 5px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:left:selected {\n"
        "   border-style: outset;\n"
        "}\n"
        "\n"
        "QTabBar::tab:right:selected {\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
        "QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
        "    margin-bottom: 0;\n"
        "}")
                self.tabWidget.setObjectName("tabWidget")
                self.Tab1 = QtWidgets.QWidget()
                self.Tab1.setEnabled(True)
                font = QtGui.QFont()
                font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                self.Tab1.setFont(font)
                self.Tab1.setObjectName("Tab1")
                self.line_2 = QtWidgets.QFrame(self.Tab1)
                self.line_2.setGeometry(QtCore.QRect(5, 0, 118, 3))
                self.line_2.setStyleSheet("background-color: #03a9f4;")
                self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                self.label_6 = QtWidgets.QLabel(self.Tab1)
                self.label_6.setGeometry(QtCore.QRect(50, 70, 231, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("#label_6{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    \n"
        "}")
                self.label_6.setObjectName("label_6")
                self.pushButton = QtWidgets.QPushButton(self.Tab1)
                self.pushButton.setGeometry(QtCore.QRect(50, 340, 251, 31))
                self.pushButton.setStyleSheet("QPushButton {\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(31, 187, 228, 255), stop:1 rgba(40, 233, 224, 255));\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "    border-radius: 4px;\n"
        "    font: bold 14px;\n"
        "    min-width: 10em;\n"
        "    padding: 6px;\n"
        "    color: #ffffff;\n"
        "    font: 13pt \"Helvetica Neue\";\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #2980b9;\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "\n"
        "}")
                self.pushButton.setObjectName("pushButton")
                self.graphicsView_4 = QtWidgets.QGraphicsView(self.Tab1)
                self.graphicsView_4.setGeometry(QtCore.QRect(10, 40, 621, 391))
                self.graphicsView_4.setStyleSheet("QGraphicsView{\n"
        "    border: 2px solid #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.graphicsView_4.setObjectName("graphicsView_4")
                self.pushButton_2 = QtWidgets.QPushButton(self.Tab1)
                self.pushButton_2.setGeometry(QtCore.QRect(330, 340, 261, 31))
                self.pushButton_2.setStyleSheet("QPushButton {\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(31, 187, 228, 255), stop:1 rgba(40, 233, 224, 255));\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "    border-radius: 4px;\n"
        "    font: bold 14px;\n"
        "    min-width: 10em;\n"
        "    padding: 6px;\n"
        "    color: #ffffff;\n"
        "    font: 13pt \"Helvetica Neue\";\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #2980b9;\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "\n"
        "}")
                self.pushButton_2.setObjectName("pushButton_2")
                self.tableView = QtWidgets.QTableView(self.Tab1)
                self.tableView.setGeometry(QtCore.QRect(50, 120, 541, 211))
                self.tableView.setStyleSheet("QTableView{\n"
        "    border: 2px solid #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.tableView.setObjectName("tableView")
                self.graphicsView_4.raise_()
                self.line_2.raise_()
                self.label_6.raise_()
                self.pushButton.raise_()
                self.pushButton_2.raise_()
                self.tableView.raise_()
                self.tabWidget.addTab(self.Tab1, "")
                self.Tab2 = QtWidgets.QWidget()
                self.Tab2.setObjectName("Tab2")
                self.line_4 = QtWidgets.QFrame(self.Tab2)
                self.line_4.setGeometry(QtCore.QRect(135, 0, 148, 3))
                self.line_4.setStyleSheet("background-color: #03a9f4;")
                self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_4.setObjectName("line_4")
                self.graphicsView_18 = QtWidgets.QGraphicsView(self.Tab2)
                self.graphicsView_18.setGeometry(QtCore.QRect(10, 40, 621, 391))
                self.graphicsView_18.setStyleSheet("QGraphicsView{\n"
        "    border: 2px solid #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.graphicsView_18.setObjectName("graphicsView_18")
                self.label_66 = QtWidgets.QLabel(self.Tab2)
                self.label_66.setGeometry(QtCore.QRect(40, 70, 241, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_66.setFont(font)
                self.label_66.setStyleSheet("#label_66{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    \n"
        "}")
                self.label_66.setObjectName("label_66")
                self.pushButton_6 = QtWidgets.QPushButton(self.Tab2)
                self.pushButton_6.setGeometry(QtCore.QRect(30, 330, 281, 31))
                self.pushButton_6.setStyleSheet("QPushButton {\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(31, 187, 228, 255), stop:1 rgba(40, 233, 224, 255));\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "    border-radius: 4px;\n"
        "    font: bold 14px;\n"
        "    min-width: 10em;\n"
        "    padding: 6px;\n"
        "    color: #ffffff;\n"
        "    font: 13pt \"Helvetica Neue\";\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #2980b9;\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "\n"
        "}")
                self.pushButton_6.setObjectName("pushButton_6")
                self.checkBox = QtWidgets.QCheckBox(self.Tab2)
                self.checkBox.setGeometry(QtCore.QRect(40, 110, 171, 20))
                self.checkBox.setStyleSheet("QCheckBox{\n"
        "    font:\"Helvetica Neue\";\n"
        "    \n"
        "}")
                self.checkBox.setObjectName("checkBox")
                self.checkBox_2 = QtWidgets.QCheckBox(self.Tab2)
                self.checkBox_2.setGeometry(QtCore.QRect(170, 110, 171, 20))
                self.checkBox_2.setStyleSheet("QCheckBox{\n"
        "    font:\"Helvetica Neue\";\n"
        "    \n"
        "}")
                self.checkBox_2.setObjectName("checkBox_2")
                self.checkBox_3 = QtWidgets.QCheckBox(self.Tab2)
                self.checkBox_3.setGeometry(QtCore.QRect(310, 110, 271, 20))
                self.checkBox_3.setStyleSheet("QCheckBox{\n"
        "    font:\"Helvetica Neue\";\n"
        "    \n"
        "}")
                self.checkBox_3.setObjectName("checkBox_3")
                self.checkBox_4 = QtWidgets.QCheckBox(self.Tab2)
                self.checkBox_4.setGeometry(QtCore.QRect(40, 150, 171, 20))
                self.checkBox_4.setStyleSheet("QCheckBox{\n"
        "    font:\"Helvetica Neue\";\n"
        "    \n"
        "}")
                self.checkBox_4.setObjectName("checkBox_4")
                self.checkBox_5 = QtWidgets.QCheckBox(self.Tab2)
                self.checkBox_5.setEnabled(True)
                self.checkBox_5.setGeometry(QtCore.QRect(170, 150, 171, 20))
                self.checkBox_5.setStyleSheet("QCheckBox{\n"
        "    font:\"Helvetica Neue\";\n"
        "    \n"
        "}")
                self.checkBox_5.setObjectName("checkBox_5")
                self.checkBox_6 = QtWidgets.QCheckBox(self.Tab2)
                self.checkBox_6.setEnabled(True)
                self.checkBox_6.setGeometry(QtCore.QRect(310, 150, 261, 20))
                self.checkBox_6.setStyleSheet("QCheckBox{\n"
        "    font:\"Helvetica Neue\";\n"
        "    \n"
        "}")
                self.checkBox_6.setObjectName("checkBox_6")
                self.checkBox_7 = QtWidgets.QCheckBox(self.Tab2)
                self.checkBox_7.setEnabled(True)
                self.checkBox_7.setGeometry(QtCore.QRect(460, 150, 161, 20))
                self.checkBox_7.setStyleSheet("QCheckBox{\n"
        "    font:\"Helvetica Neue\";\n"
        "    \n"
        "}")
                self.checkBox_7.setObjectName("checkBox_7")
                self.tableView_2 = QtWidgets.QTableView(self.Tab2)
                self.tableView_2.setGeometry(QtCore.QRect(30, 180, 581, 141))
                self.tableView_2.setStyleSheet("QTableView{\n"
        "    border: 2px solid #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.tableView_2.setObjectName("tableView_2")
                self.pushButton_11 = QtWidgets.QPushButton(self.Tab2)
                self.pushButton_11.setGeometry(QtCore.QRect(330, 330, 281, 31))
                self.pushButton_11.setStyleSheet("QPushButton {\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(31, 187, 228, 255), stop:1 rgba(40, 233, 224, 255));\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "    border-radius: 4px;\n"
        "    font: bold 14px;\n"
        "    min-width: 10em;\n"
        "    padding: 6px;\n"
        "    color: #ffffff;\n"
        "    font: 13pt \"Helvetica Neue\";\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #2980b9;\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "\n"
        "}")
                self.pushButton_11.setObjectName("pushButton_11")
                self.tabWidget.addTab(self.Tab2, "")
                self.Tab3 = QtWidgets.QWidget()
                self.Tab3.setObjectName("Tab3")
                self.line_5 = QtWidgets.QFrame(self.Tab3)
                self.line_5.setGeometry(QtCore.QRect(300, 0, 71, 3))
                self.line_5.setStyleSheet("background-color: #03a9f4;")
                self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_5.setObjectName("line_5")
                self.label_67 = QtWidgets.QLabel(self.Tab3)
                self.label_67.setGeometry(QtCore.QRect(40, 60, 271, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_67.setFont(font)
                self.label_67.setStyleSheet("#label_66{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    \n"
        "}")
                self.label_67.setObjectName("label_67")
                self.graphicsView_19 = QtWidgets.QGraphicsView(self.Tab3)
                self.graphicsView_19.setGeometry(QtCore.QRect(10, 40, 621, 401))
                self.graphicsView_19.setStyleSheet("QGraphicsView{\n"
        "    border: 2px solid #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.graphicsView_19.setObjectName("graphicsView_19")
                self.pushButton_7 = QtWidgets.QPushButton(self.Tab3)
                self.pushButton_7.setGeometry(QtCore.QRect(30, 360, 581, 31))
                self.pushButton_7.setStyleSheet("QPushButton {\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(31, 187, 228, 255), stop:1 rgba(40, 233, 224, 255));\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "    border-radius: 4px;\n"
        "    font: bold 14px;\n"
        "    min-width: 10em;\n"
        "    padding: 6px;\n"
        "    color: #ffffff;\n"
        "    font: 13pt \"Helvetica Neue\";\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #2980b9;\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "\n"
        "}")
                self.pushButton_7.setObjectName("pushButton_7")
                self.radioButton_9 = QtWidgets.QRadioButton(self.Tab3)
                self.radioButton_9.setGeometry(QtCore.QRect(40, 100, 141, 20))
                self.radioButton_9.setStyleSheet("QRadioButton{\n"
        "    font:\"Helvetica Neue\";\n"
        "    \n"
        "}")
                self.radioButton_9.setObjectName("radioButton_9")
                self.plainTextEdit = QtWidgets.QTextEdit(self.Tab3)
                self.plainTextEdit.setGeometry(QtCore.QRect(30, 180, 291, 171))
                self.plainTextEdit.setStyleSheet("#plainTextEdit{\n"
        "    border: 2px solid red;\n"
        "    border-color: #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.plainTextEdit.setObjectName("plainTextEdit")
                self.label_68 = QtWidgets.QLabel(self.Tab3)
                self.label_68.setGeometry(QtCore.QRect(40, 150, 271, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_68.setFont(font)
                self.label_68.setStyleSheet("#label_66{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    \n"
        "}")
                self.label_68.setObjectName("label_68")
                self.radioButton_10 = QtWidgets.QRadioButton(self.Tab3)
                self.radioButton_10.setEnabled(True)
                self.radioButton_10.setGeometry(QtCore.QRect(240, 100, 141, 20))
                self.radioButton_10.setStyleSheet("QRadioButton{\n"
        "    font:\"Helvetica Neue\";\n"
        "    \n"
        "}")
                self.radioButton_10.setObjectName("radioButton_10")
                self.label_72 = QtWidgets.QLabel(self.Tab3)
                self.label_72.setGeometry(QtCore.QRect(330, 60, 271, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_72.setFont(font)
                self.label_72.setStyleSheet("#label_66{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    \n"
        "}")
                self.label_72.setObjectName("label_72")
                self.label_2 = QtWidgets.QLabel(self.Tab3)
                self.label_2.setGeometry(QtCore.QRect(330, 90, 281, 261))
                self.label_2.setStyleSheet("#label_2{\n"
        "    border: 2px solid red;\n"
        "    border-color: #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.label_2.setText("")
                self.label_2.setObjectName("label_2")
                self.graphicsView_19.raise_()
                self.line_5.raise_()
                self.label_67.raise_()
                self.pushButton_7.raise_()
                self.radioButton_9.raise_()
                self.plainTextEdit.raise_()
                self.label_68.raise_()
                self.radioButton_10.raise_()
                self.label_72.raise_()
                self.label_2.raise_()
                self.tabWidget.addTab(self.Tab3, "")
                self.Tab4 = QtWidgets.QWidget()
                self.Tab4.setObjectName("Tab4")
                self.line_7 = QtWidgets.QFrame(self.Tab4)
                self.line_7.setGeometry(QtCore.QRect(387, 0, 80, 3))
                self.line_7.setStyleSheet("background-color: #03a9f4;")
                self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_7.setObjectName("line_7")
                self.graphicsView_20 = QtWidgets.QGraphicsView(self.Tab4)
                self.graphicsView_20.setGeometry(QtCore.QRect(10, 40, 621, 401))
                self.graphicsView_20.setStyleSheet("QGraphicsView{\n"
        "    border: 2px solid #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.graphicsView_20.setObjectName("graphicsView_20")
                self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.Tab4)
                self.plainTextEdit_2.setGeometry(QtCore.QRect(30, 80, 221, 61))
                self.plainTextEdit_2.setStyleSheet("#plainTextEdit_2{\n"
        "    border: 2px solid red;\n"
        "    border-color: #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.plainTextEdit_2.setObjectName("plainTextEdit_2")
                self.label_69 = QtWidgets.QLabel(self.Tab4)
                self.label_69.setGeometry(QtCore.QRect(40, 50, 271, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_69.setFont(font)
                self.label_69.setStyleSheet("#label_66{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    \n"
        "}")
                self.label_69.setObjectName("label_69")
                self.pushButton_8 = QtWidgets.QPushButton(self.Tab4)
                self.pushButton_8.setGeometry(QtCore.QRect(390, 390, 162, 31))
                self.pushButton_8.setStyleSheet("QPushButton {\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(31, 187, 228, 255), stop:1 rgba(40, 233, 224, 255));\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "    border-radius: 4px;\n"
        "    font: bold 14px;\n"
        "    min-width: 10em;\n"
        "    padding: 6px;\n"
        "    color: #ffffff;\n"
        "    font: 13pt \"Helvetica Neue\";\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #2980b9;\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "\n"
        "}")
                self.pushButton_8.setObjectName("pushButton_8")
                self.label_70 = QtWidgets.QLabel(self.Tab4)
                self.label_70.setGeometry(QtCore.QRect(40, 160, 211, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_70.setFont(font)
                self.label_70.setStyleSheet("#label_66{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    \n"
        "}")
                self.label_70.setObjectName("label_70")
                self.plainTextEdit_4 = QtWidgets.QTextEdit(self.Tab4)
                self.plainTextEdit_4.setGeometry(QtCore.QRect(30, 190, 221, 61))
                self.plainTextEdit_4.setStyleSheet("#plainTextEdit_4{\n"
        "    border: 2px solid red;\n"
        "    border-color: #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.plainTextEdit_4.setObjectName("plainTextEdit_4")
                self.label_71 = QtWidgets.QLabel(self.Tab4)
                self.label_71.setGeometry(QtCore.QRect(30, 300, 271, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_71.setFont(font)
                self.label_71.setStyleSheet("#label_66{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    \n"
        "}")
                self.label_71.setObjectName("label_71")
                self.tableView_3 = QtWidgets.QTableView(self.Tab4)
                self.tableView_3.setGeometry(QtCore.QRect(30, 340, 281, 91))
                self.tableView_3.setStyleSheet("QTableView{\n"
        "    border: 2px solid #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.tableView_3.setObjectName("tableView_3")
                self.pushButton_9 = QtWidgets.QPushButton(self.Tab4)
                self.pushButton_9.setGeometry(QtCore.QRect(30, 250, 221, 31))
                self.pushButton_9.setStyleSheet("QPushButton {\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(31, 187, 228, 255), stop:1 rgba(40, 233, 224, 255));\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "    border-radius: 4px;\n"
        "    font: bold 14px;\n"
        "    min-width: 10em;\n"
        "    padding: 6px;\n"
        "    color: #ffffff;\n"
        "    font: 13pt \"Helvetica Neue\";\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #2980b9;\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "\n"
        "}")
                self.pushButton_9.setObjectName("pushButton_9")
                self.pushButton_10 = QtWidgets.QPushButton(self.Tab4)
                self.pushButton_10.setGeometry(QtCore.QRect(150, 298, 162, 31))
                self.pushButton_10.setStyleSheet("QPushButton {\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(31, 187, 228, 255), stop:1 rgba(40, 233, 224, 255));\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "    border-radius: 4px;\n"
        "    font: bold 14px;\n"
        "    min-width: 10em;\n"
        "    padding: 6px;\n"
        "    color: #ffffff;\n"
        "    font: 13pt \"Helvetica Neue\";\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #2980b9;\n"
        "    border-style: outset;\n"
        "    border-color: #f3f5f7;\n"
        "\n"
        "}")
                self.pushButton_10.setObjectName("pushButton_10")
                self.label_73 = QtWidgets.QLabel(self.Tab4)
                self.label_73.setGeometry(QtCore.QRect(320, 50, 231, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_73.setFont(font)
                self.label_73.setStyleSheet("#label_66{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    \n"
        "}")
                self.label_73.setObjectName("label_73")
                self.plainTextEdit_3 = QtWidgets.QTextEdit(self.Tab4)
                self.plainTextEdit_3.setGeometry(QtCore.QRect(320, 80, 281, 81))
                self.plainTextEdit_3.setStyleSheet("#plainTextEdit_3{\n"
        "    border: 2px solid red;\n"
        "    border-color: #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.plainTextEdit_3.setObjectName("plainTextEdit_3")
                self.label_74 = QtWidgets.QLabel(self.Tab4)
                self.label_74.setGeometry(QtCore.QRect(320, 170, 231, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_74.setFont(font)
                self.label_74.setStyleSheet("#label_66{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    \n"
        "}")
                self.label_74.setObjectName("label_74")
                self.label_4 = QtWidgets.QLabel(self.Tab4)
                self.label_4.setGeometry(QtCore.QRect(320, 200, 281, 181))
                self.label_4.setStyleSheet("#label_4{\n"
        "    border: 2px solid red;\n"
        "    border-color: #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.label_4.setText("")
                self.label_4.setObjectName("label_4")
                self.tabWidget.addTab(self.Tab4, "")
                self.Tab5 = QtWidgets.QWidget()
                self.Tab5.setObjectName("Tab5")
                self.line_6 = QtWidgets.QFrame(self.Tab5)
                self.line_6.setGeometry(QtCore.QRect(484, 0, 94, 3))
                self.line_6.setStyleSheet("background-color: #03a9f4;")
                self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_6.setObjectName("line_6")
                self.label_7 = QtWidgets.QLabel(self.Tab5)
                self.label_7.setGeometry(QtCore.QRect(290, 40, 91, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_7.setFont(font)
                self.label_7.setStyleSheet("#label_6{\n"
        "    font: 14pt;\n"
        "    color: #78909c;\n"
        "    \n"
        "    background-color: rgb(255, 255, 255);\n"
        "color: #263238;\n"
        "}")
                self.label_7.setObjectName("label_7")
                self.graphicsView = QtWidgets.QGraphicsView(self.Tab5)
                self.graphicsView.setGeometry(QtCore.QRect(10, 150, 201, 111))
                self.graphicsView.setStyleSheet("QGraphicsView{\n"
        "    border: 2px solid #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.graphicsView.setObjectName("graphicsView")
                self.graphicsView_2 = QtWidgets.QGraphicsView(self.Tab5)
                self.graphicsView_2.setGeometry(QtCore.QRect(230, 150, 201, 111))
                self.graphicsView_2.setStyleSheet("QGraphicsView{\n"
        "    border: 2px solid #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.graphicsView_2.setObjectName("graphicsView_2")
                self.graphicsView_3 = QtWidgets.QGraphicsView(self.Tab5)
                self.graphicsView_3.setGeometry(QtCore.QRect(450, 150, 201, 111))
                self.graphicsView_3.setStyleSheet("QGraphicsView{\n"
        "    border: 2px solid #eceff1;\n"
        "    border-radius: 1px;\n"
        "}")
                self.graphicsView_3.setObjectName("graphicsView_3")
                self.label_8 = QtWidgets.QLabel(self.Tab5)
                self.label_8.setGeometry(QtCore.QRect(50, 180, 141, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_8.setFont(font)
                self.label_8.setStyleSheet("#label_8{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}")
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(self.Tab5)
                self.label_9.setGeometry(QtCore.QRect(170, 70, 331, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_9.setFont(font)
                self.label_9.setStyleSheet("#label_9{\n"
        "    font: 14pt;\n"
        "    color: #78909c;\n"
        "    \n"
        "}")
                self.label_9.setObjectName("label_9")
                self.label_10 = QtWidgets.QLabel(self.Tab5)
                self.label_10.setGeometry(QtCore.QRect(80, 210, 71, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_10.setFont(font)
                self.label_10.setStyleSheet("#label_10{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "    font: 14pt;\n"
        "    color: #78909c;\n"
        "    \n"
        "}")
                self.label_10.setObjectName("label_10")
                self.label_11 = QtWidgets.QLabel(self.Tab5)
                self.label_11.setGeometry(QtCore.QRect(250, 180, 161, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_11.setFont(font)
                self.label_11.setStyleSheet("#label_11{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}")
                self.label_11.setObjectName("label_11")
                self.label_12 = QtWidgets.QLabel(self.Tab5)
                self.label_12.setGeometry(QtCore.QRect(300, 210, 71, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_12.setFont(font)
                self.label_12.setStyleSheet("#label_12{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "    font: 14pt;\n"
        "    color: #78909c;\n"
        "    \n"
        "}")
                self.label_12.setObjectName("label_12")
                self.label_13 = QtWidgets.QLabel(self.Tab5)
                self.label_13.setGeometry(QtCore.QRect(510, 180, 91, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_13.setFont(font)
                self.label_13.setStyleSheet("#label_13{\n"
        "    font: 14pt;\n"
        "    color: #263238;\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}")
                self.label_13.setObjectName("label_13")
                self.label_14 = QtWidgets.QLabel(self.Tab5)
                self.label_14.setGeometry(QtCore.QRect(520, 210, 81, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_14.setFont(font)
                self.label_14.setStyleSheet("#label_14{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "    font: 14pt;\n"
        "    color: #78909c;\n"
        "    \n"
        "}")
                self.label_14.setObjectName("label_14")
                self.tabWidget.addTab(self.Tab5, "")
                self.label_3 = QtWidgets.QLabel(Form)
                self.label_3.setGeometry(QtCore.QRect(60, 70, 271, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("#label_3{\n"
        "    color: #78909c;\n"
        "    font: 14pt;\n"
        "}\n"
        "")
                self.label_3.setObjectName("label_3")
                self.line_3 = QtWidgets.QFrame(Form)
                self.line_3.setGeometry(QtCore.QRect(0, 160, 800, 1))
                self.line_3.setStyleSheet("background-color: rgba(0, 0, 0, 40);")
                self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_3.setObjectName("line_3")

                self.retranslateUi(Form)
                self.tabWidget.setCurrentIndex(0)
                ##----------------##----------------#
                self.pushButton.clicked.connect(self.tab1_Display)
                self.pushButton_6.clicked.connect(self.tab2_Display)
                self.pushButton_7.clicked.connect(self.tab3_Display)
                self.pushButton_8.clicked.connect(self.tab4_Display)
                self.pushButton_9.clicked.connect(self.tab4_GetLocation)
                ##----------------##----------------#
                QtCore.QMetaObject.connectSlotsByName(Form)

        def tab1_Display(self):
                if self.Data_Pre == None:
                        self.Data_Pre = Pre_Process()
                model = PandasModel(self.Data_Pre.getTrain().head(100))
                self.tableView.setModel(model)

        def tab2_Display(self):
                list_feature = []
                if self.checkBox.isChecked():
                        list_feature.append(1)
                if self.checkBox_2.isChecked():
                        list_feature.append(2)
                if self.checkBox_3.isChecked():
                        list_feature.append(3)
                if self.checkBox_4.isChecked():
                        list_feature.append(4)
                if self.checkBox_5.isChecked():
                        list_feature.append(5)
                if self.checkBox_6.isChecked():
                        list_feature.append(6)
                if self.checkBox_7.isChecked():
                        list_feature.append(7)

                if self.Train_Feature == None:
                        self.Train_Feature = Feature_Extraction(self.Data_Pre.getTrain())
                
                model = PandasModel(self.Train_Feature.getFeature(list_feature).head(100))
                self.tableView_2.setModel(model)
                self.tableView_2.resizeColumnsToContents()
                self.list_feature = list_feature

        def tab3_Display(self):
                if self.Test_Feature == None:
                        self.Test_Feature = Feature_Extraction(self.Data_Pre.getTest())

                if self.Model == None:
                        self.Model = RF(n_estimators=20)
                
                self.Model.fit(self.Train_Feature.getFeature(self.list_feature), self.Train_Feature.getY())
                
                y_predict = self.Model.predict(self.Test_Feature.getFeature(self.list_feature))

                report = str(self.Model.report(self.Test_Feature.getY(), y_predict))
                self.plainTextEdit.setText(report)

                plot_classification_report(report)
                plt.savefig('plot_tab3.png', dpi=200, format='png', bbox_inches='tight')
                plt.close()
                
                pixmap = QtGui.QPixmap('plot_tab3.png')
                self.label_2.setScaledContents(True)
                self.label_2.setPixmap(pixmap)
                self.label_2.show()
                

        def tab4_Display(self):
                self.text_input = self.plainTextEdit_2.toPlainText()
                Data_df = None
                if len(self.text_input) > 1:
                        line = self.text_input.split('\n')
                        Data = []
                        for i in line:
                                if len(i) == 0:
                                        continue
                                l = map(int, i.split(','))
                                Data.append(l)
                        Data_df = pd.DataFrame(Data, columns = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5', 'Type'])
                        
                text_input = self.plainTextEdit_4.toPlainText()
                if len(text_input) > 1:
                        Data_load = pd.read_csv(text_input, names = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','Type'])
                        if Data_df != None:
                                Data_df = pd.concat([Data_df, Data_load], ignore_index=True)
                        Data_df = Data_load

                self.Data_Input = Feature_Extraction(Data_df)

                y_predict = self.Model.predict(self.Data_Input.getFeature(self.list_feature))
                y_predict_df = pd.DataFrame(y_predict, columns = ['Type_Predict'])

                Data_df = pd.concat([Data_df, y_predict_df], axis = 1)
                model = PandasModel(Data_df.head())
                self.tableView_3.setModel(model)
                self.tableView_3.resizeColumnsToContents()
                
                acc = "ACC Score: " + accuracy_score(self.Data_Input.getY(), y_predict) + "\n"

                report = acc + str(self.Model.report(self.Data_Input.getY(), y_predict))
                self.plainTextEdit_3.setText(report)

                plot_classification_report(report)
                plt.savefig('plot_tab4.png', dpi=200, format='png', bbox_inches='tight')
                plt.close()
                
                pixmap = QtGui.QPixmap('plot_tab4.png')
                self.label_4.setScaledContents(True)
                self.label_4.setPixmap(pixmap)
                self.label_4.show()

        def tab4_GetLocation(self):
                fileName, _ = QtWidgets.QFileDialog.getOpenFileName()
                self.plainTextEdit_4.setText(fileName)

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                self.label.setText(_translate("Form", "Poker Hand Prediction"))
                self.label_6.setText(_translate("Form", "<html><head/><body><p>Data Pre-Processing:</p></body></html>"))
                self.pushButton.setText(_translate("Form", "Load dataset"))
                self.pushButton_2.setText(_translate("Form", "Statistic dataset"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), _translate("Form", "PRE-PROCESSING"))
                self.label_66.setText(_translate("Form", "Choose type of feature-extraction:"))
                self.pushButton_6.setText(_translate("Form", "Extraction"))
                self.checkBox.setText(_translate("Form", "   Raw Data"))
                self.checkBox_2.setText(_translate("Form", "   Count Card"))
                self.checkBox_3.setText(_translate("Form", "   Standard Deviation with Count Card"))
                self.checkBox_4.setText(_translate("Form", "   Count Suit"))
                self.checkBox_5.setText(_translate("Form", "   Bag Count Suit"))
                self.checkBox_6.setText(_translate("Form", "   Bag Count Card"))
                self.checkBox_7.setText(_translate("Form", "   Flag of ACE"))
                self.pushButton_11.setText(_translate("Form", "Save CSV"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab2), _translate("Form", "FEATURE-EXTRACTION"))
                self.label_67.setText(_translate("Form", "Choose type of Machine Learning models:"))
                self.pushButton_7.setText(_translate("Form", "Analysis "))
                self.radioButton_9.setText(_translate("Form", "   Random Forest"))
                self.label_68.setText(_translate("Form", "Precision Score:"))
                self.radioButton_10.setText(_translate("Form", "   SVC"))
                self.label_72.setText(_translate("Form", "HeatMap:"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab3), _translate("Form", "MODEL ML"))
                self.label_69.setText(_translate("Form", "Input record text to prediction:"))
                self.pushButton_8.setText(_translate("Form", "Predict"))
                self.label_70.setText(_translate("Form", "Select file text to prediction:"))
                self.label_71.setText(_translate("Form", "Result:"))
                self.pushButton_9.setText(_translate("Form", "Open File"))
                self.pushButton_10.setText(_translate("Form", "Save CSV"))
                self.label_73.setText(_translate("Form", "Precision Score:"))
                self.label_74.setText(_translate("Form", "HeatMap"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab4), _translate("Form", "PREDICTION"))
                self.label_7.setText(_translate("Form", "CORE TEAM"))
                self.label_8.setText(_translate("Form", "Duy Trinh Khanh Le"))
                self.label_9.setText(_translate("Form", "University of Information Technology - VNU HCM"))
                self.label_10.setText(_translate("Form", "15520159"))
                self.label_11.setText(_translate("Form", "THAO Le Nguyen Ngoc"))
                self.label_12.setText(_translate("Form", "15520818"))
                self.label_13.setText(_translate("Form", "YEN Hoang"))
                self.label_14.setText(_translate("Form", "15521042"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab5), _translate("Form", "INFORMATION"))
                self.label_3.setText(_translate("Form", "Using Machine Learning"))

