"""
STACK (LIFO - Last In First Out)
=================================
Use list or deque
"""

# USING LIST (RECOMMENDED FOR STACK)
stack = []

# PUSH - O(1)
stack.append(1)
stack.append(2)
stack.append(3)  # [1, 2, 3]

# POP - O(1)
top = stack.pop()  # 3, stack = [1, 2]

# PEEK - O(1)
top = stack[-1] if stack else None

# CHECK EMPTY
if not stack:
    print("Empty")

# SIZE
size = len(stack)

# USING DEQUE (alternative)
from collections import deque
stack = deque()
stack.append(1)
top = stack.pop()

# CP EXAMPLES

# Valid Parentheses
def is_valid(s):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in pairs:
            stack.append(c)
        elif not stack or pairs[stack.pop()] != c:
            return False
    return not stack

# Next Greater Element
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

# Evaluate Reverse Polish Notation
def eval_rpn(tokens):
    stack = []
    for t in tokens:
        if t in "+-*/":
            b, a = stack.pop(), stack.pop()
            if t == '+': stack.append(a + b)
            elif t == '-': stack.append(a - b)
            elif t == '*': stack.append(a * b)
            else: stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack[0]

# TIME COMPLEXITY
# Push: O(1)
# Pop: O(1)
# Peek: O(1)
