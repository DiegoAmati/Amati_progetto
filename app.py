import json
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Funzione per validare la password
def valida_password(password):
    with open('password_rules.json', 'r') as file:
        rules = json.load(file)
    import re
    pattern = rules['pattern']
    return re.match(pattern, password)

# Route per la pagina iniziale
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# Route per il login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        codice_operatore = request.form['codice_operatore']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM User WHERE codice_operatore = ? AND password = ?", (codice_operatore, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('blood_sample'))
        else:
            flash('Credenziali non valide. Riprova.')
    return render_template('login.html')

# Route per la registrazione
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        cognome = request.form['cognome']
        email = request.form['email']
        codice_operatore = request.form['codice_operatore']
        password = request.form['password']
        if not valida_password(password):
            flash('La password non rispetta i requisiti di sicurezza.')
            return redirect(url_for('register'))
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO User (nome, cognome, email, codice_operatore, password) VALUES (?, ?, ?, ?, ?)",
                       (nome, cognome, email, codice_operatore, password))
        conn.commit()
        conn.close()
        flash('Registrazione completata con successo!')
        return redirect(url_for('login'))
    return render_template('registration.html')

# Route per il modulo di campione di sangue
@app.route('/blood_sample', methods=['GET', 'POST'])
def blood_sample():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        luogo = request.form['luogo']
        data_ora = request.form['data_ora']
        denominazione_analisi = request.form['denominazione_analisi']
        valore1 = request.form['valore1']
        valore2 = request.form['valore2']
        codice_fiscale = request.form['codice_fiscale']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Prelievo (codice_fiscale, luogo, data_ora, denominazione_analisi, valore1, valore2) VALUES (?, ?, ?, ?, ?, ?)",
                       (codice_fiscale, luogo, data_ora, denominazione_analisi, valore1, valore2))
        conn.commit()
        conn.close()
        flash('Dati del prelievo salvati con successo!')
        return redirect(url_for('blood_sample'))
    return render_template('blood_sample.html')

# Route per visualizzare i prelievi
@app.route('/view_samples', methods=['GET', 'POST'])
def view_samples():
    samples = None
    if request.method == 'POST':
        codice_fiscale = request.form['codice_fiscale']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT luogo, data_ora, denominazione_analisi, valore1, valore2 FROM Prelievo WHERE codice_fiscale = ?", (codice_fiscale,))
        samples = cursor.fetchall()
        conn.close()
    return render_template('view_samples.html', samples=samples)

# Route per il logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codice_operatore TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Prelievo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codice_fiscale TEXT NOT NULL,
        luogo TEXT NOT NULL,
        data_ora TEXT NOT NULL,
        denominazione_analisi TEXT NOT NULL,
        valore1 TEXT NOT NULL,
        valore2 TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    app.run(debug=True)