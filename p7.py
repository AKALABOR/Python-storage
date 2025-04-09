import random
import time

def generate_secret_category():
    return random.choice(["число", "колір", "фрукт"])

def generate_secret_value(category):
    if category == "число":
        return str(random.randint(1, 10))
    elif category == "колір":
        return random.choice(["червоний", "синій", "зелений", "жовтий"])
    elif category == "фрукт":
        return random.choice(["яблуко", "банан", "груша", "персик"])

def give_hint(secret_value, category):
    truth = random.choice([True, False, True])
    fake_value = generate_secret_value(category)
    return secret_value if truth else fake_value

def is_meaningful_input(user_input):
    return any(char.isalnum() for char in user_input)

def main():
    print("Вітаємо у грі, в якій ви маєте вгадати щось… Але що саме?")
    print("Виберіть категорію для вгадування (але ми не скажемо, яка правильна):")
    print(" - число\n - колір\n - фрукт")

    category = input("Ваш вибір: ").strip().lower()

    if category not in ["число", "колір", "фрукт"]:
        print("Ми не впевнені, що це категорія, але хай буде. Починаємо.")
    else:
        print("Категорія прийнята. Час грати!")

    secret_category = generate_secret_category()
    secret_value = generate_secret_value(secret_category)
    attempts = 0
    max_attempts = random.randint(5, 15)

    while True:
        if attempts >= max_attempts:
            print("\nЧас вийшов. Гру завершено.")
            break

        guess = input("\nВаш варіант: ").strip().lower()

        if not is_meaningful_input(guess):
            print("Це що таке було?.. Спробуйте щось інше.")
            continue

        if guess == secret_value:
            print("Можливо, ви вгадали… а можливо, й ні.")
            break

        hint = give_hint(secret_value, secret_category)
        print(f"Підказка: це може бути '{hint}'")

        attempts += 1
        if random.random() < 0.1:
            print("...гра втратила інтерес до вас і йде спати.")
            break

    print("\n=== КІНЕЦЬ ГРИ ===")
    try:
        time.sleep(1.5)
        raise Exception("Ви виграли, якщо це мало сенс.")
    except Exception as e:
        if guess == secret_value and category == secret_category:
            print("Ви були напрочуд уважні. Вітаємо! Ви виграли!")
        else:
            print("Можливо, ви програли. А можливо, й ні. Дякуємо за гру.")
    finally:
        print("Залишайтесь чудернацькими 🌟")

if __name__ == "__main__":
    main()
