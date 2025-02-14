# Item 20: Prefer Raising Exceptions to Returning None

def careful_divide(a, b):
    """Divides a by b, returning None when division is undefined."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Example usage
x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('Invalid inputs')

# Issue: Misinterpreting None as False in conditionals
x, y = 0, 5
result = careful_divide(x, y)
if not result:
    print('Invalid inputs')  # Incorrectly triggers because result is 0

# Solution 1: Return a tuple indicating success

def careful_divide_v2(a, b):
    """Returns a tuple (success, result), where success is a boolean."""
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

# Using tuple unpacking to ensure proper handling
success, result = careful_divide_v2(x, y)
if not success:
    print('Invalid inputs')

# Potential issue: Callers might ignore the success flag
_, result = careful_divide_v2(x, y)
if not result:
    print('Invalid inputs')  # Same issue as before

# Solution 2: Raise exceptions instead of returning None

def careful_divide_v3(a, b):
    """Divides a by b.
    Raises:
        ValueError: If division is undefined (b == 0)
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')

# Proper exception handling
x, y = 5, 2
try:
    result = careful_divide_v3(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print(f'Result is {result:.1f}')

# Solution 3: Use type annotations to clarify expected behavior
from typing import Any

def careful_divide_v4(a: float, b: float) -> float:
    """Divides a by b, never returning None.
    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')
