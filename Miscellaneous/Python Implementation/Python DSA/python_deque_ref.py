"""
DEQUE - Double-Ended Queue
===========================
Efficient operations at both ends
"""

from collections import deque

# CREATION
dq = deque()
dq = deque([1, 2, 3, 4, 5])
dq = deque(maxlen=5)  # fixed size

# ADDING - O(1)
dq.append(6)  # add to right
dq.appendleft(0)  # add to left
dq.extend([7, 8])  # extend right
dq.extendleft([-1, -2])  # extend left (reverses!)

# REMOVING - O(1)
dq.pop()  # remove from right
dq.popleft()  # remove from left

# ACCESSING - O(1)
first = dq[0]
last = dq[-1]
# Note: middle access is O(n)!

# ROTATION - O(k)
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)  # [4, 5, 1, 2, 3] - rotate right
dq.rotate(-2)  # [1, 2, 3, 4, 5] - rotate left

# OTHER
dq.clear()  # O(n)
len(dq)  # O(1)
dq.reverse()  # O(n)
dq.count(3)  # O(n)

# MAXLEN BEHAVIOR (circular buffer)
dq = deque(maxlen=3)
dq.extend([1, 2, 3])  # [1, 2, 3]
dq.append(4)  # [2, 3, 4] - auto removes leftmost

# ITERATION
for item in dq:
    print(item)

# USE AS STACK
stack = deque()
stack.append(1)  # push
top = stack.pop()  # pop

# USE AS QUEUE
queue = deque()
queue.append(1)  # enqueue
front = queue.popleft()  # dequeue

# CP EXAMPLES

# Sliding Window
def sliding_window(nums, k):
    from collections import deque
    dq = deque()
    result = []
    
    for i, num in enumerate(nums):
        # Your logic here
        pass
    
    return result

# Palindrome Check
def is_palindrome(s):
    dq = deque(c.lower() for c in s if c.isalnum())
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

# TIME COMPLEXITY
# Append/Pop (both ends): O(1)
# Access by index: O(n) - SLOW!
# Insert/Delete middle: O(n)
# Rotation: O(k)

# WHEN TO USE
# - BFS (queue)
# - Sliding window
# - Both ends needed
# - Circular buffer
