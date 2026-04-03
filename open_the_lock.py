from collections import deque

# The problem is to find the minimum number of moves required to open a lock represented by a 4-digit string. Each digit can be rotated up or down, and there are certain deadends that cannot be used. The target is to reach a specific combination.
def openlock(deadends, target):
    dead = set(deadends)
    
    # If the initial state '0000' is a deadend, we cannot start, so return -1
    if '0000' in dead:
        return -1
    
    # Use a queue for BFS and a set to keep track of visited states to avoid cycles
    queue = deque([('0000', 0)])
    visited = set(['0000'])
    
    # Perform BFS until the queue is empty
    while queue:
        state, steps = queue.popleft()
        
        # If the current state is the target, return the number of steps taken
        if state == target:
            return steps
        
        # Generate all possible next states by rotating each digit up or down
        for i in range(4):
            digit = int(state[i])
            
            # Rotate the digit up and down, using modulo to wrap around from 9 to 0 and vice versa
            for move in [-1, 1]:
                new_digit = (digit + move) % 10
                new_state = state[ :i] + str(new_digit) + state[i+1: ]
                
                # If the new state is not a deadend and has not been visited, add it to the queue and mark it as visited
                if new_state not in dead and new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
    
    return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(openlock(deadends, target))
