# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node,min_value,max_value)->int:
            if not node:
                return abs(max_value-min_value)

            min_value=min(min_value,node.val)
            max_value=max(max_value,node.val)
           

            left=dfs(node.left,min_value,max_value)
            right=dfs(node.right,min_value,max_value)

            return max(left,right)

        return dfs(root,float('inf'),float('-inf'))


        