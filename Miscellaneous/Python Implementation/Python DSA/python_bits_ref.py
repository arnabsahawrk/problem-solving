"""
BIT MANIPULATION
================
Bitwise operations and tricks
"""

# BASIC OPERATIONS
a = 5   # 101
b = 3   # 011

# AND
result = a & b  # 001 = 1

# OR
result = a | b  # 111 = 7

# XOR
result = a ^ b  # 110 = 6

# NOT (flip all bits)
result = ~a  # -6 (two's complement)

# LEFT SHIFT (multiply by 2^n)
result = a << 1  # 1010 = 10
result = a << 2  # 10100 = 20

# RIGHT SHIFT (divide by 2^n)
result = a >> 1  # 10 = 2
result = a >> 2  # 1 = 1

# BUILT-IN FUNCTIONS

# Count set bits (1s)
count = bin(n).count('1')
# Python 3.10+: count = n.bit_count()

# Count bits needed
bits_needed = n.bit_length()  # 5 needs 3 bits (101)

# Binary representation
binary = bin(n)  # "0b101"
binary = bin(n)[2:]  # "101" - remove prefix
binary = format(n, 'b')  # "101"

# Binary to decimal
decimal = int("101", 2)  # 5

# Hex representation
hexa = hex(n)  # "0x5"
hexa = format(n, 'x')  # "5"

# BIT TRICKS

# Check if n-th bit is set
def is_bit_set(num, n):
    return (num & (1 << n)) != 0

# Set n-th bit
def set_bit(num, n):
    return num | (1 << n)

# Clear n-th bit
def clear_bit(num, n):
    return num & ~(1 << n)

# Toggle n-th bit
def toggle_bit(num, n):
    return num ^ (1 << n)

# Check if power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

# Get lowest set bit
def lowest_set_bit(n):
    return n & -n

# Clear lowest set bit
def clear_lowest(n):
    return n & (n - 1)

# Count set bits (Brian Kernighan)
def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1  # clear lowest bit
        count += 1
    return count

# XOR all numbers 1 to n
def xor_1_to_n(n):
    # Pattern: 1, 3, 0, 4 repeats
    if n % 4 == 1: return 1
    if n % 4 == 2: return n + 1
    if n % 4 == 3: return 0
    return n

# Swap two numbers
a, b = 5, 7
a ^= b
b ^= a
a ^= b
# Now a=7, b=5 (but a,b = b,a is simpler!)

# CP EXAMPLES

# Single Number (XOR property: a^a=0, a^0=a)
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Missing Number
def missing_number(nums):
    n = len(nums)
    xor_all = 0
    for i in range(n + 1):
        xor_all ^= i
    for num in nums:
        xor_all ^= num
    return xor_all

# Hamming Distance
def hamming_distance(x, y):
    return bin(x ^ y).count('1')

# Power of Two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Power of Four
def is_power_of_four(n):
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

# Reverse Bits
def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Subsets (using bits)
def subsets(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):  # 2^n subsets
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)
    return result

# XOR Queries
def xor_queries(arr, queries):
    # Prefix XOR
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] ^ num)
    
    result = []
    for l, r in queries:
        result.append(prefix[r + 1] ^ prefix[l])
    return result

# COMMON PATTERNS
"""
XOR Properties:
- a ^ a = 0
- a ^ 0 = a
- a ^ b = b ^ a (commutative)
- (a ^ b) ^ c = a ^ (b ^ c) (associative)

AND Properties:
- a & 0 = 0
- a & a = a
- a & (a-1) clears lowest set bit

OR Properties:
- a | 0 = a
- a | a = a

Useful Tricks:
- Check even/odd: n & 1
- Multiply by 2^k: n << k
- Divide by 2^k: n >> k
- Toggle case: c ^ 32 (for letters)
- Lowercase: c | 32
- Uppercase: c & ~32
"""

# TIME COMPLEXITY
# All bit operations: O(1)
# Operations on n bits: O(n) or O(log num)
