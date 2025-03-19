import json
from flask import Blueprint, request, jsonify
from models.usuario import cadastrar_usuario, editar_usuario, buscar_usuario, deletar_usuario
from schemas.usuario_schema import UsuarioSchema

# Criação de um Blueprint para as rotas de usuário
usuario_rotas = Blueprint('usuarios', __name__)

# Rota para cadastrar um usuário (Método POST)
@usuario_rotas.route('/usuarios', methods=['POST'])

def cadastrar_usuario_handle():
    # Obtendo os dados do corpo da requisição
    dados = request.get_json()
    nome = dados['nome']
    endereco = dados['endereco']
    email = dados['email']
    telefone = dados['telefone']

    # Chamando a função para cadastrar o usuário
    cadastrar_usuario(nome, endereco, email, telefone)
    
    # Retornando uma resposta de sucesso
    return jsonify({'message': 'Usuário cadastrado com sucesso!'}), 201


# Rota para editar um usuário existente (Método PUT)
@usuario_rotas.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario_handle(id):
    # Recebendo os dados do corpo da requisição (supondo que use JSON)
    nome = request.json.get('nome')
    endereco = request.json.get('endereco')
    email = request.json.get('email')
    telefone = request.json.get('telefone')

    # Chamando a função para editar o usuário e buscar os dados atualizados
    usuario = editar_usuario(nome, endereco, email, telefone, id)
    
    # Verificando se o usuário foi editado corretamente
    if usuario:
        usuario_schema = UsuarioSchema()
        usuario_dict = usuario_schema.dump(usuario)

        # Teste com json.dumps para verificar a ordem
        json_data = json.dumps(usuario_dict)
        return jsonify(json_data)  # Aqui retorna a resposta com json.dumps diretamente

    return jsonify({'message': 'Usuário não encontrado'}), 404

# Rota para buscar um usuário pelo ID (Método GET)
@usuario_rotas.route('/usuarios/<int:id>', methods=['GET'])
def buscar_usuario_handle(id):
    # Chamando a função para buscar o usuário pelo ID
    usuario = buscar_usuario(id)
    
    # Verificando se o usuário foi encontrado
    if usuario:
        usuario_schema = UsuarioSchema()
        usuario_dict = usuario_schema.dump(usuario)

        # Teste com json.dumps para verificar a ordem
        json_data = json.dumps(usuario_dict)
        return jsonify(json_data)  # Aqui retorna a resposta com json.dumps diretamente

    return jsonify({'message': 'Usuário não encontrado'}), 404

# Rota para deletar um usuário (Método DELETE)
@usuario_rotas.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario_handle(id):
    # Chamando a função para deletar o usuário
    deletar_usuario(id)
    
    # Retornando uma resposta de sucesso
    return jsonify({'message': 'Usuário deletado com sucesso'}), 200