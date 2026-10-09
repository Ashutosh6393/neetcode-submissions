# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        
        f = head
        s = prev


        while s: 
            ptr1, ptr2 = f.next, s.next
        
            f.next = s
            s.next = ptr1

            f = ptr1
            s = ptr2


        

        





        







    
            




            

        


        