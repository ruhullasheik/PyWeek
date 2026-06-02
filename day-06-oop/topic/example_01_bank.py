"""Example 1: Bank Account with Property Validation

Demonstrates @property for validation.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance

    def __str__(self):
        return f"{self.owner}: ${self._balance:.2f}"


acc = BankAccount("Alice", 1000)
print(acc)
acc.deposit(500)
print(acc)
acc.withdraw(200)
print(acc)
# acc.withdraw(2000)  # Would raise ValueError
