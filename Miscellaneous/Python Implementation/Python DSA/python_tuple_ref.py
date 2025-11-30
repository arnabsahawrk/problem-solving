"""
TUPLE - Immutable List
=======================
Ordered, immutable, allows duplicates
Faster than list, used for fixed data
"""

# CREATION
t = ()  # empty
t = (1, 2, 3, 4, 5)
t = 1, 2, 3  # parentheses optional
single = (1,)  # note comma for single element

# ACCESSING
first = t[0]  # O(1)
last = t[-1]

# SLICING
sub = t[1:4]  # (2, 3, 4)
sub = t[::-1]  # reverse

# UNPACKING
a, b, c = (1, 2, 3)  # a=1, b=2, c=3
first, *rest = (1, 2, 3, 4)  # first=1, rest=[2,3,4]
first, *mid, last = (1, 2, 3, 4, 5)

# OPERATIONS
len(t)  # O(1)
t.count(2)  # O(n)
t.index(3)  # O(n)

# CHECKING
if 3 in t:  # O(n)
    pass

# ITERATION
for item in t:
    print(item)

# IMMUTABLE
# t[0] = 10  # ERROR!
# t.append(6)  # ERROR!

# CONCATENATION (creates new tuple)
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2

# REPETITION
repeated = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)

# USE CASES
# Return multiple values
def get_coords():
    return (10, 20)

x, y = get_coords()

# Dict keys (list can't be key)
locations = {(0, 0): "origin"}

# Fixed config
CONFIG = ("localhost", 8080)

# TIME COMPLEXITY
# Access: O(1)
# Search: O(n)
# Cannot modify (immutable)
