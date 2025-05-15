import sqlite3

# Connessione al database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Dati di esempio per la tabella User
users = [
    ("Mario", "Rossi", "mario.rossi@example.com", "MROSSI", "Password123!"),
    ("Luigi", "Verdi", "luigi.verdi@example.com", "LVERDI", "Password456!"),
    ("Anna", "Bianchi", "anna.bianchi@example.com", "ABIANCHI", "Password789!"),
    ("Giulia", "Neri", "giulia.neri@example.com", "GNERI", "Password321!"),
    ("Marco", "Gialli", "marco.gialli@example.com", "MGIALLI", "Password654!"),
    ("Elena", "Blu", "elena.blu@example.com", "EBLU", "Password987!"),
    ("Francesco", "Viola", "francesco.viola@example.com", "FVIOLA", "Password111!"),
    ("Chiara", "Rosa", "chiara.rosa@example.com", "CROSA", "Password222!"),
    ("Alessandro", "Marrone", "alessandro.marrone@example.com", "AMARRONE", "Password333!"),
    ("Valentina", "Grigio", "valentina.grigio@example.com", "VGRIGIO", "Password444!"),
    ("Giorgio", "Argento", "giorgio.argento@example.com", "GARGENTO", "Password555!"),
    ("Martina", "Oro", "martina.oro@example.com", "MORO", "Password666!"),
    ("Luca", "Verde", "luca.verde@example.com", "LVERDE", "Password777!"),
    ("Sara", "Azzurro", "sara.azzurro@example.com", "SAZZURRO", "Password888!"),
    ("Davide", "Bianco", "davide.bianco@example.com", "DBIANCO", "Password999!"),
    ("Federica", "Nero", "federica.nero@example.com", "FNERO", "Password000!"),
    ("Simone", "Porpora", "simone.porpora@example.com", "SPORPORA", "Password101!"),
    ("Ilaria", "Turchese", "ilaria.turchese@example.com", "ITURCHESE", "Password202!"),
    ("Andrea", "Indaco", "andrea.indaco@example.com", "AINDACO", "Password303!"),
    ("Paola", "Lilla", "paola.lilla@example.com", "PLILLA", "Password404!")
]

# Inserisci dati nella tabella User
cursor.executemany("""
    INSERT INTO User (nome, cognome, email, codice_operatore, password)
    VALUES (?, ?, ?, ?, ?)
""", users)

# Dati di esempio per la tabella Prelievo
prelievi = [
    ("RSSMRA85M01H501Z", "Ospedale San Raffaele", "2023-10-01T09:00", "Emocromo completo", "4.7", "6.5", "42.0", "13.5"),
    ("RSSMRA85M01H501Z", "Clinica Sant'Anna", "2023-10-05T14:30", "Analisi del sangue", "4.8", "6.8", "43.0", "14.0"),
    ("VRDLGU90M01H501Z", "Ospedale Niguarda", "2023-10-10T11:15", "Emocromo completo", "4.6", "6.2", "41.5", "13.2"),
    ("BNCANN95F01H501Z", "Policlinico Milano", "2023-10-15T08:45", "Analisi del sangue", "4.9", "6.9", "44.0", "14.2"),
    ("RSSMRA85M01H501Z", "Ospedale San Raffaele", "2023-10-20T10:00", "Emocromo completo", "4.5", "6.4", "41.0", "13.0"),
    ("VRDLGU90M01H501Z", "Clinica Sant'Anna", "2023-10-25T15:30", "Analisi del sangue", "4.9", "6.7", "43.5", "14.1"),
    ("BNCANN95F01H501Z", "Ospedale Niguarda", "2023-10-30T12:00", "Emocromo completo", "4.8", "6.3", "42.5", "13.8"),
    ("RSSMRA85M01H501Z", "Policlinico Milano", "2023-11-01T09:15", "Analisi del sangue", "4.6", "6.6", "42.0", "13.6"),
    ("VRDLGU90M01H501Z", "Ospedale San Raffaele", "2023-11-05T14:00", "Emocromo completo", "4.7", "6.5", "42.2", "13.7"),
    ("BNCANN95F01H501Z", "Clinica Sant'Anna", "2023-11-10T11:45", "Analisi del sangue", "4.8", "6.8", "43.8", "14.3"),
    ("RSSMRA85M01H501Z", "Ospedale Niguarda", "2023-11-15T08:30", "Emocromo completo", "4.9", "6.9", "44.5", "14.5"),
    ("VRDLGU90M01H501Z", "Policlinico Milano", "2023-11-20T10:45", "Analisi del sangue", "4.5", "6.4", "41.8", "13.4"),
    ("BNCANN95F01H501Z", "Ospedale San Raffaele", "2023-11-25T13:30", "Emocromo completo", "4.6", "6.2", "41.2", "13.1"),
    ("RSSMRA85M01H501Z", "Clinica Sant'Anna", "2023-11-30T16:00", "Analisi del sangue", "4.7", "6.5", "42.3", "13.8"),
    ("VRDLGU90M01H501Z", "Ospedale Niguarda", "2023-12-01T09:00", "Emocromo completo", "4.8", "6.3", "42.7", "13.9"),
    ("BNCANN95F01H501Z", "Policlinico Milano", "2023-12-05T14:15", "Analisi del sangue", "4.9", "6.7", "43.9", "14.4"),
    ("RSSMRA85M01H501Z", "Ospedale San Raffaele", "2023-12-10T11:30", "Emocromo completo", "4.5", "6.4", "41.5", "13.2"),
    ("VRDLGU90M01H501Z", "Clinica Sant'Anna", "2023-12-15T08:45", "Analisi del sangue", "4.6", "6.6", "42.1", "13.5"),
    ("BNCANN95F01H501Z", "Ospedale Niguarda", "2023-12-20T12:30", "Emocromo completo", "4.7", "6.5", "42.4", "13.6"),
    ("RSSMRA85M01H501Z", "Policlinico Milano", "2023-12-25T10:15", "Analisi del sangue", "4.8", "6.8", "43.6", "14.2")
]

# Inserisci dati nella tabella Prelievo
cursor.executemany("""
    INSERT INTO Prelievo (codice_fiscale, luogo, data_ora, denominazione_analisi, rbc, wbc, hct, hgb)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", prelievi)

# Conferma le modifiche e chiudi la connessione
conn.commit()
conn.close()

print("Database popolato con successo!")
