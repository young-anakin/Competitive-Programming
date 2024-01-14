class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 100000000000
        summ = 0
        a = 0
        for ind in range(len(nums)):
            summ += nums[ind]
            while summ >= target:
                ans = min(ans, (ind+1) - a)
                summ -= nums[a]
                a+=1

        if ans != 100000000000:
            return ans
        return 0