# Servidor Backend - API em Python, Flask e SQLite

Este projeto contém uma **API REST** desenvolvida com **Python** e **Flask** para gerenciar Cadastro de usuários através do **SQLite**. A API permite realizar operações básicas como **cadastrar, consultar, editar e excluir usuários**.

---

## 📌 1. Requisitos
Antes de iniciar a instalação, certifique-se de que seu ambiente atenda aos seguintes requisitos:

✔ **Python 3.8 ou superior** instalado  
✔ **Pip** (gerenciador de pacotes do Python) instalado  
✔ **Git** instalado (opcional, mas recomendado)  

Para verificar a instalação do Python e Pip, execute no terminal:

```bash
python --version
pip --version
```

Caso precise instalar o Python, faça o download em: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## 📌 2. Clonando o Repositório
Se você deseja baixar o projeto diretamente do GitHub, use o comando abaixo:

```bash
git clone https://github.com/Frezende76/mvp_backEnd.git
```

Caso contrário, você pode baixar o código compactado (.zip) e extraí-lo manualmente.

Entre no diretório do projeto:

```bash
cd mvp_backEnd
```

---

## 📌 3. Criando o Ambiente Virtual

```bash
python -m venv venv
```

### ✅ Ativando o Ambiente Virtual
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

---

## 📌 4. Instalando as Dependências

```bash
pip install -r requirements.txt
```

Caso precise atualizar o `requirements.txt` após instalar novos pacotes:

```bash
pip freeze > requirements.txt
```

---

## 📌 5. Iniciando o Servidor

```bash
flask run
```

O servidor estará rodando em:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📌 6. Endpoints da API

| Método | Endpoint            | Descrição                      |
|--------|---------------------|--------------------------------|
| POST   | `/usuarios/`        | Cadastrar um novo usuário      |
| GET    | `/usuarios/`        | Listar todos os usuários       |
| GET    | `/usuarios/<id>`    | Consultar um usuário por ID    |
| PUT    | `/usuarios/<id>`    | Editar um usuário              |
| DELETE | `/usuarios/<id>`    | Excluir um usuário             |

---

## 📌 7. Testando a API

### ✅ Testando com Postman

1. Abra o **Postman**  
2. Escolha o método HTTP (POST, GET, PUT ou DELETE)  
3. Insira o endpoint da API  
4. No caso de POST e PUT, vá até a aba "Body" → "raw" → "JSON"  
5. Insira os dados e clique em "Send"  

### ✅ Testando no Navegador
Para testar a listagem, basta acessar no navegador:

```bash
http://127.0.0.1:5000/usuarios/
```

---

## 📌 8. Documentação Swagger

A API possui documentação interativa com **Swagger**, acessível em:

[http://127.0.0.1:5000/swagger.json](http://127.0.0.1:5000/swagger.json)

Se você adicionou **Flask-Swagger-UI**, acesse:

[http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)

---

## 📌 9. Estrutura do Projeto

```
📂 mvp_backEnd
│  │── 📂 databases
│  │   │── dados_cliente.db
│  │── 📂 models
│  │   │── usuario.py
│  │── 📂 routes
│  │   │── usuario_rotas.py
│  │── 📂 schemas
│  │   │── usuario_schema.py
│  │── app.py
│  │── README.md
│  │── requirements.txt

```

---

## 📌 10. Erros Comuns e Soluções

1️⃣ **Erro: `ModuleNotFoundError: No module named 'flask'`**  
➡ Solução: Instale o Flask com `pip install flask`  

2️⃣ **Erro: `sqlite3.OperationalError: unable to open database file`**  
➡ Solução: Certifique-se de que a pasta `banco_de_dados/` existe e tem permissão de escrita  

3️⃣ **Erro: `Address already in use`**  
➡ Solução: Encerre processos Flask em execução com `CTRL + C` e reinicie  

---

## 📌 11. Licença

Este projeto está sob a licença **MIT**. Sinta-se livre para usá-lo e modificá-lo conforme necessário.