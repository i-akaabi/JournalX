# Flask Funktionen importieren
# Flask = Framework für unsere Webanwendung
# jsonify = Python Daten als JSON zurückgeben
# request = Daten vom Frontend/API empfangen
# render_template = HTML Seiten anzeigen

from flask import Flask, jsonify, request, render_template

# SQLite importieren
# SQLite ist unsere lokale Datenbank

import sqlite3


# Flask Anwendung erstellen
app = Flask(__name__)


# ---------------------------------------------------
# DATENBANK INITIALISIERUNG
# ---------------------------------------------------

def init_db():

    # Verbindung zur SQLite Datenbank herstellen
    connection = sqlite3.connect("database.db", timeout=10)

    # Cursor erstellen
    # Cursor führt SQL Befehle aus
    cursor = connection.cursor()


    # Tabelle für Journal Einträge erstellen
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS entries (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL

        )

    """)


    # Tabelle für Benutzer erstellen
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL

        )

    """)


    # Änderungen speichern
    connection.commit()

    # Verbindung schließen
    connection.close()


# Datenbank beim Start initialisieren
init_db()


# ---------------------------------------------------
# HTML STARTSEITE
# ---------------------------------------------------

# Route für die Hauptseite
# render_template zeigt index.html an

@app.route("/")
def home():

    return render_template("index.html")

# Login Seite anzeigen

@app.route("/login-page")
def login_page():

    return render_template("login.html")

# Registrierungsseite anzeigen

@app.route("/register-page")
def register_page():

    return render_template("register.html")

# Journal Seite anzeigen

@app.route("/journal")
def journal_page():

    return render_template("journal.html")


# ---------------------------------------------------
# ALLE EINTRÄGE ANZEIGEN (READ)
# ---------------------------------------------------

@app.route("/entries")
def get_entries():

    # Verbindung zur Datenbank
    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    # Alle Einträge abrufen
    cursor.execute("SELECT * FROM entries")

    entries = cursor.fetchall()

    # Verbindung schließen
    connection.close()


    # SQLite Daten in JSON Objekte umwandeln
    entries_list = []

    for entry in entries:

        entries_list.append({

            "id": entry[0],
            "title": entry[1],
            "content": entry[2]

        })


    # JSON Antwort zurückgeben
    return jsonify(entries_list)


# ---------------------------------------------------
# EINTRAG ERSTELLEN (CREATE)
# ---------------------------------------------------

@app.route("/entries", methods=["POST"])
def create_entry():

    # JSON Daten empfangen
    data = request.get_json()

    # Werte auslesen
    title = data["title"]
    content = data["content"]


    # Verbindung zur Datenbank
    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()


    # SQL INSERT Befehl
    cursor.execute("""

        INSERT INTO entries (title, content)
        VALUES (?, ?)

    """, (title, content))


    # Änderungen speichern
    connection.commit()

    # Verbindung schließen
    connection.close()


    # Antwort zurückgeben
    return jsonify({

        "message": "Eintrag gespeichert"

    })


# ---------------------------------------------------
# EINTRAG AKTUALISIEREN (UPDATE)
# ---------------------------------------------------

@app.route("/entries/<int:id>", methods=["PUT"])
def update_entry(id):

    # JSON Daten empfangen
    data = request.get_json()

    # Neue Werte auslesen
    title = data["title"]
    content = data["content"]


    # Verbindung zur Datenbank
    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()


    # SQL UPDATE Befehl
    cursor.execute("""

        UPDATE entries
        SET title = ?, content = ?
        WHERE id = ?

    """, (title, content, id))


    # Änderungen speichern
    connection.commit()

    # Verbindung schließen
    connection.close()


    # Antwort zurückgeben
    return jsonify({

        "message": "Eintrag aktualisiert",
        "id": id

    })


# ---------------------------------------------------
# EINTRAG LÖSCHEN (DELETE)
# ---------------------------------------------------

@app.route("/entries/<int:id>", methods=["DELETE"])
def delete_entry(id):

    # Verbindung zur Datenbank
    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()


    # SQL DELETE Befehl
    cursor.execute("""

        DELETE FROM entries
        WHERE id = ?

    """, (id,))


    # Änderungen speichern
    connection.commit()

    # Verbindung schließen
    connection.close()


    # Antwort zurückgeben
    return jsonify({

        "message": "Eintrag gelöscht",
        "id": id

    })



# ---------------------------------------------------
# BENUTZER REGISTRIEREN
# ---------------------------------------------------

@app.route("/register", methods=["POST"])
def register():

    # JSON Daten empfangen
    data = request.get_json()

    # Werte auslesen
    username = data["username"]
    password = data["password"]


    # Verbindung zur Datenbank
    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()


    # Benutzer speichern
    cursor.execute("""

        INSERT INTO users (username, password)
        VALUES (?, ?)

    """, (username, password))


    # Änderungen speichern
    connection.commit()

    # Verbindung schließen
    connection.close()


    # Antwort zurückgeben
    return jsonify({

        "message": "Benutzer registriert",
        "username": username

    })


# ---------------------------------------------------
# LOGIN SYSTEM
# ---------------------------------------------------

@app.route("/login", methods=["POST"])
def login():

    # JSON Daten empfangen
    data = request.get_json()

    # Werte auslesen
    username = data["username"]
    password = data["password"]

    # Verbindung zur Datenbank
    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    # Benutzer überprüfen
    cursor.execute("""

        SELECT * FROM users
        WHERE username = ? AND password = ?

    """, (username, password))

    # Erstes Ergebnis holen
    user = cursor.fetchone()

    # Verbindung schließen
    connection.close()


    # Prüfen ob Benutzer existiert
    if user:

        return jsonify({

            "message": "Login erfolgreich"

        })

    else:

        return jsonify({

            "message": "Falsche Login Daten"

        })

# ---------------------------------------------------
# FLASK SERVER STARTEN
# ---------------------------------------------------

if __name__ == "__main__":

    # Flask Entwicklungsserver starten
    app.run(debug=True)