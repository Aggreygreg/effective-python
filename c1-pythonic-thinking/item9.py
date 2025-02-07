# Item 9: Avoid else Blocks After for and while Loops

# Example 1: Else block runs after the loop completes normally
for i in range(3):
    print('Loop', i)
else:
    print('Else block!')

# Example 2: Else block is skipped when a break statement is encountered
for i in range(3):
    print('Loop', i)
    if i == 1:
        break
else:
    print('Else block!')

# Example 3: Else block runs when the loop is empty
for x in []:
    print('Never runs')
else:
    print('For Else block!')

# Example 4: Else block runs when the while condition is initially False
while False:
    print('Never runs')
else:
    print('While Else block!')

# Example 5: Using else in a loop to check if two numbers are coprime
a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')

# Alternative 1: Early return style for checking coprimality
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False  # Not coprime
    return True  # Coprime

# Test cases
assert coprime(4, 9)  # True
assert not coprime(3, 6)  # False

# Alternative 2: Using a flag variable for checking coprimality
def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

# Test cases
assert coprime_alternate(4, 9)  # True
assert not coprime_alternate(3, 6)  # False
