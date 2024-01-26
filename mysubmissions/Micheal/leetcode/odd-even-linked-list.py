# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = None
        temp = head
        cp = 1
        if temp == None:
            return head
        while temp.next:
            cp +=1
            temp = temp.next
        if cp == 2:
            return head
        end = temp
        temp = head

        if cp %2 == 0:
            stepp = int(cp//2)
        else:
            stepp = int(cp//2)
        print(end)
        print(stepp)
        i = 1
        while i <= stepp:
            print("hey")
            sub = temp.next
            n = ListNode(sub.val)
            temp.next = sub.next
            end.next = n
            end = end.next
            temp = temp.next
            i +=1
        return head

