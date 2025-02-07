# Item 13: Prefer Catch-All Unpacking Over Slicing

# Example 1: Basic unpacking causing an exception
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)

# Uncommenting the following line raises an error:
# oldest, second_oldest = car_ages_descending
# ValueError: too many values to unpack (expected 2)

# Example 2: Using slicing (error-prone and verbose)
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)  # Output: 20 19 [15, 9, 8, 7, 6, 4, 1, 0]

# Example 3: Using catch-all unpacking
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)  # Output: 20 19 [15, 9, 8, 7, 6, 4, 1, 0]

# Example 4: Starred expression in different positions
oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)  # Output: 20 0 [19, 15, 9, 8, 7, 6, 4, 1]

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)  # Output: 0 1 [20, 19, 15, 9, 8, 7, 6, 4]

# Example 5: Invalid starred expressions
# Uncommenting the following lines raises SyntaxError:
# *others = car_ages_descending
# first, *middle, *second_middle, last = [1, 2, 3, 4]

# Example 6: Multiple starred expressions in a multilevel structure
car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova'),
}
((loc1, (best1, *rest1)), (loc2, (best2, *rest2))) = car_inventory.items()
print(f'Best at {loc1} is {best1}, {len(rest1)} others')  # Output: Best at Downtown is Silver Shadow, 2 others
print(f'Best at {loc2} is {best2}, {len(rest2)} others')  # Output: Best at Airport is Skyline, 3 others

# Example 7: Starred expressions result in lists
short_list = [1, 2]
first, second, *rest = short_list
print(first, second, rest)  # Output: 1 2 []

# Example 8: Unpacking arbitrary iterators
it = iter(range(1, 3))
first, second = it
print(f'{first} and {second}')  # Output: 1 and 2

# Example 9: Unpacking with a starred expression for an iterator
def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')
    for i in range(200):
        yield (f'Date{i}', f'Make{i}', f'Model{i}', f'Year{i}', f'Price{i}')

it = generate_csv()
header, *rows = it
print('CSV Header:', header)  # Output: CSV Header: ('Date', 'Make', 'Model', 'Year', 'Price')
print('Row count: ', len(rows))  # Output: Row count: 200
