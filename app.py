from flask import Flask
from routes.usuario_rotas import usuario_rotas
from models.usuario import criar_tabela

app = Flask(__name__)

# Criar a tabela de usuários no banco
criar_tabela()

# Registrar as rotas
app.register_blueprint(usuario_rotas)

if __name__ == '__main__':
    app.run(debug=True)

