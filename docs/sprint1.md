# Sprint 1 – Woche 1

## 📅 Ziel der Woche
Aufbau der Projektstruktur und erste Backend-Grundlagen.
## Montag & Dienstag 📅

---

## 🧱 Aufgaben

- GitHub Repository erstellen
- Projekt lokal einrichten
- README erstellen
- Ordnerstruktur (docs) erstellen
- Flask installieren
- Erste API vorbereiten

---

## ✅ Erledigt

- Repository erstellt
- GitHub verbunden
- README erstellt
- docs Ordner angelegt

---

## ⚠️ Probleme

- GitHub Push Fehler (Token Problem)
- Verständnis von Git Pull / Push

---

## 💡 Lösungen

- Token erstellt und verwendet
- Git Workflow verstanden (add, commit, push)

---

## 🔄 Nächste Schritte

- Flask starten
- Erste Route erstellen
- API Grundlagen verstehen

---

## 📅 Mittwoch

## ✅ Fortschritt

- Flask installiert
- Virtuelle Umgebung (venv) aktieviert
- app.py erstellt
- Erste Flask-App aufgebaut
- Erste Route "/" erstellt
- Lokalen Entwicklungsserver gestartet
- API erfolgreich im Browser getestet
- Route /entries erfolgreich erstellt
- JSON-Daten über API zurückgegeben
- Mehrere API-Endpunkte getestet
- Flask-App Struktur erweitert

---

## 🧠 Gelernt

- Was Flask ist
- Wie Routing funktioniert
- Unterschried zwischen lokalem Server und GitHub
- Bedeutung von venv
- Grundaufbau einer Flask-App
- Wie JSON-Daten aufgebaut sind
- Wie Flask mehrere Routes verarbeitet
- Unterschied zwischen normaler Rückgabe und jsonify()
- Aufbau eines API-Endpunkts
- Bedeutung von API-Routen

## ⚠️ Probleme

- pip wurde zuerst nicht erkannt
- Verständnis vom Lokalen Server
- Erste Orientirung in Flask
- Fehler bei der Reihenfolge der Flask-Routen
- Einrückungsfehler (Indentation)
- Route /entries wurde zuerst nicht gefunden
- Verständnis von jsonify()

## 💡 Lösungen

- Flask mit python3 -m pip install flask installiert
- Virteuelle Umgebung korrekt aktiviert
- Flask-Server erfolgreich gestartet
- Flask-Struktur korrekt angeordnet
- app.run() ans Ende verschoben
- Einrückungen korrigiert
- jsonify() für JSON-Antworten verwendet

## 🔄 Nächste Schritte

- Datenbank vorbereiten
- SQLite integrieren
- Neue API-Routen planen

---

## 📅 Donnerstag

## ✅ Fortschritt

- SQLite Datenbankdatei erstellt
- sqlite3 in Flask integriert
- Funktion init_db() erstellt
- Tabelle "entries" vorbereitet
- Verbindung zwischen Flask und SQLite aufgebaut
- Datenbank wird beim Start automatisch initialisiert
- Kleine Kommentare im Code hinzugefügt
- Code-Struktur verbessert
- Ersten Testeintrag in SQLite gespeichert

---

## 🧠 Gelernt

- Wie SQLite mit Python funktioniert
- Wie Tabellen erstellt werden
- Bedeutung von PRIMARY KEY und AUTOINCREMENT
- Nutzung von sqlite3.connect()
- Warum commit() und close() wichtig sind
- Wie Flask mit einer Datenbank verbunden wird
- Nutzung von INSERT INTO
- Wie Daten in SQLite gespeichert werden

---

## ⚠️ Probleme

- Verständnis für Datenbankstruktur am Anfang ungewohnt
- Reihenfolge von init_db() und app.run() verstehen

---

## 💡 Lösungen

- init_db() vor app.run() eingebunden
- Datenbankstruktur Schritt für Schritt aufgebaut
- Code-Struktur sauber getrennt
- Testdaten erfolgreich in SQLite gespeichert

---

## 🔄 Nächste Schritte

- Daten direkt aus SQLite abrufen
- Feste Python-Testdaten ersetzen
- API-Routen erweitern
- POST Requests verstehen

## 📅 Freitag

## 🎯 Ziele für heute

- Daten direkt aus SQLite abrufen
- Feste Python-Testdaten ersetzen
- API dynamisch machen
- Verstehen, wie Flask Daten aus der Datenbank verarbeitet

---

## ✅ Fortschritt

- Daten direkt aus SQLite abgerufen
- Feste Python-Testdaten ersetzt
- SELECT * FROM entries verwendet
- fetchall() genutzt
- Dynamische API aufgebaut
- Flask erfolgreich mit SQLite-Daten verbunden
- POST Route für neue Journal Einträge erstellt
- JSON Daten über request.get_json() empfangen
- Neue Einträge erfolgreich in SQLite gespeichert
- REST Client zum Testen von POST Requests verwendet

---

## 🧠 Gelernt

- Wie Daten aus SQLite gelesen werden
- Unterschied zwischen statischen und dynamischen Daten
- Nutzung von SELECT *
- Nutzung von fetchall()
- Wie Flask Daten aus der Datenbank an die API sendet
- Unterschied zwischen GET und POST Requests
- Nutzung von request.get_json()
- Wie JSON Daten verarbeitet werden
- Wie neue Daten in SQLite gespeichert werden
- Nutzung des REST Client für API Tests

---

## ⚠️ Probleme

- Verständnis für dynamische Datenabfragen
- Unterschied zwischen Python-Testdaten und echten Datenbankdaten verstehen
- Verständnis für POST Requests und JSON Daten
- Verständnis für API Testanfragen mit REST Client

---

## 💡 Lösungen

- Datenbankabfrage Schritt für Schritt aufgebaut
- Feste Python-Daten erfolgreich ersetzt
- SQLite-Daten erfolgreich als JSON zurückgegeben
- POST Route Schritt für Schritt aufgebaut
- REST Client erfolgreich zum Testen verwendet
- JSON Daten erfolgreich verarbeitet und gespeichert

---

## 🔄 Nächste Schritte

- API Antworten verbessern
- Neue Daten strukturierter zurückgeben
- PUT Requests verstehen
- DELETE Requests verstehen
- CRUD weiter ausbauen