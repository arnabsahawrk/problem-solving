"""
STRING - Immutable Sequence
============================
Cannot be modified after creation
"""

# CREATION
s = "Hello World"
s = 'Hello World'
s = """Multi
line"""

# ACCESSING
first = s[0]  # 'H' - O(1)
last = s[-1]  # 'd'
# s[0] = 'h'  # ERROR - immutable!

# SLICING
s = "Hello World"
sub = s[0:5]  # "Hello"
sub = s[:5]  # "Hello"
sub = s[6:]  # "World"
sub = s[::2]  # "HloWrd" - every 2nd char
sub = s[::-1]  # "dlroW olleH" - reverse

# CONCATENATION
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2  # "Hello World"
result = s1 * 3  # "HelloHelloHello"

# JOIN (efficient for multiple strings)
words = ["Hello", "World"]
result = " ".join(words)  # "Hello World"
result = "".join(words)  # "HelloWorld"

# CASE
s.lower()  # "hello world"
s.upper()  # "HELLO WORLD"
s.title()  # "Hello World"
s.capitalize()  # "Hello world"

# STRIP (remove whitespace)
s = "  hello  "
s.strip()  # "hello"
s.lstrip()  # "hello  "
s.rstrip()  # "  hello"

# REPLACE
s.replace("World", "Python")  # O(n)
s.replace("l", "L", 1)  # replace first only

# SPLIT/JOIN
s = "a,b,c"
parts = s.split(",")  # ["a", "b", "c"]
words = "hello  world".split()  # split by whitespace

joined = "-".join(parts)  # "a-b-c"

# SEARCH
s = "Hello World"
idx = s.find("World")  # 6 (returns -1 if not found)
idx = s.index("World")  # 6 (raises error if not found)
count = s.count("l")  # 3

# CHECKING
s.startswith("Hello")  # True
s.endswith("World")  # True
s.isalpha()  # all letters?
s.isdigit()  # all digits?
s.isalnum()  # alphanumeric?
s.isspace()  # all whitespace?

if "World" in s:  # O(n)
    pass

# FORMATTING (f-strings recommended)
name = "Alice"
age = 25
s = f"Name: {name}, Age: {age}"
s = f"Math: {5 + 3}"  # "Math: 8"
s = f"{3.14159:.2f}"  # "3.14"

# STRING BUILDING (efficient way)
# BAD: result = ""; result += char (O(n²))
# GOOD: use list + join
chars = []
for c in "hello":
    chars.append(c.upper())
result = "".join(chars)  # "HELLO"

# CP TRICKS
# Reverse
rev = s[::-1]

# Palindrome check
is_pal = s == s[::-1]

# Character frequency
from collections import Counter
freq = Counter("hello")  # {'h':1, 'e':1, 'l':2, 'o':1}

# Remove vowels
no_vowels = "".join(c for c in s if c not in "aeiou")

# Anagram check
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# TIME COMPLEXITY
# Access: O(1)
# Concatenation: O(n+m)
# Search: O(n*m) where m is pattern
# Slice: O(k)
# Split/Join: O(n)
