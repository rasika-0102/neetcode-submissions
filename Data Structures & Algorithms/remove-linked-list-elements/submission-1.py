# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev = dummy
        curr = head

        while curr:
            tmp = curr.next
            if curr.val == val:
                prev.next = tmp
            else:
                prev = curr
            curr = tmp
        return dummy.next
            




        