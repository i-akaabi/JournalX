import requests

# URL von deinem Flask Backend
url = "http://127.0.0.1:5000/register"

# JSON Daten
data = {
    "username": "amir",
    "password": "1234"
}

# POST Request senden
response = requests.post(url, json=data)

# Antwort ausgeben
print("Status Code:", response.status_code)
print("Antwort:", response.text)