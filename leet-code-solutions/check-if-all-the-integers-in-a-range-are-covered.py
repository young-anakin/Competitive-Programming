class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        frequency = {}
        for index in range(0, len(ranges)):
            for LR in range(left, right+1):
                if ranges[index][0] <= LR <= ranges[index][1]:
                    if LR not in frequency:
                        frequency[LR] = 1
        # print(frequency, right+1-left)
        return len(frequency) == right+1-left
            