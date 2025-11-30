"""
QUEUE (FIFO - First In First Out)
==================================
Use deque (NOT list - inefficient)
"""

from collections import deque

# CREATION
queue = deque()

# ENQUEUE (add to back) - O(1)
queue.append(1)
queue.append(2)
queue.append(3)  # deque([1, 2, 3])

# DEQUEUE (remove from front) - O(1)
front = queue.popleft()  # 1, queue = deque([2, 3])

# PEEK FRONT - O(1)
front = queue[0] if queue else None

# PEEK BACK - O(1)
back = queue[-1] if queue else None

# CHECK EMPTY
if not queue:
    print("Empty")

# SIZE
size = len(queue)

# WHY NOT LIST?
# list.pop(0) is O(n) - SLOW!
# deque.popleft() is O(1) - FAST!

# CP EXAMPLES

# BFS Template
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Level Order Traversal
def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Sliding Window Maximum (monotonic queue)
def max_sliding_window(nums, k):
    from collections import deque
    dq = deque()  # stores indices
    result = []
    
    for i, num in enumerate(nums):
        # Remove elements outside window
        if dq and dq[0] <= i - k:
            dq.popleft()
        
        # Maintain decreasing order
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# TIME COMPLEXITY
# Enqueue: O(1)
# Dequeue: O(1)
# Peek: O(1)
