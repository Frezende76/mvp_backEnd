from flask import Blueprint, request, jsonify, Response
from models.usuario import cadastrar_usuario, editar_usuario, buscar_usuario, deletar_usuario, buscar_todos_usuarios
from schemas.usuario_schema import UsuarioSchema
import json

# Função auxiliar para gerar respostas JSON
def gerar_resposta_json(data, status_code=200):
    return Response(json.dumps(data, ensure_ascii=False), mimetype='application/json', status=status_code)

# Criação de um Blueprint para as rotas de usuário
usuario_rotas = Blueprint('usuarios', __name__)

# Rota para cadastrar um usuário (Método POST)
@usuario_rotas.route('/usuarios/cadastrar', methods=['POST'])
def cadastrar_usuario_bd():
    dados = request.json  # Alterado para JSON
    nome = dados.get('nome')
    endereco = dados.get('endereco')
    email = dados.get('email')
    telefone = dados.get('telefone')
    
    # Verificação para garantir que todos os campos foram preenchidos
    if not all([nome, endereco, email, telefone]):
        return jsonify({'message': 'Todos os campos são obrigatórios!'}), 400
    
    # Tentativa de cadastrar o usuário
    novo_usuario = cadastrar_usuario(nome, endereco, email, telefone)
    if novo_usuario is None:
        return jsonify({'message': 'Usuário já cadastrado!'}), 400
    
    return jsonify({'message': 'Usuário cadastrado com sucesso!'}), 201

# Rota para editar um usuário existente (Método PUT)
@usuario_rotas.route('/usuarios/editar/<int:id>', methods=['PUT'])
def editar_usuario_bd(id):
    dados = request.get_json(silent=True)
    
    if isinstance(dados, list):  # Se for uma lista, pega o primeiro elemento
        dados = dados[0]
    
    if not isinstance(dados, dict):  # Garante que seja um dicionário
        return jsonify({'message': 'Dados inválidos!'}), 400
    
    nome = dados.get('nome')
    endereco = dados.get('endereco')
    email = dados.get('email')
    telefone = dados.get('telefone')
    
    # Verificação para garantir que todos os campos foram preenchidos
    if not all([nome, endereco, email, telefone]):
        return jsonify({'message': 'Todos os campos são obrigatórios!'}), 400
    
    usuario = editar_usuario(id, nome, endereco, email, telefone)
    if usuario:
        usuario_schema = UsuarioSchema()
        usuario_dict = usuario_schema.dump(usuario)
        return gerar_resposta_json(usuario_dict), 200
    
    return gerar_resposta_json({'message': 'Nenhum usuário encontrado'}, 404)

# Rota para buscar um usuário pelo ID (Método GET)
@usuario_rotas.route('/usuarios/buscar/<int:id>', methods=['GET'])
def buscar_usuario_bd(id):
    usuario = buscar_usuario(id)
    if usuario:
        usuario_schema = UsuarioSchema()
        usuario_dict = usuario_schema.dump(usuario)
        return gerar_resposta_json(usuario_dict), 200
    
    return gerar_resposta_json({'message': 'Nenhum usuário encontrado'}, 404)

# Rota para deletar um usuário (Método DELETE)
@usuario_rotas.route('/usuarios/deletar/<int:id>', methods=['DELETE'])
def deletar_usuario_bd(id):
    usuario = buscar_usuario(id)

    if usuario:
        deletar_usuario(id)
        return jsonify({'message': 'Usuário deletado com sucesso'}), 200
    
    return jsonify({'message': 'Usuário não encontrado'}), 404

# Rota para buscar todos os usuários (Método GET)
@usuario_rotas.route('/usuarios/todos', methods=['GET'])
def buscar_todos_usuarios_bd():
    nome = request.args.get('nome', '')
    endereco = request.args.get('endereco', '')
    email = request.args.get('email', '')
    telefone = request.args.get('telefone', '')

    # Lógica de busca com filtros
    usuarios = buscar_todos_usuarios(nome, endereco, email, telefone)
    if usuarios:
        usuario_schema = UsuarioSchema(many=True)  # many=True para lidar com múltiplos usuários
        usuarios_dict = usuario_schema.dump(usuarios)
        return gerar_resposta_json(usuarios_dict), 200
    
    return gerar_resposta_json({'message': 'Nenhum usuário encontrado'}, 404)

# Nova rota para verificar se um usuário existe (Método POST)
@usuario_rotas.route('/usuarios/verificar', methods=['POST'])
def verificar_usuario_bd():
    dados = request.json
    nome = dados.get('nome', '')
    endereco = dados.get('endereco', '')
    email = dados.get('email', '')
    telefone = dados.get('telefone', '')
 
    # Verificar se o usuário já existe no banco de dados com os mesmos dados
    usuarios = buscar_todos_usuarios(nome, endereco, email, telefone)
    
      # Log para mostrar os usuários encontrados
    if usuarios:
        return gerar_resposta_json({'usuarioExistente': True, 'message': 'Usuário já cadastrado'}), 400
    
    return gerar_resposta_json({'usuarioExistente': False, 'message': 'Nenhum usuário encontrado'}, 200)