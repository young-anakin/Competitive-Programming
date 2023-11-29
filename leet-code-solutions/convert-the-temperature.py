class Solution(object):
    def convertTemperature(self, celsius):
        arr = []
        arr.append(celsius + 273.15)
        arr.append(celsius * 1.80 +32.00)
        return arr
        