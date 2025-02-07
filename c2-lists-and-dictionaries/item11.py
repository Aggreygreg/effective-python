# item11.py: How ro slice sequences in Python

# Example sequence
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Basic slicing
print('Middle two:', a[3:5])            # ['d', 'e']
print('All but ends:', a[1:7])         # ['b', 'c', 'd', 'e', 'f', 'g']

# Slicing without 0 or len(a) for cleaner code
assert a[:5] == a[0:5]                # Equivalent to a[0:5]
assert a[5:] == a[5:len(a)]           # Equivalent to a[5:]

# Slicing with negative indexes
actions = [
    (a[:], "a[:]"),                    # Full copy of the list
    (a[:5], "a[:5]"),                  # First 5 elements
    (a[:-1], "a[:-1]"),                # All except the last element
    (a[4:], "a[4:]"),                  # All elements from index 4 to end
    (a[-3:], "a[-3:]"),                # Last 3 elements
    (a[2:5], "a[2:5]"),                # Elements from index 2 to 4
    (a[2:-1], "a[2:-1]"),              # Elements from index 2 to second-to-last
    (a[-3:-1], "a[-3:-1]")             # Second-to-last 2 elements
]
for result, desc in actions:
    print(f"{desc}: {result}")

# Slicing out of bounds
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
first_twenty_items = a[:20]           # Works fine, omits missing items
last_twenty_items = a[-20:]           # Works fine, omits missing items
print('First 20:', first_twenty_items)
print('Last 20:', last_twenty_items)

# Direct access beyond bounds raises an error
try:
    print(a[20])
except IndexError as e:
    print('IndexError:', e)

# Modifying slices does not affect the original list
b = a[3:]
print('Before:', b)
b[1] = 99
print('After:', b)
print('No change in original:', a)

# Assigning to slices modifies the original list
print('Before:', a)
a[2:7] = [99, 22, 14]                # Shrinks the list
print('After shrinking:', a)
a[2:3] = [47, 11]                    # Grows the list
print('After growing:', a)

# Copying lists with slices
b = a[:]
assert b == a and b is not a          # New list but identical contents

# Assigning to full slice replaces the entire list
print('Before a:', a)
print('Before b:', b)
a[:] = [101, 102, 103]               # Replaces the list contents
assert a is b                        # a and b are still the same object
print('After a:', a)
print('After b:', b)
