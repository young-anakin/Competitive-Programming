# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = 0

        temp = head
        while temp:
            x +=1
            temp = temp.next
        
        temp = head
        sub = x - n
        print(sub, x)
        if sub == 0:
            print(head)
            head = head.next
            return head
        else:
            x = 1

            while temp:
                if x == sub:
                    vl = temp.next
                    temp.next = vl.next
                    break
                x +=1
                temp = temp.next
            return head
