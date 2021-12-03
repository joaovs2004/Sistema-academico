# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aviso.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class AvisoWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 248)
        MainWindow.setStyleSheet("background-color: #EDFDFF;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelAviso = QtWidgets.QLabel(self.centralwidget)
        self.labelAviso.setGeometry(QtCore.QRect(10, 40, 511, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelAviso.setFont(font)
        self.labelAviso.setText("")
        self.labelAviso.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAviso.setObjectName("labelAviso")
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(210, 180, 101, 41))
        self.btnOk.setStyleSheet("QPushButton {\n"
"    background-color: #8ED498;\n"
"    border: 1px solid #353e40;\n"
"    border-radius: 5px;\n"
"    color: #353e40;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #85C78F;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #74AD7D;\n"
"}")
        self.btnOk.setObjectName("btnOk")
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self.btnOk)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aviso"))
        self.btnOk.setText(_translate("MainWindow", "Ok"))
