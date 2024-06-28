"""
File: savingsaccount.py
This module defines the SavingsAccount class.
"""

'''
    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string rep."""
        result =  'Name:    ' + self.name + '\n' 
        result += 'PIN:     ' + self.pin + '\n' 
        result += 'Balance: ' + str(self.balance)
        return result

    def getName(self):
        """Returns the current name."""
        return self.name

'''

class SavingsAccount:

    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    RATE = 0.02    # Single rate for all accounts

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def get_name(self):
        return self.name

    def __str__(self):
        """Returns the string rep."""
        result =  'Name:    ' + self.name + '\n' 
        result += 'PIN:     ' + self.pin + '\n' 
        result += 'Balance: ' + str(self.balance)
        return result

    def getPin(self):
        """Returns the current pin."""
        return self.pin
    
    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def deposit(self, amount):
        """If the amount is valid, adds it
        to the balance and returns None;
        otherwise, returns an error message."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """If the amount is valid, sunstract it
        from the balance and returns None;
        otherwise, returns an error message."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest
    
    def __lt__(self, other):
        return self.name < other.name