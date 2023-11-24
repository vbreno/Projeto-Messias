import os
import csv
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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



@app.route('/excluir_termo/<int:termo_id>', methods=['POST'])
def excluir_termo(termo_id):
    with open('bd_python.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        linhas = list(reader)

    if 0 <= termo_id < len(linhas):
        del linhas[termo_id]

        with open('bd_python.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(linhas)

    return redirect(url_for('python'))


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


if __name__ == "__main__":
    app.run(debug=True)
