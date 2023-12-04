class Solution(object):
    def kidsWithCandies(self, candies, extracandies):
        arr = []
        for candy in candies:
            if candy + extracandies >= max(candies):
                arr.append(True)
            else:
                arr.append(False)
        return arr
        