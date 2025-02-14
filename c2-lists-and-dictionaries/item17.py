# Prefer defaultdict Over setdefault to Handle Missing items in Internal state

from collections import defaultdict

# Dictionary mapping country names to sets of visited cities
visits = {
    'Mexico': {'Tulum', 'Puerto Vallarta'},
    'Japan': {'Hakone'},
}

# Using setdefault to add a new city to a country's set
visits.setdefault('France', set()).add('Arles')  # Short

# Using get with an assignment expression (available since Python 3.8)
if (japan := visits.get('Japan')) is None:  # Long
    visits['Japan'] = japan = set()
japan.add('Kyoto')

print(visits)
# Output:
# {'Mexico': {'Tulum', 'Puerto Vallarta'},
#  'Japan': {'Kyoto', 'Hakone'},
#  'France': {'Arles'}}


# Defining a class to manage visits using a dictionary
class Visits:
    def __init__(self):
        self.data = {}  # Initialize an empty dictionary

    def add(self, country, city):
        # Use setdefault to ensure a set exists for the country
        city_set = self.data.setdefault(country, set())
        city_set.add(city)

# Example usage of the Visits class
visits = Visits()
visits.add('Russia', 'Yekaterinburg')
visits.add('Tanzania', 'Zanzibar')

print(visits.data) # {'Russia': {'Yekaterinburg'}, 'Tanzania': {'Zanzibar'}}


# Improving the Visits class with defaultdict
class ImprovedVisits:
    def __init__(self):
        self.data = defaultdict(set)  # Using defaultdict to handle missing keys

    def add(self, country, city):
        self.data[country].add(city)  # No need for setdefault anymore

# Example usage of the ImprovedVisits class
visits = ImprovedVisits()
visits.add('England', 'Bath')
visits.add('England', 'London')

print(visits.data)
# Output:
# defaultdict(<class 'set'>, {'England': {'London', 'Bath'}})
