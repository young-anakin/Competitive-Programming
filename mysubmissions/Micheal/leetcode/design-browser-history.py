class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:
    def __init__(self, homepage: str):
        node = ListNode(homepage)
        self.curr = node
        self.root = self.curr
    def visit(self, url: str) -> None:
        node = ListNode(url)
        temp = self.curr
        self.curr.next = node
        self.curr = node
        self.curr.prev = temp
    def back(self, steps: int) -> str:
        x = 0
        while self.curr.prev != None:
            x +=1
            self.curr = self.curr.prev

            if x == steps:
                return(self.curr.val)
                break

        if x != steps:
            return(self.curr.val)

        
    def forward(self, steps: int) -> str:
        x = 0
        while self.curr.next != None:
            self.curr = self.curr.next
            x +=1
            if x == steps:
                return(self.curr.val)
                break

        if x != steps:
            return(self.curr.val)            
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)