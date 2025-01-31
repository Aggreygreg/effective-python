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
# try:
#     reordered_tuple = '%-10s = %.2f' % (value, key)
# except TypeError as e:
#     print(f"Error: {e}")

# Runtime error due to mismatched format string
# try:
#     reordered_string = '%.2f = %-10s' % (key, value)
# except TypeError as e:
#     print(f"Error: {e}")

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
