def factorial_recursive(n):
    if not isinstance(n, int):
        raise TypeError("Аргумент має бути цілим числом.")
    if n < 0:
        raise ValueError("Факторіал визначено лише для невід'ємних чисел.")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    if not isinstance(n, int):
        raise TypeError("Аргумент має бути цілим числом.")
    if n < 0:
        raise ValueError("Число Фібоначчі визначено лише для невід'ємних індексів.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum_list_recursive(lst):
    if not isinstance(lst, list):
        raise TypeError("Аргумент має бути списком.")
    if not lst:
        return 0
    if not isinstance(lst[0], (int, float)):
        raise TypeError("Список повинен містити лише числа.")
    return lst[0] + sum_list_recursive(lst[1:])


def is_palindrome_recursive(s):
    if not isinstance(s, str):
        raise TypeError("Аргумент має бути рядком.")
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    def helper(subs):
        if len(subs) <= 1:
            return True
        if subs[0] != subs[-1]:
            return False
        return helper(subs[1:-1])
    return helper(cleaned)


if __name__ == "__main__":
    try:
        n_fact = int(input("Введіть число для обчислення факторіалу: "))
        print("Факторіал:", factorial_recursive(n_fact))

        n_fib = int(input("Введіть номер для обчислення числа Фібоначчі: "))
        print("Число Фібоначчі:", fibonacci_recursive(n_fib))

        list_input = input("Введіть список чисел через пробіл для обчислення суми: ")
        numbers = list(map(float, list_input.strip().split()))
        print("Сума елементів списку:", sum_list_recursive(numbers))

        string_input = input("Введіть рядок для перевірки на паліндром: ")
        print("Є паліндромом:" if is_palindrome_recursive(string_input) else "Не є паліндромом.")

    except Exception as e:
        print("Помилка:", e)
