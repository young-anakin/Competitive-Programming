# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        if head == None:
            return head
        second = head.next

        while second:
            if first == second:
                return True
            first = first.next
            if second.next == None:
                break
            second = second.next.next
        return False
