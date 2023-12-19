from collections import defaultdict
class FrequencyTracker:
    def __init__(self):
        self.actualFrequency = defaultdict(int)
        self.frequencyCount = defaultdict(int)
    def add(self, number: int) -> None:
        if self.frequencyCount[self.actualFrequency[number]] != 0:
            self.frequencyCount[self.actualFrequency[number]] -=1
        self.actualFrequency[number] +=1
        self.frequencyCount[self.actualFrequency[number]] +=1
    def deleteOne(self, number: int) -> None:
        if self.actualFrequency[number] != 0:
            self.frequencyCount[self.actualFrequency[number]] -=1
            self.actualFrequency[number] -=1
            self.frequencyCount[self.actualFrequency[number]] +=1
    def hasFrequency(self, frequency: int) -> bool:
        return bool(self.frequencyCount[frequency])


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)