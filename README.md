# insta-follow-bot
327.paradies
# Insta Follow Bot (Privat)

**⚠️ Wichtiger Hinweis / Disclaimer**

Dieses Skript automatisiert Aktionen auf Instagram. **Die Nutzung erfolgt auf eigene Gefahr.**  
Der Autor übernimmt **keine Haftung** für:  
- Sperrung, Einschränkung oder Deaktivierung von Instagram-Accounts  
- Datenverlust oder andere Schäden  
- Verletzungen von Instagram-Nutzungsbedingungen

Instagram verbietet die Automatisierung von Aktionen durch Bots. **Bitte nutze diesen Bot verantwortungsvoll und in Maßen.**

---

## Features

- Folgen von Followern oder Following eines Zielaccounts  
- Dry-Run Modus zum Testen ohne echte Aktionen  
- Zufällige Pausen zwischen Follows (3–4 Sekunden, optional längere Pausen)  
- Limitierungen pro Stunde / Tag einstellbar  
- Filter: Accounts ohne Profilbild oder mit sehr hoher Followerzahl überspringen  
- Logging der Aktionen

---

## Installation

1. Python 3.11+ installieren: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. Repository klonen oder Zip herunterladen
3. Virtuelle Umgebung erstellen:
    ```bash
    python -m venv venv
    ```
4. Umgebung aktivieren:
    - **Windows PowerShell**:  
      ```powershell
      .\venv\Scripts\Activate.ps1
      ```
    - **CMD**:  
      ```cmd
      .\venv\Scripts\activate.bat
      ```
5. Abhängigkeiten installieren:
    ```bash
    pip install -r requirements.txt
    ```
6. Konfiguration:
    - `.env.example` kopieren und in `.env` umbenennen
    - Instagram-Username und Passwort eintragen:
      ```
      INSTA_USERNAME=dein_username
      INSTA_PASSWORD=dein_passwort
      ```
7. Bot starten:
    ```bash
    python follow_bot.py
    ```

---

## Nutzung

- **Dry-Run**: Testmodus ohne echte Follows
- **Mode**: Follower oder Following eines Zielaccounts auswählen
- **Limits**: Tages- und Stundenlimits einstellen, um Sperrungen vorzubeugen

---

## Hinweise zur Sicherheit

- Niemals Passwörter oder sensible Daten öffentlich teilen  
- Keine massenhaften Aktionen — starte klein (10–20 Follows pro Tag) und steigere langsam  
- Überwache Logs regelmäßig  
- Vermeide aggressive Follow-/Unfollow-Muster  

---

## Lizenz

Dieses Skript wird unter MIT-Lizenz bereitgestellt.  
Die Nutzung erfolgt auf **eigene Verantwortung**.  
