# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        temp = head
        while temp:
            n+=1
            temp = temp.next
        temp = head
        if n <= k:
            # print("bazinga")
            arr = []
            rem = n%k
            for ind in range(k):
                if temp == None:
                    arr.append(None)
                else:
                    vl = ListNode(temp.val)
                    arr.append(vl)
                    temp = temp.next
            return arr

        else:
            arr = []
            rem = n%k
            for ind in range(k):
                vl = ListNode(0)
                tmp = vl
                sp = 0
                if rem >=1:
                    sp +=1
                for j in range((n//k) + sp):
                    rd = ListNode(temp.val)
                    print(temp.val)
                    tmp.next = rd
                    tmp = tmp.next
                    temp = temp.next
                print(vl)
                vl = vl.next
                arr.append(vl)
                if rem != 0:
                    rem -=1
                sp = 0
            return arr


