# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp:
            sec = temp.next
            while sec:
                if sec.val < temp.val:
                    sp = temp.val
                    temp.val = sec.val
                    sec.val = sp
                sec = sec.next
            temp = temp.next
        return head
