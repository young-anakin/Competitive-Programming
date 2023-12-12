class UndergroundSystem:

    def __init__(self):
        self.checkInHash = {}
        self.destinationHash = {}
        self.destinationFrequency = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInHash[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if self.checkInHash[id][0] + " " + stationName not in self.destinationHash:
            self.destinationHash[self.checkInHash[id][0] + " " + stationName] = [t - self.checkInHash[id][1]]
        else:
            self.destinationHash[self.checkInHash[id][0] + " " + stationName].append(t - self.checkInHash[id][1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
            x = sum(self.destinationHash[startStation + " " + endStation])/len(self.destinationHash[startStation + " " + endStation])
            return x
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)