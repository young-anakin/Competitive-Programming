# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # first store head in temp node 
        temp = head
        ans = ListNode(10)


        # Construct a new linked list from the first to the left
        i = 1
        first = ListNode(10)
        beg = first
        while i < left:
            tmp = ListNode(temp.val)
            beg.next = tmp
            beg = beg.next
            temp = temp.next
            i +=1
        
        first = first.next



        # if first != None:
        #     while first.next:
        #         ans.next = first.val
        #         first = first.next

        # construct a new linked list that contains the middle values
        temp = head
        i = 1

        middle = ListNode(10)
        beg = middle
        while i <= right:
            if i >= left: 
                tmp = ListNode(temp.val)
                beg.next = tmp
                beg = beg.next
            temp = temp.next
            i +=1

        middle = middle.next

        # if middle != None:
        #     while middle.next:
        #         ans.next = middle.val
        #         middle = middle.next
        # construct a new linked list that containts the last values

        temp = head
        last = ListNode(10)
        beg = last
        i = 1
        while temp:
            if i > right:
                tmp = ListNode(temp.val)
                beg.next = temp
                beg = beg.next
            temp = temp.next
            i +=1
        
        last = last.next

        # reverse the middle list 
        curr = middle
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        middle = prev


        # Link all of the lists together 
        final = ListNode(10)
        final.next = first
        bb = final

        while bb.next:
            bb = bb.next
        bb.next = middle

        bb = final
        while bb.next:
            bb = bb.next
        
        bb.next = last
        final = final.next
        return final

            
            