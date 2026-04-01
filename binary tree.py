# idea of this is to visit nodes level by level (top to down)
# using tree BFS
# How it works:
# 1. use a queue (structure)
# 2. add root to queue
# 3. visit all node at current level before going to next level

from collections import deque
def level_order_traversal(root):
    if not root:
        return []
    queue = deque([root])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result                