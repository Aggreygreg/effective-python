# Item 15: Be Cautious When Relying on dict Insertion Ordering

# Python 3.5 and earlier: Dictionary iteration order was arbitrary
baby_names_old = {'cat': 'kitten', 'dog': 'puppy'}
print(baby_names_old)  # Output order may vary

# Python 3.7+: Dictionaries preserve insertion order
baby_names = {
    'cat': 'kitten',
    'dog': 'puppy',
}
print(baby_names)  # Output: {'cat': 'kitten', 'dog': 'puppy'}

# Demonstrating iteration order consistency
print(list(baby_names.keys()))    # ['cat', 'dog']
print(list(baby_names.values()))  # ['kitten', 'puppy']
print(list(baby_names.items()))   # [('cat', 'kitten'), ('dog', 'puppy')]
print(baby_names.popitem())       # ('dog', 'puppy') - Last item inserted

# Keyword arguments now maintain order

def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

my_func(goose='gosling', kangaroo='joey')  # Order is preserved

# Class attributes preserve order
class MyClass:
    def __init__(self):
        self.alligator = 'hatchling'
        self.elephant = 'calf'

a = MyClass()
for key, value in a.__dict__.items():
    print(f'{key} = {value}')  # Order of assignment is preserved

# Handling custom dictionary-like objects
from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(sorted(self.data.keys()))

    def __len__(self):
        return len(self.data)

votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)

def get_winner(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name

winner = get_winner(sorted_ranks)
print(winner)  # Correctly identifies 'otter' as the winner

# Type safety enforcement using annotations
from typing import Dict, MutableMapping

def get_winner_safe(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))

try:
    get_winner_safe(sorted_ranks)  # This will trigger a static type check error in mypy
except TypeError as e:
    print(e)

# ___Didn't get it all___