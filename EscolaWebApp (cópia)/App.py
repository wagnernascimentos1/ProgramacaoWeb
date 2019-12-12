from flask import Flask
from flask import request
from flask import jsonify
'''
Adicionar a importação do CORS e não esquecer de fazer o pip no flask-env:
$ pip install -U flask-cors
'''
from flask_cors import CORS

from flask_json_schema import JsonSchema, JsonValidationError
import sqlite3
import logging

# Inicializando a aplicação.
app = Flask(__name__)

# Logging
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("escolaapp.log")
handler.setFormatter(formatter)

logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Validação
schema = JsonSchema()
schema.init_app(app)

endereco_schema = {
    'required': ['logradouro', 'complemento',  'bairro', 'cep', 'numero'],
    'properties': {
        'logradouro': {'type': 'string'},
        'complemento': {'type': 'string'},
        'bairro': {'type': 'string'},
        'cep': {'type': 'string'},
        'numero': {'type': 'string'}
    }
}

escola_schema = {
    'required': ['nome', 'id_endereco', 'id_campus'],
    'properties': {
        'nome': {'type': 'string'},
        'id_endereco': {'type': 'string'},
        'id_campus': {'type': 'string'}
    }
}

aluno_schema = {
    'required': ['nome', 'matricula', 'cpf', 'nascimento', 'id_endereco', 'id_curso'],
    'properties': {
        'nome': {'type': 'string'},
        'matricula': {'type': 'string'},
        'cpf': {'type': 'string'},
        'nascimento': {'type': 'string'},
        'id_endereco': {'type': 'string'},
        'id_curso': {'type': 'string'}
    }
}

professor_schema = {
    'required': ['nome', 'id_endereco'],
    'properties': {
        'nome': {'type': 'string'},
        'id_endereco': {'type': 'string'}
    }
}

disciplina_schema = {
    'required': ['nome', 'id_professor'],
    'properties': {
        'nome': {'type': 'string'},
        'id_professor': {'type': 'string'}
    }
}

curso_schema = {
    'required': ['nome','id_turno'],
    'properties': {
        'nome': {'type': 'string'},
        'id_turno': {'type': 'string'}
    }
}

campus_schema = {
    'required': ['sigla','cidade'],
    'properties': {
        'sigla': {'type': 'string'},
        'cidade': {'type': 'string'}
    }
}

turma_schema = {
    'required': ['nome','id_curso'],
    'properties': {
        'nome': {'type': 'string'},
        'id_curso': {'type': 'string'}
    }
}

turno_schema = {
    'required': ['nome'],
    'properties': {
        'nome': {'type': 'string'}
    }
}

databaseName = 'EscolaApp_versao2.db'

#getEnderecos
@app.route("/enderecos", methods=['GET'])
def getEnderecos():
    logger.info("Listando endereços")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_endereco;
        """)

        enderecos = []
        for linha in cursor.fetchall():
            endereco = {
                "idtb_endereco":linha[0],
                "logradouro":linha[1],
                "complemento":linha[2],
                "bairro":linha[3],
                "cep":linha[4],
                "numero":linha[5]
            }
            enderecos.append(endereco)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(enderecos)

#getEnderecosByID
@app.route("/enderecos/<int:id>", methods=['GET'])
def getEnderecosByID(id):
    logger.info("Listando endereço pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_endereco
            WHERE idtb_endereco = ?;
        """, (id, ))

        linha = cursor.fetchone()
        endereco = {
            "idtb_endereco":linha[0],
            "logradouro":linha[1],
            "complemento":linha[2],
            "bairro":linha[3],
            "cep":linha[4],
            "numero":linha[5]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(endereco)

#setEndereco
@app.route("/endereco", methods=['POST'])
@schema.validate(endereco_schema)
def setEndereco():
    logger.info('Cadastrando o endereco')

    try:
        endereco = request.get_json()
        logradouro = endereco["logradouro"]
        complemento = endereco["complemento"]
        bairro = endereco["bairro"]
        cep = endereco["cep"]
        numero = endereco["numero"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_endereco(logradouro, complemento, bairro, cep, numero)
            VALUES(?, ?, ?, ?, ?);
        """, (logradouro, complemento, bairro, cep, numero))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        endereco['id_endereco'] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Endereço cadastrado com sucesso.")

    return jsonify(endereco)

#updateEndereco
@app.route("/endereco/<int:id>", methods=['PUT'])
@schema.validate(endereco_schema)
def updateEndereco(id):
    logger.info('Atualizando o endereço')

    try:
        endereco = request.get_json()
        logradouro = endereco["logradouro"]
        complemento = endereco["complemento"]
        bairro = endereco["bairro"]
        cep = endereco["cep"]
        numero = endereco["numero"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_endereco
            WHERE id_endereco = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_endereco
                SET logradouro=?, complemento=?, bairro=?, cep=?, numero=?
                where id_endereco = ?
                """, (logradouro,complemento, bairro, cep, numero, id))
            conn.commit()
        else:
            cursor.execute("""
                INSERT INTO tb_endereco(logradouro, complemento, bairro, cep, numero)
                VALUES(?, ?, ?, ?, ?);
            """, (logradouro, complemento, bairro, cep, numero))

            conn.commit()
            conn.close()

            id = cursor.lastrowid
            endereco['idtb_endereco'] = id

        conn.close()

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Update feito com sucesso.")

    return jsonify(endereco)

#getEscolas
@app.route("/escolas", methods=['GET'])
def getEscolas():
    logger.info("Listando escolas")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_escola;
        """)

        escolas = []
        for linha in cursor.fetchall():
            escola = {
                "id_escola":linha[0],
                "nome":linha[1],
                "id_endereco":linha[2],
                "id_campus":linha[3]
            }
            escolas.append(escola)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escolas)

#getEscolasByID
@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolasByID(id):
    logger.info("Listando escola pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_escola
            WHERE id_escola = ?;
        """, (id, ))

        linha = cursor.fetchone()
        escola = {
            "id_escola":linha[0],
            "nome":linha[1],
            "id_endereco":linha[2],
            "id_campus":linha[3]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escola)

#setEscola
@app.route("/escola", methods=['POST'])
@schema.validate(escola_schema)
def setEscola():
    logger.info('Cadastrando a escola')

    try:
        escola = request.get_json()
        nome = escola["nome"]
        id_endereco = escola["id_endereco"]
        id_campus = escola["id_campus"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_escola(nome, id_endereco, id_campus)
            VALUES(?, ?, ?);
        """, (nome, id_endereco, id_campus))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        escola['id_escola'] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Escola cadastrada com sucesso.")

    return jsonify(escola)

#updateEscola
@app.route("/escola/<int:id>", methods=['PUT'])
@schema.validate(escola_schema)
def updateEscola(id):
    logger.info('Atualizando a escola')

    try:
        escola = request.get_json()
        nome = escola["nome"]
        id_endereco = escola["id_endereco"]
        id_campus = escola["id_campus"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_escola
            WHERE id_escola = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_escola
                SET nome=?, id_endereco=?, id_campus=?
                where id_escola =?
                """, (nome,fk_id_endereco, id_campus, id))
            conn.commit()
        else:
            cursor.execute("""
                INSERT INTO tb_escola(nome, id_endereco, id_campus)
                VALUES(?, ?, ?);
            """, (nome, id_endereco, id_campus))

            conn.commit()
            conn.close()

            id = cursor.lastrowid
            escola['id_escola'] = id

        conn.close()

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Update realizado com sucesso.")

    return jsonify(escola)

#getAlunos
@app.route("/alunos", methods=['GET'])
def getAlunos():
    logger.info("Listando os alunos")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_aluno;
        """)

        alunos = []
        for linha in cursor.fetchall():
            aluno = {
                "id_aluno":linha[0],
                "nome":linha[1],
                "matricula":linha[2],
                "cpf":linha[3],
                "nascimento":linha[4],
                "id_endereco":linha[5],
                "id_curso":linha[6]
            }
            alunos.append(aluno)

        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(alunos)

#getAlunosByID
@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):
    logger.info("Listando o aluno pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_aluno
            WHERE id_aluno = ?;
        """,(id, ))

        linha = cursor.fecthone()
        aluno = {
            "id_aluno":linha[0],
            "nome":linha[1],
            "matricula":linha[2],
            "cpf":linha[3],
            "nascimento":linha[4],
            "id_endereco":linha[5],
            "id_curso":linha[6]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(aluno)

#setAluno
@app.route("/aluno", methods=['POST'])
@schema.validate(aluno_schema)
def setAluno():
    logger.info('Cadastrando o aluno')

    try:
        #Recuperando o JSON
        aluno = request.get_json()
        nome = aluno["nome"]
        matricula = aluno["matricula"]
        cpf = aluno["cpf"]
        nascimento = aluno["nascimento"]
        id_endereco = aluno["id_endereco"]
        id_curso = aluno["id_curso"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_aluno(nome, matricula, cpf, nascimento, id_endereco, id_curso)
            VALUES(?, ?, ?, ?, ?, ?);
        """, (nome, matricula, cpf, nascimento, id_endereco, id_curso))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        aluno['id_aluno'] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Aluno cadastrado com sucesso.")

    return jsonify(aluno)

#updateAluno
@app.route("/aluno/<int:id>", methods=['PUT'])
@schema.validate(aluno_schema)
def updateAluno(id):
    logger.info('Atualizando o aluno')

    try:
        aluno = request.get_json()
        nome = aluno["nome"]
        matricula = aluno["matricula"]
        cpf = aluno["cpf"]
        nascimento = aluno["nascimento"]
        id_endereco = aluno["id_endereco"]
        id_curso = aluno["id_curso"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_aluno
            WHERE id_aluno = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_aluno
                SET nome=?, matricula=?, cpf=?,nascimento=?, id_endereco=?, id_curso=?
                WHERE id_aluno = ?
                """, (nome, matricula, cpf, nascimento, id_endereco, id_curso, id))
            conn.commit()
        else:
            cursor.execute("""
                INSERT INTO tb_aluno(nome, matricula, cpf, nascimento, id_endereco, id_curso)
                VALUES(?, ?, ?, ?, ?, ?);
            """, (nome, matricula, cpf, nascimento, id_endereco, id_curso))

            conn.commit()
            conn.close()

            id = cursor.lastrowid
            aluno['id_aluno'] = id

        conn.close()

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Update realizado com sucesso.")

    return jsonify(aluno)

#getProfessores
@app.route("/professores", methods=['GET'])
def getProfessores():
    logger.info("Listando os professores")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_professor;
        """)

        professores = []
        for linha in cursor.fetchall():
            professor = {
                "id_professor":linha[0],
                "nome":linha[1],
                "id_endereco":linha[2]
            }
            professores.append(professor)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(professores)

#getProfessoresByID
@app.route("/professores/<int:id>", methods=['GET'])
def getProfessoresByID(id):
    logger.info("Listando o professor pelo id: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_professor
            WHERE id_professor = ?
        """, (id, ))

        linha = cursor.fetchone()
        professor = {
            "id_professor":linha[0],
            "nome":linha[1],
            "id_endereco":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(professor)

#setProfessor
@app.route("/professor", methods=['POST'])
@schema.validate(professor_schema)
def setProfessor():
    logger.info('Cadastrando o professor')

    try:
        professor = request.get_json()
        nome = professor["nome"]
        id_endereco = professor["id_endereco"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_professor(nome, id_endereco)
            VALUES(?, ?);
        """, (nome, id_endereco))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        professor["id_professor"] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Professor cadastrado com sucesso.")

    return jsonify(professor)

#updateProfessor
@app.route("/professor/<int:id>", methods=['PUT'])
@schema.validate(professor_schema)
def updateProfessor(id):
    logger.info('Atualizando o professor')

    try:
        professor = request.get_json()
        nome = professor["nome"]
        id_endereco = professor["id_endereco"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_professor
            WHERE id_professor = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_professor
                SET nome=?, id_endereco=?
                WHERE id_professor= ?
                """, (nome, fk_id_endereco, id))
            conn.commit()
        else:
            cursor.execute("""
                INSERT INTO tb_professor(nome, id_endereco)
                VALUES(?, ?);
            """, (nome, id_endereco))

            conn.commit()
            conn.close()

            id = cursor.lastrowid
            professor["id_professor"] = id

        conn.close()

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Update realizado com sucesso.")

    return jsonify(professor)

#getDisciplinas
@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    logger.info("Listando as disciplinas")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_disciplina;
        """)

        disciplinas = []
        for linha in cursor.fetchall():
            disciplina = {
                "id_disciplina":linha[0],
                "nome":linha[1],
                "id_professor":linha[2]
            }
            disciplinas.append(disciplina)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplinas)

#getDisciplinasByID
@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinasByID(id):
    logger.info("Listando a disciplina pelo id: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_disciplina
            WHERE id_disciplina = ?
        """, (id, ))

        linha = cursor.fetchone()
        disciplina = {
            "id_disciplina":linha[0],
            "nome":linha[1],
            "id_professor":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplina)

#setDisciplina
@app.route("/disciplina", methods=['POST'])
@schema.validate(disciplina_schema)
def setDisciplina():
    logger.info('Cadastrando a disciplina')

    try:
        disciplina = request.get_json()
        nome = disciplina["nome"]
        id_professor = disciplina["id_professor"]
        print(nome)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_disciplina(nome, id_professor)
            VALUES(?, ?);
        """, (nome, id_professor))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        disciplina["id_disciplina"] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Disciplina cadastrada com sucesso.")

    return jsonify(disciplina)

#updateDisciplina
@app.route("/disciplina/<int:id>", methods=['PUT'])
@schema.validate(disciplina_schema)
def updateDisciplina(id):
    logger.info("Atualizando a disciplina")

    try:
        disciplina = request.get_json()
        nome = disciplina['nome']
        fk_id_professor = disciplina['id_professor']

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_disciplina
            WHERE id_disciplina = ?;
            """, (id,))

        tab = cursor.fetchone()
        if (tab is not None):
            cursor.execute("""
                UPDATE tb_disciplina
                SET nome=?, fk_id_professor=?
                WHERE id_disciplina = ?
                """, (nome, fk_id_professor, id))
            conn.commit()
        else:
            cursor.execute("""
                INSERT INTO tb_disciplina(nome, id_professor)
                VALUES(?, ?);
            """, (nome, id_professor))

            conn.commit()
            conn.close()

            id = cursor.lastrowid
            disciplina["id_disciplina"] = id

        conn.close()

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Update realizado com sucesso.")

    return jsonify(disciplina)

#getCursos
@app.route("/cursos", methods=['GET'])
def getCursos():
    logger.info("Listando os cursos")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_curso;
        """)

        cursos = []
        for linha in cursor.fetchall():
            curso = {
                "id_curso":linha[0],
                "nome":linha[1],
                "id_turno":linha[2]
            }
            cursos.append(curso)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(cursos)

#getCursosByID
@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID(id):
    logger.info("Listando o curso pelo id: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_curso
            WHERE id_curso = ?;
        """, (id, ))

        linha = cursor.fecthone()
        curso = {
            "id_curso":linha[0],
            "nome":linha[1],
            "id_turno":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(curso)

#setCurso
@app.route("/curso", methods=['POST'])
@schema.validate(curso_schema)
def setCurso():
    logger.info('Cadastrando o curso')

    try:
        curso = request.get_json()
        nome = curso["nome"]
        id_turno = curso["id_turno"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_curso(nome, id_turno)
            VALUES(?, ?);
        """, (nome, id_turno))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        curso['id_curso'] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Curso cadastrado com sucesso.")

    return jsonify(curso)

#updateCurso
@app.route("/curso/<int:id>", methods=['PUT'])
@schema.validate(curso_schema)
def updateCurso(id):
    logger.info("Atualizando o curso")

    try:
        curso = request.get_json()
        nome = curso['nome']
        id_turno = curso['id_turno']

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
                SELECT *
                FROM tb_curso
                WHERE id_curso = ?;
        """, (id, ))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_curso
                SET nome=?, id_turno=?
                WHERE id_curso = ?
            """, (nome, id_turno, id))
            conn.commit()
        else:
            cursor.execute("""
                INSERT INTO tb_curso(nome, id_turno)
                VALUES(?, ?);
            """, (nome, id_turno))
            conn.commit()

            id = cursor.lastrowid
            curso['id_curso'] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Update realizado com sucesso.")

    return jsonify(curso)

#getCampus
@app.route("/campi", methods=['GET'])
def getCampus():
    logger.info("Listando os campi.")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_campus;
        """)

        campi = []
        for linha in cursor.fetchall():
            campus = {
                "id_campus":linha[0],
                "sigla":linha[1],
                "cidade":linha[2]
            }
            campi.append(campus)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(campi)

#getCampusByID
@app.route("/campus/<int:id>", methods=['GET'])
def getCampusByID(id):
    logger.info("Listando o campus pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_campus
            WHERE id_campus = ?
        """, (id, ))

        linha = cursor.fetchone()
        campus = {
            "id_campus":linha[0],
            "sigla":linha[1],
            "cidade":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(campus)

#setCampus
@app.route("/campus", methods=['POST'])
@schema.validate(campus_schema)
def setCampus():
    logger.info('Cadastrando o campus')

    try:
        campus = request.get_json()
        sigla = campus["sigla"]
        cidade = campus["cidade"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_campus(sigla, cidade)
            VALUES(?, ?);
        """, (sigla, cidade))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        campus['id_campus'] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Campus cadastrado com sucesso.")

    return jsonify(campus)

#updateCampus
@app.route("/campus/<int:id>", methods=['PUT'])
@schema.validate(campus_schema)
def updateCampus(id):
    logger.info("Atualizando o campus")

    try:
        campus = request.get_json()
        sigla = campus["sigla"]
        cidade = campus["cidade"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_campus
            WHERE id_campus = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_campus
                SET sigla=?, cidade=?
                WHERE id_campus = ?
                """, (sigla, cidade, id))
            conn.commit()
        else:
            cursor.execute("""
                INSERT INTO tb_campus(sigla, cidade)
                VALUES(?, ?);
            """, (sigla, cidade))

            conn.commit()
            conn.close()

            id = cursor.lastrowid
            campus['id_campus'] = id


        conn.close()

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Update realizado com sucesso.")

    return jsonify(campus)

#getTurmas
@app.route("/turmas", methods=['GET'])
def getTurmas():
    logger.info("Listando as turmas")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_turma;
        """)

        turmas = []
        for linha in cursor.fetchall():
            turma = {
                "id_turma":linha[0],
                "nome":linha[1],
                "id_curso":linha[2]
            }
            turmas.append(turma)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turmas)

#getTurmasByID
@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID(id):
    logger.info("Listando a turma pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_turma
            WHERE id_turma = ?
        """, (id, ))

        linha = cursor.fetchone()
        turma = {
            "id_turma":linha[0],
            "nome":linha[1],
            "id_curso":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turma)

#setTurma
@app.route("/turma", methods=['POST'])
@schema.validate(turma_schema)
def setTurma():
    logger.info('Cadastrando a turma')

    try:
        turma = request.get_json()
        nome = turma["nome"]
        id_curso = turma["id_curso"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_turma(nome, id_curso)
            VALUES(?, ?);
        """, (nome, id_curso))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        turma["id_turma"] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Turma cadastrada com sucesso.")

    return jsonify(turma)

#updateTurma
@app.route("/turma/<int:id>", methods=['PUT'])
@schema.validate(turma_schema)
def updateTurma(id):
    logger.info("Atualizando a turma")

    try:
        turma = request.get_json()
        nome = turma['nome']
        id_curso = turma['id_curso']

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_turma
            WHERE id_turma = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_turma
                SET nome=?, id_curso=?
                WHERE id_disciplina = ?
                """, (nome,fk_id_curso, id))
            conn.commit()
        else:
            cursor.execute("""
                INSERT INTO tb_turma(nome, id_curso)
                VALUES(?, ?);
            """, (nome, fk_id_curso))

            conn.commit()
            conn.close()

            id = cursor.lastrowid
            turma["id_turma"] = id

        conn.close()

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Update realizado com sucesso.")

    return jsonify(turma)

#getTurnos
@app.route("/turnos", methods=['GET'])
def getTurnos():
    logger.info("Listando turnos")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_turno;
        """)

        turnos = []
        for linha in cursor.fetchall():
            turno = {
                "id_turno":linha[0],
                "nome":linha[1]
            }
            turnos.append(turno)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turnos)

#getTurnosByID
@app.route("/turnos/<int:id>", methods=['GET'])
def getTurnosByID(id):
    logger.info("Listando turno pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_turno
            WHERE id_turno = ?;
        """, (id, ))

        linha = cursor.fetchone()
        turno = {
            "id_turno":linha[0],
            "nome":linha[1]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turno)

#setTurno
@app.route("/turno", methods=['POST'])
@schema.validate(turno_schema)
def setTurno():
    logger.info('Cadastrando o turno')

    try:
        turno = request.get_json()
        nome = turno["nome"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_turno(nome)
            VALUES(?);
        """, (nome, ))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        turno['id_turno'] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Turno cadastrado com sucesso.")

    return jsonify(turno)

#updateTurno
@app.route("/turno/<int:id>", methods=['PUT'])
@schema.validate(turno_schema)
def updateTurno(id):
    logger.info('Atualizando o turno')

    try:
        turno = request.get_json()
        nome = turno["nome"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_turno
            WHERE id_turno = ?;
            """, (id, ))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_turno
                SET nome=?
                where id_turno = ?
                """, (nome, id))
            conn.commit()
        else:
            cursor.execute("""
                INSERT INTO tb_turno(nome)
                VALUES(?);
            """, (nome, ))

            conn.commit()
            conn.close()

            id = cursor.lastrowid
            turno['id_turno'] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)

    finally:
        if conn:
            conn.close()

    logger.info("Update realizado com sucesso.")

    return jsonify(turno)

def dict_factory(linha, cursor):
    dicionario = {}
    for idx, col in enumerate(cursor.description):
        dicionario[col[0]] = linha[idx]
    return dicionario

# Mensagem de erro para recurso não encontrado.
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]})

'''
    Instaciar o objeto CORS passando como parâmetros a app e as urls permitidas.
'''
cors = CORS(app, resources={r"/*": {"origins": "*"}})

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5001, debug=True, use_reloader=True)
