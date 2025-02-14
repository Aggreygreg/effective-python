# Item 23: Provide Optional Behavior with Keyword Arguments

# Function arguments can be specified by position or keyword
def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6
assert remainder(20, divisor=7) == 6
assert remainder(number=20, divisor=7) == 6
assert remainder(divisor=7, number=20) == 6

# Positional arguments must come before keyword arguments
# remainder(number=20, 7)  # SyntaxError

# Each argument can be specified only once
# remainder(20, number=7)  # TypeError

# Using a dictionary to pass keyword arguments
my_kwargs = {'number': 20, 'divisor': 7}
assert remainder(**my_kwargs) == 6

# Mixing dictionary unpacking with explicit keyword arguments
my_kwargs = {'divisor': 7}
assert remainder(number=20, **my_kwargs) == 6

# Merging multiple dictionaries
my_kwargs = {'number': 20}
other_kwargs = {'divisor': 7}
assert remainder(**my_kwargs, **other_kwargs) == 6

# Function to print all keyword arguments
def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

print_parameters(alpha=1.5, beta=9, gamma=4)

# Function with a default keyword argument
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

weight_diff = 0.5
time_diff = 3
flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)

# Extending a function while maintaining backward compatibility
def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period

pounds_per_hour = flow_rate(weight_diff, time_diff, period=3600, units_per_kg=2.2)

# Always prefer keyword arguments for optional parameters to improve readability
