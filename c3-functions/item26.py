# Item 26: Define Function Decorators with functools.wraps

from functools import wraps

def trace(func):
    """Decorator that prints function calls with arguments and return values."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number."""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

# Example usage
if __name__ == "__main__":
    print(fibonacci(4))
