"""
SET - Unique Elements (Unordered)
==================================
No duplicates, mutable, unordered
"""

# CREATION
s = set()  # empty set
s = {1, 2, 3, 4, 5}
# Note: {} creates dict, not set!
s = set([1, 2, 2, 3])  # {1, 2, 3} - dupes removed

# ADDING
s.add(6)  # O(1)
s.update([7, 8, 9])  # O(k) - add multiple

# REMOVING
s.remove(3)  # O(1) - KeyError if not found
s.discard(3)  # O(1) - no error (safer)
s.pop()  # O(1) - remove arbitrary
s.clear()  # O(n)

# CHECKING
if 3 in s:  # O(1)
    pass

len(s)  # O(1)

# SET OPERATIONS
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b  # {1, 2, 3, 4, 5, 6}
intersection = a & b  # {3, 4}
difference = a - b  # {1, 2}
symmetric_diff = a ^ b  # {1, 2, 5, 6}

# METHODS
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)

# SUBSET/SUPERSET
a.issubset(b)  # is a ⊆ b?
a.issuperset(b)  # is a ⊇ b?
a.isdisjoint(b)  # no common elements?

# IN-PLACE OPERATIONS
a |= b  # union update
a &= b  # intersection update
a -= b  # difference update

# ITERATION
for item in s:
    print(item)  # order not guaranteed

# CONVERTING
lst = [1, 2, 2, 3]
unique = list(set(lst))  # remove duplicates

# FROZENSET (immutable)
fs = frozenset([1, 2, 3])
# Can be dict key or set element

# CP TRICKS
# Check duplicates exist
has_dupes = len(lst) != len(set(lst))

# Find duplicates
dupes = [x for x in set(lst) if lst.count(x) > 1]

# Remove duplicates keep order
seen = set()
unique = [x for x in lst if x not in seen and not seen.add(x)]

# TIME COMPLEXITY
# Add/Remove/Search: O(1) average
# Union/Intersection: O(min(len(a), len(b)))
