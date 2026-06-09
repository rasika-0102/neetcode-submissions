"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        my_map = {}

        def dfs(curr):
            if curr in my_map:
                return my_map[curr]
            
            copy = Node(curr.val)
            my_map[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None