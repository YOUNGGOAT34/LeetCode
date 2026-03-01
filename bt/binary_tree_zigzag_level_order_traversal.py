# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res

        q=deque()
        q.append(root)

        level_index=0

        while q:
            level=[]
           
            n=len(q)

            for _ in range(n):
                node =q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level.append(node.val)

            if level_index%2==1:
                level.reverse()

            res.append(level)
            level_index+=1

        return res
            
        