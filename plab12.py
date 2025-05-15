#Завдання 1: Інвентаризація товарів

inventory = [
    {"назва": "Ноутбук", "кількість": 10, "ціна": 20000, "категорія": "Електроніка"},
    {"назва": "Мишка", "кількість": 25, "ціна": 300, "категорія": "Електроніка"},
    {"назва": "Футболка", "кількість": 15, "ціна": 250, "категорія": "Одяг"},
    {"назва": "Штани", "кількість": 8, "ціна": 500, "категорія": "Одяг"},
    {"назва": "Молоко", "кількість": 5, "ціна": 30, "категорія": "Продукти"},
    {"назва": "Хліб", "кількість": 20, "ціна": 15, "категорія": "Продукти"},
    {"назва": "Навушники", "кількість": 12, "ціна": 800, "категорія": "Електроніка"}
]

def show_inventory(data):
    print(f"{'Назва':<15}{'Кількість':<10}{'Ціна':<10}{'Категорія':<15}")
    print("-" * 50)
    for item in data:
        print(f"{item['назва']:<15}{item['кількість']:<10}{item['ціна']:<10}{item['категорія']:<15}")

print("Інвентаризація товарів:")
show_inventory(inventory)

#Завдання 2: Складний пошук та редагування

def search_product(data, search_key, search_value):
    results = [item for item in data if item[search_key].lower() == search_value.lower()]
    if results:
        return results
    print("Товар не знайдено.")
    return []

def update_product(data, name, field, new_value):
    for item in data:
        if item["назва"].lower() == name.lower():
            try:
                item[field] = int(new_value) if field == "кількість" else float(new_value)
                print(f"Товар '{name}' оновлено.")
                return
            except ValueError:
                print("Некоректне значення.")
                return
    print("Товар не знайдено.")

print("\nПошук товару:")
name = input("Введіть назву або категорію товару: ")
results = search_product(inventory, "назва", name) or search_product(inventory, "категорія", name)
if results:
    show_inventory(results)

print("\nОновлення товару:")
name = input("Введіть назву товару: ")
field = input("Що оновити (кількість/ціна): ")
new_value = input("Нове значення: ")
update_product(inventory, name, field, new_value)

#Завдання 3: Аналітика складу та фінансів 

def calculate_total_per_category(data):
    totals = {}
    for item in data:
        category = item["категорія"]
        total_value = item["кількість"] * item["ціна"]
        totals[category] = totals.get(category, 0) + total_value
    return totals

def find_most_valuable_category(totals):
    return max(totals, key=totals.get)

def low_stock_items(data, threshold=5):
    return [item for item in data if item["кількість"] < threshold]

print("\nАналітика:")
totals = calculate_total_per_category(inventory)
print("Загальна вартість по категоріях:")
for category, total in totals.items():
    print(f"{category}: {total}")

max_category = find_most_valuable_category(totals)
print(f"Категорія з найбільшою вартістю товарів: {max_category}")

print("\nТовари з низьким запасом:")
low_stock = low_stock_items(inventory)
if low_stock:
    show_inventory(low_stock)
else:
    print("Немає товарів з низьким запасом.")
