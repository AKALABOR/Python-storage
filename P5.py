temperature = float(input("Введіть температуру приміщення (°C): "))

if temperature < 16:
    print("Температура занизька! Увімкніть обігрівач.")
    exit()
if temperature > 28:
    print("Температура зависока! Увімкніть кондиціонер.")
    exit()
print("Температура комфортна.")
