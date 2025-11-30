"""
CP TRICKS & PATTERNS
====================
Common competitive programming patterns
"""

# FAST INPUT/OUTPUT (for CP platforms)
import sys
input = sys.stdin.readline  # faster input

# READ INTEGERS
n = int(input())
a, b, c = map(int, input().split())
lst = list(map(int, input().split()))

# READ STRING
s = input().strip()  # remove trailing \n

# INFINITY
INF = float('inf')
NEG_INF = float('-inf')
# Or: INF = int(1e9), sys.maxsize

# MODULO OPERATIONS
MOD = 10**9 + 7
result = (a + b) % MOD
result = (a * b) % MOD
result = (a - b + MOD) % MOD  # handle negative
result = pow(a, b, MOD)  # fast modular exponentiation

# 2D ARRAY INITIALIZATION
n, m = 5, 5
matrix = [[0] * m for _ in range(n)]  # CORRECT
# matrix = [[0] * m] * n  # WRONG - shallow copy!

# COORDINATE DIRECTIONS
# 4-directional
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
# 8-directional
dirs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

# CHECK BOUNDS
def in_bounds(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

# SWAP WITHOUT TEMP
a, b = b, a

# MULTIPLE ASSIGNMENT
x = y = z = 0

# TERNARY OPERATOR
result = a if condition else b

# CHAINED COMPARISONS
if 0 < x < 10:  # instead of x > 0 and x < 10
    pass

# TUPLE COMPARISON (lexicographic)
(1, 2) < (1, 3)  # True
(1, 2) < (2, 1)  # True

# SORTING WITH MULTIPLE KEYS
arr = [(1, 3), (1, 2), (2, 1)]
arr.sort()  # sorts by first, then second

# Sort by custom criteria
students.sort(key=lambda x: (-x[1], x[0]))  # score desc, name asc

# ACCUMULATE (prefix sum/product)
from itertools import accumulate
lst = [1, 2, 3, 4, 5]
prefix = list(accumulate(lst))  # [1, 3, 6, 10, 15]
prefix_product = list(accumulate(lst, lambda x, y: x * y))

# ROTATE LIST
lst = [1, 2, 3, 4, 5]
k = 2
rotated = lst[k:] + lst[:k]  # [3, 4, 5, 1, 2]

# CHUNKING
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

# MEMOIZATION
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# FAST POWER
def power(base, exp):
    result = 1
    while exp > 0:
        if exp % 2:
            result *= base
        base *= base
        exp //= 2
    return result

# GCD
import math
gcd = math.gcd(a, b)

# LCM
lcm = abs(a * b) // math.gcd(a, b)

# SIEVE OF ERATOSTHENES
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

# KADANE'S ALGORITHM (max subarray sum)
def max_subarray_sum(arr):
    max_so_far = float('-inf')
    max_ending = 0
    for num in arr:
        max_ending += num
        max_so_far = max(max_so_far, max_ending)
        max_ending = max(0, max_ending)
    return max_so_far

# PREFIX SUM
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

def range_sum(prefix, l, r):
    return prefix[r + 1] - prefix[l]

# TWO POINTERS
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

# SLIDING WINDOW
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum

# FLATTEN NESTED LIST
nested = [[1, 2], [3, 4]]
flat = [x for row in nested for x in row]

# MATRIX TRANSPOSE
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [list(row) for row in zip(*matrix)]

# CARTESIAN PRODUCT
from itertools import product
result = list(product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# PERMUTATIONS & COMBINATIONS
from itertools import permutations, combinations
perms = list(permutations([1, 2, 3]))
combs = list(combinations([1, 2, 3], 2))

# BINARY CONVERSION
binary = bin(10)  # "0b1010"
binary = bin(10)[2:]  # "1010"
decimal = int("1010", 2)  # 10

# REMOVE DUPLICATES
unique = list(set(lst))  # unordered
unique = list(dict.fromkeys(lst))  # ordered

# FINDING DUPLICATES
dupes = [x for x in set(lst) if lst.count(x) > 1]

# TEMPLATE
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # your solution
    print(result)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    solve()  # single case
    # main()  # multiple cases
