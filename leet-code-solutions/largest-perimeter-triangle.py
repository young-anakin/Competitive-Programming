class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        a = len(nums)-1
        nums.sort()
        while True:
            if a-2 < 0:
                break
            if nums[a] + nums[a-1] > nums[a-2] and nums[a] + nums[a-2] > nums[a-1] and nums[a-2] + nums[a-1] > nums[a]:
                return nums[a] + nums[a-2] + nums[a-1]
            a -=1
        return 0