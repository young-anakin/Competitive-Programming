class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)//3
        dict = {}
        arr = []
        for a in range(0, len(nums)):
            if nums[a] not in dict:
                dict[nums[a]] = 1
                if N == 0:
                    arr.append(nums[a])
            else:
                if nums[a] not in arr and dict[nums[a]] == N:
                    arr.append(nums[a])
                dict[nums[a]] += 1
        return arr
