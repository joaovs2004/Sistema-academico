class Turma():
    def __init__(self) -> None:
        self.ano = None
        self.nivel = None

    def variavel_para_modelo(self, ano, nivel):
        self.ano = ano
        self.nivel = nivel

class Professor():
    def __init__(self) -> None:
        self.nome = None
        self.materia = None
        self.nascimento = None
    
    def variavel_para_modelo(self, nome = None, nascimento = None):
        self.nascimento = nascimento
        self.nome = nome

    def materia_no_modelo(self, materia):
        self.materia = materia

class Aluno():
    def __init__(self) -> None:
        self.nome = None
        self.nascimento = None
        
    
    def variavel_para_modelo(self, nome = None, nascimento = None):
        self.nascimento = nascimento
        self.nome = nome 
        

class Usuario():
    def __init__(self) -> None:
        self.usuario = None
        self.senha = None
        self.id = None

    def variavel_para_modelo(self, usuario = None, senha = None, id = None):
        self.usuario = usuario
        self.senha = senha
        self.id = id