# Item 5: Write Helper Functions Instead of Complex Expressions

# This script demonstrates the importance of using helper functions 
# instead of complex one-liner expressions to improve readability 
# and maintainability in Python code.


from urllib.parse import parse_qs

# Example query string decoding
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))
# Output:
# {'red': ['5'], 'blue': ['0'], 'green': ['']}

# Accessing values with default handling for missing or blank values
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print(f'Red: {red!r}')
print(f'Green: {green!r}')
print(f'Opacity: {opacity!r}')


# Converting values to integers
red = int(my_values.get('red', [''])[0] or 0)

# Using a ternary expression for improved readability
green_str = my_values.get('green', [''])
green = int(green_str[0]) if green_str[0] else 0

# Using a full if/else statement for even better readability
opacity_str = my_values.get('opacity', [''])
if opacity_str[0]:
    opacity = int(opacity_str[0])
else:
    opacity = 0

# Encapsulating the logic in a helper function
def get_first_int(values, key, default=0):
    """
    Get the first integer value for a given key in the dictionary.

    Args:
        values (dict): Dictionary with key-value pairs.
        key (str): Key to search for in the dictionary.
        default (int, optional): Default value if the key is missing or invalid. Defaults to 0.

    Returns:
        int: The integer value for the given key or the default value.
    """
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

# Using the helper function for clarity and reusability
red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
opacity = get_first_int(my_values, 'opacity')

print(f'Red: {red}')
print(f'Green: {green}')
print(f'Opacity: {opacity}')
# Output:
# Red: 5
# Green: 0
# Opacity: 0    