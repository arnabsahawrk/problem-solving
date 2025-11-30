"""
TIME COMPLEXITY CHEAT SHEET
============================
Common operations and their complexities
"""

# LIST
"""
Access: O(1)
Append: O(1) amortized
Insert at index: O(n)
Delete: O(n)
Pop last: O(1)
Pop at index: O(n)
Search: O(n)
Sort: O(n log n)
Reverse: O(n)
"""

# DICT
"""
Access by key: O(1) average
Insert: O(1) average
Delete: O(1) average
Search key: O(1) average
Iteration: O(n)
"""

# SET
"""
Add: O(1) average
Remove: O(1) average
Search: O(1) average
Union: O(len(a) + len(b))
Intersection: O(min(len(a), len(b)))
Difference: O(len(a))
"""

# DEQUE
"""
Append/Pop (both ends): O(1)
Access by index: O(n)  # SLOW!
Insert/Delete middle: O(n)
"""

# HEAP
"""
Push: O(log n)
Pop: O(log n)
Peek: O(1)
Heapify: O(n)
nsmallest/nlargest: O(n log k)
"""

# STRING
"""
Access: O(1)
Concatenation: O(n + m)
Search (in, find): O(n * m)
Slice: O(k)
Split: O(n)
Join: O(n)
"""

# SORTING
"""
list.sort(): O(n log n)
sorted(): O(n log n)
min/max: O(n)
"""

# COMMON ALGORITHMS
"""
Binary Search: O(log n)
Linear Search: O(n)
BFS/DFS: O(V + E)
Kadane's: O(n)
Two Pointers: O(n)
Sliding Window: O(n)
Prefix Sum: O(n)
Sieve: O(n log log n)
GCD: O(log min(a, b))
Power: O(log exp)
"""

# BIG O NOTATION
"""
O(1) - Constant
  - Dict/Set access
  - List access by index
  - Append to list

O(log n) - Logarithmic
  - Binary search
  - Heap operations
  - Balanced tree operations

O(n) - Linear
  - List search
  - Min/max
  - Sum
  - Single loop

O(n log n) - Linearithmic
  - Efficient sorting (Timsort)
  - Merge sort
  - Heap sort

O(n²) - Quadratic
  - Nested loops
  - Bubble sort
  - Selection sort

O(2^n) - Exponential
  - Recursive fibonacci
  - Generate all subsets

O(n!) - Factorial
  - Generate all permutations
"""

# PRACTICAL LIMITS (approximate)
"""
n ≤ 10: O(n!) or O(2^n)
n ≤ 20: O(2^n)
n ≤ 100: O(n³)
n ≤ 1000: O(n²)
n ≤ 10^5: O(n log n)
n ≤ 10^6: O(n) or O(n log n)
n ≤ 10^8: O(n)
n ≤ 10^9: O(log n) or O(1)
"""

# SPACE COMPLEXITY
"""
List/Dict/Set: O(n)
Deque: O(n)
Heap: O(n)
Recursion depth: O(depth)
"""

# EXAMPLES

# O(1)
def constant(arr):
    return arr[0]

# O(log n)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n)
def linear(arr):
    total = 0
    for x in arr:
        total += x
    return total

# O(n log n)
def nlogn(arr):
    return sorted(arr)

# O(n²)
def quadratic(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            count += 1
    return count

# O(2^n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# COMMON MISTAKES

# BAD: O(n²) - repeated searching
for x in arr1:
    if x in arr2:  # O(n) each time
        print(x)

# GOOD: O(n) - use set
set2 = set(arr2)  # O(n)
for x in arr1:  # O(n)
    if x in set2:  # O(1)
        print(x)

# BAD: O(n²) - string concatenation in loop
result = ""
for c in s:
    result += c  # creates new string each time

# GOOD: O(n) - use list + join
chars = []
for c in s:
    chars.append(c)
result = "".join(chars)

# BAD: O(n²) - list.remove in loop
for x in lst:
    lst.remove(x)  # O(n) each time

# GOOD: O(n) - list comprehension
lst = [x for x in lst if condition]

# AMORTIZED COMPLEXITY
"""
list.append() is O(1) amortized:
- Usually O(1)
- Occasionally O(n) when resizing
- Average over many operations is O(1)
"""

# TIPS
"""
1. Dict/Set lookup is O(1), not O(n) like list
2. Use deque for queue, not list
3. heapq operations are O(log n)
4. Sorting is O(n log n), not O(n²)
5. String concatenation in loop is O(n²), use join
6. Multiple passes O(n) + O(n) = O(n), not O(n²)
7. Nested loops are usually O(n²)
8. Binary search is O(log n), but requires sorted array
"""
