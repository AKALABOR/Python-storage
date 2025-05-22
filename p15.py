class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def get_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Місто: {self.city}"

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def get_full_info(self):
        return f"{self.year} {self.brand} {self.model}, Колір: {self.color}"

    def change_color(self, new_color):
        self.color = new_color
        print(f"Колір змінено на {self.color}")

class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Поповнено: {amount} грн")
        else:
            print("Сума поповнення має бути більшою за 0.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Знято: {amount} грн")
        else:
            print("Недостатньо коштів на рахунку.")

    def check_balance(self):
        return f"Баланс рахунку {self.account_number}: {self.balance} грн"

person1 = Person("Олена", 30, "Київ")
print(person1.get_info())

car1 = Car("Toyota", "Camry", 2020, "Чорний")
print(car1.get_full_info())
car1.change_color("Білий")
print(car1.get_full_info())

account1 = BankAccount("Іван Петренко", "UA1234567890", 1000)
print(account1.check_balance())
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)
print(account1.check_balance())
