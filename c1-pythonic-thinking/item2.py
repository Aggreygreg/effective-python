# Item 2: Follow the PEP 8 Style Guide

# Examples of PEP 8 style guidelines
# Whitespace examples:
def example_function(param1, param2):
    result = param1 + param2  # Use spaces around operators
    return result

example_dict = {
    "key1": "value1",
    "key2": "value2",
}  # No spaces before the colon, one space after

# Naming conventions:
class ExampleClass:
    def __init__(self, name):
        self.name = name  # Instance attribute

    def _protected_method(self):
        pass

    def __private_method(self):
        pass

EXAMPLE_CONSTANT = 42

# Expressions and statements:
def check_items(some_list):
    if not some_list:  # Check for empty list
        print("The list is empty.")
    else:
        print("The list is not empty.")

# Imports:
# Good practice - use absolute imports
# from math import sqrt
# import os

# Avoid relative imports unless necessary
# use the explicit syntax from . import foo.