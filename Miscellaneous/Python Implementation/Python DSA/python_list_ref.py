"""
LIST - Dynamic Array
====================
Ordered, mutable, allows duplicates
"""

# CREATION
lst = []
lst = [1, 2, 3, 4, 5]
lst = [0] * 5  # [0, 0, 0, 0, 0]
lst = list(range(5))  # [0, 1, 2, 3, 4]

# ADDING
lst.append(6)  # O(1) - add to end
lst.insert(0, 10)  # O(n) - insert at index
lst.extend([7, 8])  # O(k) - add multiple

# ACCESSING
first = lst[0]  # O(1)
last = lst[-1]  # O(1) - negative indexing
element = lst[2]

# REMOVING
lst.pop()  # O(1) - remove last
lst.pop(0)  # O(n) - remove at index
lst.remove(10)  # O(n) - remove first occurrence
del lst[1]  # O(n) - delete by index
lst.clear()  # O(n) - remove all

# SLICING
lst = [1, 2, 3, 4, 5]
sub = lst[1:4]  # [2, 3, 4] - index 1 to 3
sub = lst[:3]  # [1, 2, 3] - first 3
sub = lst[2:]  # [3, 4, 5] - from index 2
sub = lst[::2]  # [1, 3, 5] - every 2nd
sub = lst[::-1]  # [5, 4, 3, 2, 1] - reverse

# OPERATIONS
lst.reverse()  # O(n) - in-place reverse
lst.sort()  # O(n log n) - in-place sort
lst.sort(reverse=True)  # descending
sorted_lst = sorted(lst)  # O(n log n) - new list

len(lst)  # O(1) - length
lst.count(3)  # O(n) - count occurrences
lst.index(3)  # O(n) - find first index

# CHECKING
if 3 in lst:  # O(n) - membership
    pass

# ITERATION
for item in lst:
    print(item)

for i, item in enumerate(lst):  # with index
    print(i, item)

# LIST COMPREHENSION
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]

# 2D LISTS
matrix = [[0] * 3 for _ in range(3)]  # CORRECT
# matrix = [[0] * 3] * 3  # WRONG - shallow copy!

# CP TRICKS
# Remove duplicates
unique = list(set(lst))  # loses order
unique = list(dict.fromkeys(lst))  # keeps order

# Flatten 2D list
nested = [[1, 2], [3, 4]]
flat = [x for row in nested for x in row]

# TIME COMPLEXITY
# Access: O(1)
# Append: O(1)
# Insert/Delete: O(n)
# Search: O(n)
# Sort: O(n log n)
