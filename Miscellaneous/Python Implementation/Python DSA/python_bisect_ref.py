"""
BISECT - Binary Search on Sorted Lists
=======================================
REQUIRES SORTED LIST!
"""

import bisect

# SORTED LIST REQUIRED
lst = [1, 3, 4, 4, 5, 7, 9]

# BISECT_LEFT (leftmost position)
# Find first position where value can be inserted
pos = bisect.bisect_left(lst, 4)  # 2 - first 4
pos = bisect.bisect_left(lst, 6)  # 5 - where 6 would go
pos = bisect.bisect_left(lst, 0)  # 0 - before all
pos = bisect.bisect_left(lst, 10)  # 7 - after all

# BISECT_RIGHT (rightmost position)
# Find last position where value can be inserted
pos = bisect.bisect_right(lst, 4)  # 4 - after last 4
pos = bisect.bisect(lst, 4)  # same as bisect_right
pos = bisect.bisect_right(lst, 6)  # 5

# INSERT WHILE MAINTAINING ORDER - O(n)
lst = [1, 3, 5, 7, 9]
bisect.insort_left(lst, 6)  # [1, 3, 5, 6, 7, 9]
bisect.insort_right(lst, 6)  # rightmost position
bisect.insort(lst, 6)  # alias for insort_right

# COMMON PATTERNS

# Check if element exists
def exists(arr, x):
    pos = bisect.bisect_left(arr, x)
    return pos < len(arr) and arr[pos] == x

# Count occurrences
def count_occurrences(arr, x):
    left = bisect.bisect_left(arr, x)
    right = bisect.bisect_right(arr, x)
    return right - left

# Count in range [x, y]
def count_range(arr, x, y):
    left = bisect.bisect_left(arr, x)
    right = bisect.bisect_right(arr, y)
    return right - left

# Floor (largest <= x)
def floor(arr, x):
    pos = bisect.bisect_right(arr, x)
    if pos == 0:
        return None
    return arr[pos - 1]

# Ceiling (smallest >= x)
def ceiling(arr, x):
    pos = bisect.bisect_left(arr, x)
    if pos == len(arr):
        return None
    return arr[pos]

# Closest element
def closest(arr, x):
    pos = bisect.bisect_left(arr, x)
    if pos == 0:
        return arr[0]
    if pos == len(arr):
        return arr[-1]
    before = arr[pos - 1]
    after = arr[pos]
    return after if (after - x) < (x - before) else before

# CP EXAMPLES

# Search Insert Position
def search_insert(nums, target):
    return bisect.bisect_left(nums, target)

# First Bad Version
def first_bad_version(n):
    left = bisect.bisect_left(range(1, n+1), True,
                               key=lambda x: isBadVersion(x))
    return left + 1

# Find K Closest Elements
def find_closest_elements(arr, k, x):
    left = bisect.bisect_left(arr, x) - 1
    right = left + 1
    result = []
    
    while len(result) < k:
        if left < 0:
            result.append(arr[right])
            right += 1
        elif right >= len(arr):
            result.insert(0, arr[left])
            left -= 1
        elif x - arr[left] <= arr[right] - x:
            result.insert(0, arr[left])
            left -= 1
        else:
            result.append(arr[right])
            right += 1
    
    return result

# TIME COMPLEXITY
# bisect_left/right: O(log n)
# insort: O(n) - O(log n) to find + O(n) to insert

# WHEN TO USE
# - Find insert position
# - Count elements in range
# - Floor/ceiling values
# - Sorted list operations
