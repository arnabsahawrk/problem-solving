"""
COMMON ALGORITHM PATTERNS
==========================
Frequently used patterns (usage only, not full implementations)
"""

# TWO POINTERS
"""
Pattern: Use two pointers moving towards each other or same direction
Use when: Sorted array, finding pairs, removing duplicates
"""
# Example: Two Sum in sorted array
def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1

# SLIDING WINDOW
"""
Pattern: Maintain a window and slide it
Use when: Subarray/substring problems, fixed/variable size
"""
# Example: Max sum of k consecutive elements
def max_sum_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# PREFIX SUM
"""
Pattern: Precompute cumulative sums for range queries
Use when: Multiple range sum queries
"""
# Build prefix sum: O(n)
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)

# Query [l, r]: O(1)
range_sum = prefix[r + 1] - prefix[l]

# KADANE'S ALGORITHM
"""
Pattern: Track max ending here and max so far
Use when: Maximum subarray sum
"""
def max_subarray(arr):
    max_so_far = float('-inf')
    max_ending = 0
    for num in arr:
        max_ending += num
        max_so_far = max(max_so_far, max_ending)
        max_ending = max(0, max_ending)
    return max_so_far

# BINARY SEARCH
"""
Pattern: Divide and conquer in sorted array
Use when: Search in sorted array, find boundaries
"""
# Standard binary search
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

# FAST POWER (EXPONENTIATION BY SQUARING)
"""
Pattern: Reduce power by half each step
Use when: Computing a^b efficiently
"""
def power(base, exp):
    result = 1
    while exp > 0:
        if exp % 2:
            result *= base
        base *= base
        exp //= 2
    return result

# Modular version
def power_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# GCD (EUCLIDEAN ALGORITHM)
"""
Pattern: Repeatedly take modulo until one is zero
Use when: Finding greatest common divisor
"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Or use: import math; math.gcd(a, b)

# SIEVE OF ERATOSTHENES
"""
Pattern: Mark multiples of each prime as composite
Use when: Finding all primes up to n
"""
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

# MONOTONIC STACK
"""
Pattern: Stack that maintains monotonic order
Use when: Next greater/smaller element, histogram problems
"""
# Next greater element
def next_greater(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result

# MONOTONIC QUEUE (DEQUE)
"""
Pattern: Deque that maintains monotonic order
Use when: Sliding window maximum/minimum
"""
from collections import deque

def sliding_window_max(nums, k):
    dq = deque()  # stores indices
    result = []
    for i, num in enumerate(nums):
        # Remove outside window
        if dq and dq[0] <= i - k:
            dq.popleft()
        # Maintain decreasing order
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

# UNION FIND (DISJOINT SET)
"""
Pattern: Group elements and find connected components
Use when: Dynamic connectivity, graph problems
"""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

# TOPOLOGICAL SORT (KAHN'S ALGORITHM)
"""
Pattern: Process nodes with no incoming edges
Use when: DAG ordering, dependency resolution
"""
from collections import deque

def topological_sort(graph, n):
    in_degree = [0] * n
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else []  # cycle check

# BIT MANIPULATION PATTERNS
"""
Common bit tricks
"""
# Check power of 2
is_power_2 = n > 0 and (n & (n - 1)) == 0

# Get lowest set bit
lowest = n & -n

# Clear lowest set bit
cleared = n & (n - 1)

# Count set bits
count = bin(n).count('1')

# XOR all 1 to n (pattern: 1, n+1, 0, n)
def xor_1_to_n(n):
    mod = n % 4
    if mod == 1: return 1
    if mod == 2: return n + 1
    if mod == 3: return 0
    return n

# DUTCH NATIONAL FLAG
"""
Pattern: Three-way partitioning
Use when: Sort with 3 values, partition around pivot
"""
def dutch_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# BACKTRACKING TEMPLATE
"""
Pattern: Try all possibilities, backtrack on failure
Use when: Permutations, combinations, subsets, N-queens
"""
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])
        return
    
    for choice in choices:
        if is_valid(choice):
            path.append(choice)  # choose
            backtrack(path, next_choices)  # explore
            path.pop()  # unchoose

# MEMOIZATION TEMPLATE
"""
Pattern: Cache results of expensive function calls
Use when: Overlapping subproblems (DP)
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Or manual memoization
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]
