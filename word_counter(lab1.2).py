def count_words_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return 0

filename = "quote.txt"
word_count = count_words_in_file(filename)
print(f"Кількість слів у файлі '{filename}': {word_count}")
