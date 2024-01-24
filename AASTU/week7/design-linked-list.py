class Node: 
    def __init__(self, val = -1):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None 
        self.tail = None


    def get(self, index: int) -> int:
        ind = 0
        n = self.head
        while n:
            if ind == index:
                return n.val
            n = n.next
            ind +=1
        return -1

    def addAtHead(self, val: int) -> None:
        temp = self.head
        n = Node(val)
        self.head = n
        n.next = temp


    def addAtTail(self, val: int) -> None:
        new = Node(val)
        temp = self.head    
        if temp == None:
            self.head = new
        else:
            while temp:
                val = temp
                temp = temp.next
            val.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        n = Node(val)
        ind = 0
        if index == 0:
            self.head = n
            n.next = temp
        else:
            while temp:
                if ind == index-1:
                    secondTemp = temp
                    temp = n
                    temp.next = secondTemp.next
                    secondTemp.next = temp
                    break
                temp = temp.next
                ind +=1        
    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        i = 0
        if index == 0:
            self.head = temp.next
        else:
            while temp:
                if i == index-1:
                    val = temp.next
                    if val != None:
                        temp.next = val.next
                    break
                temp = temp.next
                i +=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)