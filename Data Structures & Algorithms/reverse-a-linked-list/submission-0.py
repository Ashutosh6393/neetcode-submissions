# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: 
            return None
        
        first = None

        while head != None: 
            
            temp = head.next
            head.next = first

            first = head
            head = temp

        
        return first
