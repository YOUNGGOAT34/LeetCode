# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque([root])

        root.val=0
        while q:
            level=[]
            level_sum=0

            for node in q:
                

                if node.left:
                    level_sum+=node.left.val
                    level.append(node.left)

                if node.right:
                    level_sum+=node.right.val
                    level.append(node.right)



            for node in q:

                siblings_sum=0
                if node.left:
                    siblings_sum+=node.left.val
                if node.right:
                    siblings_sum+=node.right.val
                
                if node.left:
                    node.left.val=level_sum-siblings_sum
                    
                if node.right:
                    node.right.val=level_sum-siblings_sum
                    

            q=level

        return root
        