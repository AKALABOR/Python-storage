def task1():
    print("Завдання 1: Форматування за допомогою f-strings")
    first_name = input("Введіть ім'я: ")
    last_name = input("Введіть прізвище: ")
    age = float(input("Введіть вік: "))
    city = input("Введіть місто: ")

    result = f"Ім'я: {first_name:<10} | Вік: {age:.2f} | Місто: {city:>15}"
    print(result)
    print("\n" + "="*50 + "\n")


def task2():
    print("Завдання 2: Таблиця товарів з використанням .format()")
    print("{:<20} {:>10} {:^8}".format("Назва товару", "Ціна", "К-сть"))
    print("-" * 40)

    products = [
        {"name": "Ноутбук", "price": 24999.90, "quantity": 5},
        {"name": "Миша", "price": 599.50, "quantity": 20},
        {"name": "Клавіатура", "price": 799.99, "quantity": 15}
    ]

    for p in products:
        print("{:<20} {:>10.2f} {:^8}".format(p["name"], p["price"], p["quantity"]))
    print("\n" + "="*50 + "\n")


def task3():
    print("Завдання 3: Генерація текстового звіту")
    students = [
        {"name": "Іван Петренко", "avg_grade": 91.3, "attendance": 96},
        {"name": "Олена Коваль", "avg_grade": 84.75, "attendance": 88},
        {"name": "Марко Бондар", "avg_grade": 78.6, "attendance": 92},
        {"name": "Анна Сидоренко", "avg_grade": 89.2, "attendance": 99},
    ]

    print("=" * 50)
    print(f"{'ЗВІТ ПРО УСПІШНІСТЬ СТУДЕНТІВ':^50}")
    print("=" * 50)

    print("{:<20} {:>15} {:>12}".format("Ім'я", "Сер. бал", "Відвідуваність"))
    print("-" * 50)

    total_grade = 0
    for s in students:
        print("{:<20} {:>15.2f} {:>12}%".format(s["name"], s["avg_grade"], s["attendance"]))
        total_grade += s["avg_grade"]

    avg_group = total_grade / len(students)
    print("-" * 50)
    print("{:<20} {:>15.2f}".format("Середній бал групи:", avg_group))


if __name__ == "__main__":
    task1()
    task2()
    task3()
