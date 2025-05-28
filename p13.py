import argparse
import os

def create_file(path):
    """Створює новий текстовий файл і записує туди декілька рядків."""
    print(f"Введіть текст для файлу (щоб завершити — введіть рядок із одним символом точка «.»):")
    lines = []
    while True:
        line = input()
        if line.strip() == '.':
            break
        lines.append(line)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"\nФайл '{path}' успішно створено. Вміст файлу:")
    print('-' * 40)
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read())
    print('-' * 40)

def analyze_file(path):
    """Підраховує кількість рядків, слів і символів у файлі."""
    if not os.path.isfile(path):
        print(f"Файл '{path}' не знайдено.")
        return
    n_lines = n_words = n_chars = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            n_lines += 1
            n_chars += len(line)
            n_words += len(line.split())
    # Вивід у структурованому вигляді
    print(f"Аналіз файлу '{path}':")
    print(f"{'Рядків':<15}{'Слів':<10}{'Символів':<10}")
    print(f"{'-'*35}")
    print(f"{n_lines:<15}{n_words:<10}{n_chars:<10}")

def replace_in_file(src_path, dst_path, old, new):
    """Шукає й замінює всі входження old → new, зберігає результат у новому файлі."""
    if not os.path.isfile(src_path):
        print(f"Файл '{src_path}' не знайдено.")
        return
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    replaced = content.replace(old, new)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(replaced)
    print(f"У файлі '{src_path}' замінено всі '{old}' → '{new}'.")
    print(f"Результат збережено в '{dst_path}'.")

def main():
    parser = argparse.ArgumentParser(
        description="Простий текстовий редактор / аналізатор / пошук і заміна"
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Завдання 1: create
    p1 = subparsers.add_parser('create', help='Створити новий текстовий файл')
    p1.add_argument('filepath', help='Шлях до нового файлу')

    # Завдання 2: analyze
    p2 = subparsers.add_parser('analyze', help='Аналіз вмісту файлу')
    p2.add_argument('filepath', help='Шлях до існуючого файлу')

    # Завдання 3: replace
    p3 = subparsers.add_parser('replace', help='Пошук і заміна в файлі')
    p3.add_argument('source', help='Шлях до оригінального файлу')
    p3.add_argument('destination', help='Шлях до файлу з результатом')
    p3.add_argument('old', help='Слово/фразу для заміни')
    p3.add_argument('new', help='Нове слово/фразу')

    args = parser.parse_args()

    if args.command == 'create': 
        create_file(args.filepath)
    elif args.command == 'analyze':
        analyze_file(args.filepath)
    elif args.command == 'replace':
        replace_in_file(args.source, args.destination, args.old, args.new)

if __name__ == '__main__':
    main()
