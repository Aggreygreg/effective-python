# Item 8: Use zip to Process Iterators in Parallel: zip() and itertools.zip_longest()

# Using a list comprehension to derive a list of counts from names
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
print(counts)

# Iterating over lists in parallel using indexing
longest_name = None
max_count = 0
for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count
print(longest_name)

#  Using enumerate to slightly improve readability 
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

#  Using zip for cleaner parallel iteration
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count
print(longest_name)

# zip truncates to the shortest iterator 
# (Here, names' updated but counts is not)
names.append('Rosalind')
for name, count in zip(names, counts):
    print(name)

# Using itertools.zip_longest for iterators of unequal lengths
import itertools
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')
