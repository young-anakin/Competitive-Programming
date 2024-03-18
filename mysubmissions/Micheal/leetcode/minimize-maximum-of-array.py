class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ps = 0
        curr = 0
        mx = nums[0]
        for ind in range(len(nums)):
            curr += nums[ind]
            ps = math.ceil(curr/(ind+1))
            mx = max(ps, mx)
        return mx