from datetime import datetime
from collections import Counter

class UkrainianCalendar:
    def get_holiday_list(self):
        return [
            "2025-01-01", "2025-01-07", "2025-03-08",
            "2025-04-20", "2025-05-01", "2025-05-09",
            "2025-06-28", "2025-08-24", "2025-10-14",
            "2025-12-25"
        ]
    def is_working_day(self, date_str):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if date.weekday() >= 5:
            return False
        return date_str not in self.get_holiday_list()

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Ділення на нуль"
        return a / b

class TextStats:
    def __init__(self, text):
        self.text = text
    def count_words(self):
        return len(self.text.split())
    def most_common_letter(self):
        letters = [c.lower() for c in self.text if c.isalpha()]
        if not letters:
            return None
        return Counter(letters).most_common(1)[0][0]

def calendar_demo():
    uc = UkrainianCalendar()
    print("Свята:", uc.get_holiday_list())
    d = input("Введіть дату (рррр-мм-дд): ")
    if uc.is_working_day(d):
        print("Це робочий день.")
    else:
        print("Це вихідний або свято.")

def calculator_demo():
    calc = Calculator()
    a = float(input("Число 1: "))
    b = float(input("Число 2: "))
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    op = input("Операція: ")
    if op == "1":
        print(calc.add(a, b))
    elif op == "2":
        print(calc.subtract(a, b))
    elif op == "3":
        print(calc.multiply(a, b))
    elif op == "4":
        print(calc.divide(a, b))

def text_demo():
    text = input("Введіть текст: ")
    stats = TextStats(text)
    print("Кількість слів:", stats.count_words())
    print("Найпоширеніша літера:", stats.most_common_letter())

def main():
    while True:
        print("\n1. Календар")
        print("2. Калькулятор")
        print("3. Аналіз тексту")
        print("4. Вихід")
        choice = input("Оберіть опцію: ")
        if choice == "1":
            calendar_demo()
        elif choice == "2":
            calculator_demo()
        elif choice == "3":
            text_demo()
        elif choice == "4":
            break

main()
