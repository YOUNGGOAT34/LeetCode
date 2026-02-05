# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        q=deque()
        q.append(root)
        avgs=[]

        while q:
            avg=0
            level_size=len(q)

            for _ in range(level_size):
                node=q.popleft()
                avg+=node.val

                if node.left:q.append(node.left)
                if node.right:q.append(node.right)

            avgs.append(avg/level_size)



        return avgs

        