# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # arr = []

        # ptr = head
        # while ptr:
        #     arr.append(ptr)
        #     ptr = ptr.next
        

        # element_to_remove = len(arr) - n


        # if n == len(arr): 
        #     head = arr[element_to_remove].next
        # elif n == 1 and len(arr) > 1:
        #     arr[element_to_remove-1].next = None
        # else: 
        #     arr[element_to_remove-1].next = arr[element_to_remove+1]


        # return head


        length = 0

        ptr = head

        while ptr:
            length += 1
            ptr = ptr.next
        


        if n == length:
            return head.next
        elif length > 1 and n == 1:

            ptr2 = head
            while ptr2.next.next != None:
                ptr2 = ptr2.next

            ptr2.next = None

            return head
        else:

            count = length - n -1
            ptr3 = head
            while count > 0: 
                ptr3 = ptr3.next
                count -= 1
            
            tmp = ptr3.next.next
            ptr3.next = tmp

            return head



