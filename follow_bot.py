from instagrapi import Client
import time
import random

# Login
cl = Client()
username = input("👉 Instagram Benutzername: ")
password = input(" Instagram Passwort: ")
cl.login(username, password)
print(f"✅ Eingeloggt als {username}")

# Zielaccount
target_username = input("👉 Ziel-Account eingeben: ")
mode = input("👉 Modus wählen (followers/following): ").lower()
max_follows = int(input("👉 Wie viele Accounts sollen bearbeitet werden?: "))
dry_run_input = input("👉 Dry-Run Modus? (ja/nein): ").lower()
dry_run = dry_run_input == "ja"

# User-ID abrufen
try:
    user_info = cl.user_info_by_username(target_username)
    target_user_id = user_info.pk
    print(f"✅ User-ID von {target_username}: {target_user_id}")
except Exception as e:
    print(f"❌ Fehler beim Abrufen des Ziel-Accounts: {e}")
    exit()

# Follower oder Following laden
if mode == "followers":
    users = cl.user_followers(target_user_id, amount=max_follows)
else:
    users = cl.user_following(target_user_id, amount=max_follows)

print(f"📥 {len(users)} Accounts von {target_username} geladen")

# Already following prüfen
already_following = cl.user_following(cl.user_id)

count = 0
for user_id, user in users.items():
    if count >= max_follows:
        break

    # Filter für unechte Accounts / Bots
    if user.is_private or (user.follower_count < 5000 and user.media_count > 5):
        if user.pk in already_following:
            print(f"⏩ Schon gefolgt: {user.username}")
        else:
            print(f"➡️  Account: {user.username}")
            if not dry_run:
                cl.user_follow(user.pk)
                print(f"✅ Gefolgt: {user.username}")
            else:
                print(f"DRY RUN: Würde {user.username} folgen")
            count += 1
            pause = round(random.uniform(3, 4), 2)
            print(f"⏸️  Pause {pause} Sekunden")
            time.sleep(pause)

print("🎉 Dry-Run / Follow-Durchlauf beendet ✅")
