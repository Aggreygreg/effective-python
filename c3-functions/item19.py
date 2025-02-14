# Item 19: Never Unpack More Than Three Variables When Functions Return Multiple Values

from collections import namedtuple

def get_stats(numbers):
    """Calculate statistics for a list of numbers."""
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count
    sorted_numbers = sorted(numbers)
    middle = count // 2
    
    # Compute median based on even or odd count
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
    
    return minimum, maximum, average, median, count

# Sample data
lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

# Unpacking two return values
minimum, maximum = get_stats(lengths)[:2]
print(f'Min: {minimum}, Max: {maximum}')

# Catch-all unpacking with starred expression
def get_avg_ratio(numbers):
    """Return list of ratios relative to average."""
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)
print(f'Longest: {longest:>4.0%}')
print(f'Shortest: {shortest:>4.0%}')

# Returning multiple values with a named tuple for better readability
Stats = namedtuple('Stats', ['minimum', 'maximum', 'average', 'median', 'count'])

def get_stats_namedtuple(numbers):
    """Calculate statistics and return as a named tuple."""
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count
    sorted_numbers = sorted(numbers)
    middle = count // 2
    
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
    
    return Stats(minimum, maximum, average, median, count)

# Using the named tuple approach
stats = get_stats_namedtuple(lengths)
print(f'Min: {stats.minimum}, Max: {stats.maximum}')
print(f'Average: {stats.average}, Median: {stats.median}, Count: {stats.count}')