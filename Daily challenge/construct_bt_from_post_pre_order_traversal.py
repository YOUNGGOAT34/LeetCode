# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from ast import List

from pyparsing import Optional


class Solution:
    def __init__(self):
        self.pre_index=0
        self.post_index=0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        curr=TreeNode(preorder[self.pre_index]) # type: ignore
        self.pre_index+=1

        if curr.val !=postorder[self.post_index]:
            curr.left=self.constructFromPrePost(preorder,postorder)

        if curr.val !=postorder[self.post_index]:
            curr.right=self.constructFromPrePost(preorder,postorder)
        self.post_index+=1
        return curr
        