import sqlite3
import os

# Caminho absoluto para o banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Diretório do arquivo atual
DB_DIR = os.path.join(BASE_DIR, '..', 'databases')  # Caminho da pasta databases
DB_PATH = os.path.join(DB_DIR, 'dados_cliente.db')  # Caminho do arquivo do banco de dados

# Garantir que a pasta databases exista
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

def criar_tabela():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

def cadastrar_usuario(nome, endereco, email, telefone):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, endereco, email, telefone) '
    'VALUES (?, ?, ?, ?)', (nome, endereco, email, telefone))
    conn.commit()

    # Pegando o id do último usuário inserido
    id = cursor.lastrowid  # Agora o id está corretamente definido

    # Buscando o usuário recém-inserido
    cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
    usuario = cursor.fetchone()
    conn.close()

    # Se o usuário foi encontrado, retornamos seus dados na ordem correta
    if usuario:
        usuario_dict = {
            'id': usuario[0],
            'nome': usuario[1],
            'endereco': usuario[2],
            'email': usuario[3],
            'telefone': usuario[4]
        }
        return usuario_dict
    return None  # Caso o usuário não seja encontrado

def editar_usuario(nome, endereco, email, telefone, id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Atualizando os dados do usuário
    cursor.execute('UPDATE usuarios SET nome = ?, endereco = ?, email = ?, telefone = ? WHERE id = ?', 
                   (nome, endereco, email, telefone, id))
    conn.commit()

    # Buscando o usuário atualizado após a atualização no banco
    cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
    usuario_atualizado = cursor.fetchone()

    conn.close()

    # Se o usuário foi encontrado, retorna como um dicionário
    if usuario_atualizado:
        return {
            'id': usuario_atualizado[0],
            'nome': usuario_atualizado[1],
            'endereco': usuario_atualizado[2],
            'email': usuario_atualizado[3],
            'telefone': usuario_atualizado[4]
        }
    
    return None  # Caso o usuário não seja encontrado

def buscar_usuario(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
    usuario = cursor.fetchone()
    conn.close()
    # Se o usuário não for encontrado, retorna None
    if usuario:
        # Convertendo a tupla para um dicionário
        usuario_dict = {
            'id': usuario[0],  # Supondo que 'id' seja a primeira coluna
            'nome': usuario[1],  # 'nome' sendo a segunda coluna, ajuste conforme seu banco
            'endereco': usuario[2],  # 'endereco'
            'email': usuario[3],  # 'email'
            'telefone': usuario[4],  # 'telefone'
        }
        print(usuario_dict)
        return usuario_dict
    
    return None  # Retorna None se o usuário não for encontrado

def deletar_usuario(id,):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conn.commit()
    conn.close()