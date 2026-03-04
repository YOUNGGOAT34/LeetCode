# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q=deque([(root,0)])
        res=0
        while q:

            n=len(q)

            _,first_index=q[0]
            _,last_index=q[-1]
            res=max(res,last_index-first_index+1)
            
            for _ in range(n):
                node,index=q.popleft()
                if node.left:
                    q.append((node.left,2*index))
                if node.right:
                    q.append((node.right,2*index+1))

        return res


              

