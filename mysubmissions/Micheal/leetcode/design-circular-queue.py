class Node: 
    def __init__(self, val = -1):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.head = Node(-1)
        self.cp = 0
        self.curr = self.head
    def enQueue(self, value: int) -> bool:
        print(self.cp, self.size)
        if self.cp < self.size:
            temp = self.head
            print(temp)
            val = Node(value)
            self.cp +=1

            if temp == None:
                self.head = Node(value)

                return True
            elif temp.val == -1:
                self.head = Node(value)
                return True
            while temp.next:
                temp = temp.next
            
            temp.next = val
            return True
        return False

    def deQueue(self) -> bool:
        if self.cp > 0:
            temp = self.head
            if temp == None:
                return False
            self.head = temp.next
            self.cp -=1
            return True
        return False

    def Front(self) -> int:
        temp = self.head
        if self.cp > 0:
            return temp.val
        return -1
    def Rear(self) -> int:
        temp = self.head

        if self.cp > 0:
            temp = self.head
            if temp == None:
                return -1
            while temp.next:
                temp = temp.next
            
            return temp.val
        return -1
    def isEmpty(self) -> bool:
        if self.cp == 0:
            return True
        return False

    def isFull(self) -> bool:
        
        if self.cp == self.size:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()