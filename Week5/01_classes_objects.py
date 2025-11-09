"""
Week 5: Classes and Objects Examples
Topics: Creating classes, __init__, attributes, methods
"""

# Simple class
class Dog:
    """A simple Dog class"""

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

    def info(self):
        return f"{self.name} is a {self.breed}"


print("=== Simple Class ===")
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(dog1.bark())
print(dog2.info())

# Class with class variable
class Car:
    """Car class with class and instance variables"""
    wheels = 4  # Class variable

    def __init__(self, brand, model, year):
        self.brand = brand  # Instance variables
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, distance):
        self.mileage += distance
        return f"{self.brand} {self.model} drove {distance} km"

    def info(self):
        return f"{self.year} {self.brand} {self.model} - {self.mileage} km"


print("\n=== Class and Instance Variables ===")
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

print(f"Car1 wheels: {car1.wheels}")  # Access class variable
print(f"Car2 wheels: {car2.wheels}")

print(car1.drive(100))
print(car1.info())

# Bank Account class
class BankAccount:
    """Bank account with balance management"""

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        if amount > 0:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Invalid withdrawal amount"

    def get_balance(self):
        return f"Current balance: ${self.balance}"


print("\n=== Bank Account Class ===")
account = BankAccount("Alice", 1000)
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
