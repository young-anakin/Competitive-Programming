class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lastInd = 0
        for a in range(len(arr2)):
            for b in range(len(arr1)):
                if arr1[b] == arr2[a]:
                    arr1[b], arr1[lastInd] = arr1[lastInd], arr1[b]
                    lastInd +=1
        new_arr = arr1[0:lastInd]
        side = arr1[lastInd:]
        side = sorted(side)
        new_arr = new_arr  + side
        return new_arr