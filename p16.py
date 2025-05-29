from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def update_content(self, new_content):
        self.content = new_content


class BookDisplayer:
    @staticmethod
    def display(book: Book):
        print(f"{book.title} by {book.author}")
        print(book.content)


class BookStorage:
    @staticmethod
    def save_to_file(book: Book, filename):
        with open(filename, 'w') as f:
            f.write(f"{book.title} by {book.author}\n{book.content}")

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of ${amount:.2f}")


class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}")


class CryptoPayment(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing cryptocurrency payment of ${amount:.2f}")


def make_payment(payment_method: PaymentProcessor, amount: float):
    payment_method.process_payment(amount)

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending email: {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending SMS: {message}")


class PushNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending push notification: {message}")


class EventAlert:
    def __init__(self, notifiers: list[Notifier]):
        self.notifiers = notifiers

    def notify_all(self, message: str):
        for notifier in self.notifiers:
            notifier.send(message)

if __name__ == "__main__":
    book = Book("1984", "George Orwell", "It was a bright cold day in April...")
    BookDisplayer.display(book)
    book.update_content("It was a dark and stormy night...")
    BookStorage.save_to_file(book, "book.txt")

    print("\n---\n")

    make_payment(CreditCardPayment(), 100)
    make_payment(PayPalPayment(), 55.5)
    make_payment(CryptoPayment(), 999.99)

    print("\n---\n")

    notifiers = [EmailNotifier(), SMSNotifier(), PushNotifier()]
    alert = EventAlert(notifiers)
    alert.notify_all("System update scheduled for 3:00 AM.")
