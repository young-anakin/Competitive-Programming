from collections import defaultdict
import random
class RandomizedSet:

    def __init__(self):
        self.occurence = set()
        self.one = 0
        self.chance = 0

    def insert(self, val: int) -> bool:
        if val not in self.occurence:
            self.occurence.add(val)
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if val in self.occurence:
            self.occurence.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.occurence))       


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()