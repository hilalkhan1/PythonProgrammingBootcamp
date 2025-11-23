"""
Week 6: Encapsulation Examples
Topics: Private attributes, @property, getters/setters
"""

class BankAccount:
    """Demonstrates encapsulation with private attributes"""

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute

    @property
    def balance(self):
        """Getter for balance"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter with validation"""
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}"
        return "Invalid amount"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds!"
        if amount > 0:
            self.__balance -= amount
            return f"Withdrew ${amount}"
        return "Invalid amount"


print("=== Encapsulation with @property ===")
account = BankAccount("Alice", 1000)
print(f"Balance: ${account.balance}")
print(account.deposit(500))
print(f"New Balance: ${account.balance}")

# Cannot directly modify private attribute
# account.__balance = 5000  # This won't work
