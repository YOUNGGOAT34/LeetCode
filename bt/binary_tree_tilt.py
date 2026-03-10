# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total=0
        def dfs(node)->int:
            nonlocal total
            if not node:
                return 0

            left=dfs(node.left)
            right=dfs(node.right)

            total+=abs(left-right)

            return left+right+node.val

        dfs(root)

        return total
        