class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]

        new = self.getRow(rowIndex-1)

        arr = [0 for h in range(rowIndex+1)]
        
        arr[0] = 1
        arr[-1] = 1

        for j in range(1, len(arr)-1):
            arr[j] = new[j] + new[j-1]
        return arr 