import sqlite3

conn = sqlite3.connect('EscolaApp_versao2.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_endereco(
        id_endereco INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        logradouro VARCHAR(65) NOT NULL,
        complemento VARCHAR(45) NOT NULL,
        bairro VARCHAR(45) NOT NULL,
        cep VARCHAR(8) NOT NULL,
        numero INTEGER NOT NULL
    );
""")

print('table "tb_endereco" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_escola(
        id_escola INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        id_endereco INTEGER NOT NULL,
        id_campus INTEGER NOT NULL
    );
""")

print('table "tb_escola" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_aluno(
        id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        matricula VARCHAR(12) NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        nascimento DATE NOT NULL,
        id_endereco INTEGER NOT NULL,
        id_curso INTEGER NOT NULL
    );
""")

print('table "tb_aluno" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_professor(
        id_professor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        id_endereco INTEGER NOT NULL
    )
""")

print('table "tb_professor" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_disciplina(
        id_disciplina INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        id_professor INTEGER NOT NULL
    );
""")

print('table "tb_disciplina" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_curso(
        id_curso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        id_turno INTEGER NOT NULL
    );
""")

print('table "tb_curso" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_campus(
        id_campus INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        sigla VARCHAR(3) NOT NULL,
        cidade VARCHAR(45) NOT NULL
    )
""")

print('table "tb_campus" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_turma(
        id_turma INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        id_curso INTEGER NOT NULL
    );
""")

print('table "tb_turma" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_turno(
        id_turno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(10) NOT NULL
    )
""")

print('table "tb_turno" created successfully =)')

conn.close()
