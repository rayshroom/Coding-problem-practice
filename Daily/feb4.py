'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        isloop = True

        if head is None:
            return False

        if head.next is None:
            return False

        it1 = head
        it2 = head.next

        while it1 != it2:
            if it1 is None or it2 is None:
                isloop = False
                break

            it1 = it1.next

            if it2.next is None:
                isloop = False
                break

            it2 = it2.next.next

        return isloop