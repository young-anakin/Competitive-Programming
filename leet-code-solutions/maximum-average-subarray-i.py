class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        a = 0
        b = a + k
        summ = 0
        for ind in range(a, b):
            summ += nums[ind]
            
        mx = summ
        while b <= len(nums)-1:
            summ -= nums[a]
            summ += nums[b]
            mx = max(summ, mx)
            a+=1
            b+=1
        return mx/k
            