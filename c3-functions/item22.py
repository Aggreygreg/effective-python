# Item 22: Reduce Visual Noise with Variable Positional Arguments

def log(message, *values):  # Using *args to allow variable arguments
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

# Example usage
log('My numbers are', 1, 2)
log('Hi there')

# Using * to unpack a list into arguments
favorites = [7, 33, 99]
log('Favorite numbers', *favorites)

# Potential memory issue with generator unpacking

def my_generator():
    for i in range(10):
        yield i

it = my_generator()
log('Generated numbers', *it)  # Be cautious when using * with generators

# Issue when adding a new positional argument before *args

def log_with_sequence(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {values_str}')

log_with_sequence(1, 'Favorites', 7, 33)
log_with_sequence(1, 'Hi there')
# log_with_sequence('Favorite numbers', 7, 33)  # This would cause incorrect behavior
