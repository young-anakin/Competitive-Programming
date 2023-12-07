class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        largest = max(nums)
        smallest = min(nums)
        prefixSum = sum(range(smallest, largest+1))
        MySum = sum(nums)
        val = prefixSum-MySum
        if smallest != 0:
            return 0
        if val == 0:
            return largest+1 
        return val