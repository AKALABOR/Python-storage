def count_words(filename):
    """Функція підраховує кількість слів у текстовому файлі."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0

filename = "quote.txt"
word_count = count_words(filename)
print(f"Кількість слів у файлі '{filename}': {word_count}")
