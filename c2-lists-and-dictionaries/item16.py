# Item 16: Prefer get Over in and KeyError to Handle Missing Dictionary Keys

# Dictionary to store votes for different types of bread
counters = {
    'pumpernickel': 2, 'sourdough': 1,
}

# Incrementing a counter using an if statement with 'in'
key = 'wheat'
if key in counters:
    count = counters[key]
else:
    count = 0
counters[key] = count + 1

# Incrementing a counter using KeyError exception handling
try:
    count = counters[key]
except KeyError:
    count = 0
counters[key] = count + 1

# Incrementing a counter using the 'get' method
count = counters.get(key, 0)
counters[key] = count + 1

# Alternative approaches that are less readable
dict_methods = [
    ("if key not in counters", "counters[key] = 0\ncounters[key] += 1"),
    ("if key in counters", "counters[key] += 1\nelse:\ncounters[key] = 1"),
    ("try/except", "try:\ncounters[key] += 1\nexcept KeyError:\ncounters[key] = 1")
]

# Using a dictionary to store votes with names instead of counters
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}

key = 'brioche'
who = 'Elmer'

# Handling missing keys using 'in'
if key in votes:
    names = votes[key]
else:
    votes[key] = names = []
names.append(who)
print(votes)

# Handling missing keys using KeyError exception
try:
    names = votes[key]
except KeyError:
    votes[key] = names = []
names.append(who)

# Handling missing keys using 'get'
names = votes.get(key)
if names is None:
    votes[key] = names = []
names.append(who)

# Using an assignment expression (Python 3.8+)
if (names := votes.get(key)) is None:
    votes[key] = names = []
names.append(who)

# Using setdefault
names = votes.setdefault(key, [])
names.append(who)

# Demonstrating the issue with setdefault when dealing with mutable values
data = {}
key = 'foo'
value = []
data.setdefault(key, value)
print('Before:', data)
value.append('hello')
print('After: ', data)

# Using setdefault for counters (inefficient due to extra assignment)
count = counters.setdefault(key, 0)
counters[key] = count + 1
