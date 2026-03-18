# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast=slow=head

        #detect the cycle:
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if fast is slow:
                break

        #check if the cycle exists

        if not fast or not fast.next:
            return None

        #if the cycle exists find the starting point

        fast=head

        while fast is not slow:
    
            slow=slow.next
            fast=fast.next

        return fast



        