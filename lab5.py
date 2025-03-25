import random

def generate_pin():
    return str(random.randint(1000, 9999))

def count_matches(secret, guess):
    """Підрахунок збігів цифр на правильних позиціях"""
    return sum(1 for s, g in zip(secret, guess) if s == g)

def main():
    secret_pin = generate_pin()
    attempts = 5

    print("Вас вітає гра 'Таємний код'!")
    print("Вгадайте 4-значний PIN-код. У вас є 5 спроб")

    for attempt in range(1, attempts + 1):
        a = input(f"Спроба {attempt}/{attempts}: ")

        if not a.isdigit() or len(a) != 4:
            print("Введіть рівно 4 цифри!")
            continue

        if a == secret_pin:
            print("Вітаємо! Ви вгадали PIN-код!")
            return
        
        matches = count_matches(secret_pin, a)
        print(f"Невірно. Збігів на правильних позиціях: {matches}")

    print(f"Спроби закінчились! PIN-код був: {secret_pin}")

if __name__ == "__main__":
    main()
