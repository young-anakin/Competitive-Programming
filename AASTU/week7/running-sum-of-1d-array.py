class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_arr = []
        summ = 0

        for ind in range(len(nums)):
            summ += nums[ind]
            new_arr.append(summ)
        return new_arr