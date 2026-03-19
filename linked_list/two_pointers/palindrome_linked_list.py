# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast=slow=head


        #find the middle and the end of the list
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
           

        prev=None

        #reverse the half end of the list
        while slow:
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp

        #check if the two halfs match

        left,right=head,prev

        while right:
            if right.val!=left.val:
                return False

            right=right.next
            left=left.next

        return True
        