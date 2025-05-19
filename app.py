from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'segredo'  # Para controle de sessão

# Fake database usando um dicionário (matricula: pontos)
fake_db = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        matricula = request.form['matricula']

        # Verifica se a matrícula já está no "fake_db"
        if matricula in fake_db:
            print(f"Matrícula {matricula} já existe com {fake_db[matricula]} pontos.")
        else:
            # Se não existe, insere a matrícula com 0 pontos
            fake_db[matricula] = 0
            print(f"Matrícula {matricula} inserida com 0 pontos.")

        # Exibe o conteúdo do "fake_db" para checar se os dados foram adicionados
        print("Banco de dados atual:", fake_db)

        # Armazena a matrícula na sessão
        session['matricula'] = matricula

        # Redireciona para o dashboard com a matrícula
        return redirect(url_for('dashboard'))

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    matricula = session.get('matricula')
    if not matricula:
        return redirect(url_for('login'))

    # Pega os pontos do "fake_db" baseado na matrícula
    pontos = fake_db.get(matricula, 0)

    # Gerar o QR Code (pode ser um código simples, ex: URL com a matrícula)
    qr_code_data = url_for('validar_qrcode', matricula=matricula, _external=True)

    return render_template('dashboard.html', matricula=matricula, pontos=pontos, qr_code_data=qr_code_data)

@app.route('/validar_qrcode')
def validar_qrcode():
    matricula = request.args.get('matricula')

    if matricula and matricula in fake_db:
        # Se a matrícula for válida, adiciona 10 pontos
        fake_db[matricula] += 10
        return redirect(url_for('dashboard'))  # Redireciona de volta para o dashboard

    # Se a matrícula não for válida, redireciona para a tela de login
    return redirect(url_for('login'))

@app.route('/ranking')
def ranking():
    # Ordena os alunos pelo número de pontos (decrescente)
    sorted_students = sorted(fake_db.items(), key=lambda x: x[1], reverse=True)
    
    # Gerar a lista de alunos com suas pontuações
    ranking_list = [{'matricula': matricula, 'pontos': pontos} for matricula, pontos in sorted_students]

    # Imprimir o ranking no console para checar os dados
    print("Ranking atualizado:", ranking_list)

    return render_template('ranking.html', ranking_list=ranking_list)


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa a porta fornecida pelo Render
    app.run(host='0.0.0.0', port=port)

@app.route('/funcionamento')
def funcionamento():
    return render_template('funcionamento.html')
