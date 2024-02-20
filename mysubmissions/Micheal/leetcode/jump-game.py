class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1
        mx = 0
        for ind in range(len(nums)):
            if nums[ind] == 0:
                if mx <= nums[ind] + ind:
                    if ind == len(nums)-1:
                        return True
                    return False
            mx = max(mx, nums[ind] + ind)
            # print(mx)
        return True
