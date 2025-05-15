# Завдання 1
grades = [85, 60, 90, 70, 55, 100, 40, 78]
high_grades = [grade for grade in grades if grade > 70]
print("Високі оцінки:", high_grades)
print("Кількість високих оцінок:", len(high_grades))

# Завдання 2
shopping_list = ["молоко", "хліб", "масло", "яйця", "сир", "яблука"]
long_items = [item for item in shopping_list if len(item) > 4]
print("Товари з назвою довше 4 символів:", long_items)
print("Кількість таких товарів:", len(long_items))

# Завдання 3
numbers = [1, 2, 3, 4, 3, 2, 5, 6, 5, 7]
duplicates = []
seen = set()
for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.add(num)
print("Повторювані числа:", duplicates)
