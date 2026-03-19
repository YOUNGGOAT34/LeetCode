# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        fast=slow=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next


        curr=slow.next
        slow.next=None
      
        prev=None

        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp

        right,left=prev,head

        while right:
            tmp1=left.next
            tmp2=right.next
            
            left.next=right
            right.next=tmp1

            left=tmp1
            right=tmp2


        