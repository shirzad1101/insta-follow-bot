# test_env.py
# Minimaltest: Login-Daten fest im Code (nur zu Testzwecken)

USERNAME = "327.paradies"
PASSWORD = "##Madar1224!"

if USERNAME and PASSWORD:
    print(f"Login-Daten geladen! Benutzername: {USERNAME}")
else:
    print("Fehler: Login-Daten nicht gesetzt.")
