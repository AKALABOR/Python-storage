number = input("Введіть трицифрове число: ")
if not number.isdigit() or len(number) != 3:
    print("Помилка: потрібно ввести трицифрове число.")
else:
    number = int(number)

    first_digit = number // 100
    last_digit = number % 10

    if first_digit == last_digit:
        print("Число є паліндромом.")
    else:
        print("Число не є паліндромом.")
