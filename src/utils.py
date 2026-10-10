"""Calculator utility functions for the Git practice project."""


def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Calculator inputs must be numbers.")


def add(a, b):
    validate_numbers(a, b)
    return a + b


def subtract(a, b):
    validate_numbers(a, b)
    return a - b


def multiply(a, b):
    validate_numbers(a, b)
    return a * b


def divide(a, b):
    validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
