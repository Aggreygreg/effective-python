# Item 14: Sort by Complex Criteria Using the key Parameter

"""
This script demonstrates how to use the sort method with the key parameter to
sort lists of built-in types and custom objects by different criteria.
"""

# Sorting built-in types
numbers = [93, 86, 11, 68, 70]
numbers.sort()
print("Sorted numbers:", numbers)  # [11, 68, 70, 86, 93]

# Defining a class with no natural ordering
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

# Creating a list of tools
tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25),
]

# Sorting tools by name
tools.sort(key=lambda x: x.name)
print("\nSorted by name:", tools)

# Sorting tools by weight
tools.sort(key=lambda x: x.weight)
print("Sorted by weight:", tools)

# Case-insensitive sorting of strings
places = ['home', 'work', 'New York', 'Paris']
places.sort()
print("\nCase sensitive:", places)
places.sort(key=lambda x: x.lower())
print("Case insensitive:", places)

# Sorting by multiple criteria (first by weight, then by name)
power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]
power_tools.sort(key=lambda x: (x.weight, x.name))
print("\nSorted by weight and name:", power_tools)

# Sorting by descending weight, then ascending name
power_tools.sort(key=lambda x: (-x.weight, x.name))
print("Sorted by descending weight and ascending name:", power_tools)

# Alternative method: sorting in multiple steps
power_tools.sort(key=lambda x: x.name)  # Sort by name first
power_tools.sort(key=lambda x: x.weight, reverse=True)  # Then by weight descending
print("Sorted using multiple sorts:", power_tools)
