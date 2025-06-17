import json
import random
import string
import os

SETTINGS_FILE = "settings.json"

# Default settings
default_settings = {
    "length": 12,
    "turkish_characters": False,
    "use_special_characters": True,
    "custom_special_characters": "",
    "include_uppercase": True,
    "include_lowercase": True,
    "include_digits": True
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return default_settings.copy()

def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)

def generate_password(settings):
    character_pool = ""

    if settings["include_lowercase"]:
        character_pool += string.ascii_lowercase
    if settings["include_uppercase"]:
        character_pool += string.ascii_uppercase
    if settings["include_digits"]:
        character_pool += string.digits

    if settings["use_special_characters"]:
        if settings["custom_special_characters"]:
            character_pool += settings["custom_special_characters"]
        else:
            character_pool += string.punctuation

    if settings["turkish_characters"]:
        character_pool += "çğıöşüÇĞİÖŞÜ"

    if not character_pool:
        return "No character types selected!"

    return ''.join(random.choices(character_pool, k=settings["length"]))

def change_settings():
    settings = {}

    settings["length"] = int(input("Password length: "))

    turkish = input("Include Turkish characters? (y/n): ").lower()
    settings["turkish_characters"] = turkish == "y"

    special_chars = input("Include special characters? (y/n): ").lower()
    settings["use_special_characters"] = special_chars == "y"

    if settings["use_special_characters"]:
        specific = input("Do you want to use specific special characters? (y/n): ").lower()
        if specific == "y":
            settings["custom_special_characters"] = input("Enter the specific special characters you want to use: ")
        else:
            settings["custom_special_characters"] = ""

    settings["include_uppercase"] = input("Include uppercase letters? (y/n): ").lower() == "y"
    settings["include_lowercase"] = input("Include lowercase letters? (y/n): ").lower() == "y"
    settings["include_digits"] = input("Include digits? (y/n): ").lower() == "y"

    save_settings(settings)
    print("Settings saved.")
    return settings

def menu():
    settings = load_settings()

    # Generate initial password with current settings
    print("\n✨ Your first password (with current settings):")
    print("🔐", generate_password(settings))

    while True:
        print("\n[1] Generate new password")
        print("[2] Change settings")
        print("[0] Exit")
        choice = input("Your choice: ")

        if choice == "1":
            print("\n🔐 New password:", generate_password(settings))
        elif choice == "2":
            settings = change_settings()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
