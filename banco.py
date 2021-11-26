import sqlite3

def conectar():
    banco = sqlite3.connect('banco.db')
    banco.cursor().execute('PRAGMA foreign_keys = ON')
    return banco

def criar_tabela_usuario():
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(usuario TEXT, senha TEXT, tipo_usuario INTEGER, id INTEGER PRIMARY KEY);')
    banco.commit()
    banco.close()

def criar_tabela_professor():
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS professor(nome TEXT, nascimento TEXT, cpf TEXT, email TEXT, telefone TEXT, sexo TEXT, matricula TEXT, usuario_id INTEGER PRIMARY KEY, CONSTRAINT fk_usuarios FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE);')
    banco.commit()
    banco.close()

def criar_tabela_aluno():
    banco = conectar()
    cursor = banco.cursor() 
    cursor.execute('CREATE TABLE IF NOT EXISTS aluno(nome TEXT, responsavel TEXT, nascimento TEXT, cpf TEXT, email TEXT, telefone TEXT, sexo TEXT, matricula TEXT, usuario_id INTEGER PRIMARY KEY, CONSTRAINT fk_usuarios FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE);')
    banco.commit()
    banco.close()

def criar_tabela_turmas_aluno():
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS turmasAluno(ano TEXT, nivel TEXT, aluno TEXT, aluno_id INTEGER , UNIQUE (aluno_id), CONSTRAINT fk_aluno FOREIGN KEY (aluno_id) REFERENCES aluno(usuario_id) ON DELETE CASCADE)')
    banco.commit()
    banco.close()

def criar_tabela_turmas_professor():
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS turmasProfessor(ano TEXT, nivel TEXT, professor TEXT, materia TEXT, professor_id INTEGER , UNIQUE (professor_id, ano, nivel, materia), CONSTRAINT fk_professor FOREIGN KEY (professor_id) REFERENCES professor(usuario_id) ON DELETE CASCADE)')
    banco.commit()
    banco.close()

def criar_tabela_bimestre():
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS bimestres(atual INTEGER)')
    banco.commit()
    banco.close()

def criar_tabela_notas():
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS notas(materia TEXT, p1 REAL, p2 REAL, p3 REAL, r1 REAL, r2 REAL, r3 REAL, bimestre_atual INTEGER, aluno_id INTEGER, CONSTRAINT fk_aluno FOREIGN KEY (aluno_id) REFERENCES aluno(usuario_id) ON DELETE CASCADE)')
    banco.commit()
    banco.close()

def criar_usuario(usuario, senha, tipo_usuario):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO usuarios (usuario, senha, tipo_usuario) VALUES("{usuario}", "{senha}", {tipo_usuario});')
    banco.commit()
    banco.close()

def criar_aluno(nome, responsavel, nascimento, cpf, email, telefone, sexo, matricula, id):
    criar_tabela_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO aluno VALUES("{nome}", "{responsavel}", "{nascimento}", "{cpf}", "{email}", "{telefone}", "{sexo}", "{matricula}", {id});')
    banco.commit()
    banco.close()

def criar_professor(nome, nascimento, cpf, email, telefone, sexo, matricula, id):
    criar_tabela_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO professor VALUES("{nome}", "{nascimento}", "{cpf}", "{email}", "{telefone}", "{sexo}","{matricula}", {id});')
    banco.commit()
    banco.close()

def deletar_usuario_por_senha(senha):
    criar_tabela_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'DELETE FROM usuarios WHERE senha="{senha}"')
    banco.commit()
    banco.close()

def deletar_aluno_por_matricula(matricula):
    criar_tabela_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'DELETE FROM aluno WHERE matricula="{matricula}"')
    banco.commit()
    banco.close()

def deletar_professor_por_matricula(matricula):
    criar_tabela_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'DELETE FROM professor WHERE matricula="{matricula}"')
    banco.commit()
    banco.close()

def buscar_professor_por_usuario_id(id):
    criar_tabela_usuario()
    criar_tabela_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * from professor WHERE usuario_id="{id}"')
    return cursor.fetchone()

def buscar_professor_por_matricula(matricula):
    criar_tabela_usuario()
    criar_tabela_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT rowid, * from professor WHERE matricula="{matricula}"')
    return cursor.fetchone()

def buscar_aluno_por_usuario_id(id):
    criar_tabela_usuario()
    criar_tabela_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * from aluno WHERE usuario_id="{id}"')
    return cursor.fetchone()

def buscar_usuario_por_nome_e_senha(usuario, senha):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT rowid, * FROM usuarios WHERE usuario="{usuario}" AND senha="{senha}";')
    return cursor.fetchone()

def buscar_usuario_por_matricula(matricula):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT rowid, * FROM usuarios WHERE senha="{matricula}"')
    return cursor.fetchone()

def buscar_matricula(matricula):
    criar_tabela_aluno()
    criar_tabela_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT p.matricula, a.matricula FROM professor p JOIN aluno a WHERE p.matricula="{matricula}" OR a.matricula="{matricula}";')
    return cursor.fetchone()

def buscar_cpf(cpf):
    criar_tabela_aluno()
    criar_tabela_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT p.cpf, a.cpf FROM professor p JOIN aluno a WHERE p.cpf="{cpf}" OR a.cpf="{cpf}";')
    return cursor.fetchone()

def buscar_todos_alunos():
    criar_tabela_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('SELECT rowid, * FROM aluno')
    return cursor.fetchall()

def buscar_aluno_por_nome_like(nome):
    criar_tabela_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM aluno WHERE nome LIKE '%{nome}%'")
    return cursor.fetchall()

def buscar_aluno_por_matricula(matricula):
    criar_tabela_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM aluno WHERE matricula="{matricula}"')
    return cursor.fetchone()

def buscar_professor_por_nome_like(nome):
    criar_tabela_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM professor WHERE nome LIKE "%{nome}%"')
    return cursor.fetchall()

def buscar_aluno_por_nome_exato(nome):
    criar_tabela_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM aluno WHERE nome='{nome}'")
    return cursor.fetchone()

def buscar_turmas_aluno_por_matricula(matricula):
    criar_tabela_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM aluno WHERE matricula="{matricula}"')
    return cursor.fetchone()

def buscar_professor_por_nome_exato(nome):
    criar_tabela_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT rowid, * FROM professor WHERE nome="{nome}"')
    return cursor.fetchone()

def buscar_todos_professores():
    criar_tabela_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('SELECT rowid, * FROM professor')
    return cursor.fetchall()

def buscar_professores_turma(ano, nivel):
    criar_tabela_turmas_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM turmasProfessor WHERE ano="{ano}" AND nivel="{nivel}"')
    return cursor.fetchall()

def buscar_materia_professores_turma(ano, nivel, professor):
    criar_tabela_turmas_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM turmasProfessor WHERE ano="{ano}" AND nivel="{nivel}" AND professor_id="{professor}"')
    return cursor.fetchall()

def buscar_turmas_por_professor_id(professor_id):
    criar_tabela_turmas_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM turmasProfessor WHERE professor_id="{professor_id}"')
    return cursor.fetchall()

def buscar_materias_por_aluno(aluno_id):
    criar_tabela_notas()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT materia FROM notas WHERE aluno_id="{aluno_id}"')
    return cursor.fetchall()

def buscar_alunos_turma(ano, nivel):
    criar_tabela_turmas_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM turmasAluno WHERE ano="{ano}" AND nivel="{nivel}"')
    return cursor.fetchall()

def buscar_notas_por_materia_aluno(materia, aluno):
    criar_tabela_notas()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM notas WHERE materia="{materia}" AND aluno_id="{aluno}"')
    return cursor.fetchall()

def buscar_notas_por_aluno_id(materia, aluno_id, bimestre):
    criar_tabela_notas()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM notas WHERE materia="{materia}" AND aluno_id={aluno_id} AND bimestre_atual={bimestre}')
    return cursor.fetchone()

def buscar_todas_notas_por_aluno_id(aluno_id):
    criar_tabela_notas()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM notas WHERE aluno_id={aluno_id}')
    return cursor.fetchall()

def alterar_aluno(nome, email, telefone, matricula):
    criar_tabela_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'UPDATE aluno SET nome = "{nome}", email = "{email}", telefone = "{telefone}" WHERE matricula="{matricula}"')
    banco.commit()
    banco.close()

def alterar_professor(nome, email, telefone, matricula):
    criar_tabela_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'UPDATE professor SET nome = "{nome}", email = "{email}", telefone = "{telefone}" WHERE matricula="{matricula}"')
    banco.commit()
    banco.close()

def adicionar_professor_turma(ano, nivel, professor, materia, id):
    criar_tabela_professor()
    criar_tabela_turmas_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO turmasProfessor VALUES("{ano}", "{nivel}", "{professor}", "{materia}", {id})')
    banco.commit()
    banco.close()

def adicionar_aluno_turma(ano, nivel, aluno, id):
    criar_tabela_aluno()
    criar_tabela_turmas_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO turmasAluno VALUES('{ano}', '{nivel}', '{aluno}', {id})")
    banco.commit()
    banco.close()

def excluir_professor_turma(matricula, ano, nivel):
    criar_tabela_professor()
    criar_tabela_turmas_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'DELETE FROM turmasProfessor WHERE professor_id=(SELECT usuario_id FROM professor WHERE matricula="{matricula}") AND ano="{ano}" AND nivel="{nivel}"')
    banco.commit()
    banco.close()

def excluir_aluno_turma(matricula, ano):
    criar_tabela_aluno()
    criar_tabela_turmas_professor()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'DELETE FROM turmasAluno WHERE aluno_id=(SELECT usuario_id FROM aluno WHERE matricula="{matricula}") AND ano="{ano}"')
    banco.commit()
    banco.close()

def inserir_notas(materia, p1, p2, p3, r1, r2, r3, bimestre, aluno_id):
    criar_tabela_bimestre()
    criar_tabela_notas()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO notas VALUES("{materia}", {p1}, {p2}, {p3}, {r1}, {r2}, {r3}, {bimestre}, {aluno_id})')
    banco.commit()
    banco.close()

def alterar_notas(materia, p1, p2, p3, r1, r2, r3, aluno_id):
    criar_tabela_bimestre()
    criar_tabela_notas()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'UPDATE notas SET p1 = {p1}, p2 = {p2}, p3 = {p3}, r1 = {r1}, r2 = {r2}, r3 = {r3} WHERE aluno_id={aluno_id} AND materia="{materia}"')
    banco.commit()
    banco.close()

def buscar_bimestre():
    criar_tabela_bimestre()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM bimestres')
    return cursor.fetchone()

def inserir_bimestre():
    criar_tabela_bimestre()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('INSERT INTO bimestres VALUES(1)')
    banco.commit()
    banco.close()

def atualizar_bimestre(bimestre):
    criar_tabela_bimestre()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'UPDATE bimestres SET atual={bimestre}')
    banco.commit()
    banco.close()

def dropar_tabela_notas():
    criar_tabela_notas()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('DROP TABLE notas')
    banco.commit()
    banco.close()

if __name__ == "__main__":
    criar_usuario('adm', '123', 0)
