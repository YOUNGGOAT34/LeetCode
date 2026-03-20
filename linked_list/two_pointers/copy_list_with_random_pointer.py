"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        if not head: return None

        curr=head

        #This dictionary maps the nodes of the original list into nodes of the new list

        mapping={}

        #create the mapping
        while curr:
            node=Node(x=curr.val)
            mapping[curr]=node
            curr=curr.next

        curr=head
        #connect the nodes of the new list
        while curr:
            new_node=mapping[curr]
            new_node.next=mapping.get(curr.next)
            new_node.random=mapping.get(curr.random)
            curr=curr.next

        return mapping[head]



        