class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for a in range(len(nums)):
            for b in range(a, len(nums)):
                first = str(nums[a]) + str(nums[b])
                second = str(nums[b]) + str(nums[a])
                if int(first) < int(second):
                    nums[b], nums[a] = nums[a], nums[b]
        ab = ""
        for a in nums:
            ab += str(a)
        if ab.count('0') == len(ab):
            return "0"
        return ab
                