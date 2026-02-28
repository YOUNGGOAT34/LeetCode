# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node,minn,maxx)->bool:
            if not node:
                return True

            if node.val<=minn or node.val>=maxx:
                return False
            
            return isValid(node.left,minn,node.val) and isValid(node.right,node.val,maxx)

        return isValid(root,float('-inf'),float('inf'))

        