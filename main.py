import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter, QMainWindow, QApplication, QTableWidgetItem

from banco import *
import cpf as lib_cpf
from pyisemail import is_email

from random import randint
from classes import Aluno, Professor, Turma, Usuario

from interfaces.aviso import AvisoWindow
from interfaces.login import LoginWindow

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

        self.btnEditarAlunos.clicked.connect(lambda: tela_editarAluno.show() if self.tabela_aluno.currentRow() + 1 != 0 else mostrar_aviso('Clique em um item'))
        self.btnEditarProfessor.clicked.connect(lambda: tela_editarProfessor.show() if self.tabela_professor.currentRow() + 1 != 0 else mostrar_aviso('Clique em um item'))

        self.btnBuscarProfessor.clicked.connect(self.buscar_professor)
        self.btnBuscarAlunos.clicked.connect(self.buscar_aluno)

        self.btnExcluirAlunos.clicked.connect(self.excluir_aluno)
        self.btnExcluirProfessor.clicked.connect(self.excluir_professor)

        self.btnLogout.clicked.connect(lambda: logout(self))
        self.trazer_alunos()
        self.trazer_professores()
    
    def mostrar_turma(self, item):
        linha = self.listaTurmas.currentRow()
        tipo = None
        professor_banco = buscar_todos_professores()
        aluno_banco = buscar_todos_alunos()

        nomesProfessores = []
        nomesAlunos = []

        for nome in aluno_banco:
            nomesAlunos.append(nome[1])
        for nome in professor_banco:
            nomesProfessores.append(nome[1])
        
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
        
        if matricula_banco != None:
            while matricula_banco != None:
                matricula = randint(100000, 999999)
                matricula_banco = buscar_matricula(matricula)
        
        if nome == '' or nascimento == '' or sexo == '' or responsavel == '':
            mostrar_aviso('Preencha todos os dados') 
        elif lib_cpf.checar(cpf) == False:
            mostrar_aviso('Cpf invalido')
        elif is_email(email) == False:
            mostrar_aviso('Email invalido') 
        elif cpf_banco != None:
            mostrar_aviso('Cpf já existe') 
        else:
            criar_usuario(nome, matricula, 2)
            usuario_banco = buscar_usuario_por_nome(nome)
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

        if matricula_banco != None:
            while matricula_banco != None:
                matricula = randint(100000, 999999)
                matricula_banco = buscar_matricula(matricula)

        if nome == '' or nascimento == '' or sexo == '':
            mostrar_aviso('Preencha todos os dados')
        elif lib_cpf.checar(cpf) == False:
            mostrar_aviso('Cpf invalido')
        elif is_email(email) == False:
            mostrar_aviso('Email invalido')
        elif cpf_banco != None:
            mostrar_aviso('Cpf já existe')
        else:
            criar_usuario(nome, matricula, 1)
            usuario_banco = buscar_usuario_por_nome(nome)
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
            deletar_aluno_por_matricula(matricula)
            deletar_usuario_por_senha(matricula)
            self.trazer_alunos()
    
    def excluir_professor(self):
        linha = tela_adm.tabela_professor.currentRow()
        tabela = self.tabela_professor

        if linha + 1 == 0:
            mostrar_aviso('Selecione um professor para excluir')
        else:
            matricula = int(tabela.item(linha, 4).text())
            deletar_professor_por_matricula(matricula)
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
            rowPos += 1

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
                professor = buscar_professor_por_nome_exato(professorres[2])
                tabela.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(professor[2]))
                rowPos += 1

        def trazer_alunos(self):
            tabela = self.tabelaAlunos
            aluno_banco = buscar_alunos_turma(modelo_turma.ano, modelo_turma.nivel)
            tabela.setRowCount(len(aluno_banco))
            rowPos = 0

            for alunos in aluno_banco:
                tabela.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(alunos[2]))
                aluno = buscar_aluno_por_nome_exato(alunos[2])
                tabela.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(aluno[3]))
                rowPos += 1
        
        def excluir_professor(self):
            tabela = self.tabelaProfessor
            linha = tabela.currentRow()
            
            if linha < 0:
                mostrar_aviso('Selecione um professor para excluir')
            else:
                nome = tabela.item(linha, 0).text()
                professor_banco = buscar_professor_por_nome_exato(nome)

                excluir_professor_turma(professor_banco[7], modelo_turma.ano)
                
                self.trazer_professores()


        def excluir_aluno(self):
            tabela = self.tabelaAlunos
            linha = tabela.currentRow()
            
            if linha < 0:
                mostrar_aviso('Selecione um aluno para excluir')
            else:
                nome = tabela.item(linha, 0).text()
                aluno_banco = buscar_aluno_por_nome_exato(nome) 

                excluir_aluno_turma(aluno_banco[8], modelo_turma.ano)
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
                professor_banco = buscar_professor_por_nome_exato(nome)
                adicionar_professor_turma(modelo_turma.ano, modelo_turma.nivel, nome, materia, professor_banco[8])
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
                aluno_banco = buscar_aluno_por_nome_exato(nome)
                try:
                    adicionar_aluno_turma(modelo_turma.ano, modelo_turma.nivel, nome, aluno_banco[0])
                except:
                    mostrar_aviso('Aluno já inserido em uma turma')

                limpar_campos(self.inputAluno)
                self.close()
                tela_turma.trazer_alunos()
        
    class EditarAluno(QMainWindow, EditAlunoWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)

            self.btnEditar.clicked.connect(self.edit_aluno)
            self.btnCancelar.clicked.connect(lambda: fechar(self, self.alunoNome, self.alunoEmail, self.alunoTelefone))
        
        def edit_aluno(self):
            linha = tela_adm.tabela_aluno.currentRow() + 1

            nome = self.alunoNome.text()
            email = self.alunoEmail.text()
            telefone = self.alunoTelefone.text()
            
            if nome == '':
                mostrar_aviso('Preencha o nome')
            elif is_email(email) == False:
                mostrar_aviso('Email invalido')
            else:
                alterar_aluno(nome, email, telefone, linha)
                limpar_campos(self.alunoNome, self.alunoEmail, self.alunoTelefone)

                self.close()
                tela_adm.trazer_alunos()
        
    class EditarProfessor(QMainWindow, EditProfessorWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)
            
            self.btnEditar.clicked.connect(self.edit_professor)
            self.btnCancelar.clicked.connect(lambda: fechar(self, self.professorEmail, self.professorNome, self.professorTelefone))

        def edit_professor(self):
            linha = tela_adm.tabela_professor.currentRow() + 1

            nome = self.professorNome.text()
            email = self.professorEmail.text()
            telefone = self.professorTelefone.text()

            if nome == '':
                mostrar_aviso('Preencha o nome')
            elif is_email(email) == False:
                mostrar_aviso('Email invalido')
            else:
                alterar_professor(nome, email, telefone, linha)
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
        turmas_banco = buscar_turmas_por_professor(modelo_professor.nome)

        lista = self.ListaTurmas_2
        fundamental = 1
        medio = 2
        lista.clear()
        turmas_banco.sort()

        if turmas_banco == []:
            lista.addItem('Você não está em nenhuma turma')
        else:
            lista.addItem('Ensino Fundamental')

            for turma in turmas_banco:
                if turma[1] == 'Ensino Fundamental':                       
                    lista.insertItem(fundamental, turma[0])
                    fundamental += 1
                    medio = fundamental + 1
                elif turma[1] == 'Ensino Medio':
                    if lista.count() == 1:
                        lista.addItem('Ensino Medio')
                    lista.insertItem(medio, turma[0])
                    medio += 1
    
    def mostrar_informacoes(self):
        professor_banco = buscar_professor_por_usuario(modelo_usuario.usuario, modelo_usuario.senha)     

        self.labelNome.setText(f'Nome: {professor_banco[0]}')
        self.labelEmail.setText(f'Email: {professor_banco[3]}')
        self.labelSexo.setText(f'Sexo: {professor_banco[5]}')
        self.labelTelefone.setText(f'Telefone: {professor_banco[4]}')
        self.labelNasc.setText(f'Nascimento: {professor_banco[1]}')
        self.labelCpf.setText(f'Cpf: {professor_banco[2]}')

    def trazer_alunos(self, item):
        linha = self.ListaTurmas_2.currentRow() 
        medio = self.ListaTurmas_2.findItems('Ensino Medio', QtCore.Qt.MatchContains)
        linha_medio = self.ListaTurmas_2.row(medio[0])
        
        if linha > linha_medio:
            tipo = 'Ensino Medio'
        else:
            tipo = 'Ensino Fundamental'

        modelo_turma.variavel_para_modelo(item.text(), tipo)
        professor_banco = buscar_materia_professores_turma(modelo_turma.ano, modelo_turma.nivel, modelo_usuario.id)
        modelo_professor.materia_no_modelo(professor_banco[0][3])
        aluno_banco = buscar_alunos_turma(modelo_turma.ano, modelo_turma.nivel)
        tela_alunos.listWidget.clear()

        for aluno in aluno_banco:
            tela_alunos.listWidget.addItem(aluno[2])

        tela_alunos.show()

    class Alunos(QMainWindow, AlunosWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)

            self.listWidget.itemDoubleClicked.connect(self.mostrar_notas)

        def mostrar_notas(self, item):
            tela_notas.label_2.setText(f'Notas de: {item.text()}')
            
            aluno_banco = buscar_aluno_por_nome_exato(item.text())

            modelo_aluno.variavel_para_modelo(aluno_banco[1])

            tela_notas.show()
    
    class Notas(QMainWindow, NotasWindow):
        def __init__(self, parent = None):
            super().__init__(parent=parent)
            super().setupUi(self)
        
            self.btnAplicar.clicked.connect(self.aplicar_notas)
        
        def aplicar_notas(self):
            p1 = float(self.inputP1.text())
            p2 = float(self.inputP2.text())
            p3 = float(self.inputP3.text())

            r1 = float(self.inputR1.text())
            r2 = float(self.inputR2.text())
            r3 = float(self.inputR3.text())

            bimestre_banco = buscar_bimestre()
            aluno_banco = buscar_aluno_por_nome_exato(modelo_aluno.nome)

            if bimestre_banco == None:
                inserir_bimestre()

            bimestre_banco = buscar_bimestre()
            inserir_notas(modelo_professor.materia, p1, p2, p3, r1, r2, r3, bimestre_banco[0], aluno_banco[9])
            self.close()

class VisaoAluno(QMainWindow, AlunoWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.buttonGroup.buttonClicked.connect(self.mudar_pagina)
        self.btnLogout.clicked.connect(lambda: logout(self))
    
    def mudar_pagina(self, button):
        self.stackedWidget.setCurrentIndex(self.buttonGroup.id(button))

    def mostrar_materias(self):
        lista = self.listaNotas
        materias_banco = buscar_materias_por_aluno(modelo_usuario.id)
        
        lista.clear()
        
        for materia in materias_banco:           
            lista.addItem(materia[0])      

    def mostrar_informacoes(self):
        aluno_banco = buscar_aluno_por_usuario(modelo_usuario.usuario, modelo_usuario.senha)
        
        self.labelNome.setText(f'Nome: {aluno_banco[0]}')
        self.labelEmail.setText(f'Email: {aluno_banco[4]}')
        self.labelSexo.setText(f'Sexo: {aluno_banco[6]}')
        self.labelResponsavel.setText(f'Responsavel: {aluno_banco[1]}')
        self.labelTelefone.setText(f'Telefone: {aluno_banco[5]}')
        self.labelNasc.setText(f'Nascimento: {aluno_banco[2]}')
        self.labelCpf.setText(f'Cpf: {aluno_banco[3]}')      

class Login(QMainWindow, LoginWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.btnEntrar.clicked.connect(self.logar)
    
    def logar(self):
        usuario = self.inputUsuario.text()
        senha = self.inputSenha.text()

        usuario_banco = buscar_usuario_por_nome(usuario)

        if usuario_banco is None:
            mostrar_aviso('Usuario não existe')
        elif senha != usuario_banco[2]:
            mostrar_aviso('Senha errada!')
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
                aluno_banco = buscar_turmas_aluno_por_matricula(modelo_usuario.senha)
                #print(aluno_banco)
                #modelo_turma.variavel_para_modelo(aluno_banco[0], aluno_banco[1])
                tela_aluno.show()
                tela_aluno.mostrar_materias()
                tela_aluno.mostrar_informacoes()

class Aviso(QMainWindow, AvisoWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.btnOk.clicked.connect(lambda: self.close())

if __name__ == "__main__":
    qt = QApplication(sys.argv)

    tela_adm = Adm()
    tela_turma = Adm().Turma()
    tela_addProfessor = Adm().AddProfessor()
    tela_addAluno = Adm().AddAluno()
    tela_editarProfessor = Adm().EditarProfessor()
    tela_editarAluno = Adm().EditarAluno()

    tela_professor = VisaoProfessor()
    tela_alunos = VisaoProfessor().Alunos()
    tela_notas = VisaoProfessor().Notas()

    tela_aluno = VisaoAluno()

    tela_login = Login()
    tela_aviso = Aviso()

    modelo_turma = Turma()
    modelo_professor = Professor()
    modelo_aluno = Aluno()
    modelo_usuario = Usuario()

    tela_login.show()

    qt.exec_()
