# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        total=0

        def dfs(node):
            nonlocal total
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            if node.left and not node.left.left and not node.left.right:
                total+=node.left.val

            return

        dfs(root)
        return total


            

        