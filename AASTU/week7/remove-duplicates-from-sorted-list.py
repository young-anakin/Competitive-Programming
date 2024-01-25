# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp:
            if temp.next == None:
                break
            nx = temp.next
            # print(temp.val, nx.val)
            if temp.val == nx.val:
                temp.next = nx.next
                continue
            temp = temp.next
        return head
                
            