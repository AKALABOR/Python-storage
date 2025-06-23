import os

FILENAME = "diary.txt"

def add_entry():
    date = input("Дата (рррр-мм-дд): ")
    location = input("Локація: ")
    text = input("Текст запису: ")
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"Дата: {date}\n")
        file.write(f"Локація: {location}\n")
        file.write(f"Текст: {text}\n")
        file.write("---\n")

def search_entries():
    query = input("Введіть дату або ключове слово: ").lower()
    with open(FILENAME, "r", encoding="utf-8") as file:
        content = file.read()
    entries = content.strip().split("---\n")
    for entry in entries:
        if query in entry.lower():
            print(entry.strip())
            print("---")

def analyze_entries():
    with open(FILENAME, "r", encoding="utf-8") as file:
        content = file.read()
    entries = content.strip().split("---\n")
    total_entries = len(entries)
    locations = set()
    word_count = 0
    for entry in entries:
        lines = entry.strip().split("\n")
        for line in lines:
            if line.startswith("Локація:"):
                locations.add(line.replace("Локація:", "").strip())
            if line.startswith("Текст:"):
                text = line.replace("Текст:", "").strip()
                word_count += len(text.split())
    print(f"Загальна кількість записів: {total_entries}")
    print(f"Кількість унікальних локацій: {len(locations)}")
    print(f"Загальна кількість слів: {word_count}")

def main():
    while True:
        print("\n1. Додати запис")
        print("2. Пошук записів")
        print("3. Аналітика")
        print("4. Вийти")
        choice = input("Оберіть дію: ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            search_entries()
        elif choice == "3":
            analyze_entries()
        elif choice == "4":
            break

main()
