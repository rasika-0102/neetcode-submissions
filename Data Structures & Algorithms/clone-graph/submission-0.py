"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}

        def dfs(curr):
            if curr in oldtonew:
                return oldtonew[curr]

            copy = Node(curr.val)
            oldtonew[curr] = copy

            for nei in curr.neighbors:
                new_node = dfs(nei)
                copy.neighbors.append(new_node)
            return copy
        
        return dfs(node) if node else None





        