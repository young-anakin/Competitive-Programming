class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedList = sorted(nums)
        sub = []
        for a in range(len(nums)):
            sub.append(sortedList.index(nums[a]))
        return sub