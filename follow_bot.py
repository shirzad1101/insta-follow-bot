import time
import random
from instagrapi import Client

# ======== Benutzer Eingabe ========
username = input("👉 Instagram Benutzername: ")
password = input(" Instagram Passwort: ")

cl = Client()
try:
    cl.login(username, password)
    print(f"✅ Eingeloggt als {username}")
except Exception as e:
    print(f"❌ Login fehlgeschlagen: {e}")
    exit()

target_account = input("👉 Ziel-Account eingeben: ")
mode = input("👉 Modus wählen (followers/following): ").lower()
try:
    num_accounts = int(input("👉 Wie viele Accounts sollen bearbeitet werden?: "))
except ValueError:
    print("❌ Bitte eine Zahl eingeben")
    exit()
dry_run_input = input("👉 Dry-Run Modus? (ja/nein): ").lower()
dry_run = dry_run_input == "ja"

# ======== Ziel-Accounts abrufen ========
try:
    user_id = cl.user_id_from_username(target_account)
    print(f"✅ User-ID von {target_account}: {user_id}")
except Exception as e:
    print(f"❌ Fehler beim Abrufen der User-ID: {e}")
    exit()

try:
    if mode == "followers":
        accounts_to_follow = cl.user_followers(user_id, amount=num_accounts)
    elif mode == "following":
        accounts_to_follow = cl.user_following(user_id, amount=num_accounts)
    else:
        print("❌ Modus muss 'followers' oder 'following' sein")
        exit()
    print(f"📥 {len(accounts_to_follow)} Accounts von {target_account} geladen")
except Exception as e:
    print(f"❌ Fehler beim Abrufen der Accounts: {e}")
    exit()

# ======== Follow-Loop ========
for user in accounts_to_follow.values():
    try:
        user_full = cl.user_info(user.pk)
    except Exception as e:
        print(f"⚠️ Fehler beim Laden von {user.username}: {e}")
        continue

    # Skip bereits gefolgte oder unerwünschte Accounts
    if cl.user_following(user_full.pk) or user_full.is_private or (user_full.follower_count < 5000 and user_full.media_count < 5):
        continue

    if dry_run:
        print(f"DRY RUN: Würde {user_full.username} folgen")
    else:
        try:
            cl.user_follow(user_full.pk)
            print(f"✅ Gefolgt: {user_full.username}")
        except Exception as e:
            print(f"❌ Fehler beim Folgen von {user_full.username}: {e}")

    # Random Pause
    time.sleep(random.uniform(3, 4))

print(f"🎉 {'Dry-Run / ' if dry_run else ''}Follow-Durchlauf beendet!")
