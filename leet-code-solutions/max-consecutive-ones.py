class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res = 0
        count = 0
        for a in range(0, len(nums)):
            if nums[a] == 1:
                count +=1
            else:
                count = 0
            res = max(count, res)
        return res
        