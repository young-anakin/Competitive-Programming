from collections import Counter
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxx = max(arr)
        if arr[-1] == maxx or arr[0] == maxx:
            return False
        ind = arr.index(maxx)
        minArr = arr[0:ind+1]
        maxArr = arr[ind:]
        if len(arr) < 3:
            return False
        for a in range(0, len(minArr)-1):
            if minArr[a] < minArr[a+1]:
                continue
            else:
                return False
        for a in range(0, len(maxArr)-1):
            if maxArr[a] > maxArr[a+1]:
                continue
            else:
                return False
        return True
        