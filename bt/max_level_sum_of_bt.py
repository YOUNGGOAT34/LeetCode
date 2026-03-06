# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        level=1
        current_level=1
        q=deque([root])

        max_sum=float('-inf')
        while q:
            sum_level=0
            n=len(q)
            for _ in range(n):
                node=q.popleft()
                sum_level+=node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if sum_level>max_sum:
                max_sum=sum_level
                level=current_level

            current_level+=1


        return level
        