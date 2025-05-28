def simple_text_editor():
    filename = input("1) Новий файл – введіть ім'я файлу (з розширенням, напр. file.txt): ")
    print("Вводьте текст. Для завершення введення введіть порожній рядок.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\nФайл '{filename}' збережено. Вміст файлу:")
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

def analyze_file():
    filename = input("2) Аналіз – введіть ім'я файлу для аналізу: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)
    print(f"\nАналіз файлу '{filename}':")
    print(f"{'Показник':<10} {'Кількість':>10}")
    print("-" * 22)
    print(f"{'Рядків':<10} {num_lines:>10}")
    print(f"{'Слів':<10} {num_words:>10}")
    print(f"{'Символів':<10} {num_chars:>10}")


def search_and_replace():
    original_file = input("3) Пошук/заміна – введіть ім'я файлу для обробки: ")
    try:
        with open(original_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Файл '{original_file}' не знайдено.")
        return
    search_word = input("   Слово/фразу для пошуку: ")
    replace_word = input("   Слово/фразу для заміни: ")
    new_content = content.replace(search_word, replace_word)
    new_file = input("   Ім'я нового файлу для збереження: ")
    with open(new_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Зміни збережено у файлі '{new_file}'.")


def main_menu():
    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1. Створити новий текстовий файл")
        print("2. Аналіз вмісту файлу")
        print("3. Пошук і заміна в файлі")
        print("4. Вихід")
        choice = input("Виберіть дію (1–4): ")
        if choice == "1":
            simple_text_editor()
        elif choice == "2":
            analyze_file()
        elif choice == "3":
            search_and_replace()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()
