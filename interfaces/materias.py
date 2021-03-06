# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'materias.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MateriasWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 296)
        MainWindow.setStyleSheet("background-color: #EDFDFF;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxMateria = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxMateria.setGeometry(QtCore.QRect(30, 120, 371, 31))
        self.comboBoxMateria.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #9FBBBF;\n"
"    border-radius: 5px;\n"
"    color: #353e40;\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"    background-color: #e6e6e6;\n"
"}")
        self.comboBoxMateria.setObjectName("comboBoxMateria")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnSelecionar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelecionar.setGeometry(QtCore.QRect(260, 200, 121, 51))
        self.btnSelecionar.setStyleSheet("QPushButton {\n"
"    background-color: #8ED498;\n"
"    border: 1px solid rgb(53, 62, 64);\n"
"    border-radius: 5px;\n"
"    color: rgb(53, 62, 64);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #85C78F;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #74AD7D;\n"
"}")
        self.btnSelecionar.setObjectName("btnSelecionar")
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self.btnSelecionar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Materia"))
        self.label.setText(_translate("MainWindow", "Selecione a materia que deseja aplicar as notas"))
        self.btnSelecionar.setText(_translate("MainWindow", "Selecionar"))
