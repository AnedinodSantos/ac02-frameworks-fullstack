import os
from flask import Flask, redirect, render_template, request
from flaskext.mysql import MySQL


mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dino1234'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_aluno')
def cadastro_de_aluno():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST',])
def cadastrar_aluno():
    nome = request.form['nome']
    email = request.form['email']
    endereco = request.form['endereco']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into aluno (nome, email, endereco) VALUES (%s, %s, %s)', ( nome,email,endereco))
    conn.commit()

    return redirect('lista.html')

@app.route('/lista')
def lista_alunos():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute ('SELECT nome, email, endereco FROM aluno')
    data = cursor.fetchall()
    conn.commit()
    return render_template('lista.html', data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(debug=True)
