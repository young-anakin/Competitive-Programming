class MinStack(object):
    from collections import deque
    def __init__(self):
        self.container = deque()
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.container.append(val)

    def pop(self):
        """
        :rtype: None
        """
        return self.container.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.container[-1]

    def getMin(self):
        min = self.container[0]
        for a in range(0, len(self.container)):
            if min >= self.container[a]:
                min = self.container[a]
        return min
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()