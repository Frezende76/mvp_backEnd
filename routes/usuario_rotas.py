from flask import Blueprint, request, jsonify
from models.usuario import cadastrar_usuario, editar_usuario, buscar_usuario, deletar_usuario, buscar_todos_usuarios
from schemas.usuario_schema import UsuarioSchema

# Criação de um Blueprint para as rotas de usuário
usuario_rotas = Blueprint('usuarios', __name__)

# Rota para cadastrar um usuário (Método POST)
@usuario_rotas.route('/usuarios', methods=['POST'])
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
@usuario_rotas.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario_bd(id):
    dados = request.json  # Alterado para JSON
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
        return jsonify(usuario_dict)
    
    return jsonify({'message': 'Usuário não encontrado'}), 404

# Rota para buscar um usuário pelo ID (Método GET)
@usuario_rotas.route('/usuarios/<int:id>', methods=['GET'])
def buscar_usuario_bd(id):
    usuario = buscar_usuario(id)
    if usuario:
        usuario_schema = UsuarioSchema()
        usuario_dict = usuario_schema.dump(usuario)
        return jsonify(usuario_dict)
    
    return jsonify({'message': 'Usuário não encontrado'}), 404

# Rota para deletar um usuário (Método DELETE)
@usuario_rotas.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario_bd(id):
    usuario = buscar_usuario(id)

    if usuario:
        deletar_usuario(id)
        return jsonify({'message': 'Usuário deletado com sucesso'}), 200
    
    return jsonify({'message': 'Usuário não encontrado'}), 404

# Rota para buscar todos os usuários (Método GET)
@usuario_rotas.route('/usuarios', methods=['GET'])
def buscar_todos_usuarios_bd():
    usuarios = buscar_todos_usuarios()
    if usuarios:
        usuario_schema = UsuarioSchema(many=True)  # many=True para lidar com múltiplos usuários
        usuarios_dict = usuario_schema.dump(usuarios)
        return jsonify(usuarios_dict)
    
    return jsonify({'message': 'Nenhum usuário encontrado'}), 404