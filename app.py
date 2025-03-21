from flask import Flask
from flask_cors import CORS
from routes.usuario_rotas import usuario_rotas
from models.usuario import criar_tabela

app = Flask(__name__)

# Habilitar CORS para todas as rotas
CORS(app)

# Criar a tabela de usuários no banco
criar_tabela()

# Registrar as rotas
app.register_blueprint(usuario_rotas)

if __name__ == '__main__':
    app.run(debug=True)

