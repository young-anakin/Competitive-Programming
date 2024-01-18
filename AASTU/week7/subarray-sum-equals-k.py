class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = 0
        summ = 0
        cp = defaultdict(int)
        cp[0] = 1
        for ind in range(len(nums)):
            ps += nums[ind]
            summ += cp[ps - k]
            cp[ps] +=1
        return summ
        