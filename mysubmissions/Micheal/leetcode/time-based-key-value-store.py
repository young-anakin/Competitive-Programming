class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append(timestamp)
        self.arr[key + "Location"].append(value) 



    def get(self, key: str, timestamp: int) -> str:
        val = bisect_left(self.arr[key], timestamp)
        if val >= len(self.arr[key]) and self.arr[key]:
            return self.arr[key + "Location"][-1]

        if len(self.arr[key]) == 0 or (val == 0 and self.arr[key][val] > timestamp)  :
            return ""
        if self.arr[key][val] > timestamp:
            return self.arr[key + "Location"][val-1]
        return self.arr[key + "Location"][val]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
