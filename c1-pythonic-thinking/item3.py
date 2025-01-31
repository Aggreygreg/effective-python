# Item 3: Know the Differences Between bytes and str

# Example of bytes and str
bytes_data = b"hello"
str_data = "hello"

# Convert bytes to str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value

print(repr(to_str(bytes_data)))
print(repr(to_str(str_data)))

# Convert str to bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value

print(repr(to_bytes(bytes_data)))
print(repr(to_bytes(str_data)))

# Example of bytes and str operations
print(b"one" + b"two")  # Bytes concatenation
print("one" + "two")  # String concatenation

# File operations with bytes and str
# Writing binary data
with open("data.bin", "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")

# Reading binary data
with open("data.bin", "rb") as f:
    data = f.read()
assert data == b"\xf1\xf2\xf3\xf4\xf5"

# Specifying encoding for text files
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("This is a test.")

with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
assert text == "This is a test."