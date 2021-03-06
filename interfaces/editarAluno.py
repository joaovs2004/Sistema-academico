# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarAluno.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class EditAlunoWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 555)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #EDFDFF;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #353e40;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #9FBBBF;\n"
"    border-radius: 5px;\n"
"    color: #353e40;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #353e40;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #353e40;\n"
"}\n"
"\n"
"QPushButton {\n"
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 130, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 176, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.alunoNome = QtWidgets.QLineEdit(self.centralwidget)
        self.alunoNome.setGeometry(QtCore.QRect(320, 130, 321, 31))
        self.alunoNome.setObjectName("alunoNome")
        self.alunoEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.alunoEmail.setGeometry(QtCore.QRect(320, 170, 321, 31))
        self.alunoEmail.setObjectName("alunoEmail")
        self.alunoTelefone = QtWidgets.QLineEdit(self.centralwidget)
        self.alunoTelefone.setGeometry(QtCore.QRect(320, 210, 321, 31))
        self.alunoTelefone.setObjectName("alunoTelefone")
        self.alunoTelefone.setInputMask('(00) 00000-0000')
        self.btnEditar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditar.setGeometry(QtCore.QRect(310, 340, 131, 61))
        self.btnEditar.setObjectName("btnEditar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(480, 340, 131, 61))
        self.btnCancelar.setStyleSheet("QPushButton {\n"
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
        self.btnCancelar.setObjectName("btnCancelar")
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self.btnEditar)
        MainWindow.setCentralWidget(self.centralwidget)

        def trocar_posicao_cursor():
            texto = self.alunoTelefone.text()

            if texto == '() -':
                self.alunoTelefone.setCursorPosition(0)

        self.alunoTelefone.cursorPositionChanged.connect(trocar_posicao_cursor)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editar Aluno"))
        self.label_2.setText(_translate("MainWindow", "Editar Aluno"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.label_3.setText(_translate("MainWindow", "Email:"))
        self.label_4.setText(_translate("MainWindow", "Telefone:"))
        self.btnEditar.setText(_translate("MainWindow", "Editar"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))
