from flask import Flask
from flask_cors import CORS
from routes.usuario_rotas import usuario_rotas
from models.usuario import criar_tabela

app = Flask(__name__)

# Habilitar CORS para todas as rotas e métodos (incluindo OPTIONS) com as configurações específicas para /usuarios/*
CORS(app, resources={r"/usuarios/*": {
    "origins": "*",        # Permite qualquer origem (alterar conforme necessário para maior segurança)
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Permite os métodos necessários
    "allow_headers": ["Content-Type", "Accept"]  # Permite os cabeçalhos necessários
}})

# Criar a tabela de usuários no banco de dados, caso ainda não exista
criar_tabela()

# Registrar as rotas do blueprint
app.register_blueprint(usuario_rotas)

if __name__ == '__main__':
    app.run(debug=True)

