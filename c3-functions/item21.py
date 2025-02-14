# Item 21: Know How Closures Interact with Variable Scope

def sort_priority(values, group):
    """Sorts values, placing group elements first."""
    def helper(x):
        if x in group:
            return (0, x)  # Prioritize elements in the group
        return (1, x)  # Others come later
    values.sort(key=helper)

# Example usage
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)  # [2, 3, 5, 7, 1, 4, 6, 8]


def sort_priority2(numbers, group):
    """Attempts to track whether group elements were found (but fails)."""
    found = False  # This variable won't be modified correctly in closure
    
    def helper(x):
        if x in group:
            found = True  # Creates a new local 'found', doesn't modify outer one
            return (0, x)
        return (1, x)
    
    numbers.sort(key=helper)
    return found  # Always False due to scoping rules

# Example usage
found = sort_priority2(numbers, group)
print('Found:', found)  # Incorrectly prints False


def sort_priority3(numbers, group):
    """Corrects scoping issue using nonlocal."""
    found = False
    
    def helper(x):
        nonlocal found  # Now correctly modifies found in enclosing scope
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    
    numbers.sort(key=helper)
    return found

# Example usage
found = sort_priority3(numbers, group)
print('Found:', found)  # Correctly prints True


class Sorter:
    """Uses a class to encapsulate sorting state, avoiding nonlocal."""
    def __init__(self, group):
        self.group = group
        self.found = False
    
    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

# Example usage
sorter = Sorter(group)
numbers.sort(key=sorter)
print('Found:', sorter.found)  # Correctly prints True
