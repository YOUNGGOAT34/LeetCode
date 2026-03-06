# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root,curr):
            if not root:
                return 0

            curr=curr*10+root.val

            if not root.left and not root.right:
                return curr

            return dfs(root.left,curr)+dfs(root.right,curr)
       

        return dfs(root,0)

            