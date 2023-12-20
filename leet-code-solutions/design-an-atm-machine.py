from collections import defaultdict
class ATM:

    def __init__(self):
        self.availableBankNotes = defaultdict(int)
        self.balances = [20,50,100,200,500]
        
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for a in range(0, len(banknotesCount)):
            self.availableBankNotes[a] += banknotesCount[a]
        # print(self.availableBankNotes)
    def withdraw(self, amount: int) -> List[int]:
        x = 4
        deductable = [0,0,0,0,0]
        while x >= 0:
            avail = amount // self.balances[x]
            if self.availableBankNotes[x] >= avail:
                amount = amount - avail * self.balances[x]
                deductable[x] += avail
            else:
                avail = self.availableBankNotes[x]
                deductable[x] += avail
                amount = amount - self.availableBankNotes[x] * self.balances[x]
            x-=1
        if amount == 0:
            for x in range(5):
                self.availableBankNotes[x] -= deductable[x]
            return deductable
        else:
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)