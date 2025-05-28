text = input("Введіть текст для аналізу: ")
output_format = input("Формат результату (list/set/dict): ").strip().lower()
frequency_target = int(input("Введіть кількість повторень для фільтрації: "))


def count_characters(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


char_frequency = count_characters(text)
unique_chars = set(text)
filtered = [char for char, count in char_frequency.items() if count == frequency_target]


print("\n=== Частота символів ===")
if output_format == "dict":
    print(char_frequency)
elif output_format == "set":
    print(set(char_frequency.items()))
elif output_format == "list":
    print(list(char_frequency.items()))
else:
    print("Невідомий формат. Використано словник за замовчуванням.")
    print(char_frequency)


print("\n=== Унікальні символи ===")
print(unique_chars)


print(f"\n=== Символи, що зустрічаються рівно {frequency_target} раз(и) ===")
print(filtered)
