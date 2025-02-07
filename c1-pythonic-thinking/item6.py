# Item 6: Prefer Multiple Assignment Unpacking Over Indexing

# Example 1: Accessing tuple values with unpacking
item = ('Peanut butter', 'Jelly')
first, second = item  # Unpacking
print(f"{first} and {second}")  # Output: Peanut butter and Jelly

# Example 2: Complex unpacking within nested iterables
favorite_snacks = {
    'salty': ('pretzels', 100),
    'sweet': ('cookies', 180),
    'veggie': ('carrots', 20),
}
((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items()

print(f"Favorite {type1} is {name1} with {cals1} calories")
print(f"Favorite {type2} is {name2} with {cals2} calories")
print(f"Favorite {type3} is {name3} with {cals3} calories")

# Example 3: Swapping values using unpacking
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]  # Swap

names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)

# Example 4: Using unpacking in loops
snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for rank, (name, calories) in enumerate(snacks, 1):
    print(f"#{rank}: {name} has {calories} calories")


