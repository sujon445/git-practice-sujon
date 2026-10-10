def validate_numbers(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Inputs must be numbers, not booleans.")

    if not isinstance(a, (int, float)):
        raise TypeError("First input must be a number.")

    if not isinstance(b, (int, float)):
        raise TypeError("Second input must be a number.")


def add(a, b):
    validate_numbers(a, b)
    return a + b


def subtract(a, b):
    validate_numbers(a, b)
    return a - b


def multiply(a, b):
    validate_numbers(a, b)
    return a * b