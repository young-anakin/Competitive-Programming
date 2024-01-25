# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Approach : 1 -> Find the middle of the Node and iterate from the begining to that node and from that node to the end simuntaneously
        self.count = 0
        temp = head
        while temp:
            self.count +=1
            temp = temp.next
        
        # the middle value of the linked list ( if count is even, it'll be at count//2 if not it'll be at count//2 +1)
        final = int(self.count//2) if self.count%2 == 0 else int(self.count//2)+1
        
        # variable to hold the second node we will start from
        sec = head
        i = 0
        while i != final:
            i+=1
            sec = sec.next
            
        temp = head
        arr1 = []
        arr2 = []
        # check starting from both indices ( the first one and middle one) if all the elements are the same
        while sec:
            arr1.append(temp.val)
            arr2.append(sec.val)
            temp = temp.next
            sec = sec.next
        arr2.reverse()
        print(arr1)
        print(arr2)
        if arr1 == arr2:
            return True
        return False