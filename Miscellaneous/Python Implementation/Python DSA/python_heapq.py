"""
HEAPQ - Priority Queue (C++ priority_queue equivalent)
=======================================================
- Min-heap by default (opposite of C++ max-heap default)
- Implemented as binary heap using list
- O(log n) push/pop
- Python 3.14+ now has NATIVE max-heap support!

Author: Arnab Saha
Updated: 2025 (Python 3.14 features added)
"""

import heapq

# =============================================================================
# SECTION 1: HEAP CREATION & BASICS
# =============================================================================

heap = []  # empty heap (just a regular list)

# =============================================================================
# SECTION 2: MIN HEAP (DEFAULT BEHAVIOR)
# =============================================================================

# Push elements - O(log n) each
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)  # heap maintains min-heap property: [1, 2, 8, 5]

# Peek at minimum - O(1)
min_val = heap[0]  # Returns smallest without removing (like top() in C++)

# Pop minimum - O(log n)
min_val = heapq.heappop(heap)  # Removes and returns smallest element

# Heapify - Convert existing list to heap - O(n)
lst = [5, 2, 8, 1, 9]
heapq.heapify(lst)  # Transforms list in-place to min-heap

# =============================================================================
# SECTION 3: MAX HEAP - PYTHON 3.14+ (NEW NATIVE SUPPORT!)
# =============================================================================
"""
Python 3.14 introduced native max-heap functions!
No more negating values or custom classes needed.

New functions:
    - heapify_max()     : Convert list to max-heap in-place
    - heappush_max()    : Push item onto max-heap
    - heappop_max()     : Pop largest item from max-heap
    - heappushpop_max() : Push then pop (efficient single operation)
    - heapreplace_max() : Pop then push (efficient single operation)
"""

# Create and use a max-heap natively (Python 3.14+)
max_heap_native = [5, 2, 8, 1, 9, 3, 7]

# Convert to max-heap - O(n)
heapq.heapify_max(max_heap_native)  # Now it's a max-heap: largest at index 0

# Peek at maximum - O(1)
max_val = max_heap_native[0]  # Returns 9 (largest element)

# Push onto max-heap - O(log n)
heapq.heappush_max(max_heap_native, 15)  # 15 becomes new max

# Pop maximum - O(log n)
max_val = heapq.heappop_max(max_heap_native)  # Returns 15, removes it

# Push then pop in one operation - O(log n)
# More efficient than separate push + pop
result = heapq.heappushpop_max(max_heap_native, 6)  # Push 6, then pop max

# Pop then push in one operation - O(log n)
# Useful when replacing the max with a new value
result = heapq.heapreplace_max(max_heap_native, 4)  # Pop max, then push 4


# -----------------------------------------------------------------------------
# PRACTICAL EXAMPLE: Find K Largest Elements (Python 3.14+ way)
# -----------------------------------------------------------------------------
def k_largest_modern(nums: list, k: int) -> list:
    """
    Find k largest elements using native max-heap.
    Time: O(n + k log n) - heapify is O(n), k pops are O(k log n)
    """
    heap = nums.copy()  # Don't modify original
    heapq.heapify_max(heap)
    return [heapq.heappop_max(heap) for _ in range(k)]


# Example
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(k_largest_modern(numbers, 3))  # [9, 6, 5]

# =============================================================================
# SECTION 4: MAX HEAP - LEGACY METHODS (Pre-Python 3.14)
# =============================================================================
"""
These workarounds are still useful to know because:
1. Many interview platforms use older Python versions
2. Production systems may not have upgraded yet
3. Understanding these shows deeper knowledge of heaps
"""

# -----------------------------------------------------------------------------
# Method 1: Negate Values (Most Common Workaround)
# -----------------------------------------------------------------------------
# Concept: Since heapq is min-heap, negating values inverts the order
# -8 < -5 < -2, so -8 is at top, which represents 8 as max

max_heap_negated = []
heapq.heappush(max_heap_negated, -5)  # Store negative
heapq.heappush(max_heap_negated, -2)
heapq.heappush(max_heap_negated, -8)

# To get max: negate again when popping
max_val = -heapq.heappop(max_heap_negated)  # Returns 8

# To peek at max:
max_val = -max_heap_negated[0]  # Returns current max without removing

# -----------------------------------------------------------------------------
# Method 2: Custom Class with Reversed Comparison
# -----------------------------------------------------------------------------
# Concept: Override __lt__ to invert comparison logic
# When heapq compares objects, our "less than" actually means "greater than"


class MaxHeapObj:
    """Wrapper class that inverts comparison for max-heap behavior."""

    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        # INVERTED: Return True if self is GREATER than other
        # This tricks heapq into treating larger values as "smaller"
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __repr__(self):
        return f"MaxHeapObj({self.val})"


# Usage
max_heap_custom = []
heapq.heappush(max_heap_custom, MaxHeapObj(5))
heapq.heappush(max_heap_custom, MaxHeapObj(2))
heapq.heappush(max_heap_custom, MaxHeapObj(8))

max_val = heapq.heappop(max_heap_custom).val  # Returns 8

# -----------------------------------------------------------------------------
# Method 3: Using nlargest() for One-Time Operations
# -----------------------------------------------------------------------------
# If you just need the k largest elements once, this is cleaner
lst = [5, 2, 8, 1, 9, 3, 7]
largest_3 = heapq.nlargest(3, lst)  # [9, 8, 7] - O(n log k)

# =============================================================================
# SECTION 5: EFFICIENT COMBINED OPERATIONS
# =============================================================================

heap = [1, 3, 5, 7, 9]
heapq.heapify(heap)

# heappushpop: Push new item, then pop smallest - O(log n)
# More efficient than push() followed by pop()
# Use case: Maintain fixed-size heap (e.g., "keep only k smallest")
result = heapq.heappushpop(heap, 4)  # Push 4, pop smallest, return popped

# heapreplace: Pop smallest, then push new item - O(log n)
# More efficient than pop() followed by push()
# Use case: Replace minimum with new value in streaming data
result = heapq.heapreplace(heap, 2)  # Pop smallest (returns it), push 2

# KEY DIFFERENCE:
# heappushpop(heap, x): If x is smallest, returns x immediately (no heap change)
# heapreplace(heap, x): Always pops current min first, then pushes x

# =============================================================================
# SECTION 6: N SMALLEST / N LARGEST
# =============================================================================

lst = [5, 2, 8, 1, 9, 3, 7, 4, 6]

# Get n smallest elements - O(n log k) where k is count
smallest_3 = heapq.nsmallest(3, lst)  # [1, 2, 3]

# Get n largest elements - O(n log k)
largest_3 = heapq.nlargest(3, lst)  # [9, 8, 7]

# With key function (like sorted's key parameter)
students = [
    {"name": "Alice", "gpa": 3.8},
    {"name": "Bob", "gpa": 3.2},
    {"name": "Charlie", "gpa": 3.9},
    {"name": "Diana", "gpa": 3.5},
]
top_2_students = heapq.nlargest(2, students, key=lambda x: x["gpa"])
# [{"name": "Charlie", "gpa": 3.9}, {"name": "Alice", "gpa": 3.8}]

# WHEN TO USE WHAT:
# - nsmallest/nlargest: Best when k is small relative to n
# - sorted()[:k]: Better when k is close to n
# - heapify + pop: Better when you need repeated access

# =============================================================================
# SECTION 7: MERGE SORTED ITERABLES
# =============================================================================

# Merge multiple sorted iterables into single sorted output - O(n log k)
# where n = total elements, k = number of iterables
# Returns an iterator (memory efficient for large data)

sorted_lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
merged = list(heapq.merge(*sorted_lists))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# With key function
words = [["apple", "cherry"], ["banana", "date"]]
merged_words = list(heapq.merge(*words, key=str.lower))
# ['apple', 'banana', 'cherry', 'date']

# Use case: Merge K sorted files/arrays (common interview problem!)

# =============================================================================
# SECTION 8: HEAP WITH CUSTOM OBJECTS / TUPLES
# =============================================================================

# Using tuples: First element is priority (lower = higher priority)
tasks = []
heapq.heappush(tasks, (1, "urgent task"))  # Priority 1 (highest)
heapq.heappush(tasks, (5, "low priority"))  # Priority 5 (lowest)
heapq.heappush(tasks, (3, "medium priority"))  # Priority 3

priority, task = heapq.heappop(tasks)  # Returns (1, "urgent task")

# IMPORTANT: If priorities are equal, Python compares the second element
# This can cause errors if second elements aren't comparable!

import itertools

# Solution: Use a counter as tiebreaker
from dataclasses import dataclass, field
from typing import Any

counter = itertools.count()  # Unique sequence number

# Method A: Tuple with counter (priority, counter, task)
tasks_safe = []
heapq.heappush(tasks_safe, (1, next(counter), "task A"))
heapq.heappush(
    tasks_safe, (1, next(counter), "task B")
)  # Same priority, but counter differs


# Method B: Dataclass with ordering
@dataclass(order=True)
class PrioritizedTask:
    priority: int
    task: Any = field(compare=False)  # Exclude from comparison


pq = []
heapq.heappush(pq, PrioritizedTask(2, {"name": "Write code"}))
heapq.heappush(pq, PrioritizedTask(1, {"name": "Fix bug"}))
top_task = heapq.heappop(pq)  # PrioritizedTask(priority=1, task={'name': 'Fix bug'})

# =============================================================================
# SECTION 9: TIME COMPLEXITY SUMMARY
# =============================================================================
"""
Operation           | Time Complexity | Notes
--------------------|-----------------|----------------------------------
heappush            | O(log n)        | Add element, maintain heap property
heappop             | O(log n)        | Remove & return min/max
heap[0] (peek)      | O(1)            | View min/max without removing
heapify             | O(n)            | Convert list to heap in-place
heappushpop         | O(log n)        | Push then pop (optimized)
heapreplace         | O(log n)        | Pop then push (optimized)
nsmallest(k, lst)   | O(n log k)      | Find k smallest elements
nlargest(k, lst)    | O(n log k)      | Find k largest elements
merge(*iterables)   | O(n log k)      | Merge k sorted iterables

Python 3.14+ Max-Heap:
heapify_max         | O(n)            | Convert list to max-heap
heappush_max        | O(log n)        | Push to max-heap
heappop_max         | O(log n)        | Pop max from max-heap
heappushpop_max     | O(log n)        | Push then pop max
heapreplace_max     | O(log n)        | Pop max then push
"""

# =============================================================================
# SECTION 10: COMMON USE CASES & INTERVIEW PATTERNS
# =============================================================================
"""
1. Dijkstra's Algorithm (Shortest Path)
   - Use min-heap to always process nearest unvisited node
   
2. K-th Largest/Smallest Element
   - Min-heap of size k for k-th largest
   - Max-heap of size k for k-th smallest
   
3. Merge K Sorted Lists/Arrays
   - Push first element of each list with list index
   - Pop min, push next element from same list
   
4. Top K Frequent Elements
   - Count frequencies, then use heap to get top k
   
5. Task Scheduling by Priority
   - Priority queue with (priority, task) tuples
   
6. Median in a Data Stream
   - Two heaps: max-heap for lower half, min-heap for upper half
   
7. Huffman Coding
   - Build optimal prefix code using min-heap
   
8. Meeting Rooms II (Minimum Rooms Needed)
   - Min-heap tracking end times of ongoing meetings
"""

# =============================================================================
# SECTION 11: PRACTICAL EXAMPLES
# =============================================================================


# -----------------------------------------------------------------------------
# Example 1: K-th Largest Element (LeetCode 215)
# -----------------------------------------------------------------------------
def find_kth_largest(nums: list[int], k: int) -> int:
    """
    Find k-th largest element in unsorted array.
    Using min-heap of size k.
    Time: O(n log k), Space: O(k)
    """
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove smallest, keep k largest
    return min_heap[0]  # k-th largest is the smallest among k largest


# Python 3.14+ version using max-heap
def find_kth_largest_v2(nums: list[int], k: int) -> int:
    """Using native max-heap - more intuitive approach."""
    heap = nums.copy()
    heapq.heapify_max(heap)
    for _ in range(k - 1):
        heapq.heappop_max(heap)
    return heapq.heappop_max(heap)


# -----------------------------------------------------------------------------
# Example 2: Merge K Sorted Lists
# -----------------------------------------------------------------------------
def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    """
    Merge k sorted lists into one sorted list.
    Time: O(n log k), where n = total elements, k = number of lists
    """
    result = []
    heap = []

    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list_idx, element_idx)

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # If there's a next element in this list, add it
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result


# -----------------------------------------------------------------------------
# Example 3: Find Median from Data Stream (LeetCode 295)
# -----------------------------------------------------------------------------
class MedianFinder:
    """
    Two-heap approach:
    - max_heap: stores smaller half (use negation for max-heap behavior)
    - min_heap: stores larger half

    Invariant: len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1
    """

    def __init__(self):
        self.max_heap = []  # Smaller half (negated values)
        self.min_heap = []  # Larger half

    def addNum(self, num: int) -> None:
        # Always add to max_heap first (as negated value)
        heapq.heappush(self.max_heap, -num)

        # Balance: move largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Ensure max_heap has equal or one more element
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2


# Python 3.14+ version (cleaner with native max-heap)
class MedianFinderModern:
    """Using Python 3.14's native max-heap - no negation needed!"""

    def __init__(self):
        self.max_heap = []  # Smaller half (native max-heap)
        self.min_heap = []  # Larger half (min-heap)

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.max_heap, num)
        heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]  # No negation needed!
        return (self.max_heap[0] + self.min_heap[0]) / 2


# =============================================================================
# QUICK REFERENCE CHEAT SHEET
# =============================================================================
"""
MIN-HEAP (Default):
    heapq.heapify(lst)          # List -> Min-heap
    heapq.heappush(heap, x)     # Add element
    heapq.heappop(heap)         # Remove & return min
    heap[0]                     # Peek min

MAX-HEAP (Python 3.14+):
    heapq.heapify_max(lst)      # List -> Max-heap
    heapq.heappush_max(heap, x) # Add element
    heapq.heappop_max(heap)     # Remove & return max
    heap[0]                     # Peek max

MAX-HEAP (Legacy - Pre 3.14):
    heapq.heappush(heap, -x)    # Negate on push
    -heapq.heappop(heap)        # Negate on pop
    -heap[0]                    # Negate on peek

UTILITIES:
    heapq.nsmallest(k, lst)     # K smallest
    heapq.nlargest(k, lst)      # K largest
    heapq.merge(*sorted_lsts)   # Merge sorted iterables
"""
