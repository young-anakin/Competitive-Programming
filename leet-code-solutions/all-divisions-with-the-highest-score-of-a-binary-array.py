from collections import defaultdict
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        oneCount = 0
        zeroCount = 0
        total = defaultdict(list)
        for a in range(0, len(nums)):
            if nums[a] == 1:
                oneCount +=1
        maxx = zeroCount + oneCount
        total[maxx].append(0)
        # print(maxx)
        for b in range(0, len(nums)):
            if nums[b] == 0:
                zeroCount +=1
            else:
                oneCount -= 1
            sums = oneCount + zeroCount
            total[sums].append(b+1)
            maxx = max(maxx, sums)
            # print(sums)
        # print(maxx)
        # print(total)
        return total[maxx]