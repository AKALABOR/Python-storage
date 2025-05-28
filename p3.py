import sys

def task1():
    input_str = input("Завдання 1. Введіть число (int або float) - ")
    try:
        if '.' in input_str:
            num = float(input_str)
            num += 5.0
        else:
            num = int(input_str)
            num += 5
        result_str = str(num)
        print("Результат після додавання 5 = ", result_str)
    except ValueError:
        print("Помилка: введено нечислове значення.")

def task2():
    a = input("Завдання 2. Введіть перше число - ")
    b = input("Завдання 2. Введіть друге число - ")
    try:
        a_val = float(a)
        b_val = float(b)
        print(f"Сума: {a_val + b_val}")
        print(f"Різниця: {a_val - b_val}")
        print(f"Добуток: {a_val * b_val}")
        if b_val != 0:
            print(f"Частка: {a_val / b_val}")
        else:
            print("Ділення на нуль неможливе.")
    except ValueError:
        print("Помилка: одне з введених значень не є число")

def task3():
    input_str = input("Завдання 3. Введіть числа через кому (наприклад, '1, 2, 3') - ")
    try:
        str_list = input_str.split(",")
        num_list = [float(item.strip()) for item in str_list]
        total = sum(num_list)
        avg = total / len(num_list)
        print(f"Сума чисел: {total}")
        print(f"Середнє значення: {avg}")
    except ValueError:
        print("Помилка: деякі елементи не є числами - ")

def task4():
    num_str = input("Завдання 4. Введіть число з плаваючою комою - ")
    try:
        num = float(num_str)
        formatted = f"{num:.2f}"
        print("Відформатоване число з двома знаками після коми:", formatted)
    except ValueError:
        print("Помилка: введено нечислове значення.")

def main():
    while True:
        print("""
Оберіть завдання:
  1 – Перетворення рядка в число та зворотне перетворення
  2 – Арифметичні операції з введеними даними
  3 – Конвертація списку рядків у список чисел
  4 – Форматування числових значень
  0 – Вийти
""")
        choice = input("Ваш вибір ").strip()
        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "0":
            print("Вихід із програми.")
            sys.exit(0)
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
