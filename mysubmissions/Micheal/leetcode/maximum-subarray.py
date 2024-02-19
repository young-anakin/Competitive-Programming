class Solution(object):
    def maxSubArray(self, nums):
        currSum = 0
        maxSub = nums[0]
        for num in nums:
            if currSum <0:
                currSum = 0
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub