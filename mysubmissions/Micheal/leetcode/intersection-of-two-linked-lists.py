# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB

        n = 1
        m = 1
        while temp1.next:
            n +=1
            temp1 = temp1.next
        
        while temp2.next:
            m+=1
            temp2 = temp2.next

        print(n, m)

        temp1 = headA
        temp2 = headB

        if n < m:
            while n != m:
                temp2 = temp2.next
                m-=1
                # print("Ya", temp2)
        else:
            while n != m:
                temp1 = temp1.next
                n -=1
                # print("No")

        while temp1:
            if temp1 == temp2 :
                return temp1 
            temp1 = temp1.next
            temp2 = temp2.next