class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ind = []
        ans = []
        for i in range(0, len(boxes)):
            if boxes[i] == "1":
                ind.append(i)
        for i in range(len(boxes)):
            temp = 0
            for value in ind:
                temp += abs(value - i)
            ans.append(temp)
        return ans
            
            
        