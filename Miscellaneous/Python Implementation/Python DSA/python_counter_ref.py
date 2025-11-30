"""
COUNTER - Frequency Counter
============================
Subclass of dict for counting
"""

from collections import Counter

# CREATION
cnt = Counter()
cnt = Counter([1, 2, 2, 3, 3, 3])  # {3: 3, 2: 2, 1: 1}
cnt = Counter("hello")  # {'l': 2, 'h': 1, 'e': 1, 'o': 1}
cnt = Counter(a=4, b=2)  # {'a': 4, 'b': 2}

# ACCESSING
count = cnt[1]  # get count (returns 0 if not found, no error!)
count = cnt['z']  # 0 (missing key)

# UPDATING
cnt.update([1, 2, 2])  # add counts
cnt.update("hello")  # add from string
cnt.subtract([1, 2])  # subtract counts (can go negative)

# MOST COMMON
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
cnt = Counter(lst)
top_2 = cnt.most_common(2)  # [(4, 4), (3, 3)]
all_sorted = cnt.most_common()  # all by frequency

# OPERATIONS
cnt1 = Counter([1, 2, 2, 3])
cnt2 = Counter([2, 3, 3, 4])

# Addition
result = cnt1 + cnt2  # {2: 3, 3: 4, 1: 1, 4: 1}

# Subtraction (keeps only positive)
result = cnt1 - cnt2  # {2: 1, 1: 1}

# Intersection (minimum)
result = cnt1 & cnt2  # {2: 1, 3: 1}

# Union (maximum)
result = cnt1 | cnt2  # {3: 2, 2: 2, 1: 1, 4: 1}

# CONVERSION
dct = dict(cnt)  # to regular dict
lst = list(cnt.elements())  # with repeated elements
# Counter({3: 3, 2: 2}) → [3, 3, 3, 2, 2]

# ITERATION
for item, count in cnt.items():
    print(f"{item}: {count}")

# CP EXAMPLES

# Character Frequency
text = "hello world"
freq = Counter(text)
# {' ': 1, 'd': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}

# Most Common Character
most_common = freq.most_common(1)[0][0]

# Anagram Check
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

# First Non-Repeating Character
def first_unique(s):
    freq = Counter(s)
    for c in s:
        if freq[c] == 1:
            return c
    return None

# Word Frequency
text = "hello world hello python"
words = text.split()
word_freq = Counter(words)
# {'hello': 2, 'world': 1, 'python': 1}

# Top K Frequent Elements
def top_k_frequent(nums, k):
    freq = Counter(nums)
    return [num for num, _ in freq.most_common(k)]

# Valid Anagram (different from first)
def valid_anagram(s, t):
    return Counter(s) == Counter(t)

# Check if Permutation Exists
def can_permute_palindrome(s):
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2)
    return odd_count <= 1

# TIME COMPLEXITY
# All operations: O(1) average (it's a dict)
# most_common(k): O(n log k)
# elements(): O(n)

# WHEN TO USE
# - Frequency counting
# - Anagram problems
# - Most/least common elements
# - Histogram data
