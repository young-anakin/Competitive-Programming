class Bitset:

    def __init__(self, size: int):
        self.ones = [1 for i in range(size)]
        self.zeroes = [0 for i in range(size)]
        self.oneCount = 0
        self.zeroCount = size
        self.size = size
    def fix(self, idx: int) -> None:
        if self.zeroes[idx] != 1:
            self.zeroCount -=1
            self.oneCount +=1
        self.zeroes[idx] = 1
        self.ones[idx] = 0

    def unfix(self, idx: int) -> None:
        if self.zeroes[idx] != 0:
            self.zeroCount +=1
            self.oneCount -=1
        self.zeroes[idx] = 0
        self.ones[idx] = 1

    def flip(self) -> None:
        self.zeroCount, self.oneCount = self.oneCount, self.zeroCount
        self.ones, self.zeroes = self.zeroes, self.ones

    def all(self) -> bool:
        return self.oneCount == self.size
        

    def one(self) -> bool:
        return self.oneCount >= 1

    def count(self) -> int:
        return self.oneCount

    def toString(self) -> str:
        strs = ""
        for a in range(len(self.zeroes)):
            strs += str(self.zeroes[a])
        return strs

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()