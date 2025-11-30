"""
HEAP / PRIORITY QUEUE
======================
Min-heap by default (Python 3.14+ has max-heap!)
"""

import heapq

# MIN HEAP (DEFAULT)
heap = []

# PUSH - O(log n)
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)  # heap = [2, 5, 8]

# POP (remove min) - O(log n)
min_val = heapq.heappop(heap)  # 2

# PEEK (view min) - O(1)
min_val = heap[0] if heap else None

# HEAPIFY (convert list to heap) - O(n)
lst = [5, 2, 8, 1, 9]
heapq.heapify(lst)  # transforms in-place

# N SMALLEST/LARGEST - O(n log k)
lst = [5, 2, 8, 1, 9, 3, 7]
smallest_3 = heapq.nsmallest(3, lst)  # [1, 2, 3]
largest_3 = heapq.nlargest(3, lst)  # [9, 8, 7]

# With key function
students = [{"name": "Alice", "gpa": 3.8}, {"name": "Bob", "gpa": 3.2}]
top_2 = heapq.nlargest(2, students, key=lambda x: x["gpa"])

# PUSH + POP - O(log n)
heapq.heappushpop(heap, 10)  # push 10, then pop min
heapq.heapreplace(heap, 10)  # pop min, then push 10

# MERGE SORTED - O(n log k)
sorted_lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
merged = list(heapq.merge(*sorted_lists))

# ==================== MAX HEAP ====================

# METHOD 1: NEGATE VALUES (LEGACY - WORKS EVERYWHERE)
max_heap = []
heapq.heappush(max_heap, -5)  # push negative
heapq.heappush(max_heap, -2)
max_val = -heapq.heappop(max_heap)  # negate when pop

# METHOD 2: PYTHON 3.14+ NATIVE MAX HEAP
# NOTE: Only if Python 3.14+ available
# heapq.heapify_max(lst)  # convert to max-heap
# heapq.heappush_max(heap, x)  # push to max-heap
# max_val = heapq.heappop_max(heap)  # pop max

# ==================== TUPLES IN HEAP ====================

# Heap with tuples (priority, value)
tasks = []
heapq.heappush(tasks, (1, "urgent"))  # priority 1
heapq.heappush(tasks, (5, "low"))  # priority 5
heapq.heappush(tasks, (3, "medium"))

priority, task = heapq.heappop(tasks)  # (1, "urgent")

# With tiebreaker (if priorities equal)
import itertools
counter = itertools.count()
heapq.heappush(tasks, (1, next(counter), "task1"))
heapq.heappush(tasks, (1, next(counter), "task2"))

# ==================== CP EXAMPLES ====================

# K-th Largest Element (min-heap of size k)
def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# K Closest Points
def k_closest(points, k):
    heap = []
    for x, y in points:
        dist = x*x + y*y
        heapq.heappush(heap, (-dist, x, y))  # max-heap
        if len(heap) > k:
            heapq.heappop(heap)
    return [(x, y) for _, x, y in heap]

# Median Finder (two heaps)
class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negated)
        self.large = []  # min-heap
    
    def addNum(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

# TIME COMPLEXITY
# Push: O(log n)
# Pop: O(log n)
# Peek: O(1)
# Heapify: O(n)
# nsmallest/nlargest: O(n log k)
