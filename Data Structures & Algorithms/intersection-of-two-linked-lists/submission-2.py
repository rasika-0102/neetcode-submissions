# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB

        if headA is None or headB is None:
            return None
        
        while pointerA != pointerB:
            if pointerA is not None:
                pointerA = pointerA.next
            else:
                pointerA = headB

            if pointerB is not None:
                pointerB = pointerB.next
            else:
                pointerB = headA
        return pointerA
            
            