# def careful_divide(a, b): 
#     try:
#         return True, a / b
#     except ZeroDivisionError:
#         return False, None

# success, result = careful_divide(0, 5)
# print(success, result)
# if not success:
#     print('Invalid inputs')  # This runs, but shouldn't!

# def careful_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as e:
#         raise ValueError('Invalid inputs')
# x, y = 0, 5
# try:
#     result = careful_divide(x, y)
# except ValueError:
#     print('Invalid inputs')
# else:
#     print(f'Result is {result}')     

def careful_divide(a: float, b: float) -> float:
    """Divides a by b.
    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')
x, y = 5, 0
try:
    result = careful_divide(x, y)
except ValueError:
    print(f'Invalid inputs: {y}')
else:
    print(f'The result is {result}')