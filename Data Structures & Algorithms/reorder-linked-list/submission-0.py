# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle of the list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second half
        second = slow.next
        prev = None
        slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge 2 lists alternatively
        first = head
        sec = prev

        while sec:
            tmp1 = first.next
            tmp2 = sec.next

            first.next = sec
            sec.next = tmp1
            first = tmp1
            sec = tmp2
        

    
        