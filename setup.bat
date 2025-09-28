@echo off
echo ===== Insta-Follow-Bot Setup =====
echo Prüfe Python-Installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python ist nicht installiert. Bitte lade Python von https://www.python.org/downloads/ herunter und installiere es.
    pause
    exit /b
) else (
    echo Python ist installiert.
)

echo Erstelle virtuelle Umgebung...
python -m venv venv
call venv\Scripts\Activate.bat

echo Upgrade pip...
python -m pip install --upgrade pip

echo Installiere benötigte Pakete...
pip install instagrapi python-dotenv

echo ===== Setup abgeschlossen! =====
echo Du kannst jetzt follow_bot.py starten.
pause
