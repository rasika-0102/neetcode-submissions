# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            left = root.left
            right = root.right

            diameter = dfs(left) + dfs(right)

            res = max (res, diameter)

            return 1 + max(dfs(left), dfs(right))
        
        dfs(root)

        return res
    
        

            

        