class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        uniqueNums = set(nums)
        visited = set()
        # values = {}
        hashedValues = {}
        for num in nums:
            hashedValues[num] = 1
        maxx = 1
        count = 1

        for num in uniqueNums:
            if num not in visited:
                while num+1 in hashedValues:
                    count += 1
                    visited.add(num)
                    num +=1
                # visited.add(num)
                maxx = max(maxx, count)
                count = 1
        return maxx