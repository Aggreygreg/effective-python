# Demonstrating slicing with strides

# Example 1: Basic slicing with positive strides
x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]  # Select every second item starting from the beginning
print("Odds:", odds)  # ['red', 'yellow', 'blue']

evens = x[1::2]  # Select every second item starting from index 1
print("Evens:", evens)  # ['orange', 'green', 'purple']

# Example 2: Reversing a sequence with a negative stride
x = b'mongoose'
y = x[::-1]  # Reverse the sequence
print("Reversed bytes:", y)  # b'esoognom'

# Example 3: Reversing Unicode strings
x = ''
y = x[::-1]  # Reverse the string
print("Reversed Unicode:", y)  # ''

# Example 4: Encoding and decoding with negative strides
w = ''
x = w.encode('utf-8')  # Encode the Unicode string
y = x[::-1]  # Reverse the encoded bytes
try:
    z = y.decode('utf-8')  # Attempt to decode the reversed bytes
except UnicodeDecodeError as e:
    print("Error decoding reversed bytes:", e)

# Example 5: Complex stride behavior
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("Every second item (start to end):", x[::2])  # ['a', 'c', 'e', 'g']
print("Every second item (end to start):", x[::-2])  # ['h', 'f', 'd', 'b']
print("Every second item starting from index 2:", x[2::2])  # ['c', 'e', 'g']
print("Backward slicing with stride -2:", x[-2::-2])  # ['g', 'e', 'c', 'a']
print("Backward slicing with start and end:", x[-2:2:-2])  # ['g', 'e']
print("Empty result due to incompatible slicing:", x[2:2:-2])  # []

# Example 6: Two-step slicing for clarity
y = x[::2]  # First, take every second item
z = y[1:-1]  # Then, slice the result
print("Two-step slicing result:", z)  # ['c', 'e']

# Example 7: Using itertools.islice for efficient slicing
from itertools import islice
result = list(islice(x, 2, None, 2))  # Equivalent to x[2::2]
print("Slicing with itertools.islice:", result)  # ['c', 'e', 'g']
