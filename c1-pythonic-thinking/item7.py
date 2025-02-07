# Item 7: Prefer enumerate Over range 

# Example of using range to iterate over indices and modify random bits
from random import randint

random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i
print("Random bits:", bin(random_bits))  # Example output: 0b11101000100100000111000010000001

# Iterating directly over a list of strings
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print(f'{flavor} is delicious')

# Using range to loop over indices and access list elements
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1}: {flavor}')

# Using enumerate to loop over indices and values
for i, flavor in enumerate(flavor_list):
    print(f'{i + 1}: {flavor}')

# Using enumerate with a custom start index
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')
