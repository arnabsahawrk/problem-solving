"""
COMMON PITFALLS & BEST PRACTICES
=================================
Things to watch out for
"""

# ========== PITFALL 1: MUTABLE DEFAULT ARGUMENTS ==========
# WRONG
def add_item(item, lst=[]):
    lst.append(item)
    return lst
# Same list reused! add_item(1) then add_item(2) gives [1, 2]

# CORRECT
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# ========== PITFALL 2: SHALLOW VS DEEP COPY ==========
# Shallow copy - nested objects are shared!
lst1 = [[1, 2], [3, 4]]
lst2 = lst1.copy()  # or lst1[:]
lst2[0][0] = 999  # Modifies lst1 too!

# Deep copy - completely independent
import copy
lst2 = copy.deepcopy(lst1)

# ========== PITFALL 3: INTEGER DIVISION ==========
# Python 3 behavior
5 / 2   # 2.5 (float division)
5 // 2  # 2 (integer division)
-5 // 2  # -3 (floors toward negative infinity!)

# For C++-like division (toward zero)
int(-5 / 2)  # -2

# ========== PITFALL 4: MODIFYING LIST WHILE ITERATING ==========
# WRONG - skips elements
for item in lst:
    if item % 2 == 0:
        lst.remove(item)  # BUG!

# CORRECT
lst = [x for x in lst if x % 2 != 0]

# Or iterate over copy
for item in lst[:]:
    if item % 2 == 0:
        lst.remove(item)

# ========== PITFALL 5: 'is' VS '==' ==========
# 'is' checks identity (same object)
# '==' checks equality (same value)
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # True (same value)
a is b  # False (different objects)

# Use 'is' only for None, True, False
if x is None:  # CORRECT
    pass

# ========== PITFALL 6: LIST MULTIPLICATION ==========
# WRONG - creates shallow copies!
matrix = [[0] * 3] * 3  # All rows are same object!
matrix[0][0] = 1  # Changes all rows!

# CORRECT
matrix = [[0] * 3 for _ in range(3)]

# ========== PITFALL 7: MODULO WITH NEGATIVES ==========
-5 % 3  # 1 in Python (always non-negative)
# In C++: -5 % 3 = -2

# ========== PITFALL 8: DICT KEY ORDER ==========
# Python 3.7+ maintains insertion order, but don't rely on it for sorting!

# To iterate in sorted order
for key in sorted(dct):
    print(key)

# ========== PITFALL 9: VARIABLE SCOPE IN LOOPS ==========
# Variables in loops remain in scope after loop
for i in range(5):
    x = i
print(x)  # 4 - still accessible (unlike C++)

# ========== PITFALL 10: FUNCTION ARGUMENTS ==========
# Immutable objects (int, str, tuple) - pass by value
def modify_int(x):
    x += 1  # doesn't affect original

# Mutable objects (list, dict, set) - pass by reference
def modify_list(lst):
    lst.append(1)  # modifies original!

# ========== BEST PRACTICES ==========

# 1. Use list comprehension instead of loops
# GOOD
result = [x for x in lst if x > 0]
# Instead of: result = []; for x in lst: if x > 0: result.append(x)

# 2. Use enumerate instead of range(len())
# GOOD
for i, val in enumerate(lst):
    print(i, val)
# Instead of: for i in range(len(lst)): print(i, lst[i])

# 3. Use 'in' for membership
# GOOD
if x in lst:
    pass
# Instead of: if lst.count(x) > 0:

# 4. Use defaultdict to avoid KeyError
from collections import defaultdict
dct = defaultdict(list)
dct[key].append(val)  # no need to check existence

# 5. Use Counter for frequency
from collections import Counter
freq = Counter(lst)
# Instead of: freq = {}; for x in lst: freq[x] = freq.get(x, 0) + 1

# 6. Use set for O(1) lookup
# GOOD
s = set(lst)
if x in s:  # O(1)
    pass
# Instead of: if x in lst:  # O(n)

# 7. Use join for string concatenation
# GOOD
result = "".join(chars)
# Instead of: result = ""; for c in chars: result += c  # O(n²)

# 8. Use tuple for immutable sequences
# If data shouldn't change, use tuple instead of list

# 9. Use f-strings for formatting (3.6+)
# GOOD
s = f"Name: {name}, Age: {age}"
# Instead of: s = "Name: " + name + ", Age: " + str(age)

# 10. Check empty with truthiness
# GOOD
if not lst:  # empty
    pass
if lst:  # not empty
    pass
# Instead of: if len(lst) == 0:

# 11. Use any/all for boolean checks
# GOOD
has_positive = any(x > 0 for x in lst)
all_positive = all(x > 0 for x in lst)

# 12. Use zip for multiple lists
# GOOD
for name, score in zip(names, scores):
    print(name, score)
# Instead of: for i in range(len(names)): print(names[i], scores[i])

# 13. Chain comparisons
# GOOD
if 0 < x < 10:
    pass
# Instead of: if x > 0 and x < 10:

# 14. Use unpacking
# GOOD
a, b = b, a  # swap
first, *rest = lst  # unpack
# Instead of: temp = a; a = b; b = temp

# 15. Use get() for dict with default
# GOOD
val = dct.get(key, 0)
# Instead of: if key in dct: val = dct[key]; else: val = 0

# ========== PERFORMANCE TIPS ==========

# String concatenation in loops - use join()
# BAD: result = ""; for s in lst: result += s  # O(n²)
# GOOD: result = "".join(lst)  # O(n)

# Check if list is empty - use truthiness
# BAD: if len(lst) == 0:
# GOOD: if not lst:

# Reverse iteration
# GOOD: for item in reversed(lst):
# Instead of: for i in range(len(lst)-1, -1, -1): print(lst[i])

# Remove duplicates maintaining order
# GOOD: unique = list(dict.fromkeys(lst))
# BAD: unique = list(set(lst))  # loses order

# Multiple conditions
# GOOD: if x in (1, 2, 3, 4, 5):
# Instead of: if x==1 or x==2 or x==3 or x==4 or x==5:

# Floor division
# GOOD: a // b
# Instead of: int(a / b)

# Exponentiation
# GOOD: a ** b
# Instead of: math.pow(a, b)
