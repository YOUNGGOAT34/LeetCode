# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        result=[]
        if not root:
            return result
        q.append(root)
        while q:
            level_max=q[0].val
            n=len(q)
            for _ in range(n):
                node=q.popleft()
                level_max=max(level_max,node.val)
                if node.left: q.append(node.left)
                if node.right:q.append(node.right)

            result.append(level_max)
        return result