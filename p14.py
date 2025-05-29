import json
import os

GAME_STATS_FILE = "game_stats.json"
CONTACTS_FILE = "contacts.json"
CLIENTS_FILE = "clients_db.json"

def load_json(file_path, default):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return default

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def update_game_stats(player, result):
    stats = load_json(GAME_STATS_FILE, {})
    player_stats = stats.get(player, {"games_played": 0, "wins": 0, "losses": 0})
    player_stats["games_played"] += 1
    if result == "win":
        player_stats["wins"] += 1
    elif result == "loss":
        player_stats["losses"] += 1
    stats[player] = player_stats
    save_json(GAME_STATS_FILE, stats)

def add_contact(name, phone, email):
    contacts = load_json(CONTACTS_FILE, {})
    contacts[name] = {"phone": phone, "email": email}
    save_json(CONTACTS_FILE, contacts)

def load_contacts():
    return load_json(CONTACTS_FILE, {})

def add_client(name, email):
    clients = load_json(CLIENTS_FILE, [])
    clients.append({"name": name, "email": email})
    save_json(CLIENTS_FILE, clients)

def find_client(name):
    clients = load_json(CLIENTS_FILE, [])
    return [c for c in clients if c["name"].lower() == name.lower()]

def update_client(name, new_email):
    clients = load_json(CLIENTS_FILE, [])
    for client in clients:
        if client["name"].lower() == name.lower():
            client["email"] = new_email
    save_json(CLIENTS_FILE, clients)

def delete_client(name):
    clients = load_json(CLIENTS_FILE, [])
    clients = [c for c in clients if c["name"].lower() != name.lower()]
    save_json(CLIENTS_FILE, clients)

def main_menu():
    while True:
        print("\n=== Головне меню ===")
        print("1. Оновити статистику гри")
        print("2. Додати контакт")
        print("3. Переглянути контакти")
        print("4. Додати клієнта")
        print("5. Знайти клієнта")
        print("6. Оновити email клієнта")
        print("7. Видалити клієнта")
        print("0. Вихід")
        
        choice = input("Ваш вибір: ")
        
        if choice == "1":
            player = input("Ім'я гравця: ")
            result = input("Результат (win/loss): ").lower()
            if result in ["win", "loss"]:
                update_game_stats(player, result)
                print("Статистика оновлена.")
            else:
                print("Невірний результат.")
        
        elif choice == "2":
            name = input("Ім'я контакту: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            add_contact(name, phone, email)
            print("Контакт додано.")
        
        elif choice == "3":
            contacts = load_contacts()
            print("Контакти:")
            for name, info in contacts.items():
                print(f"{name}: Телефон: {info['phone']}, Email: {info['email']}")
        
        elif choice == "4":
            name = input("Ім'я клієнта: ")
            email = input("Email клієнта: ")
            add_client(name, email)
            print("Клієнт доданий.")
        
        elif choice == "5":
            name = input("Ім'я для пошуку: ")
            results = find_client(name)
            if results:
                for client in results:
                    print(f"{client['name']} — {client['email']}")
            else:
                print("Клієнта не знайдено.")
        
        elif choice == "6":
            name = input("Ім'я клієнта для оновлення: ")
            new_email = input("Новий email: ")
            update_client(name, new_email)
            print("Email оновлено.")
        
        elif choice == "7":
            name = input("Ім'я клієнта для видалення: ")
            delete_client(name)
            print("Клієнт видалений.")
        
        elif choice == "0":
            print("Вихід з програми.")
            break
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()
