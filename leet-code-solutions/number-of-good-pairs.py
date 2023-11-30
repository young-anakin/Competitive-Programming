class Solution(object):
    def numIdenticalPairs(self, nums):
        coun = 0
        for a in range(0, len(nums)):
            for b in range(a+1, len(nums)):
                if nums[a] == nums[b]:
                    coun +=1
        return coun
        