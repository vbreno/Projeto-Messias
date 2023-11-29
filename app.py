import os
import csv
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('modelo.html')



@app.route('/contato')
def contato():
    return render_template('contato.html')



@app.route('/python', methods=['GET', 'POST'])
def python():
    python_termos = []

    if request.method == 'POST':
        novo_termo = request.form['termo']
        definicao = request.form['definicao']

        with open('bd_python.csv', 'a', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerow([novo_termo, definicao])

    with open('bd_python.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        python_termos = list(reader)

    return render_template('python.html', python=python_termos)



@app.route('/html', methods=['GET', 'POST'])
def html():
    html_termos = []

    if request.method == 'POST':
        novo_termo = request.form['termo']
        definicao = request.form['definicao']

        with open('bd_html.csv', 'a', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerow([novo_termo, definicao])

    with open('bd_html.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        html_termos = list(reader)

    return render_template('html.html', html=html_termos)




@app.route('/task', methods=['GET', 'POST'])
def task():
    tasks = []

    if request.method == 'POST':
        novo_termo = request.form['termo']
        definicao = request.form['definicao']

        with open('bd_task.csv', 'a', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerow([novo_termo, definicao])

    with open('bd_task.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        tasks = list(reader)

    return render_template('task.html', task=tasks)



@app.route('/excluir_python/<int:termo_id>', methods=['POST'])
def excluir_python(termo_id):
    # Excluindo termo do arquivo Python
    with open('bd_python.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        linhas = list(reader)

    if 0 <= termo_id < len(linhas):
        del linhas[termo_id]

        with open('bd_python.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(linhas)
    
    referer = request.headers.get("Referer")

    return redirect(referer or url_for('home'))



@app.route('/excluir_html/<int:termo_id>', methods=['POST'])
def excluir_html(termo_id):
    # Excluindo termo do arquivo HTML
    with open('bd_html.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        linhas = list(reader)

    if 0 <= termo_id < len(linhas):
        del linhas[termo_id]

        with open('bd_html.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(linhas)

    referer = request.headers.get("Referer")

    return redirect(referer or url_for('home'))



@app.route('/excluir_task/<int:termo_id>', methods=['POST'])
def excluir_task(termo_id):
    # Excluindo termo do arquivo Task
    with open('bd_task.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        linhas = list(reader)

    if 0 <= termo_id < len(linhas):
        del linhas[termo_id]

        with open('bd_task.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(linhas)

    referer = request.headers.get("Referer")

    return redirect(referer or url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)