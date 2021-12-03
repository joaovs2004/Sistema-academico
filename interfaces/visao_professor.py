# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visao_professor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class VisaoProfessorWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1414, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-190, 0, 341, 821))
        self.frame_2.setStyleSheet("QFrame {\n"
"    background-color: #d3f9ff;\n"
"    border: 1px solid #a7c4a0;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #353e40;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #353e40;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover,  QPushButton:focus {\n"
"    background-color: #BEE0E6\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btnTurmas = QtWidgets.QPushButton(self.frame_2)
        self.btnTurmas.setGeometry(QtCore.QRect(190, 80, 151, 51))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btnTurmas.setFont(font)
        self.btnTurmas.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnTurmas.setTabletTracking(False)
        self.btnTurmas.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnTurmas.setAutoFillBackground(False)
        self.btnTurmas.setAutoDefault(False)
        self.btnTurmas.setObjectName("btnTurmas")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btnTurmas)
        self.btnInformacoes = QtWidgets.QPushButton(self.frame_2)
        self.btnInformacoes.setGeometry(QtCore.QRect(190, 140, 151, 51))
        self.btnInformacoes.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnInformacoes.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnInformacoes.setObjectName("btnInformacoes")
        self.buttonGroup.addButton(self.btnInformacoes)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(200, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.btnLogout = QtWidgets.QPushButton(self.frame_2)
        self.btnLogout.setGeometry(QtCore.QRect(190, 760, 151, 61))
        self.btnLogout.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnLogout.setStyleSheet("QPushButton {\n"
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
        self.btnLogout.setObjectName("btnLogout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(150, 0, 1371, 821))
        self.frame.setStyleSheet("background-color: #EDFDFF;\n"
"border: none;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1261, 821))
        self.stackedWidget.setStyleSheet("QLabel {\n"
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
"QComboBox {\n"
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
"    \n"
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
"}\n"
"\n"
"QDateTimeEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #9FBBBF;\n"
"    border-radius: 5px;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageInformacoes = QtWidgets.QWidget()
        self.pageInformacoes.setObjectName("pageInformacoes")
        self.label_23 = QtWidgets.QLabel(self.pageInformacoes)
        self.label_23.setGeometry(QtCore.QRect(460, 40, 191, 141))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("src/icone_perfil.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.labelEmail = QtWidgets.QLabel(self.pageInformacoes)
        self.labelEmail.setGeometry(QtCore.QRect(430, 320, 700, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelEmail.setFont(font)
        self.labelEmail.setObjectName("labelEmail")
        self.labelTelefone = QtWidgets.QLabel(self.pageInformacoes)
        self.labelTelefone.setGeometry(QtCore.QRect(410, 360, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTelefone.setFont(font)
        self.labelTelefone.setObjectName("labelTelefone")
        self.labelCpf = QtWidgets.QLabel(self.pageInformacoes)
        self.labelCpf.setGeometry(QtCore.QRect(450, 286, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCpf.setFont(font)
        self.labelCpf.setObjectName("labelCpf")
        self.labelNome = QtWidgets.QLabel(self.pageInformacoes)
        self.labelNome.setGeometry(QtCore.QRect(430, 200, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")
        self.labelNasc = QtWidgets.QLabel(self.pageInformacoes)
        self.labelNasc.setGeometry(QtCore.QRect(330, 240, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNasc.setFont(font)
        self.labelNasc.setObjectName("labelNasc")
        self.labelSexo = QtWidgets.QLabel(self.pageInformacoes)
        self.labelSexo.setGeometry(QtCore.QRect(430, 400, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSexo.setFont(font)
        self.labelSexo.setObjectName("labelSexo")
        self.stackedWidget.addWidget(self.pageInformacoes)
        self.pageTurmas = QtWidgets.QWidget()
        self.pageTurmas.setObjectName("pageTurmas")
        self.ListaTurmas_2 = QtWidgets.QListWidget(self.pageTurmas)
        self.ListaTurmas_2.setGeometry(QtCore.QRect(100, 120, 1091, 631))
        self.ListaTurmas_2.setStyleSheet("background-color: white;\n"
"border: 1px solid #9FBBBF;\n"
"border-radius: 10px;\n"
"color: rgb(53, 62, 64);")
        self.ListaTurmas_2.setObjectName("ListaTurmas_2")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaTurmas_2.addItem(item)
        self.label_22 = QtWidgets.QLabel(self.pageTurmas)
        self.label_22.setGeometry(QtCore.QRect(580, 40, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.stackedWidget.addWidget(self.pageTurmas)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.btnTurmas.setStyleSheet('background-color: #BEE0E6')

        def mudar_cor(button):
                for btn in [self.btnTurmas, self.btnInformacoes]:
                        btn.setStyleSheet("QPushButton {\n"
        "    color: #353e40;\n"
        "    border: none;\n"
        "}\n"
        "\n"
        "QPushButton:hover,  QPushButton:focus {\n"
        "    background-color: #BEE0E6\n"
        "}\n")
                        button.setStyleSheet('background-color: #BEE0E6')

        self.buttonGroup.buttonClicked.connect(mudar_cor)
        self.btnTurmas.setFocus()
        self.buttonGroup.setId(self.btnTurmas, 1)
        self.buttonGroup.setId(self.btnInformacoes, 0)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Visão Professor"))
        self.btnTurmas.setText(_translate("MainWindow", "Turmas"))
        self.btnInformacoes.setText(_translate("MainWindow", "Informações"))
        self.label_12.setText(_translate("MainWindow", "Escola"))
        self.btnLogout.setText(_translate("MainWindow", "Logout"))
        self.labelEmail.setText(_translate("MainWindow", "Email:"))
        self.labelTelefone.setText(_translate("MainWindow", "Telefone:"))
        self.labelCpf.setText(_translate("MainWindow", "Cpf:"))
        self.labelNome.setText(_translate("MainWindow", "Nome:"))
        self.labelNasc.setText(_translate("MainWindow", "Data de nascimento:"))
        self.labelSexo.setText(_translate("MainWindow", "Sexo:"))
        __sortingEnabled = self.ListaTurmas_2.isSortingEnabled()
        self.ListaTurmas_2.setSortingEnabled(False)
        item = self.ListaTurmas_2.item(0)
        item.setText(_translate("MainWindow", "Fundamental"))
        item = self.ListaTurmas_2.item(1)
        item.setText(_translate("MainWindow", "1º Ano"))
        item = self.ListaTurmas_2.item(2)
        item.setText(_translate("MainWindow", "2º Ano"))
        item = self.ListaTurmas_2.item(3)
        item.setText(_translate("MainWindow", "3º Ano"))
        item = self.ListaTurmas_2.item(4)
        item.setText(_translate("MainWindow", "4º Ano"))
        item = self.ListaTurmas_2.item(5)
        item.setText(_translate("MainWindow", "5º Ano"))
        item = self.ListaTurmas_2.item(6)
        item.setText(_translate("MainWindow", "6º Ano"))
        item = self.ListaTurmas_2.item(7)
        item.setText(_translate("MainWindow", "7º Ano"))
        item = self.ListaTurmas_2.item(8)
        item.setText(_translate("MainWindow", "8º Ano"))
        item = self.ListaTurmas_2.item(9)
        item.setText(_translate("MainWindow", "9º Ano"))
        item = self.ListaTurmas_2.item(10)
        item.setText(_translate("MainWindow", "Medio"))
        item = self.ListaTurmas_2.item(11)
        item.setText(_translate("MainWindow", "1º Ano"))
        item = self.ListaTurmas_2.item(12)
        item.setText(_translate("MainWindow", "2º Ano"))
        item = self.ListaTurmas_2.item(13)
        item.setText(_translate("MainWindow", "3º Ano"))
        self.ListaTurmas_2.setSortingEnabled(__sortingEnabled)
        self.label_22.setText(_translate("MainWindow", "Turmas"))
