# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #Find the last element of the first list (slow pointer)
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse the second half (sec - starting point of  
                                #second reveresed list)
        sec = slow.next 
        prev = None
        slow.next = None

        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp 
        
        #merge alternatively

        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2





        