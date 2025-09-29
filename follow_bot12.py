from instagrapi import Client
import time
import random
import getpass

# --- Login-Daten sicher abfragen ---
USERNAME = input("👉 Instagram Benutzername: ").strip()
PASSWORD = getpass.getpass("👉 Instagram Passwort: ")

cl = Client()
cl.login(USERNAME, PASSWORD)
print(f"✅ Eingeloggt als {USERNAME}")

# --- Ziel-Account, Modus, Anzahl & Dry-Run abfragen ---
TARGET_USERNAME = input("👉 Ziel-Account eingeben: ").strip()
MODE = input("👉 Modus wählen (followers/following): ").strip().lower()
LIMIT = int(input("👉 Wie viele Accounts sollen bearbeitet werden?: ").strip())
DRY_RUN = input("👉 Dry-Run Modus? (ja/nein): ").strip().lower() == "ja"

# --- User-ID vom Zielaccount holen ---
try:
    target_user_id = cl.user_id_from_username(TARGET_USERNAME)
    print(f"✅ User-ID von {TARGET_USERNAME}: {target_user_id}")
except Exception as e:
    print("❌ Fehler beim Laden der User-ID:", e)
    exit()

# --- Follower oder Following laden ---
try:
    if MODE == "followers":
        users = cl.user_followers(target_user_id, amount=LIMIT)
        print(f"📥 {len(users)} Follower von {TARGET_USERNAME} geladen")
    elif MODE == "following":
        users = cl.user_following(target_user_id, amount=LIMIT)
        print(f"📥 {len(users)} Gefolgte von {TARGET_USERNAME} geladen")
    else:
        print("❌ Ungültiger Modus – bitte 'followers' oder 'following' wählen")
        exit()
except Exception as e:
    print("❌ Fehler beim Abrufen der Nutzer:", e)
    exit()

# --- Follow-Durchlauf ---
for user_id, user_data in list(users.items()):
    print(f"➡️  Account: {user_data.username}")

    if DRY_RUN:
        print(f"💡 Dry-Run: Würde folgen -> {user_data.username}")
    else:
        try:
            cl.user_follow(user_id)
            print(f"✅ Gefolgt: {user_data.username}")
        except Exception as e:
            print(f"⚠️ Fehler bei {user_data.username}: {e}")

    # Zufällige Pause zwischen 1-2 Sekunden
    sleep_time = round(random.uniform(1, 2), 2)
    print(f"⏸️  Pause {sleep_time} Sekunden")
    time.sleep(sleep_time)

print("🎉 Dry-Run / Follow-Durchlauf beendet!")
