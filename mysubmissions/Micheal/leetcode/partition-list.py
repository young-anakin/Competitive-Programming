# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        higher = ListNode()
        smaller = ListNode()

        stemp = smaller
        htemp = higher

        temp = head
        while temp:
            n = ListNode(temp.val)
            if temp.val >= x:
                htemp.next = n
                htemp = htemp.next
            else:
                stemp.next = n
                stemp = stemp.next
            temp = temp.next

        
        higher = higher.next
        stemp.next = higher
        smaller = smaller.next
        return smaller