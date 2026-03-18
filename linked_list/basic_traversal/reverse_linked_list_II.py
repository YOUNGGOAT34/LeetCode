# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left==right:
            return head

        curr=head
        leftPrev=None

        #find left

        for _ in range(left-1):
            leftPrev=curr
            curr=curr.next

        tail=curr
        prev=None

        for _ in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        if leftPrev:
            leftPrev.next=prev

        else:
            head=prev

        tail.next=curr

        return head
        
        



        

     

        