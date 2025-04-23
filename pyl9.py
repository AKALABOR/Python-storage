def calculate_cosmic_distance(speed_of_light_fraction, time_years):
    return speed_of_light_fraction * time_years

def calculate_simplified_gravity(mass1, mass2, cosmic_factor=1.0):
    return mass1 * mass2 * cosmic_factor

def calculate_time_dilation_approximation(speed_of_light_fraction, time_seconds):
    try:
        return time_seconds / (1 - speed_of_light_fraction)
    except ZeroDivisionError:
        return float('inf') 

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Помилка")

def main():
    
    while True:
        print("\nОберіть розрахунок")
        print("1 - Космічна відстань")
        print("2 - Спрощена гравітація")
        print("3 - Наближення сповільнення часу")
        print("0 - Вихід з програми")

        choice = input("Твій вибір: ")

        if choice == "1":
            speed = get_float_input("Введіть частку швидкості світла (від 0 до 1): ")
            time = get_float_input("Введіть час у роках: ")
            result = calculate_cosmic_distance(speed, time)
            print(f"Приблизна космічна відстань: {result} світлових років.")

        elif choice == "2":
            mass1 = get_float_input("Введіть масу першого об'єкта: ")
            mass2 = get_float_input("Введіть масу другого об'єкта: ")
            factor = input("Введіть космічний фактор (або натисни Enter для 1.0): ")
            factor = float(factor) if factor else 1.0
            result = calculate_simplified_gravity(mass1, mass2, factor)
            print(f"Спрощене гравітаційне притягання: {result} умовних одиниць.")

        elif choice == "3":
            speed = get_float_input("Введіть частку швидкості світла (менше 1): ")
            time = get_float_input("Введіть час у секундах: ")
            if speed >= 1:
                print("Швидкість повинна бути меншою за швидкість світла.")
            else:
                result = calculate_time_dilation_approximation(speed, time)
                print(f"Наближене сповільнення часу: {result:.2f} секунд.")

        elif choice == "0":
            break

        else:
            print("Невідомий вибір. Будь ласка, обери опцію з меню.")

        again = input("\Бажаете провести ще один розрахунок? (так/ні): ").strip().lower()
        if again != "так":
            print("Програма завершена.")
            break

if __name__ == "__main__":
    main()
