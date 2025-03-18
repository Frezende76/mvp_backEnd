from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configuração da aplicação Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dados_cliente.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Rodando a aplicação
if __name__ == "__main__":
    db.create_all() # Cria as tabelas no banco de dados
    app.run(debug=True)


