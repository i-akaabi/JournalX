from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


# Erstellt die Datenbank und Tabelle
def init_db():

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")

    cursor.execute("""
        INSERT INTO entries (title, content)
        VALUES (?, ?)
    """, ("Test Eintrag", "SQLite funktioniert"))

    connection.commit()

    connection.close()


# Startseite der API
@app.route("/")
def home():
    return "Journal API läuft"


# Gibt alle Einträge als JSON zurück
@app.route("/entries")
def get_entries():

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM entries")

    entries = cursor.fetchall()

    connection.close()

    return jsonify(entries)

@app.route("/entries", methods=["POST"])
def create_entry():

    data = request.get_json()

    title = data["title"]

    content = data["content"]

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO entries (title, content)
        VALUES (?, ?)
    """, (title, content))

    connection.commit()

    connection.close()

    return jsonify({
    "message": "Neuer Eintrag erstellt"
})

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data["username"]

    password = data["password"]

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (?, ?)
    """, (username, password))

    connection.commit()

    connection.close()

    return jsonify({
        "message": "Benutzer registriert",
        "username": username
    })

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data["username"]

    password = data["password"]

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE username = ? AND password = ?
    """, (username, password))

    user = cursor.fetchone()

    connection.close()

    if user:

        return jsonify({
            "message": "Login erfolgreich"
        })

    else:

        return jsonify({
            "message": "Falsche Login Daten"
        })

@app.route("/entries/<int:id>", methods=["PUT"])
def update_entry(id):

    data = request.get_json()

    title = data["title"]

    content = data["content"]

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE entries
        SET title = ?, content = ?
        WHERE id = ?
    """, (title, content, id))

    connection.commit()

    connection.close()

    return jsonify({
        "message": "Eintrag aktualisiert",
        "id": id,
        "title": title,
        "content": content
    })

@app.route("/entries/<int:id>", methods=["DELETE"])
def delete_entry(id):

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
    """, (id,))

    connection.commit()

    connection.close()

    return jsonify({
        "message": "Eintrag gelöscht",
        "id": id
    })

if __name__ == "__main__":

    init_db()

    app.run(debug=True)