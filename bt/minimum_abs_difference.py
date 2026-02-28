# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev=None
        self.minDiff=float('inf')

        def inorder(node)->None:
            if not node: return

            inorder(node.left)
             
            if self.prev:
                self.minDiff=min(self.minDiff,node.val-self.prev.val)

            self.prev=node

            inorder(node.right)

        inorder(root)

        return self.minDiff
            
        