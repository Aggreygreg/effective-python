# Item 10: Prevent Repetition with Assignment Expressions
# Examples demonstrating how the walrus operator (:=) can reduce redundancy
# and improve readability in Python code.

# Example 1: Checking inventory for lemonade
fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5
}

def make_lemonade(count):
    print(f"Making lemonade with {count} lemons.")

def out_of_stock():
    print("Out of stock!")

# Using walrus operator to check inventory and act accordingly
if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

# Example 2: Checking inventory for cider
def make_cider(count):
    print(f"Making cider with {count} apples.")

# Using walrus operator with a comparison
if (count := fresh_fruit.get('apple', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()

# Example 3: Splitting variable assignment based on condition
def slice_bananas(count):
    print(f"Slicing {count} bananas.")
    return count * 2

class OutOfBananas(Exception):
    pass

def make_smoothies(pieces):
    print(f"Making smoothies with {pieces} pieces of banana.")
    if pieces < 4:
        raise OutOfBananas

try:
    if (count := fresh_fruit.get('banana', 0)) >= 2:
        pieces = slice_bananas(count)
    else:
        pieces = 0
    make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

# Example 4: Simplifying nested conditionals for juice precedence
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('apple', 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get('lemon', 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = "Nothing"
print(f"Customer gets: {to_enjoy}")

# Example 5: Using the walrus operator to emulate a do/while loop

def pick_fruit():
    from random import randint, choice
    fruits = ['apple', 'banana', 'lemon']
    return {choice(fruits): randint(0, 5) for _ in range(2)} if randint(0, 1) else {}

def make_juice(fruit, count):
    print(f"Making juice with {count} {fruit}(s).")
    return [f"{fruit} juice bottle {i + 1}" for i in range(count)]

bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print("Bottled juices:", bottles)
