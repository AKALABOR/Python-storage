# Завдання 1
cities = ["Київ", "Одеса", "Львів", "Харків", "Житомир"]
city_set = set(cities)
for city in ["Одеса", "Полтава"]:
    print(f"Місто {city} {'присутнє' if city in city_set else 'відсутнє'} у списку.")

# Завдання 2
students = {"Іван": 80, "Марія": 95, "Олег": 78, "Анна": 85}
try:
    name = input("Введіть ім'я студента: ")
    print(f"Оцінка студента {name}: {students[name]}")
except KeyError:
    print("Студента з таким ім'ям немає у словнику.")

# Завдання 3
import random
numbers = [random.randint(1, 1000) for _ in range(1000)]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
max_num = max(frequency, key=frequency.get)
print(f"Число {max_num} повторюється {frequency[max_num]} разів.")
