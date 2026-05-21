# JournalX – Digitale Journal Webanwendung

JournalX ist eine moderne Journal- und Tagebuch-Webanwendung, die mit Python, Flask, SQLite, HTML, CSS und JavaScript entwickelt wurde.

Benutzer können persönliche Journal-Einträge erstellen, anzeigen, bearbeiten und löschen. Zusätzlich verfügt die Anwendung über ein Login- und Registrierungssystem.

Die Anwendung verbindet Frontend, Backend und Datenbank über eine REST API.

---

# Projektbeschreibung

Das Ziel des Projekts war die Entwicklung einer interaktiven Webanwendung für digitale Journal-Einträge.

Benutzer können:

- persönliche Gedanken speichern
- Einträge verwalten
- sich registrieren
- sich einloggen
- Einträge bearbeiten und löschen

Die Anwendung wurde lokal mit Flask entwickelt und verwendet SQLite als Datenbank.

---

# Funktionen

## Benutzer Funktionen

- Registrierung
- Login System
- Benutzerverwaltung

---

## Journal Funktionen

- Einträge erstellen
- Einträge anzeigen
- Einträge bearbeiten
- Einträge löschen

---

## CRUD System

Die Anwendung unterstützt vollständige CRUD Operationen:

- Create → Einträge erstellen
- Read → Einträge anzeigen
- Update → Einträge bearbeiten
- Delete → Einträge löschen

---

# Frontend

Die Benutzeroberfläche wurde mit:

- HTML
- CSS
- JavaScript

entwickelt.

JavaScript kommuniziert über Fetch API Requests mit dem Flask Backend.

---

# Backend

Das Backend wurde mit Flask entwickelt.

Die REST API verarbeitet:

- GET Requests
- POST Requests
- PUT Requests
- DELETE Requests

---

# Datenbank

Als Datenbank wird SQLite verwendet.

Es existieren folgende Tabellen:

## users

Speichert Benutzer:

- id
- username
- password

---

## entries

Speichert Journal Einträge:

- id
- title
- content

---

# Verwendete Technologien

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Git
- GitHub

---

# API Endpoints

## GET /entries

Gibt alle Journal Einträge zurück.

---

## POST /entries

Erstellt einen neuen Journal Eintrag.

---

## PUT /entries/<id>

Bearbeitet einen bestehenden Eintrag.

---

## DELETE /entries/<id>

Löscht einen Journal Eintrag.

---

## POST /register

Registriert einen Benutzer.

---

## POST /login

Überprüft Login Daten.

---

# Projekt starten

## Virtuelle Umgebung aktivieren

```bash
source .venv/bin/activate

# Sprint Dokumentation

## Sprint 1
- Projektplanung
- Flask Setup
- SQLite Integration

## Sprint 2
- CRUD Funktionen umgesetzt
- REST API entwickelt
- Login und Registrierung integriert

## Sprint 3
- Frontend verbessert
- API getestet
- Präsentation vorbereitet
- Dokumentation ergänzt