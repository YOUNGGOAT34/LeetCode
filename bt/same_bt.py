# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.same(p,q)

    def same(self,p,q)->bool:
        if not p and not q:
            return True

        if (not p and q) or (p and not q):
            return False

        if p.val != q.val:
            return False

        return self.same(p.right,q.right) and self.same(p.left,q.left)



        