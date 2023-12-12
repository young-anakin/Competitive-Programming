class OrderedStream:

    def __init__(self, n: int):
        self.order = {i:"" for i in range(1, n+2)}
        self.n = n
        self.ptr = 1
    def insert(self, idKey: int, value: str) -> List[str]:
        self.order[idKey] = value
        arr = []
        while self.order[self.ptr] != "":
            arr.append(self.order[self.ptr])
            self.ptr +=1
        return arr

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)