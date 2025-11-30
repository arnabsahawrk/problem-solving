"""
PYTHON SYNTAX QUICK REFERENCE
==============================
Common syntax patterns for CP
"""

# LIST COMPREHENSION
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
matrix = [[0] * n for _ in range(m)]

# DICT COMPREHENSION
squares = {x: x**2 for x in range(5)}
filtered = {k: v for k, v in d.items() if v > 20}

# SET COMPREHENSION
unique = {x for x in lst}

# UNPACKING
a, b = (1, 2)
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2,3,4]
first, *mid, last = [1, 2, 3, 4, 5]
a, b = b, a  # swap

# ENUMERATE
for i, val in enumerate(lst):
    print(i, val)

for i, val in enumerate(lst, start=1):  # start from 1
    print(i, val)

# ZIP
names = ["Alice", "Bob"]
scores = [85, 90]
for name, score in zip(names, scores):
    print(name, score)

# Unzip
pairs = [("Alice", 85), ("Bob", 90)]
names, scores = zip(*pairs)

# RANGE
range(5)  # 0, 1, 2, 3, 4
range(2, 5)  # 2, 3, 4
range(0, 10, 2)  # 0, 2, 4, 6, 8
range(5, 0, -1)  # 5, 4, 3, 2, 1

# SORTING
lst.sort()  # in-place
sorted_lst = sorted(lst)  # new list
lst.sort(key=lambda x: -x)  # descending
lst.sort(key=abs)  # by absolute value
lst.sort(key=len)  # by length

# FILTER & MAP
evens = list(filter(lambda x: x % 2 == 0, lst))
squares = list(map(lambda x: x**2, lst))

# ANY & ALL
any([True, False, False])  # True - at least one
all([True, True, False])  # False - not all
any(x > 0 for x in lst)  # at least one positive
all(x > 0 for x in lst)  # all positive

# MIN & MAX
min(lst)
max(lst)
min(lst, key=abs)  # by absolute value
max(words, key=len)  # longest word

# SUM
sum(lst)
sum(lst, 10)  # start from 10

# REVERSED
for x in reversed(lst):
    print(x)
rev_lst = list(reversed(lst))
rev_lst = lst[::-1]  # same

# COMPARISON OPERATORS
==  # equal
!=  # not equal
<, >, <=, >=
is  # identity (same object)
in  # membership

# LOGICAL OPERATORS
and, or, not

# CONDITIONAL EXPRESSION
result = a if condition else b

# CHAINED COMPARISON
if 0 < x < 10:
    pass

# MULTIPLE ASSIGNMENT
x = y = z = 0

# LAMBDA
add = lambda x, y: x + y
square = lambda x: x**2

# STRING FORMATTING
# f-strings (best)
s = f"Value: {x}"
s = f"{x:.2f}"  # 2 decimal places

# format method
s = "Value: {}".format(x)
s = "Values: {}, {}".format(x, y)

# % operator (old)
s = "Value: %d" % x
s = "Values: %d, %s" % (x, name)

# SLICING
lst[start:end]  # start to end-1
lst[start:]  # start to end
lst[:end]  # beginning to end-1
lst[::step]  # every step-th element
lst[::-1]  # reverse
lst[start:end:step]

# MEMBERSHIP
if x in lst:
    pass
if x not in lst:
    pass

# IDENTITY
if x is None:
    pass
if x is not None:
    pass

# WALRUS OPERATOR (3.8+)
if (n := len(lst)) > 10:
    print(f"Length {n} is too long")

# LIST METHODS
lst.append(x)  # add to end
lst.extend([1, 2])  # add multiple
lst.insert(0, x)  # insert at index
lst.remove(x)  # remove first occurrence
lst.pop()  # remove and return last
lst.pop(0)  # remove at index
lst.clear()  # remove all
lst.reverse()  # reverse in-place
lst.sort()  # sort in-place
lst.count(x)  # count occurrences
lst.index(x)  # find first index

# STRING METHODS
s.lower(), s.upper()
s.strip(), s.lstrip(), s.rstrip()
s.split(), s.split(',')
'-'.join(lst)
s.replace(old, new)
s.startswith(prefix)
s.endswith(suffix)
s.find(sub)  # returns -1 if not found
s.index(sub)  # raises error if not found
s.count(sub)
s.isalpha(), s.isdigit(), s.isalnum()

# DICT METHODS
d[key] = value
d.get(key, default)
d.pop(key)
del d[key]
d.clear()
d.keys(), d.values(), d.items()
d.update({key: value})

# SET METHODS
s.add(x)
s.remove(x)  # KeyError if not found
s.discard(x)  # no error
s.pop()  # remove arbitrary
s.clear()
a | b  # union
a & b  # intersection
a - b  # difference
a ^ b  # symmetric difference

# GENERATORS
gen = (x**2 for x in range(10))  # generator expression
for val in gen:
    print(val)

# EXCEPTION HANDLING
try:
    result = x / y
except ZeroDivisionError:
    result = 0
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Always runs")

# ASSERTIONS
assert x > 0, "x must be positive"

# TYPE HINTS (optional, for clarity)
def func(x: int, y: str) -> list:
    return [x, y]

# COMMON PATTERNS
# Check empty
if not lst:  # empty
    pass

# Check not empty
if lst:  # not empty
    pass

# Safe division
result = a / b if b != 0 else 0

# Get or default
value = d.get(key, 0)

# Remove duplicates keep order
unique = list(dict.fromkeys(lst))

# Flatten 2D list
flat = [x for row in matrix for x in row]

# Count frequency
from collections import Counter
freq = Counter(lst)
