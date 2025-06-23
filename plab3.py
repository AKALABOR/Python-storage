import random

def generate_code():
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:4])

def get_feedback(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def is_valid_guess(guess):
    return guess.isdigit() and len(guess) == 4

def play_game():
    secret_code = generate_code()
    attempts = 0
    while True:
        guess = input("Введіть 4-цифровий код: ")
        if not is_valid_guess(guess):
            print("Некоректне введення. Спробуйте ще раз.")
            continue
        attempts += 1
        bulls, cows = get_feedback(secret_code, guess)
        print(f"Бики: {bulls}, Корови: {cows}")
        if bulls == 4:
            print(f"Ви вгадали код {secret_code} за {attempts} спроб!")
            break

play_game()