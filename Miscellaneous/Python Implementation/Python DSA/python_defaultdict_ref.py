"""
DEFAULTDICT - Dict with Default Values
=======================================
Auto-creates default value for missing keys
No KeyError!
"""

from collections import defaultdict

# CREATION
dd = defaultdict(int)  # default 0
dd = defaultdict(list)  # default []
dd = defaultdict(set)  # default set()
dd = defaultdict(str)  # default ""
dd = defaultdict(lambda: "N/A")  # custom default

# USAGE - INT (COUNTING)
freq = defaultdict(int)
for c in "hello":
    freq[c] += 1  # no need to check if key exists!
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# USAGE - LIST (GROUPING)
graph = defaultdict(list)
graph[1].append(2)  # auto-creates []
graph[1].append(3)
# {1: [2, 3]}

# USAGE - SET (UNIQUE GROUPING)
groups = defaultdict(set)
groups["vowels"].add('a')
groups["vowels"].add('e')
groups["vowels"].add('a')  # duplicate ignored
# {'vowels': {'a', 'e'}}

# USAGE - DICT (NESTED)
nested = defaultdict(dict)
nested["user1"]["age"] = 25
# {'user1': {'age': 25}}

# CONVERT TO REGULAR DICT
regular = dict(dd)

# CP EXAMPLES

# Graph Adjacency List
graph = defaultdict(list)
edges = [(1, 2), (1, 3), (2, 4)]
for u, v in edges:
    graph[u].append(v)

# Group by Property
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"}
]
by_grade = defaultdict(list)
for s in students:
    by_grade[s["grade"]].append(s["name"])
# {'A': ['Alice', 'Charlie'], 'B': ['Bob']}

# Accumulate Values
scores = [("Alice", 10), ("Bob", 5), ("Alice", 15)]
totals = defaultdict(int)
for name, score in scores:
    totals[name] += score
# {'Alice': 25, 'Bob': 5}

# Tree Structure
tree = lambda: defaultdict(tree)
users = tree()
users["user1"]["profile"]["age"] = 25

# Character Frequency
text = "hello"
freq = defaultdict(int)
for c in text:
    freq[c] += 1

# Anagram Grouping
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)
for s in strs:
    key = "".join(sorted(s))
    groups[key].append(s)

# TIME COMPLEXITY
# Same as dict: O(1) average for all operations

# WHEN TO USE
# - Grouping elements
# - Graph adjacency list
# - Counting without checking existence
# - Avoiding KeyError
