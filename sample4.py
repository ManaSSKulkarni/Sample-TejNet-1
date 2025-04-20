"""SAMPLE CODING FILE"""


def concatenation(str1, str2):
    """Adds two strings"""
    return str1 + str2


def reverse_array(arr):
    """Reversing an Array"""
    return arr[::-1]


def add(a, b):
    """Adding two numbers"""
    return a + b


class Calculator:
    """Calculator Class"""

    def square(self, num):
        """Squaring a number"""
        return num**2

    def add(self, a, b):
        """Addition"""
        return a + b

    def subtract(self, a, b):
        """Subtraction"""
        return a - b

    def multiply(self, a, b):
        """Multiplication"""
        return a * b

    def divide(self, a, b):
        """Division"""
        if b == 0:
            raise ValueError("Division by zero")
        return a // b


print(concatenation("Hello ", "World"))
