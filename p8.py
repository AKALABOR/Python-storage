multiples = [n for n in range(1, 101) if n % 3 == 0 and n % 5 != 0]
print(multiples)

celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(fahrenheit)

even_squares = [n**2 for n in range(1, 51) if n % 2 == 0]
print(even_squares)

text = "Python is amazing and powerful language"
lengths = [len(word) for word in text.split()]
print(lengths)

composites = [n for n in range(1, 101) if n > 1 and len([d for d in range(2, n) if n % d == 0]) > 0]
print(composites)
