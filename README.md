# Progetto Amati - Sistema di Gestione Prelievi

### Descrizione

Questo progetto è un sistema di gestione dei prelievi medici che consente agli utenti di registrarsi, effettuare il login e inserire o visualizzare i dati relativi ai prelievi. Il sistema è progettato per essere utilizzato in un contesto ospedaliero, con funzionalità per operatori e utenti.

---

### Funzionalità Principali

1. **Registrazione e Login**:
   - Gli utenti possono registrarsi fornendo nome, cognome, email, codice operatore e password.
   - Gli utenti registrati possono effettuare il login per accedere alle funzionalità del sistema.

2. **Gestione Prelievi**:
   - Gli utenti possono inserire i dati relativi ai prelievi, inclusi luogo, data e ora, denominazione analisi, valori (RBC, WBC, Hct, Hgb) e codice fiscale.
   - È possibile cercare i prelievi in base a diversi parametri, come nome, codice fiscale, data, luogo o codice operatore.

3. **Visualizzazione Prelievi**:
   - Gli utenti possono visualizzare i prelievi associati al proprio codice fiscale.

4. **Interfaccia Utente**:
   - Pagine con design responsivo per login, registrazione, inserimento e ricerca dei prelievi.
   - Sfondo personalizzato con immagini ospedaliere per migliorare l'esperienza utente.

---

### Porzioni di Codice

#### Registrazione Utente

```python
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
```

#### Inserimento Prelievo

```python
@app.route('/blood_sample', methods=['GET', 'POST'])
def blood_sample():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        luogo = request.form['luogo']
        data_ora = request.form['data_ora']
        denominazione_analisi = request.form['denominazione_analisi']
        rbc = request.form['rbc']
        wbc = request.form['wbc']
        hct = request.form['hct']
        hgb = request.form['hgb']
        codice_fiscale = request.form['codice_fiscale']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Prelievo (codice_fiscale, luogo, data_ora, denominazione_analisi, rbc, wbc, hct, hgb)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (codice_fiscale, luogo, data_ora, denominazione_analisi, rbc, wbc, hct, hgb))
        conn.commit()
        conn.close()
        flash('Dati del prelievo salvati con successo!')
        return redirect(url_for('blood_sample'))
    return render_template('blood_sample.html')
```

#### Ricerca Prelievi

```python
@app.route('/search_samples', methods=['GET', 'POST'])
def search_samples():
    results = None
    error_message = None
    if request.method == 'POST':
        campo = request.form.get('campo')
        valore = request.form.get('valore')

        if campo == "nome":
            query = """
                SELECT u.nome, u.cognome, p.luogo, p.data_ora, p.denominazione_analisi, p.rbc, p.wbc, p.hct, p.hgb, u.codice_operatore
                FROM Prelievo p
                JOIN User u ON u.codice_operatore = p.codice_fiscale
                WHERE u.nome LIKE ?
            """
        else:
            query = f"""
                SELECT u.nome, u.cognome, p.luogo, p.data_ora, p.denominazione_analisi, p.rbc, p.wbc, p.hct, p.hgb, u.codice_operatore
                FROM Prelievo p
                JOIN User u ON u.codice_operatore = p.codice_fiscale
                WHERE {campo} LIKE ?
            """
        params = [f"%{valore}%"]

        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            conn.close()

            if not results:
                error_message = "Nessun prelievo trovato per i criteri di ricerca forniti."
        except sqlite3.Error as e:
            error_message = f"Errore nel database: {e}"

    return render_template('search_samples.html', results=results, error_message=error_message)
```

---

### Installazione e Avvio

1. **Clona il Repository**:
   ```bash
   git clone <repository-url>
   cd amati_progetto
   ```

2. **Crea un Ambiente Virtuale**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows usa: venv\Scripts\activate
   ```

3. **Installa le Dipendenze**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Popola il Database**:
   ```bash
   python popola_database.py
   ```

5. **Avvia il Server**:
   ```bash
   python app.py
   ```

6. **Accedi all'Applicazione**:
   - Apri il browser e vai su `http://127.0.0.1:5000`.

---

### Prossimi Sviluppi

- Aggiungere funzionalità di autenticazione avanzata (es. reset password).
- Implementare un sistema di ruoli per distinguere tra utenti e operatori.
- Migliorare l'interfaccia utente con animazioni e design moderni.
- Integrare un sistema di notifiche per aggiornamenti sui prelievi.

---

### Autore

Progetto sviluppato da **Amati Team**.