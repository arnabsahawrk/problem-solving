"""
DICT - Hash Map (Key-Value Pairs)
==================================
Unordered (3.7+ maintains insertion order), mutable
"""

# CREATION
d = {}
d = {"name": "Alice", "age": 25}
d = dict(name="Alice", age=25)
d = dict([("a", 1), ("b", 2)])

# ADDING/UPDATING
d["city"] = "Dhaka"  # O(1)
d.update({"country": "BD"})  # add multiple
d.update(country="BD")  # alternative

# ACCESSING
val = d["name"]  # O(1) - KeyError if missing
val = d.get("name")  # O(1) - None if missing
val = d.get("name", "Default")  # with default

# REMOVING
del d["age"]  # O(1) - KeyError if missing
val = d.pop("city")  # O(1) - remove and return
val = d.pop("city", "Not Found")  # with default
d.popitem()  # O(1) - remove arbitrary pair
d.clear()  # O(n)

# CHECKING
if "name" in d:  # O(1)
    pass

# ITERATION
for key in d:  # keys only
    print(key)

for key, val in d.items():  # key-value pairs (MOST COMMON)
    print(key, val)

for val in d.values():  # values only
    print(val)

# VIEWS
keys = d.keys()  # dict_keys view
values = d.values()  # dict_values view
items = d.items()  # dict_items view

# DICT COMPREHENSION
squares = {x: x**2 for x in range(5)}
filtered = {k: v for k, v in d.items() if v > 20}

# NESTED DICT
student = {
    "name": "Alice",
    "grades": {"math": 90, "cs": 85}
}

# MERGING (3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2  # d2 overwrites: {"a": 1, "b": 3, "c": 4}

# MERGING (older)
merged = {**d1, **d2}

# SORTING
sorted_keys = sorted(d)  # sort keys
sorted_items = sorted(d.items())  # sort by key
sorted_by_val = sorted(d.items(), key=lambda x: x[1])

# SETDEFAULT
d.setdefault("new_key", []).append(1)  # get or create

# CP TRICKS
# Frequency count
text = "hello"
freq = {}
for c in text:
    freq[c] = freq.get(c, 0) + 1

# Group by property
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[key].append(item)

# TIME COMPLEXITY
# Access/Insert/Delete: O(1) average
# Search by key: O(1) average
