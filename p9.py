def process_data(data, operation, target="values"):
    try:
        if not callable(operation):
            raise TypeError("Аргумент 'operation' має бути функцією.")

        if isinstance(data, list):
            return [operation(x) for x in data]
        elif isinstance(data, tuple):
            return tuple(operation(x) for x in data)
        elif isinstance(data, dict):
            if target == "keys":
                return {operation(k): v for k, v in data.items()}
            elif target == "values":
                return {k: operation(v) for k, v in data.items()}
            elif target == "both":
                return {operation(k): operation(v) for k, v in data.items()}
            else:
                raise ValueError("Неправильне значення параметра 'target'.")
        else:
            raise TypeError("Непідтримуваний тип даних.")
    except Exception as e:
        return f"Помилка: {str(e)}"

def filter_data(data, predicate):
    try:
        if not callable(predicate):
            raise TypeError("Аргумент 'predicate' має бути функцією.")

        if isinstance(data, list):
            return [x for x in data if predicate(x)]
        elif isinstance(data, tuple):
            return tuple(x for x in data if predicate(x))
        elif isinstance(data, dict):
            return {k: v for k, v in data.items() if predicate((k, v))}
        else:
            raise TypeError("Непідтримуваний тип даних.")
    except Exception as e:
        return f"Помилка: {str(e)}"

def combine_values(*args, separator="", initial=None):
    try:
        if not args:
            return initial

        first = args[0]

        if isinstance(first, (int, float)):
            result = initial if initial is not None else 0
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise TypeError("Усі аргументи мають бути числовими.")
                result += arg
            return result

        elif isinstance(first, str):
            result = initial if initial is not None else ""
            str_args = [str(arg) for arg in args]
            return separator.join([result] + str_args if result else str_args)

        else:
            raise TypeError("Непідтримуваний тип першого аргументу.")
    except Exception as e:
        return f"Помилка: {str(e)}"

print("=== process_data ===")
print(process_data([1, 2, 3], lambda x: x * 2))
print(process_data((1, 2, 3), lambda x: x + 1))
print(process_data({'a': 1, 'b': 2}, lambda x: x * 10, target="values"))
print(process_data({'a': 1, 'b': 2}, lambda x: x.upper(), target="keys"))

print("\n=== filter_data ===")
print(filter_data([1, 2, 3, 4], lambda x: x % 2 == 0))
print(filter_data((5, 6, 7), lambda x: x > 5))
print(filter_data({'a': 1, 'b': 2}, lambda x: x[1] > 1))

print("\n=== combine_values ===")
print(combine_values(1, 2, 3, 4))
print(combine_values("a", "b", "c", separator="-"))
print(combine_values("x", "y", "z", separator=",", initial="start"))
print(combine_values(10, 20, 30, initial=5))
