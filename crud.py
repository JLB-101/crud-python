from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configuração do MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nova_senha",
    database="empresa"
)

# Rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Rota para a página com a lista de funcionários
@app.route("/index-datas")
def index_datas():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    cursor.close()
    return render_template("index-datas.html", funcionarios=funcionarios)

# Rota para adicionar funcionário
@app.route("/adicionar", methods=["POST"])
def adicionar_funcionario():
    nome = request.form["nome"]
    localizacao = request.form["localizacao"]
    cargo = request.form["cargo"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    
    cursor = conn.cursor()
    query = "INSERT INTO funcionarios (nome, localizacao, cargo, email, telefone) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome, localizacao, cargo, email, telefone))
    conn.commit()
    cursor.close()

    return redirect("/")

# Rota para atualizar funcionário
@app.route("/atualizar", methods=["POST"])
def atualizar_funcionario():
    id = request.form["id"]
    nome = request.form["nome"]
    localizacao = request.form["localizacao"]
    cargo = request.form["cargo"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    
    cursor = conn.cursor()
    query = "UPDATE funcionarios SET nome=%s, localizacao=%s, cargo=%s, email=%s, telefone=%s WHERE id=%s"
    cursor.execute(query, (nome, localizacao, cargo, email, telefone, id))
    conn.commit()
    cursor.close()

    return redirect("/index-datas")

# Rota para excluir funcionário
@app.route("/excluir/<int:id>")
def excluir_funcionario(id):
    cursor = conn.cursor()
    query = "DELETE FROM funcionarios WHERE id=%s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    
    return redirect("/index-datas")

if __name__ == "__main__":
    app.run(debug=True)
