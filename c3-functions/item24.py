# Item 24: Use None and Docstrings to Specify Dynamic Default Arguments

from time import sleep
from datetime import datetime
import json
from typing import Optional

def log(message, when=None):
    """Log a message with a timestamp.
    
    Args:
        message: Message to print.
        when: datetime of when the message occurred.
              Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

# Example usage
log('Hi there!')
sleep(0.1)
log('Hello again!')

def decode(data, default=None):
    """Load JSON data from a string.
    
    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
                 Defaults to an empty dictionary.
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default

# Example usage
foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
assert foo is not bar

def log_typed(message: str, when: Optional[datetime] = None) -> None:
    """Log a message with a timestamp.
    
    Args:
        message: Message to print.
        when: datetime of when the message occurred.
              Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')
