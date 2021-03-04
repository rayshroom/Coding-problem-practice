# Intersection of Two Linked Lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ca = headA
        cb = headB
        cac = 0
        cbc = 0
        
        while ca != None:
            cac += 1
            ca = ca.next
            
        while cb != None:
            cbc += 1
            cb = cb.next
            
        dif = abs(cac - cbc)
        ca = headA if cac > cbc else headB
        cb = headB if cac > cbc else headA
        
        while dif > 0:
            dif -= 1
            ca = ca.next
            
        while ca != None:
            if ca is cb:
                return ca
            ca = ca.next
            cb = cb.next
        
        return None