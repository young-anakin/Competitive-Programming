class RecentCounter:

    def __init__(self):
        self.val = deque()

    def ping(self, t: int) -> int:
        self.val.append(t)
        while t > self.val[0] + 3000:
            self.val.popleft()
        return(len(self.val))

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)