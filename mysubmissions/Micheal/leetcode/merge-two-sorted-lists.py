# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        merged = ListNode()
        first = list1
        second = list2
        temp = merged
        while first and second:
            if first.val <= second.val:
                temp.next = first
                first = first.next
            else:
                temp.next = second
                second = second.next
            temp = temp.next
        if second != None:
            temp.next = second
        if first != None:
            temp.next = first
        merged = merged.next
        return merged


            
