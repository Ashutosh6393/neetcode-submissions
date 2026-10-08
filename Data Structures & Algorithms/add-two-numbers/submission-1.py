# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        ptr = l1
        place = 1
        number1 = 0  # val * place + number
        while ptr:
            number1 = ptr.val * place + number1
            ptr = ptr.next
            place = place * 10
        
        ptr2 = l2 
        place = 1
        number2 = 0

        while ptr2: 
            number2 = ptr2.val * place + number2
            ptr2 = ptr2.next 
            place = place * 10

        
        sum = number1 + number2

        sumList = ListNode()
        ptr3 = sumList

        if sum == 0: 
            return ListNode()

        while sum: 
            value = sum % 10

            newValue =  ListNode(value)
            ptr3.next = newValue
            ptr3 = ptr3.next

            sum = sum // 10

        
        return sumList.next




