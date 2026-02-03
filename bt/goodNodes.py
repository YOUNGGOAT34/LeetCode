# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxSoFar)->int:
            if not root:
                return 0

            count=1 if root.val>=maxSoFar else 0

            count+=dfs(root.left,max(maxSoFar,root.val))
            count+=dfs(root.right,max(maxSoFar,root.val))
            
            return count

        return dfs(root,root.val)
        