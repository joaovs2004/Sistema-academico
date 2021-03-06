# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'turma.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TurmaWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 636)
        MainWindow.setStyleSheet("background-color: #EDFDFF;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 891, 561))
        self.tabWidget.setStyleSheet("QPushButton {\n"
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
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.tabelaProfessor = QtWidgets.QTableWidget(self.tab)
        self.tabelaProfessor.setGeometry(QtCore.QRect(30, 30, 721, 491))
        self.tabelaProfessor.setStyleSheet("background-color: white;\n"
"border: 1px solid #9FBBBF;")
        self.tabelaProfessor.setObjectName("tabelaProfessor")
        self.tabelaProfessor.setColumnCount(3)
        self.tabelaProfessor.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaProfessor.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaProfessor.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaProfessor.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaProfessor.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaProfessor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaProfessor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaProfessor.setHorizontalHeaderItem(2, item)
        self.tabelaProfessor.horizontalHeader().setDefaultSectionSize(200)
        self.tabelaProfessor.verticalHeader().setDefaultSectionSize(50)
        self.btnAdicionarProfessor = QtWidgets.QPushButton(self.tab)
        self.btnAdicionarProfessor.setGeometry(QtCore.QRect(760, 30, 121, 51))
        self.btnAdicionarProfessor.setStyleSheet("")
        self.btnAdicionarProfessor.setObjectName("btnAdicionarProfessor")
        self.btnExcluirProfessor = QtWidgets.QPushButton(self.tab)
        self.btnExcluirProfessor.setGeometry(QtCore.QRect(760, 90, 121, 51))
        self.btnExcluirProfessor.setStyleSheet("QPushButton {\n"
"    background-color: #FFAE9F;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E69B8E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #BF8177;\n"
"}")
        self.btnExcluirProfessor.setObjectName("btnExcluirProfessor")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabelaAlunos = QtWidgets.QTableWidget(self.tab_2)
        self.tabelaAlunos.setGeometry(QtCore.QRect(30, 30, 721, 491))
        self.tabelaAlunos.setStyleSheet("background-color: white;\n"
"border: 1px solid #9FBBBF;")
        self.tabelaAlunos.setObjectName("tabelaAlunos")
        self.tabelaAlunos.setColumnCount(2)
        self.tabelaAlunos.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaAlunos.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaAlunos.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaAlunos.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaAlunos.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaAlunos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaAlunos.setHorizontalHeaderItem(1, item)
        self.tabelaAlunos.horizontalHeader().setDefaultSectionSize(200)
        self.tabelaAlunos.verticalHeader().setDefaultSectionSize(40)
        self.btnExcluirAluno = QtWidgets.QPushButton(self.tab_2)
        self.btnExcluirAluno.setGeometry(QtCore.QRect(760, 90, 121, 51))
        self.btnExcluirAluno.setStyleSheet("QPushButton {\n"
"    background-color: #FFAE9F;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E69B8E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #BF8177;\n"
"}")
        self.btnExcluirAluno.setObjectName("btnExcluirAluno")
        self.btnAdicionarAluno = QtWidgets.QPushButton(self.tab_2)
        self.btnAdicionarAluno.setGeometry(QtCore.QRect(760, 30, 121, 51))
        self.btnAdicionarAluno.setStyleSheet("")
        self.btnAdicionarAluno.setObjectName("btnAdicionarAluno")
        self.tabWidget.addTab(self.tab_2, "")
        self.labelTurma = QtWidgets.QLabel(self.centralwidget)
        self.labelTurma.setGeometry(QtCore.QRect(10, 10, 891, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelTurma.setFont(font)
        self.labelTurma.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTurma.setObjectName("labelTurma")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Turma"))
        item = self.tabelaProfessor.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tabelaProfessor.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tabelaProfessor.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tabelaProfessor.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tabelaProfessor.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tabelaProfessor.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Disciplina"))
        item = self.tabelaProfessor.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data de nascimento"))
        self.btnAdicionarProfessor.setText(_translate("MainWindow", "Adicionar"))
        self.btnExcluirProfessor.setText(_translate("MainWindow", "Excluir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Professores"))
        item = self.tabelaAlunos.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tabelaAlunos.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tabelaAlunos.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tabelaAlunos.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tabelaAlunos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tabelaAlunos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data de nascimento"))
        self.btnExcluirAluno.setText(_translate("MainWindow", "Excluir"))
        self.btnAdicionarAluno.setText(_translate("MainWindow", "Adicionar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Alunos"))
        self.labelTurma.setText(_translate("MainWindow", "Turma"))
