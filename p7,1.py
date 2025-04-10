while True:
    user_input = input("Введіть ціле невід’ємне число: ")

    if not user_input.isdigit():
        print("Помилка: введене значення не є цілим невід’ємним числом.")
        continue

    number = int(user_input)
    break

result = 1
i = 1
steps = ""

while i <= number:
    result *= i
    steps += str(i)
    if i < number:
        steps += "*"
    i += 1

print(f"{number}! = {steps} = {result}")
