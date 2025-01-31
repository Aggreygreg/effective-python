# Chapter 1 Practice Code

# Item 1: Know Which Version of Python You’re Using

# Check Python version from the command line:
# $ python --version
# $ python3 --version

# Check Python version at runtime
import sys
print(sys.version_info)
print(sys.version)

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
from math import sqrt
import os

# Avoid relative imports unless necessary

# Item 3: Know the Differences Between bytes and str

# Example of bytes and str
bytes_data = b"hello"
str_data = "hello"

# Convert bytes to str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value

print(repr(to_str(bytes_data)))
print(repr(to_str(str_data)))

# Convert str to bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value

print(repr(to_bytes(bytes_data)))
print(repr(to_bytes(str_data)))

# Example of bytes and str operations
print(b"one" + b"two")  # Bytes concatenation
print("one" + "two")  # String concatenation

# File operations with bytes and str
# Writing binary data
with open("data.bin", "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")

# Reading binary data
with open("data.bin", "rb") as f:
    data = f.read()
assert data == b"\xf1\xf2\xf3\xf4\xf5"

# Specifying encoding for text files
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("This is a test.")

with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
assert text == "This is a test."

# Item 4: Prefer Interpolated F-Strings

# Example 1: C-style format strings
# Convert binary and hexadecimal values to integer strings using % operator
a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))

# Example 2: Issues with C-style formatting
key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted)

# Runtime error due to type mismatch
try:
    reordered_tuple = '%-10s = %.2f' % (value, key)
except TypeError as e:
    print(f"Error: {e}")

# Runtime error due to mismatched format string
try:
    reordered_string = '%.2f = %-10s' % (key, value)
except TypeError as e:
    print(f"Error: {e}")

# Example 3: Long tuples with inline modifications
pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15),
]

for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))

# Adding modifications
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count)))

# Example 4: Repeated values in C-style formatting
template = '%s loves food. See %s cook.'
name = 'Max'
formatted = template % (name, name)
print(formatted)

# Using dictionary for C-style formatting
key = 'my_var'
value = 1.234
old_way = '%-10s = %.2f' % (key, value)
new_way = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}
assert old_way == new_way

# Multiple references to the same value
name = 'Max'
template = '%(name)s loves food. See %(name)s cook.'
formatted = template % {'name': name}
print(formatted)

# Example 5: Advanced formatting with str.format
key = 'my_var'
value = 1.234
formatted = '{} = {}'.format(key, value)
print(formatted)
formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)

# Example with positional indices
formatted = '{1} = {0}'.format(key, value)
print(formatted)

# Repeated value references
formatted = '{0} loves food. See {0} cook.'.format(name)
print(formatted)

# Example with dictionaries
menu = {
    'soup': 'lentil',
    'oyster': 'kumamoto',
    'special': 'schnitzel',
}
new_template = (
    'Today\'s soup is {soup}, '
    'buy one get two {oyster} oysters, '
    'and our special entrée is {special}.')
formatted = new_template.format(**menu)
print(formatted)

# Example 6: F-strings
key = 'my_var'
value = 1.234
formatted = f'{key} = {value}'
print(formatted)

# F-string with format specifiers
formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

# F-strings are shorter and clearer
f_string = f'{key:<10} = {value:.2f}'
c_tuple = '%-10s = %.2f' % (key, value)
str_args = '{:<10} = {:.2f}'.format(key, value)
str_kw = '{key:<10} = {value:.2f}'.format(key=key, value=value)
c_dict = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}
assert c_tuple == c_dict == f_string
assert str_args == str_kw == f_string

# F-string with inline modifications
for i, (item, count) in enumerate(pantry):
    f_string = f'#{i+1}: {item.title():<10s} = {round(count)}'
    print(f_string)

# Multi-line F-strings
for i, (item, count) in enumerate(pantry):
    print(f'#{i+1}: '
          f'{item.title():<10s} = '
          f'{round(count)}')

# Dynamic formatting with expressions in F-strings
places = 3
number = 1.23456
print(f'My number is {number:.{places}f}')
