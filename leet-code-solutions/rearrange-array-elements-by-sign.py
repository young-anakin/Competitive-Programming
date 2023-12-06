class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        finalement = []
        for a in range(0, len(nums)):
            if nums[a] < 0:
                negative.append(nums[a])
            else:
                positive.append(nums[a])
        for a in range(0, len(positive)):
            finalement.append(positive[a])
            finalement.append(negative[a])
        return finalement