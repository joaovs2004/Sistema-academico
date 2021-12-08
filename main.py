from sqlite3.dbapi2 import IntegrityError
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter, QMainWindow, QApplication, QTableWidgetItem

from banco import *
from pycpfcnpj import cpfcnpj as lib_cpf
from pyisemail import is_email

from random import randint
from classes import Aluno, Professor, Turma, Usuario
from interfaces.alunoNotas import AlunoNotasWindow

from interfaces.aviso import AvisoWindow
from interfaces.confimar import ConfirmarWindow
from interfaces.login import LoginWindow
from interfaces.materias import MateriasWindow

from interfaces.painel_adm import AdmWindow
from interfaces.addProfessor import AddProfessorWindow
from interfaces.addAluno import AddAlunoWindow
from interfaces.editarAluno import EditAlunoWindow
from interfaces.editarProfessor import EditProfessorWindow

from interfaces.turma import TurmaWindow
from interfaces.visao_professor import VisaoProfessorWindow
from interfaces.alunos import AlunosWindow
from interfaces.notas import NotasWindow

from interfaces.aluno import AlunoWindow

def mostrar_aviso(msg):
    tela_aviso.labelAviso.setText(msg)
    tela_aviso.show()

def logout(fechar):
    fechar.close()
    tela_login.show()

def limpar_campos(* inputs):
    for input in inputs:
        input.setText('')

def fechar(tela, * inputs):
    tela.close()
    for input in inputs:
        limpar_campos(input)

class Adm(QMainWindow, AdmWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.buttonGroup.buttonClicked.connect(self.trocarAba)
        self.listaTurmas.itemDoubleClicked.connect(self.mostrar_turma)

        self.btnAdicionarProfessor.clicked.connect(self.add_professor)
        self.btnAdicionarAluno.clicked.connect(self.add_aluno)

        self.btnEditarAlunos.clicked.connect(self.editar_aluno)
        self.btnEditarProfessor.clicked.connect(self.editar_professor)

        self.btnBuscarProfessor.clicked.connect(self.buscar_professor)
        self.btnBuscarAlunos.clicked.connect(self.buscar_aluno)
        self.shortcut1.activated.connect(self.buscar_aluno)
        self.shortcut2.activated.connect(self.buscar_professor)

        self.btnExcluirAlunos.clicked.connect(self.excluir_aluno)
        self.btnExcluirProfessor.clicked.connect(self.excluir_professor)

        self.btnProximoBimestre.clicked.connect(self.proximo_bimestre)

        self.btnVerNotas.clicked.connect(self.mostrar_notas)

        self.btnLogout.clicked.connect(lambda: logout(self))

        self.trazer_alunos()
        self.trazer_professores()
    
    def editar_aluno(self):
        tabela = tela_adm.tabela_aluno
        linha = tabela.currentRow()

        if linha + 1 != 0:
            aluno_banco = buscar_aluno_por_matricula(tabela.item(linha, 3).text())
                
            if aluno_banco != None:
                tela_editarAluno.alunoNome.setText(aluno_banco[0])
                tela_editarAluno.alunoEmail.setText(aluno_banco[4])
                tela_editarAluno.alunoTelefone.setText(aluno_banco[5])
            
            tela_editarAluno.show()
        else:
            mostrar_aviso('Selecione um aluno para editar')

    def editar_professor(self):
        tabela = tela_adm.tabela_professor
        linha = tabela.currentRow()

        if linha + 1 != 0:
            professor_banco = buscar_professor_por_matricula(tabela.item(linha, 4).text())
            if professor_banco != None:
                tela_editarProfessor.professorNome.setText(professor_banco[1])
                tela_editarProfessor.professorEmail.setText(professor_banco[4])
                tela_editarProfessor.professorTelefone.setText(professor_banco[5]) 

            tela_editarProfessor.show()  
        else:
            mostrar_aviso('Selecione um professor para editar')

    def mostrar_turma(self, item):
        linha = self.listaTurmas.currentRow()
        tipo = None
        professor_banco = buscar_todos_professores()
        aluno_banco = buscar_todos_alunos()

        nomesProfessores = []
        nomesAlunos = []

        for aluno in aluno_banco:
            if aluno[1] in nomesAlunos:
                nomesAlunos.append(f'{aluno[1]} - {aluno[8]}')
            else:
                nomesAlunos.append(aluno[1])

        for professor in professor_banco:
            if professor[1] in nomesProfessores:
                nomesProfessores.append(f'{professor[1]} - {professor[7]}')
            else:
                nomesProfessores.append(professor[1])
        
        completerProf = QCompleter(nomesProfessores)
        completerAluno = QCompleter(nomesAlunos)

        tela_addProfessor.inputProfessor.setCompleter(completerProf)
        tela_addAluno.inputAluno.setCompleter(completerAluno)

        if linha > 10:
            tipo = 'Ensino Medio'
            tela_addProfessor.comboBoxDisciplina.clear()
            tela_addProfessor.comboBoxDisciplina.addItem('Lingua Portuguesa')
            tela_addProfessor.comboBoxDisciplina.addItem('Matemática')
            tela_addProfessor.comboBoxDisciplina.addItem('História')
            tela_addProfessor.comboBoxDisciplina.addItem('Geografia')
            tela_addProfessor.comboBoxDisciplina.addItem('Biologia')
            tela_addProfessor.comboBoxDisciplina.addItem('Quimica')
            tela_addProfessor.comboBoxDisciplina.addItem('Artes')
            tela_addProfessor.comboBoxDisciplina.addItem('Fisica')
            tela_addProfessor.comboBoxDisciplina.addItem('Educação Fisica')
            tela_addProfessor.comboBoxDisciplina.addItem('Inglês')
            tela_addProfessor.comboBoxDisciplina.addItem('Sociologia')
            tela_addProfessor.comboBoxDisciplina.addItem('Filosofia')
        else:
            tipo = 'Ensino Fundamental'
            tela_addProfessor.comboBoxDisciplina.clear()
            tela_addProfessor.comboBoxDisciplina.addItem('Lingua Portuguesa')
            tela_addProfessor.comboBoxDisciplina.addItem('Matemática')
            tela_addProfessor.comboBoxDisciplina.addItem('História')
            tela_addProfessor.comboBoxDisciplina.addItem('Geografia')
            tela_addProfessor.comboBoxDisciplina.addItem('Ciências')
            tela_addProfessor.comboBoxDisciplina.addItem('Artes')
            tela_addProfessor.comboBoxDisciplina.addItem('Educação Física')
            tela_addProfessor.comboBoxDisciplina.addItem('Inglês')
            tela_addProfessor.comboBoxDisciplina.addItem('Filosofia')
        
        modelo_turma.variavel_para_modelo(item.text(), tipo)
        tela_turma.labelTurma.setText(f'{item.text()} {tipo}')

        tela_turma.trazer_professores()
        tela_turma.trazer_alunos()
        tela_turma.show()

    def trazer_alunos(self):
        tabela = self.tabela_aluno
        aluno_banco = buscar_todos_alunos()
        tabela.setRowCount(len(aluno_banco))
        rowPos = 0
        for aluno in aluno_banco:
            tabela.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(aluno[1]))
            tabela.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(aluno[2]))
            tabela.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(aluno[4]))
            tabela.setItem(rowPos, 3, QtWidgets.QTableWidgetItem(aluno[8]))
            tabela.setItem(rowPos, 4, QtWidgets.QTableWidgetItem(aluno[5]))
            tabela.setItem(rowPos, 5, QtWidgets.QTableWidgetItem(aluno[6]))

            tabela.item(rowPos, 0).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 2).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 3).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 4).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 5).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            rowPos += 1
    
    def trazer_professores(self):
        tabela = self.tabela_professor
        professor_banco = buscar_todos_professores()
        tabela.setRowCount(len(professor_banco))
        rowPos = 0
        for professor in professor_banco:
            tabela.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(professor[1]))
            tabela.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(professor[3]))
            tabela.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(professor[4]))
            tabela.setItem(rowPos, 3, QtWidgets.QTableWidgetItem(professor[5]))
            tabela.setItem(rowPos, 4, QtWidgets.QTableWidgetItem(professor[7]))

            tabela.item(rowPos, 0).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 2).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 3).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 4).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            rowPos += 1

    def add_aluno(self):
        nome = self.alunoNome.text()
        nascimento = self.dataAluno.text()
        cpf = self.cpfAluno.text()
        responsavel = self.responsavelAluno.text()
        email = self.emailAluno.text()
        telefone = self.telefoneAluno.text()
        sexo = self.alunoSexo.currentText()

        matricula = randint(100000, 999999)
        matricula_banco = buscar_matricula(matricula)
        cpf_banco = buscar_cpf(cpf)

        if matricula_banco[0] != None or matricula_banco[1] != None:
            matricula = randint(100000, 999999)
            matricula_banco = buscar_matricula(matricula)

            while matricula_banco[0] != None or matricula_banco[1] != None:
                matricula = randint(100000, 999999)
                matricula_banco = buscar_matricula(matricula)
        
        if nome == '' or nascimento == '' or sexo == '' or responsavel == '':
            mostrar_aviso('Preencha todos os dados') 
        elif lib_cpf.validate(cpf) == False:
            mostrar_aviso('Cpf invalido')
        elif is_email(email) == False:
            mostrar_aviso('Email invalido') 
        elif cpf_banco[0] != None or cpf_banco[1] != None:
            mostrar_aviso('Cpf já existe') 
        else:
            criar_usuario(nome, matricula, 2)
            usuario_banco = buscar_usuario_por_matricula(matricula)
            criar_aluno(nome, responsavel, nascimento, cpf, email, telefone, sexo, matricula, usuario_banco[0])
            mostrar_aviso('Aluno criado')
            limpar_campos(self.alunoNome, self.cpfAluno, self.emailAluno, self.telefoneAluno, self.responsavelAluno)
            self.trazer_alunos()

    def add_professor(self):
        nome = self.nomeProfessor.text()
        nascimento  = self.dataProfessor.text()
        cpf = self.cpfProfessor.text()
        email = self.emailProfessor.text()
        telefone = self.telefoneProfessor.text()
        sexo = self.professorSexo.currentText()
        
        matricula = randint(100000, 999999)
        matricula_banco = buscar_matricula(matricula)
        cpf_banco = buscar_cpf(cpf)
        
        if matricula_banco[0] != None or matricula_banco[1] != None:
            matricula = randint(100000, 999999)
            matricula_banco = buscar_matricula(matricula)

            while matricula_banco[0] != None or matricula_banco[1] != None:
                matricula = randint(100000, 999999)
                matricula_banco = buscar_matricula(matricula)

        if nome == '' or nascimento == '' or sexo == '':
            mostrar_aviso('Preencha todos os dados')
        elif lib_cpf.validate(cpf) == False:
            mostrar_aviso('Cpf invalido')
        elif is_email(email) == False:
            mostrar_aviso('Email invalido')
        elif cpf_banco[0] != None or cpf_banco[1] != None:
            mostrar_aviso('Cpf já existe')
        else:
            criar_usuario(nome, matricula, 1)
            usuario_banco = buscar_usuario_por_matricula(matricula)
            criar_professor(nome, nascimento, cpf, email, telefone, sexo, matricula, usuario_banco[0])
            mostrar_aviso('Professor adicionado')
            limpar_campos(self.nomeProfessor, self.emailProfessor, self.telefoneProfessor, self.cpfProfessor)
            self.trazer_professores()

    def excluir_aluno(self):
        linha = tela_adm.tabela_aluno.currentRow()
        tabela = self.tabela_aluno

        if linha + 1 == 0:
            mostrar_aviso('Selecione um aluno para excluir')
        else:
            matricula = int(tabela.item(linha, 3).text())
            deletar_usuario_por_senha(matricula)           
            
            self.trazer_alunos()
    
    def excluir_professor(self):
        linha = tela_adm.tabela_professor.currentRow()
        tabela = self.tabela_professor

        if linha + 1 == 0:
            mostrar_aviso('Selecione um professor para excluir')
        else:
            matricula = int(tabela.item(linha, 4).text())
            deletar_usuario_por_senha(matricula)           
            
            self.trazer_professores()

    def buscar_professor(self):
        nome = self.inputBuscarProfessores.text()
        
        tabela = self.tabela_professor
        professor_banco = buscar_professor_por_nome_like(nome)
        tabela.setRowCount(len(professor_banco))
        rowPos = 0
        
        for professor in professor_banco:
            tabela.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(professor[0]))
            tabela.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(professor[2]))
            tabela.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(professor[3]))
            tabela.setItem(rowPos, 3, QtWidgets.QTableWidgetItem(professor[4]))
            tabela.setItem(rowPos, 4, QtWidgets.QTableWidgetItem(professor[6]))

            tabela.item(rowPos, 0).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 2).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 3).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 4).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            rowPos += 1
    
    def buscar_aluno(self):
        nome = self.inputBuscarAlunos.text()

        tabela = self.tabela_aluno
        aluno_banco = buscar_aluno_por_nome_like(nome)
        tabela.setRowCount(len(aluno_banco))
        rowPos = 0

        for aluno in aluno_banco:
            tabela.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(aluno[0]))
            tabela.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(aluno[1]))
            tabela.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(aluno[3]))
            tabela.setItem(rowPos, 3, QtWidgets.QTableWidgetItem(aluno[7]))
            tabela.setItem(rowPos, 4, QtWidgets.QTableWidgetItem(aluno[4]))
            tabela.setItem(rowPos, 5, QtWidgets.QTableWidgetItem(aluno[5]))

            tabela.item(rowPos, 0).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 2).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 3).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 4).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(rowPos, 5).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            rowPos += 1

    def mostrar_notas(self):
        tabela = tela_aluno_notas.tabelaNotas
        final = 0
        linha = self.tabela_aluno.currentRow()

        if linha + 1 == 0:
            mostrar_aviso('Selecione um aluno para ver suas notas')
        else:
            matricula = int(self.tabela_aluno.item(linha, 3).text())
            tela_aluno_notas.labelMateria.setText('')
            aluno_banco = buscar_aluno_por_matricula(matricula)
            materias = ['Lingua Portuguesa', 'Matemática', 'História', 'Geografia', 'Biologia', 'Quimica', 'Artes', 'Fisica', 'Educação Fisica', 'Inglês', 'Sociologia', 'Filosofia', 'Ciências']

            rowPos = 0

            tabela.clear()
            tabela.setRowCount(0)
          
            tabela.setHorizontalHeaderItem(0, QTableWidgetItem('B1'))
            tabela.setHorizontalHeaderItem(1, QTableWidgetItem('B2'))
            tabela.setHorizontalHeaderItem(2, QTableWidgetItem('B3'))
            tabela.setHorizontalHeaderItem(3, QTableWidgetItem('B4'))

            for materia in materias:
                notas_banco = buscar_notas_por_materia_aluno(materia, aluno_banco[8])

                if notas_banco != []:
                    tabela.setRowCount(tabela.rowCount() + 1)
                    tabela.setVerticalHeaderItem(rowPos, QTableWidgetItem(materia))

                    for notas in notas_banco:                      
                        final = (notas[1] + notas[2] + notas[3] + notas[4] + notas[5] + notas[6]) / 6
                        tabela.setItem(rowPos, notas[7] - 1, QtWidgets.QTableWidgetItem(f'{final:.1f}'))

                        tabela.item(rowPos, notas[7] - 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                
                    rowPos += 1               
            
            tela_aluno_notas.show() 

    def proximo_bimestre(self):
        bimestre_atual = buscar_bimestre()

        if bimestre_atual == None:
            inserir_bimestre()
            bimestre_atual = buscar_bimestre()

        tela_confirmar.setWindowTitle(f"Bimestre {bimestre_atual[0]}")
        tela_confirmar.show()
        
    def trocarAba(self, button):
        self.stackedWidget.setCurrentIndex(self.buttonGroup.id(button))
    
    class Turma(QMainWindow, TurmaWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)

            self.btnAdicionarProfessor.clicked.connect(lambda: tela_addProfessor.show())
            self.btnAdicionarAluno.clicked.connect(lambda: tela_addAluno.show())

            self.btnExcluirProfessor.clicked.connect(self.excluir_professor)
            self.btnExcluirAluno.clicked.connect(self.excluir_aluno)

        def trazer_professores(self):
            tabela = self.tabelaProfessor
            professor_banco = buscar_professores_turma(modelo_turma.ano, modelo_turma.nivel)         
            tabela.setRowCount(len(professor_banco))
            rowPos = 0

            for professorres in professor_banco:
                tabela.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(professorres[2]))
                tabela.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(professorres[3]))
                professor = buscar_professor_por_usuario_id(professorres[4])
                tabela.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(professor[1])) 
            
                tabela.item(rowPos, 0).setData(QtCore.Qt.UserRole, professor[6])

                tabela.item(rowPos, 0).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                tabela.item(rowPos, 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                tabela.item(rowPos, 2).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

                rowPos += 1

        def trazer_alunos(self):
            tabela = self.tabelaAlunos
            aluno_banco = buscar_alunos_turma(modelo_turma.ano, modelo_turma.nivel)
            tabela.setRowCount(len(aluno_banco))
            rowPos = 0

            for alunos in aluno_banco:
                tabela.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(alunos[2]))
                aluno = buscar_aluno_por_usuario_id(alunos[3])
                tabela.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(aluno[3]))
                
                tabela.item(rowPos, 0).setData(QtCore.Qt.UserRole, aluno[7])

                tabela.item(rowPos, 0).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                tabela.item(rowPos, 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

                rowPos += 1
        
        def excluir_professor(self):
            tabela = self.tabelaProfessor
            linha = tabela.currentRow()

            if linha < 0:
                mostrar_aviso('Selecione um professor para excluir')
            else:
                matricula = tabela.item(linha, 0).data(QtCore.Qt.UserRole)
                materia = tabela.item(linha, 1).text()

                excluir_professor_turma(matricula, modelo_turma.ano, modelo_turma.nivel, materia)
                
                self.trazer_professores()

        def excluir_aluno(self):
            tabela = self.tabelaAlunos
            linha = tabela.currentRow()
            
            if linha < 0:
                mostrar_aviso('Selecione um aluno para excluir')
            else:
                matricula = tabela.item(linha, 0).data(QtCore.Qt.UserRole)
                
                excluir_aluno_turma(matricula, modelo_turma.ano)

                self.trazer_alunos()

    class AddProfessor(QMainWindow, AddProfessorWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)

            self.btnAdicionar.clicked.connect(self.adicionar_professor)
            self.btnCancelar.clicked.connect(lambda: fechar(self, self.inputProfessor))
        
        def adicionar_professor(self):
            nome = self.inputProfessor.text()
            materia = self.comboBoxDisciplina.currentText()

            if nome == '':
                mostrar_aviso('Preencha o nome')
            else:
                nome = nome.split('- ')
                
                try:
                    if len(nome) > 1:
                        professor_banco = buscar_professor_por_matricula(nome[1])
                        adicionar_professor_turma(modelo_turma.ano, modelo_turma.nivel, nome[0], materia, professor_banco[8])               
                    else:
                        professor_banco = buscar_professor_por_nome_exato(nome[0])
                        adicionar_professor_turma(modelo_turma.ano, modelo_turma.nivel, nome[0], materia, professor_banco[8])
                except:
                    mostrar_aviso('Professor não encontrado')

                limpar_campos(self.inputProfessor)
                self.close()
                tela_turma.trazer_professores()

    class AddAluno(QMainWindow, AddAlunoWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)
            
            self.btnAdicionar.clicked.connect(self.adicionar_aluno)
            self.btnCancelar.clicked.connect(lambda: fechar(self, self.inputAluno))
        
        def adicionar_aluno(self):
            nome = self.inputAluno.text()

            if nome == '':
                mostrar_aviso('Preencha o nome')
            else:
                nome = nome.split('- ')
                
                try:
                    if len(nome) > 1:                   
                        aluno_banco = buscar_aluno_por_matricula(nome[1])
                        adicionar_aluno_turma(modelo_turma.ano, modelo_turma.nivel, nome[0], aluno_banco[8])                   
                    else:
                        aluno_banco = buscar_aluno_por_nome_exato(nome[0])
                        adicionar_aluno_turma(modelo_turma.ano, modelo_turma.nivel, nome[0], aluno_banco[9])
                except IntegrityError:
                    mostrar_aviso('Aluno já inserido em uma turma')
                except TypeError:
                    mostrar_aviso('Aluno não encontrado')

                limpar_campos(self.inputAluno)
                self.close()
                tela_turma.trazer_alunos()
        
    class EditarAluno(QMainWindow, EditAlunoWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)

            self.btnEditar.clicked.connect(self.edit_aluno)
            self.shortcut.activated.connect(self.edit_aluno)
            self.btnCancelar.clicked.connect(lambda: fechar(self, self.alunoNome, self.alunoEmail, self.alunoTelefone))
        
        def edit_aluno(self):
            tabela = tela_adm.tabela_aluno
            linha = tabela.currentRow()

            nome = self.alunoNome.text()
            email = self.alunoEmail.text()
            telefone = self.alunoTelefone.text()
            
            if nome == '':
                mostrar_aviso('Preencha o nome')
            elif is_email(email) == False:
                mostrar_aviso('Email invalido')
            else:
                matricula = tabela.item(linha, 3).text()
                
                alterar_usuario(nome, matricula)
                alterar_aluno(nome, email, telefone, matricula)
                limpar_campos(self.alunoNome, self.alunoEmail, self.alunoTelefone)
                
                self.close()
                tela_adm.trazer_alunos()
        
    class EditarProfessor(QMainWindow, EditProfessorWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)
            
            self.btnEditar.clicked.connect(self.edit_professor)
            self.shortcut.activated.connect(self.edit_professor)
            self.btnCancelar.clicked.connect(lambda: fechar(self, self.professorEmail, self.professorNome, self.professorTelefone))

        def edit_professor(self):
            tabela = tela_adm.tabela_professor
            linha = tabela.currentRow()

            nome = self.professorNome.text()
            email = self.professorEmail.text()
            telefone = self.professorTelefone.text()

            if nome == '':
                mostrar_aviso('Preencha o nome')
            elif is_email(email) == False:
                mostrar_aviso('Email invalido')
            else:
                matricula = tabela.item(linha, 4).text()

                alterar_usuario(nome, matricula)
                alterar_professor(nome, email, telefone, matricula)
                limpar_campos(self.professorNome, self.professorEmail, self.professorTelefone)

                self.close()
                tela_adm.trazer_professores()

class VisaoProfessor(QMainWindow, VisaoProfessorWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.buttonGroup.buttonClicked.connect(self.mudar_tela)
        self.btnLogout.clicked.connect(lambda: logout(self))
        self.ListaTurmas_2.itemDoubleClicked.connect(self.trazer_alunos)
    
    def mudar_tela(self, button):
        self.stackedWidget.setCurrentIndex(self.buttonGroup.id(button))
    
    def trazer_turmas(self):
        turmas_banco = buscar_turmas_por_professor_id(modelo_usuario.id)
        
        lista = self.ListaTurmas_2
        fundamental = 1
        medio = 2
        lista.clear()
        turmas_banco.sort()

        if turmas_banco == []:
            item = QtWidgets.QListWidgetItem()
            item.setText('Você não está em nenhuma turma')
            item.setFlags(QtCore.Qt.ItemIsSelectable)

            lista.addItem(item)
        else:
            lista.addItem('Ensino Fundamental')

            for turma in turmas_banco:
                if turma[1] == 'Ensino Fundamental':
                    lista.insertItem(fundamental, turma[0])
                    fundamental += 1
                    medio = fundamental + 1
                elif turma[1] == 'Ensino Medio':
                    fmedio = lista.findItems('Ensino Medio', QtCore.Qt.MatchContains)
                    if fmedio == []:
                        lista.addItem('Ensino Medio')

                    lista.insertItem(medio, turma[0])
                    medio += 1

            fmedio = lista.findItems('Ensino Medio', QtCore.Qt.MatchContains)
            ffundamental = lista.findItems('Ensino Fundamental', QtCore.Qt.MatchContains)
            
            if fmedio != []:
                itemMedio = fmedio[0]
                itemMedio.setFlags(QtCore.Qt.ItemIsSelectable)

            itemFundamental = ffundamental[0]

            itemFundamental.setFlags(QtCore.Qt.ItemIsSelectable)
            
    def mostrar_informacoes(self):
        professor_banco = buscar_professor_por_usuario_id(modelo_usuario.id)     

        self.labelNome.setText(f'Nome: {professor_banco[0]}')
        self.labelEmail.setText(f'Email: {professor_banco[3]}')
        self.labelSexo.setText(f'Sexo: {professor_banco[5]}')
        self.labelTelefone.setText(f'Telefone: {professor_banco[4]}')
        self.labelNasc.setText(f'Nascimento: {professor_banco[1]}')
        self.labelCpf.setText(f'Cpf: {professor_banco[2]}')

    def trazer_alunos(self, item):
        linha = self.ListaTurmas_2.currentRow() 
        medio = self.ListaTurmas_2.findItems('Ensino Medio', QtCore.Qt.MatchContains)
        if medio != []:
            linha_medio = self.ListaTurmas_2.row(medio[0])
        
            if linha > linha_medio:
                tipo = 'Ensino Medio'
            else:
                tipo = 'Ensino Fundamental'
        else:
            tipo = 'Ensino Fundamental'

        modelo_turma.variavel_para_modelo(item.text(), tipo)
        professor_banco = buscar_materia_professores_turma(modelo_turma.ano, modelo_turma.nivel, modelo_usuario.id)
        if len(professor_banco) > 1:
            tela_materias.comboBoxMateria.clear()
            for materia in professor_banco:               
                tela_materias.comboBoxMateria.addItem(materia[3])
            tela_materias.show()

        else:
            modelo_professor.materia_no_modelo(professor_banco[0][3])
        
        aluno_banco = buscar_alunos_turma(modelo_turma.ano, modelo_turma.nivel)
        tela_alunos.listWidget.clear()

        if aluno_banco == []:
            item = QtWidgets.QListWidgetItem()
            item.setText('Nenhum aluno na turma')
            item.setFlags(QtCore.Qt.ItemIsSelectable)

            tela_alunos.listWidget.addItem(item)

        for aluno in aluno_banco:
            item = QtWidgets.QListWidgetItem()
            item.setText(aluno[2])
            item.setData(QtCore.Qt.UserRole, aluno[3])

            tela_alunos.listWidget.addItem(item)
        if len(professor_banco) == 1:
            tela_alunos.show()

    class Alunos(QMainWindow, AlunosWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)

            self.listWidget.itemDoubleClicked.connect(self.mostrar_notas)

        def mostrar_notas(self, item):
            tela_notas.label_2.setText(f'Notas de: {item.text()}')

            modelo_aluno.passar_id(item.data(QtCore.Qt.UserRole))

            tela_notas.checar_notas()
            tela_notas.show()
    
    class Notas(QMainWindow, NotasWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)
        
            self.btnAplicar.clicked.connect(self.aplicar_notas)
            self.shortcut.activated.connect(self.aplicar_notas)
        
        def checar_notas(self):
            bimestre_banco = buscar_bimestre()

            if bimestre_banco is None:
                inserir_bimestre()
                bimestre_banco = buscar_bimestre()

            notas_banco = buscar_notas_por_aluno_id(modelo_professor.materia, modelo_aluno.id, bimestre_banco[0])

            if notas_banco is None:
                self.inputP1.setValue(0)
                self.inputP2.setValue(0)
                self.inputP3.setValue(0)
                self.inputR1.setValue(0)
                self.inputR2.setValue(0)
                self.inputR3.setValue(0)
            else:
                self.inputP1.setValue(notas_banco[1])
                self.inputP2.setValue(notas_banco[2])
                self.inputP3.setValue(notas_banco[3])
                self.inputR1.setValue(notas_banco[4])
                self.inputR2.setValue(notas_banco[5])
                self.inputR3.setValue(notas_banco[6])
        
        def aplicar_notas(self):
            p1 = self.inputP1.value()
            p2 = self.inputP2.value()
            p3 = self.inputP3.value()
            
            r1 = self.inputR1.value()
            r2 = self.inputR2.value()
            r3 = self.inputR3.value()

            bimestre_banco = buscar_bimestre()

            if bimestre_banco == None:
                inserir_bimestre()    
            
            bimestre_banco = buscar_bimestre()
            notas_banco = buscar_notas_por_aluno_id(modelo_professor.materia, modelo_aluno.id, bimestre_banco[0])

            if notas_banco is None:
                inserir_notas(modelo_professor.materia, p1, p2, p3, r1, r2, r3, bimestre_banco[0], modelo_aluno.id)
            else:
                alterar_notas(modelo_professor.materia, p1, p2, p3, r1, r2, r3, modelo_aluno.id)
            self.close()

class VisaoAluno(QMainWindow, AlunoWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.buttonGroup.buttonClicked.connect(self.mudar_pagina)
        self.btnLogout.clicked.connect(lambda: logout(self))
        self.listaNotas.itemDoubleClicked.connect(self.mostrar_notas)
    
    def mudar_pagina(self, button):
        self.stackedWidget.setCurrentIndex(self.buttonGroup.id(button))

    def mostrar_materias(self):
        lista = self.listaNotas
        materias_banco = buscar_materias_por_aluno(modelo_usuario.id)
        
        lista.clear()

        if materias_banco == []:
            item = QtWidgets.QListWidgetItem()
            item.setText('Nenhuma nota adicionada')
            item.setFlags(QtCore.Qt.ItemIsSelectable)

            lista.addItem(item)
        else:
            for materia in materias_banco:
                item = lista.findItems(f'{materia[0]}', QtCore.Qt.MatchContains)
                if item == []:
                    lista.addItem(materia[0])      

    def mostrar_informacoes(self):
        aluno_banco = buscar_aluno_por_usuario_id(modelo_usuario.id)

        self.labelNome.setText(f'Nome: {aluno_banco[0]}')
        self.labelEmail.setText(f'Email: {aluno_banco[4]}')
        self.labelSexo.setText(f'Sexo: {aluno_banco[6]}')
        self.labelResponsavel.setText(f'Responsavel: {aluno_banco[1]}')
        self.labelTelefone.setText(f'Telefone: {aluno_banco[5]}')
        self.labelNasc.setText(f'Nascimento: {aluno_banco[2]}')
        self.labelCpf.setText(f'Cpf: {aluno_banco[3]}')

    def mostrar_notas(self, item):
        tabela = tela_aluno_notas.tabelaNotas
        tela_aluno_notas.labelMateria.setText(item.text())
        notas_banco = buscar_notas_por_materia_aluno(item.text(), modelo_usuario.id)
        final = 0

        tabela.clear()
        tabela.setHorizontalHeaderItem(0, QTableWidgetItem('B1'))
        tabela.setHorizontalHeaderItem(1, QTableWidgetItem('B2'))
        tabela.setHorizontalHeaderItem(2, QTableWidgetItem('B3'))
        tabela.setHorizontalHeaderItem(3, QTableWidgetItem('B4'))
        tabela.setRowCount(7)

        for notas in notas_banco:
            tabela.setVerticalHeaderItem(0, QtWidgets.QTableWidgetItem('P1'))
            tabela.setVerticalHeaderItem(1, QtWidgets.QTableWidgetItem('P2'))
            tabela.setVerticalHeaderItem(2, QtWidgets.QTableWidgetItem('P3'))
            tabela.setVerticalHeaderItem(3, QtWidgets.QTableWidgetItem('R1'))
            tabela.setVerticalHeaderItem(4, QtWidgets.QTableWidgetItem('R2'))
            tabela.setVerticalHeaderItem(5, QtWidgets.QTableWidgetItem('R3'))
            tabela.setVerticalHeaderItem(6, QtWidgets.QTableWidgetItem('Final'))

            final = (notas[1] + notas[2] + notas[3] + notas[4] + notas[5] + notas[6]) / 6

            tabela.setItem(0, notas[7] - 1, QtWidgets.QTableWidgetItem(f'{notas[1]}'))
            tabela.setItem(1, notas[7] - 1, QtWidgets.QTableWidgetItem(f'{notas[2]}'))
            tabela.setItem(2, notas[7] - 1, QtWidgets.QTableWidgetItem(f'{notas[3]}'))
            tabela.setItem(3, notas[7] - 1, QtWidgets.QTableWidgetItem(f'{notas[4]}'))
            tabela.setItem(4, notas[7] - 1, QtWidgets.QTableWidgetItem(f'{notas[5]}'))
            tabela.setItem(5, notas[7] - 1, QtWidgets.QTableWidgetItem(f'{notas[6]}'))
            tabela.setItem(6, notas[7] - 1, QtWidgets.QTableWidgetItem(f'{final:.1f}'))

            tabela.item(0, notas[7] - 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(1, notas[7] - 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(2, notas[7] - 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(3, notas[7] - 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(4, notas[7] - 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(5, notas[7] - 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            tabela.item(6, notas[7] - 1).setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

        tela_aluno_notas.show()   

class AlunoNotas(QMainWindow, AlunoNotasWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)

class Login(QMainWindow, LoginWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.btnEntrar.clicked.connect(self.logar)
        self.shortcut.activated.connect(self.logar)
    
    def logar(self):
        usuario = self.inputUsuario.text()
        senha = self.inputSenha.text()

        usuario_banco = buscar_usuario_por_nome_e_senha(usuario, senha)
        
        if usuario_banco is None:
            mostrar_aviso('Usuario ou senha errados')
        else:
            self.close()
            limpar_campos(self.inputUsuario, self.inputSenha)
            modelo_usuario.variavel_para_modelo(usuario, senha, usuario_banco[4])
            
            if usuario_banco[3] == 0:
                tela_adm.show()
            elif usuario_banco[3] == 1: 
                modelo_professor.variavel_para_modelo(usuario)           
                tela_professor.show()
                tela_professor.trazer_turmas()
                tela_professor.mostrar_informacoes()
            else:
                tela_aluno.show()
                tela_aluno.mostrar_materias()
                tela_aluno.mostrar_informacoes()

class Aviso(QMainWindow, AvisoWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.btnOk.clicked.connect(lambda: self.close())
        self.shortcut.activated.connect(lambda: self.close())

class Confirmar(QMainWindow, ConfirmarWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.btnNao.clicked.connect(lambda: self.close())
        self.btnSim.clicked.connect(self.passar_bimestre)

    def passar_bimestre(self):
        bimestre_atual = buscar_bimestre()
        
        if bimestre_atual is None:
            inserir_bimestre()
            bimestre_atual = buscar_bimestre()
            atualizar_bimestre(bimestre_atual[0] + 1)
        else:
            if bimestre_atual[0] == 4:
                atualizar_bimestre(1)
                dropar_tabela_notas()
            else:
                atualizar_bimestre(bimestre_atual[0] + 1)
        
        bimestre_atual = buscar_bimestre() 
        self.close()

class Materias(QMainWindow, MateriasWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)
        
        self.btnSelecionar.clicked.connect(self.selecionar_materia)
        self.shortcut.activated.connect(self.selecionar_materia)

    def selecionar_materia(self):
        materia = self.comboBoxMateria.currentText()

        modelo_professor.materia_no_modelo(materia)
        self.close()
        tela_alunos.show()

if __name__ == "__main__":
    QApplication.setStyle("Fusion")
    qt = QApplication(sys.argv)
    qt.setWindowIcon(QtGui.QIcon('src/icone_programa.png'))
    
    tela_adm = Adm()
    tela_turma = Adm().Turma()
    tela_addProfessor = Adm().AddProfessor()
    tela_addAluno = Adm().AddAluno()
    tela_editarProfessor = Adm().EditarProfessor()
    tela_editarAluno = Adm().EditarAluno()
    tela_confirmar = Confirmar()

    tela_professor = VisaoProfessor()
    tela_alunos = VisaoProfessor().Alunos()
    tela_notas = VisaoProfessor().Notas()
    tela_materias = Materias()

    tela_aluno = VisaoAluno()
    tela_aluno_notas = AlunoNotas()

    tela_login = Login()
    tela_aviso = Aviso()

    modelo_turma = Turma()
    modelo_professor = Professor()
    modelo_aluno = Aluno()
    modelo_usuario = Usuario()

    tela_login.show()

    qt.exec_()
