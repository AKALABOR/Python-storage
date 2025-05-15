# Завдання 1. Створення телефонної книги
phone_book = [
    {"ім'я": "Олена", "прізвище": "Іванова", "телефон": "0971112233", "місто": "Київ"},
    {"ім'я": "Ігор", "прізвище": "Петренко", "телефон": "0632223344", "місто": "Львів"},
    {"ім'я": "Марія", "прізвище": "Сидоренко", "телефон": "0503334455", "місто": "Київ"},
    {"ім'я": "Олексій", "прізвище": "Бондар", "телефон": "0674445566", "місто": "Одеса"},
    {"ім'я": "Світлана", "прізвище": "Коваленко", "телефон": "0995556677", "місто": "Харків"}
]

def print_contacts(contacts):
    print("{:<10} {:<12} {:<13} {:<10}".format("Ім'я", "Прізвище", "Телефон", "Місто"))
    print("-" * 50)
    for contact in contacts:
        print("{:<10} {:<12} {:<13} {:<10}".format(
            contact["ім'я"], contact["прізвище"], contact["телефон"], contact["місто"]
        ))

print("Повний перелік контактів:")
print_contacts(phone_book)

# Завдання 2. Пошук
def search_contacts(phone_book, key):
    value = input(f"Введіть {key}: ").strip()
    if not value:
        print("Введення не може бути порожнім.")
        return
    results = [c for c in phone_book if c[key].lower() == value.lower()]
    if results:
        print("Знайдені контакти:")
        print_contacts(results)
    else:
        print("Контакти не знайдено.")

def search_menu():
    while True:
        print("\nМеню пошуку:")
        print("1. Пошук за ім'ям")
        print("2. Пошук за прізвищем")
        print("3. Пошук за містом")
        print("4. Вийти з пошуку")
        choice = input("Ваш вибір: ")
        if choice == "1":
            search_contacts(phone_book, "ім'я")
        elif choice == "2":
            search_contacts(phone_book, "прізвище")
        elif choice == "3":
            search_contacts(phone_book, "місто")
        elif choice == "4":
            break
        else:
            print("Невірний вибір.")

# Завдання 3. Оновлення, видалення та аналітика
def find_contact_by_name(phone_book, name):
    return [c for c in phone_book if c["ім'я"].lower() == name.lower()]

def update_contact():
    name = input("Введіть ім'я контакту для оновлення: ").strip()
    matches = find_contact_by_name(phone_book, name)
    if not matches:
        print("Контакт не знайдено.")
        return
    print_contacts(matches)
    confirm = input("Ви хочете оновити цей контакт? (так/ні): ").lower()
    if confirm == "так":
        for contact in matches:
            new_phone = input("Новий телефон: ").strip()
            new_city = input("Нове місто: ").strip()
            if new_phone:
                contact["телефон"] = new_phone
            if new_city:
                contact["місто"] = new_city
        print("Контакт оновлено.")
    else:
        print("Оновлення скасовано.")

def delete_contact():
    name = input("Введіть ім'я контакту для видалення: ").strip()
    matches = find_contact_by_name(phone_book, name)
    if not matches:
        print("Контакт не знайдено.")
        return
    print_contacts(matches)
    confirm = input("Ви впевнені, що хочете видалити цей контакт? (так/ні): ").lower()
    if confirm == "так":
        for contact in matches:
            phone_book.remove(contact)
        print("Контакт видалено.")
    else:
        print("Видалення скасовано.")

def analytics():
    cities = {c["місто"] for c in phone_book}
    print(f"\nУнікальні міста: {', '.join(cities)}")

    counts = {}
    for contact in phone_book:
        city = contact["місто"]
        counts[city] = counts.get(city, 0) + 1

    print("\nКількість контактів по містах:")
    for city, count in counts.items():
        print(f"{city}: {count}")

    if counts:
        most_common = max(counts, key=counts.get)
        print(f"\nМісто з найбільшою кількістю контактів: {most_common} ({counts[most_common]})")

def main_menu():
    while True:
        print("\nГоловне меню:")
        print("1. Пошук контактів")
        print("2. Оновити контакт")
        print("3. Видалити контакт")
        print("4. Аналітика")
        print("5. Показати всі контакти")
        print("6. Вийти")
        choice = input("Оберіть опцію: ")
        if choice == "1":
            search_menu()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            analytics()
        elif choice == "5":
            print_contacts(phone_book)
        elif choice == "6":
            print("До побачення!")
            break
        else:
            print("Невірний вибір.")

main_menu()
